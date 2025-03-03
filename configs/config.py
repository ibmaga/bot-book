from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    admin_ids: list


@dataclass
class Config:
    tgbot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    config = Config(
        tgbot=TgBot(
            token=env('TOKEN'),
            admin_ids=env('ADMIN_IDS')
        )
    )

    return config
