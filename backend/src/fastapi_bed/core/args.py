from fastapi_bed.tools.common_util import ArgTypes


class Args:
    LOAD_TEST: bool = ArgTypes.Bool("--load-test")
    RELOAD: bool = ArgTypes.Bool("--reload")
