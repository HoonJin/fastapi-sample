import sqlalchemy
from databases import Database

from config import EnvConfig

__HOST = EnvConfig.get_str_config('DB_HOST', '127.0.0.1')
__USER = EnvConfig.get_str_config('DB_USERNAME', 'root')
__PWD = EnvConfig.get_str_config('DB_PASSWORD', EnvConfig.get_str_config('PASSWORD'))
__SCHEMA = EnvConfig.get_str_config('DB_SCHEMA', 'viole')
__MIN_POOL_SIZE = EnvConfig.get_int_config('DB_MIN_POOL_SIZE', 3)
__MAX_POOL_SIZE = EnvConfig.get_int_config('DB_MAX_POOL_SIZE', 10)
__DB_URL = f'mysql://{__USER}:{__PWD}@{__HOST}/{__SCHEMA}'

db = Database(__DB_URL, min_size=__MIN_POOL_SIZE, max_size=__MAX_POOL_SIZE)

metadata = sqlalchemy.MetaData()

__engine = sqlalchemy.create_engine(__DB_URL, connect_args={})

metadata.create_all(__engine)
