"""
初始化DGI_PROVIDERS与CUSTOM_PROVIDERS数组
"""
import os
import re

from multilogging import multilogger

from dicergirl.common import const
from dicergirl.reply.manager import manager
from dicergirl.reply.parsers import templates
from dicergirl.reply.parsers.matcher import MatchType

logger = multilogger(name="DicerGirl", payload="ReplyModuleInit")


def init():
    """
    初始化方法
    """
    if not os.path.exists(const.REPLY_FOLDER_PATH):
        os.makedirs(const.REPLY_FOLDER_PATH)
    _load_template_methods()
    _init_example_config()
    _init_reply_config()


def _load_template_methods():
    """
    获取 templates.py 中的所有方法
    """
    for name, method in vars(templates).items():
        if callable(method):
            manager.register_method(method)


def _init_reply_config():
    """
    加载reply文件数组中
    """
    try:
        for filename in os.listdir(const.REPLY_FOLDER_PATH):
            pattern = re.compile(r'^dg-.*\.yml$')
            file_path = os.path.join(const.REPLY_FOLDER_PATH, filename)
            logger.info(f"载入文件: [{file_path}]")
            if os.path.isfile(file_path):
                if pattern.match(filename):
                    with (open(file_path, "rb") as file):
                        data = const.REPLY_YAML.load(file)
                        items = data["items"]
                        logger.debug(items)
                        for item in items:
                            for event_name, send_text in item.items():
                                manager.register(event_name, send_text)
                elif filename.endswith(".yml"):
                    with (open(file_path, "rb") as file):
                        data = const.REPLY_YAML.load(file)
                        enable = data["enable"]
                        if not enable:
                            continue
                        items = data["items"]
                        logger.debug(items)
                    for item in items:
                        for event_name, response in item.items():
                            manager.register_event(
                                event_name,
                                response["send_text"],
                                response["match_field"],
                                MatchType[response["match_type"]],
                                response["enable"]
                            )
    except KeyError as e:
        logger.error(
            f"请确保您的回复配置文件包含了正确的键和相应的值。如果您不确定如何正确配置文件，请参考文档或向管理员寻求帮助。")
        logger.error(f"Error: {e}")
    except Exception as e:
        logger.error(f"Error: {e}")


def _init_example_config():
    """
    示例文件初始化
    """
    try:
        if not os.path.exists(const.EXAMPLE_REPLY_FILE_PATH):
            with open(file=const.EXAMPLE_REPLY_FILE_PATH, mode='wb') as drf:
                raw_data = const.REPLY_YAML.load(const.EXAMPLE_TEMPLATE)
                const.REPLY_YAML.dump(data=raw_data, stream=drf)
    except Exception as e:
        logger.error(f"{type(e)}:e")
