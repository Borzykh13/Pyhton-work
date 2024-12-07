from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import _asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())


@dp.message_handler(text = ["BorzykhBot"])
async def Borzykh_message(message):
    print('Borzykh message')
@dp.message_handler(commands=['Start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')
@dp.message_handler()
async def all_message(message):
   print('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
