from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import _asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=["Borzykh"])
async def Borzykh_message(message):
    print('Borzykh message')
    await message.answer("Borzykh, создатель бота!")


@dp.message_handler(commands=['Start'])
async def start_message(message):
    print('Start message')
    await message.answer('Привет! Я бот, чем могу помочь?')


@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение!')
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
