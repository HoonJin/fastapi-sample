from cryptography.fernet import Fernet

import config

__fernet = Fernet(config.SECRET_KEY)


def encrypt(plain_str: str) -> str:
    return __fernet.encrypt(plain_str.encode()).decode()


def decrypt(encrypted: str) -> str:
    return __fernet.decrypt(encrypted.encode()).decode()
