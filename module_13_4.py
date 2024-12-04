from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = "7740794913:AAFiIoOpc9rnb2Wcf3KvDXkYY5QE6ylhEUY"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=["Calories"])
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(text=["Urban"])
async def urban_message(message):
    print("Urban message")


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update.data(first=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update.data(first=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update.data(first=message.text)
    data = await state.get_data()
    calories = 10 * data.weight + 6.25 * data.growth - 5 * data.age - 5
    await message.answer(f"Ваша норма калорий: {calories}")
    await state.finish()


@dp.message_handler(commands=["start"])
async def start(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_messages(message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)