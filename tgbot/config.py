from dataclasses import dataclass

from environs import Env


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str
    db_uri: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token="BOT_TOKEN",
            admin_ids=[],
            use_redis=False,
        ),
        db=DbConfig(
            host='DB_HOST',
            password='DB_PASS',
            user='DB_USER',
            database='DB_NAME',
            db_uri='DB_URI'
        ),
        misc=Miscellaneous()
    )
