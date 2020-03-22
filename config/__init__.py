import os


class EnvConfig:
    @staticmethod
    def get_config(name: str, default: str = "") -> str:
        if default != "":
            return str(os.environ.get(name, default))
        else:
            return str(os.environ[name])
