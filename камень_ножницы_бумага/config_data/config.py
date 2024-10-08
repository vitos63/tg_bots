from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_id: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path=None):
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'), admin_id=env('ADMIN_ID')))
