import sqlalchemy
from databases import Database
from config import EnvConfig

__HOST = EnvConfig.get_config("DB_HOST", '127.0.0.1')
__USER = EnvConfig.get_config("DB_USERNAME", 'root')
__PWD = EnvConfig.get_config("DB_PASSWORD", EnvConfig.get_config("PASSWORD"))
__SCHEMA = EnvConfig.get_config("DB_SCHEMA", 'viole')

__DB_URL = f"mysql://{__USER}:{__PWD}@{__HOST}/{__SCHEMA}"
db = Database(__DB_URL)

metadata = sqlalchemy.MetaData()

test = sqlalchemy.table(
    "test",
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('varchar', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('created', sqlalchemy.DATETIME, nullable=False)
)

engine = sqlalchemy.create_engine(__DB_URL,
                                  # connect_args={'check_same_thread': False}
                                  connect_args={})

metadata.create_all(engine)
