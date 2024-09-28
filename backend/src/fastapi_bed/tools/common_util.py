import asyncio
import sys
import urllib.parse
from pathlib import Path
from typing import Any, Callable, Dict, Optional, Tuple, Type, Union
from urllib.parse import quote_plus

from fastapi_bed.core import config


class ArgTypes:

    @staticmethod
    def _use_arg(arg_key: str, default: Any = None) -> Any:
        if arg_key in sys.argv:
            index = sys.argv.index(arg_key)
            if index + 1 < len(sys.argv):
                return sys.argv[index + 1]
        return default

    @staticmethod
    def Str(key: str, default: str = "") -> str:
        return str(ArgTypes._use_arg(key, default))

    @staticmethod
    def Int(key: str, default: int = 0) -> int:
        return int(ArgTypes._use_arg(key, default))

    @staticmethod
    def Float(key: str, default: float = 0.0) -> float:
        return float(ArgTypes._use_arg(key, default))

    @staticmethod
    def Bool(key: str) -> bool:
        return key in sys.argv


def http_retry(
    times: int = 3,
    delay: int = 1,
    backoff: int = 2,
    additional_exceptions: Tuple[Type[Exception], ...] = (),
):
    """HTTP 异步请求重试装饰器

    Args:
        times (int, optional): 最大重试次数. Defaults to 3.
        delay (int, optional): 首次重试延迟时间. Defaults to 1.
        backoff (int, optional): 重试间隔递增倍数. Defaults to 2.
    """

    def decorator(func):
        async def wrapper(*args, **kwargs):
            nonlocal times, delay, backoff

            for i in range(times):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if i == times - 1:
                        raise
                    if isinstance(
                        e,
                        (asyncio.TimeoutError, ConnectionError, *additional_exceptions),
                    ):
                        await asyncio.sleep(delay)
                        delay *= backoff
                    raise
            raise

        return wrapper

    return decorator


def save_temp_file(
    file_name: str,
    content: Union[str, bytes],
    only_one: bool = True,
) -> Path:
    """保存临时文件

    Args:
        file_name (str): 文件名
        content (Union[str, bytes]): 文件内容
    """
    save_path = Path(config.TEMP_DIR) / file_name
    save_path.parent.mkdir(parents=True, exist_ok=True)
    if only_one and save_path.exists():
        return save_path
    if isinstance(content, str):
        save_path.write_text(content)
    else:
        save_path.write_bytes(content)
    return save_path


def url_quote(url: str) -> str:
    """URL 编码

    Args:
        url (str): 待编码 URL

    Returns:
        str: 编码后的 URL
    """
    return urllib.parse.quote(url, safe=":/%#?&=@[]!$'()*+,;")


def safe_int(value: Any) -> Optional[int]:
    """安全的整数转换

    Args:
        value (Any): 待转换的值

    Returns:
        Optional[int]: 转换后的整数值，如果转换失败则返回 None
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def safe_float(value: Any) -> Optional[float]:
    """安全的浮点数转换

    Args:
        value (Any): 待转换的值

    Returns:
        Optional[float]: 转换后的浮点数值，如果转换失败则返回 None
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def gen_mysql_conn_str(host: str, port: int, user: str, password: str, db: str) -> str:
    """生成 MySQL 连接字符串

    Args:
        host (str): 主机名或 IP 地址
        port (int): 端口号
        user (str): 用户名
        password (str): 密码
        db (str): 数据库名

    Returns:
        str: 连接字符串
    """
    user = quote_plus(user)
    password = quote_plus(password)
    db = quote_plus(db)
    return f"mysql://{user}:{password}@{host}:{port}/{db}"


def parse_cookies(cookies: str) -> Dict[str, str]:
    """解析 cookies 字符串

    Args:
        cookies (str): cookies 字符串

    Returns:
        Dict[str, str]: cookies 字典
    """
    cookies_dict = {}
    for cookie in cookies.split(";"):
        key, value = cookie.strip().split("=", 1)
        cookies_dict[key] = value
    return cookies_dict
