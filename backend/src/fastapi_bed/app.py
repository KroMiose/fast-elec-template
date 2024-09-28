from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from fastapi_bed.core import config, logger
from fastapi_bed.core.args import Args
from fastapi_bed.core.database import init_db
from fastapi_bed.routers import mount_routers

app = FastAPI(
    title="FastAPI Service",
    description="FastAPI 后端服务",
    version="0.0.1",
    docs_url="/docs",
)

""" 跨域中间件配置 """
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 挂载路由
mount_routers(app)

# 挂载静态目录
# app.mount(
#     "/",
#     StaticFiles(directory=config.FRONT_END_DIST_DIR, html=True),
#     name="static",
# )


async def startup_event():
    await init_db()
    logger.info("FastAPI Service started")


async def shutdown_event():
    logger.info("FastAPI Service stopped")


app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)


def start():
    import uvicorn

    uvicorn.run(
        "src.fastapi_bed.app:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        log_level=config.UVICORN_LOG_LEVEL.lower(),
        reload=config.APP_RELOAD or Args.RELOAD,
    )


if __name__ == "__main__":
    start()
