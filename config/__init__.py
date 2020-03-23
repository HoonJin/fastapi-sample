import os


class EnvConfig:
    @staticmethod
    def get_str_config(name: str, default: str = "") -> str:
        if default != "":
            return str(os.environ.get(name, default))
        else:
            return str(os.environ[name])

    @staticmethod
    def get_int_config(name: str, default: int = 0) -> int:
        if default != "":
            return int(os.environ.get(name, default))
        else:
            return int(os.environ[name])
