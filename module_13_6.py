from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
button1 = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.row(button1, button2)
inl_button1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
inl_button2 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
start_menu = InlineKeyboardMarkup(resize_keyboard=True)
start_menu.add(inl_button1, inl_button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите:", reply_markup=start_menu)


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("Формула, по которой рассчитываются калории: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()

@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(text="Urban")
async def urban_message(message):
    print("Urban message")


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    print(*data)
    calories = 10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) - 5
    await message.answer(f"Ваша норма калорий: {calories}")
    await state.finish()


@dp.message_handler(commands=["start"])
async def start(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler()
async def all_messages(message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)