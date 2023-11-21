from os import getenv

from dotenv import load_dotenv

load_dotenv()

DEBUG = getenv('DEBUG')

DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')
DB_URL = f'mongodb://{DB_HOST}:{DB_PORT}'

DB_HOST_TEST = getenv('DB_HOST_TEST')
DB_PORT_TEST = getenv('DB_PORT_TEST')
DB_NAME_TEST = getenv('DB_NAME_TEST')
DB_COLL_TEST = getenv('DB_COLL_TEST')
DB_URL_TEST = f'mongodb://{DB_HOST_TEST}:{DB_PORT_TEST}'
