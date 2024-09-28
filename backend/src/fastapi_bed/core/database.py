import json

from tortoise import Tortoise, fields

from .config import config

DB_INITED = False


async def init_db():
    global DB_INITED

    if DB_INITED:
        return

    # await Tortoise.init(
    #     db_url=config.DB_URL,
    #     modules={"models": ["src.models"]},  # 加载模型
    # )
    # # 生成数据库表
    # await Tortoise.generate_schemas()
    DB_INITED = True
