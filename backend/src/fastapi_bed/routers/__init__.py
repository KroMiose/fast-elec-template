from fastapi import APIRouter, Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm

from fastapi_bed.schemas.message import Ret


def mount_routers(app: FastAPI):

    api = APIRouter(prefix="/api")

    @api.get("/health", response_model=Ret, tags=["Health"], summary="健康检查")
    async def _() -> Ret:
        """测试服务是否正常运行"""
        return Ret.success(msg="FastAPI Service Running...")

    app.include_router(api)
