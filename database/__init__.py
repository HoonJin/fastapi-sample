import sqlalchemy
from databases import Database

from config import conf


__DB_URL = conf.get('DB_URL', str)
db = Database(__DB_URL,
              min_size=conf.get('DB_MIN_POOL_SIZE', int, 3),
              max_size=conf.get('DB_MAX_POOL_SIZE', int, 10)
              )

metadata = sqlalchemy.MetaData()

__engine = sqlalchemy.create_engine(__DB_URL, connect_args={})

metadata.create_all(__engine)
