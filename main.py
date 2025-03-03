import asyncio
import logging
from typing import Any, Awaitable, Callable

from aiogram import Dispatcher, Bot, BaseMiddleware
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import TelegramObject

from configs import Config, load_config
from handlers import cmds, other
from keyboards import set_my_commands
from database.database import users_dp, user_dict_template

logger = logging.getLogger(__name__)

class Middel(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: dict[str, Any]) -> Any:

        users_dp[data['event_context'].chat.id] = users_dp.get(data['event_context'].chat.id, user_dict_template)
        return await handler(event, data)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='{message} {filename}:{lineno}-{levelname} [{asctime}] {name}',
        style='{'
    )

    logger.info('Bot started')

    config: Config = load_config()

    bot = Bot(token=config.tgbot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_routers(cmds.router, other.router)
    dp.update.outer_middleware(Middel())

    dp['user_data'] = users_dp
    dp.startup.register(set_my_commands)
    await dp.start_polling(bot)


asyncio.run(main())

