import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import config

bot = Bot(token=config("2126167337:AAE-1hD-NTT7ahhVJSLLwNwk4_pkmwkfDX4"), parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO)