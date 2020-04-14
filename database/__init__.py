import sqlalchemy
from databases import Database
from sqlalchemy import Table

from config import conf

__DB_URL = conf.get('DB_URL', str)
db = Database(__DB_URL,
              min_size=conf.get('DB_MIN_POOL_SIZE', int, 3),
              max_size=conf.get('DB_MAX_POOL_SIZE', int, 10)
              )

metadata = sqlalchemy.MetaData()
__engine = sqlalchemy.create_engine(__DB_URL, connect_args={})
metadata.reflect(bind=__engine)  # schema를 reflection해서 immutabledict에 name: table 로 맵핑함
__tables = metadata.tables


def get_schema(name: str) -> Table:
    return __tables[name]


metadata.create_all(__engine)
