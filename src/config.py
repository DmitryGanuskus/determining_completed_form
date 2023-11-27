import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()


class DBSettings(BaseSettings):
    MONGO_HOST: str = Field(json_schema_extra={'env': 'MONGO_HOST'},
                            default='localhost')
    MONGO_PORT: int = Field(json_schema_extra={'env': 'MONGO_PORT'},
                            default=27017)
    MONGO_DB_NAME: str = Field(json_schema_extra={'env': 'MONGO_DB_NAME'},
                               default='db')
    MONGO_DB_COLLECTION_NAME: str = Field(
        json_schema_extra={'env': 'MONGO_DB_COLLECTION_NAME'},
        default='collection')
    model_config = SettingsConfigDict(env_file='.env.db',
                                      env_file_encoding='utf-8')

    @property
    def mongo_url(self):
        return f'mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}'


class TestDBSettings(BaseSettings):
    MONGO_HOST_TEST: str = Field(json_schema_extra={'env': 'MONGO_HOST_TEST'},
                                 default='localhost')
    MONGO_PORT_TEST: int = Field(json_schema_extra={'env': 'MONGO_PORT_TEST'},
                                 default=27017)
    MONGO_TEST_DB_NAME: str = Field(
        json_schema_extra={'env': 'MONGO_TEST_DB_NAME'},
        default='test_db')
    MONGO_TEST_DB_COLLECTION_NAME: str = Field(
        json_schema_extra={'env': 'MONGO_TEST_DB_COLLECTION_NAME'},
        default='test_collection')
    model_config = SettingsConfigDict(env_file='.env.test_db',
                                      env_file_encoding='utf-8')

    @property
    def mongo_test_url(self):
        return f'mongodb://{self.MONGO_HOST_TEST}:{self.MONGO_PORT_TEST}'


class Settings(BaseSettings):
    db: DBSettings = DBSettings(_env_file='.env.db',
                                _env_file_encoding='utf-8')
    test_db: TestDBSettings = TestDBSettings(_env_file='.env.test_db',
                                             _env_file_encoding='utf-8')
    DEBUG: bool = Field(json_schema_extra={'env': 'DEBUG'}, default=False)
    TESTING: bool = Field(json_schema_extra={'env': 'TESTING'}, default=False)
    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8')


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
