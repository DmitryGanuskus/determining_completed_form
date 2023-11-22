from pydantic import Field
from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    mongo_host: str = Field(default='127.0.0.1', env='MONGO_HOST')
    mongo_port: int = Field(default=27017, env='MONGO_PORT')
    mongo_url: str = Field(
        default='mongodb://127.0.0.1:27017',
        env=f'mongodb://{mongo_host}:{mongo_port}'
    )

    mongo_host_test: str = Field(default='127.0.0.1', env='MONGO_HOST_TEST')
    mongo_port_test: int = Field(default=27017, env='MONGO_PORT_TEST')
    mongo_url_test: str = Field(
        default='mongodb://127.0.0.1:27017',
        env=f'mongodb://{mongo_host}:{mongo_port}'
    )


class Settings(BaseSettings):
    db = DBSettings()
    debug: bool = Field(default=False, env='DEBUG')


settings = Settings()
