class Config:
    APP_HOST = "0.0.0.0"
    APP_PORT = 8866
    APP_RELOAD = True
    UVICORN_LOG_LEVEL = "info"
    APP_LOG_LEVEL = "info"

    DB_URL = "sqlite:///./data/database.db"
    DATA_DIR = "data"
    TEMP_DIR = ".temp"
    LOG_DIR = "data/logs"


config = Config()
