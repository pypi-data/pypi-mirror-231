from pathlib import Path
from typing import Dict, List, Callable
from loguru._logger import Logger
from nonebot.consts import STARTSWITH_KEY
from nonebot.plugin import on_message
from nonebot.rule import Rule
from nonebot.matcher import Matcher
from multilogging import multilogger
from .decorators import translate_punctuation
from .settings import get_package, setconfig, getconfig, change_status, load_status_settings
from ..reply.init import init as reply_init

import json
import uuid
import re
import inspect
import json
import asyncio
import httpx

package = get_package()
""" 当前 Dicer Girl 运行平台 """
version = "3.3.7"
""" Dicer Girl 版本号 """
current_dir = Path(__file__).resolve().parent
""" Dicer Girl 当前目录 """
dicer_girl_dir = Path.home() / ".dicergirl"
data_dir = dicer_girl_dir / "data"
log_dir = dicer_girl_dir / "log"
_dicer_girl_status = data_dir / "status.json"
_super_user = data_dir / "super_user.json"
_loggers_cachepath = data_dir / "loggers.json"
_modes_cachepath = data_dir / "modes.json"
logger = multilogger(name="Dicer Girl", payload="utils")
""" `utils.py`日志系统 """
su_uuid: str
""" 超级管理员鉴权令牌 """
loggers: Dict[str, Dict[int, List[Logger | str]]] = {}
""" 正在运行的日志 """
saved_loggers: Dict[str, dict]
""" 存储的日志 """

try:
    from nonebot.adapters.onebot.v11 import MessageEvent, GroupMessageEvent, PrivateMessageEvent
except ModuleNotFoundError:
    logger.warning("未找到依赖`Nonebot2`, 请检查你的配置.")
    class MessageEvent:
        pass
    class GroupMessageEvent:
        pass

def init() -> None:
    """ 骰娘初始化 """
    global saved_loggers
    dirs: Dict[str, List[Path, list]] = {
        "Dicer Girl": [dicer_girl_dir, "dir"],
        "Dicer Girl 数据": [data_dir, "dir"],
        "Dicer Girl 日志": [log_dir, "dir"],
        "Dicer Girl 状态管理": [_dicer_girl_status, "file"],
        "日志管理": [_loggers_cachepath, "file"],
        "跑团模式存储": [_modes_cachepath, "file"],
        "超级用户存储": [_super_user, "file"]
    }
    for name, dir in dirs.items():
        if not dir[0].exists():
            logger.info(f"{name}{'文件夹' if dir[1] == 'dir' else '文件'}未建立, 建立它.")
            if dir[1] == "dir":
                dir[0].mkdir(parents=True, exist_ok=True)
            else:
                with open(dir[0], "w", encoding="utf-8") as f:
                    f.write("{}")
    saved_loggers = load_loggers()
    load_status()
    reply_init()

class StartswithRule:
    """
    自定义的指令检查方法
    允许:
        1. 无视中英文字符串
        2. 无视前后多余空字符
    """
    __slots__ = ("msg", "ignorecase")

    def __init__(self, msg, ignorecase=False):
        self.msg = msg
        self.ignorecase = ignorecase

    def __repr__(self) -> str:
        return f"Startswith(msg={self.msg}, ignorecase={self.ignorecase})"

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, StartswithRule)
            and frozenset(self.msg) == frozenset(other.msg)
            and self.ignorecase == other.ignorecase
        )

    def __hash__(self) -> int:
        return hash((frozenset(self.msg), self.ignorecase))

    async def __call__(self, event, state) -> bool:
        try:
            text = translate_punctuation(event.get_plaintext()).strip()
        except Exception:
            return False
        if match := re.match(
            f"^(?:{'|'.join(re.escape(prefix) for prefix in self.msg)})",
            text,
            re.IGNORECASE if self.ignorecase else 0,
        ):
            state[STARTSWITH_KEY] = match.group()
            return True
        return False

def startswith(msg, ignorecase=True) -> Rule:
    """ 实例化指令检查方法 """
    if isinstance(msg, str):
        msg = (msg,)

    return Rule(StartswithRule(msg, ignorecase))

def on_startswith(commands, priority=0, block=True) -> Matcher:
    """ 获得`Nonebot2`指令检查及参数注入方法 """
    if isinstance(commands, str):
        commands = (commands, )

    return on_message(startswith(commands, True), priority=priority, block=block, _depth=1)

def set_name(name) -> bool | str:
    """ 给骰娘命名 """
    if len(name) >= 5:
        return "我不想要太长的名字!"

    with open(dicer_girl_dir / "name", "w") as f:
        f.write(name)

    return True

def get_name() -> str:
    """ 获得骰娘的名字 """
    path = dicer_girl_dir / "name"
    if not path.exists():
        return "欧若可"

    return path.open(mode="r").read()

def make_uuid() -> str:
    """ 创建新的超级管理员鉴权令牌 """
    global su_uuid
    su_uuid = (str(uuid.uuid1()) + str(uuid.uuid4())).replace("-", "")
    return su_uuid

def get_uuid() -> str:
    """ 获取超级管理员鉴权令牌 """
    return su_uuid

def load_modes() -> Dict[str, list]:
    """ 加载当前不同群聊的跑团模式 """
    return json.loads(open(_modes_cachepath, "r").read())

def set_mode(event, mode) -> bool:
    """ 设置当前群聊的跑团模式 """
    lm = load_modes()
    lm[get_group_id(event)] = mode
    json.dump(lm, open(_modes_cachepath, "w"))

def get_mode(event) -> str:
    """ 获得当前群聊的跑团模式 """
    lm = load_modes()
    if not get_group_id(event) in lm.keys():
        lm[get_group_id(event)] = "scp"
        json.dump(lm, open(_modes_cachepath, "w"))
        return "scp"

    return lm[get_group_id(event)]

def load_loggers() -> Dict[str, list]:
    """ 加载所有的已存储的日志 """
    return json.loads(open(_loggers_cachepath, "r").read())

def get_loggers(event) -> List[str]:
    """ 获取`event`所指向的群聊中所有的日志 """
    got_loggers = json.load(open(_loggers_cachepath, "r"))
    if not get_group_id(event) in got_loggers:
        return []

    return got_loggers[get_group_id(event)]

def add_logger(event: GroupMessageEvent, logname) -> bool:
    """ 新增日志序列 """
    global saved_loggers
    if not get_group_id(event) in saved_loggers.keys():
        saved_loggers[get_group_id(event)] = []

    try:
        saved_loggers[get_group_id(event)].append(logname)
        json.dump(saved_loggers, open(_loggers_cachepath, "w"))
        return True
    except:
        return False

def remove_logger(event: GroupMessageEvent, id: int) -> Dict[str, list]:
    """ 从存储的`loggers.json`中移除指定`logger` """
    saved_loggers[get_group_id(event)].pop(id)
    json.dump(saved_loggers, open(_loggers_cachepath, "w"))
    return saved_loggers

def set_config(appid, token) -> dict:
    """ 在`QQGuild`模式中设置频道机器人`appid`以及`token`. """
    return setconfig(appid, token, path=dicer_girl_dir, filename="config.yaml")

def get_config() -> dict:
    """ 获取`QQGuild`模式中频道机器人的`appid`以及`token`. """
    return getconfig(path=dicer_girl_dir, filename="config.yaml")

def format_msg(message, begin=None, zh_en=False) -> List[str]:
    """ 骰娘指令拆析为`list`的方法 """
    msg = format_str(message, begin=begin).split(" ")
    outer = []
    regex = r'(\d+)|([a-zA-Z\u4e00-\u9fa5]+)' if not zh_en else r"(\d+)|([a-zA-Z]+)|([\u4e00-\u9fa5]+)"

    for m in msg:
        m = re.split(regex, m)
        m = list(filter(None, m))
        outer += m

    msg = outer
    msg = list(filter(None, msg))
    logger.debug(msg)
    return msg

def format_str(message: str, begin=None) -> str:
    """ 骰娘指令转义及解析 """
    regex = r"[<\[](.*?)[\]>]"
    msg = re.sub("\s+", " ", re.sub(regex, "", str(message).lower())).strip(" ")
    msg = translate_punctuation(msg)
    logger.debug(msg)

    if begin:
        if isinstance(begin, str):
            begin = [begin, ]
        elif isinstance(begin, tuple):
            begin = list(begin)

        begin.sort(reverse=True)
        for b in begin:
            msg = msg.replace(b, "").lstrip(" ")

    logger.debug(msg)
    return msg

def get_mentions(event: GroupMessageEvent) -> List[str]:
    """ 获取`event`指向的消息所有被`@`的用户 QQ 号 """
    mentions = []
    message = json.loads(event.json())["message"]

    for mention in message:
        if mention["type"] == "at":
            mentions.append(mention["data"]["qq"])

    return mentions

def get_handlers(main) -> List[Callable]:
    """ 获取目前所有的指令触发函数方法 """
    commands_functions = []

    for _, obj in vars(main).items():
        if inspect.isfunction(obj) and hasattr(obj, '__annotations__'):
            annotations = obj.__annotations__
            if annotations.get('message') is GroupMessageEvent:
                commands_functions.append(obj)

    return commands_functions

def get_group_id(event) -> str:
    """ 获取`event`指向的群聊`ID` """
    try:
        if not isinstance(event, PrivateMessageEvent):
            return str(event.group_id)
        else:
            return "private"
    except Exception as error:
        logger.exception(error)
        return "0"

def get_user_id(event) -> str:
    """ 获取`event`指向的用户`ID` """
    try:
        if not isinstance(event, PrivateMessageEvent):
            return str(event.user_id)
        else:
            return "private"
    except Exception as error:
        logger.exception(error)
        return "0"

def get_user_card(event) -> str:
    """ 获取`event`指向的用户群名片 """
    try:
        raw_json = json.loads(event.json())['sender']
        if raw_json['card']:
            return raw_json['card']
        else:
            return raw_json['nickname']
    except:
        return "未知用户"

def add_super_user(message) -> bool:
    """ 新增超级管理员 """
    with open(_super_user, "w+") as _su:
        sr = _su.read()
        if not sr:
            sudos = {}
        else:
            sudos = json.loads(sr)
        sudos[get_user_id(message)] = ""
        _su.write(json.dumps(sudos))
    return True

def rm_super_user(message) -> bool:
    """ 删除超级管理员 """
    rsu = open(_super_user, "r")
    sr = rsu.read()
    if not sr:
        return False
    sudos = json.loads(sr)
    try:
        sudos.pop(get_user_id(message))
    except KeyError:
        return False
    _su = open(_super_user, "w")
    _su.write(json.dumps(sudos))
    return True

def is_super_user(event) -> bool:
    """ 判断`event`所指向的用户是否为超级管理员 """
    su = False
    with open(_super_user, "r") as _su:
        sr = _su.read()
        if not sr:
            sudos = {}
        else:
            sudos = json.loads(sr)
    for sudo in sudos.keys():
        if get_user_id(event) == sudo:
            su = True
            break
    return su

def botoff(event):
    """ 机器人在`event`所指向的群聊中开启指令限制 """
    status = load_status_settings()
    status[get_group_id(event)] = False
    change_status(status)
    f = open(_dicer_girl_status, "w")
    json.dump(status, f)

def boton(event):
    """ 机器人在`event`所指向的群聊中开启完全功能 """
    status = load_status_settings()
    status[get_group_id(event)] = True
    change_status(status)
    f = open(_dicer_girl_status, "w")
    json.dump(status, f)

def get_status(event):
    """ 判断机器人在`event`所指向的群聊中是否处于完全功能状态 """
    status = load_status_settings()
    group_id = get_group_id(event)

    if group_id == "private":
        return True

    if group_id not in status.keys():
        status[get_group_id(event)] = True
        f = open(_dicer_girl_status, "w")
        json.dump(status, f)
        return True

    return status[get_group_id(event)]

def load_status() -> dict:
    """ 导入目前所存储的机器人在各群聊中状态 """
    status_text = _dicer_girl_status.read_text(encoding="utf-8")
    if status_text:
        status = json.loads(status_text)
    else:
        status = {}

    change_status(status)
    return status

def rolekp(event):
    ...

def roleob(event):
    ...

async def get_latest_version(package_name):
    """ 获取当前 Pypi 上`dicergirl`的最新版本号 """
    async with httpx.AsyncClient() as client:
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = await client.get(url)

        if response.status_code == 404:
            return "0.0.0.0"

        package_info = response.json()
        return tuple(map(int, package_info["info"]["version"].split(".")))

async def run_shell_command(command):
    """ 异步执行 shell 指令的原始方法 """
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    return {
        "stdout": stdout.decode().strip(),
        "stderr": stderr.decode().strip(),
        "returncode": process.returncode
    }