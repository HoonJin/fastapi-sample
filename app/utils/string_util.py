import secrets
import string


def generate_random_token(length: int = 32):
    return ''.join([secrets.choice(string.ascii_letters + string.digits) for n in range(length)])
