from pprint import pprint

from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()


class DBSettings(BaseSettings):
    MONGO_HOST: str = Field(env='MONGO_HOST', default='localhost')
    MONGO_PORT: int = Field(env='MONGO_PORT', default=27017)
    MONGO_DB_NAME: str = Field(env='MONGO_DB_NAME', default='db')
    MONGO_DB_COLLECTION_NAME: str = Field(env='MONGO_DB_COLLECTION_NAME',
                                          default='collection')

    MONGO_HOST_TEST: str = Field(env='MONGO_HOST_TEST', default='localhost')
    MONGO_PORT_TEST: int = Field(env='MONGO_PORT_TEST', default=27017)
    MONGO_TEST_DB_NAME: str = Field(env='MONGO_TEST_DB_NAME',
                                    default='test_db')
    MONGO_TEST_DB_COLLECTION_NAME: str = Field(
        env='MONGO_TEST_DB_COLLECTION_NAME', default='test_collection')

    @property
    def mongo_url(self):
        return f'mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}'

    @property
    def mongo_test_url(self):
        return f'mongodb://{self.MONGO_HOST_TEST}:{self.MONGO_PORT_TEST}'


class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    DEBUG: bool = Field(env='DEBUG', default=False)
    TESTING: bool = Field(env='TESTING', default=False)
    if TESTING:
        db.MONGO_DB_NAME = db.MONGO_TEST_DB_NAME
        db.MONGO_DB_COLLECTION_NAME = db.MONGO_TEST_DB_COLLECTION_NAME

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
