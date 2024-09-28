from typing import Any, Type, TypeVar

from pydantic import BaseModel

RetType = TypeVar("RetType", bound="Ret")


class Ret(BaseModel):
    code: int
    msg: str
    data: Any

    def __init__(self, code: int, msg: str, data: Any):
        super().__init__(code=code, msg=msg, data=data)

    @classmethod
    def success(cls: Type[RetType], msg: str = "success", data: Any = None) -> RetType:
        return cls(code=200, msg=msg, data=data)

    @classmethod
    def fail(cls: Type[RetType], msg: str = "fail", data: Any = None) -> RetType:
        return cls(code=400, msg=msg, data=data)

    @classmethod
    def unauthorized(
        cls: Type[RetType],
        msg: str = "unauthorized",
        data: Any = None,
    ) -> RetType:
        return cls(code=401, msg=msg, data=data)

    @classmethod
    def forbidden(
        cls: Type[RetType],
        msg: str = "forbidden",
        data: Any = None,
    ) -> RetType:
        return cls(code=403, msg=msg, data=data)

    @classmethod
    def not_found(
        cls: Type[RetType],
        msg: str = "not found",
        data: Any = None,
    ) -> RetType:
        return cls(code=404, msg=msg, data=data)

    @classmethod
    def error(cls: Type[RetType], msg: str = "error", data: Any = None) -> RetType:
        return cls(code=500, msg=msg, data=data)

    def __bool__(self) -> bool:
        return self.code == 200


def ret_data_class(data_class):
    """返回格式的数据类装饰器"""

    class RetData(Ret):
        data: data_class

        def __init__(self, **kwargs):
            super().__init__(code=200, msg="success", data=data_class(**kwargs))

    return RetData
