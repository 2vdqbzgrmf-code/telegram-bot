import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = "8554983348:AAFBTRMBwBfyqk_dd4wwmbsj3M0dvDUwWPE"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# --- МЕНЮ ---
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🎁 Вещи PUBG Mobile 🎮")],
        [
            KeyboardButton("🎁 Бонусы"),
            KeyboardButton("👤 Мой профиль")
        ],
        [
            KeyboardButton("📊 Статистика"),
            KeyboardButton("ℹ️ Инфо")
        ]
    ],
    resize_keyboard=True
)

# --- START ---
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer_photo(
        photo=open("banner.jpg", "rb"),
        caption="😊 Добро пожаловать!",
        reply_markup=menu
    )

# --- РАЗДЕЛ PUBG ---
@dp.message_handler(text="🎁 Вещи PUBG Mobile 🎮")
async def pubg(message: types.Message):
    await message.answer(
        "🎮 *Вещи PUBG Mobile*\n\n"
        "• UC\n"
        "• Скины\n"
        "• Аккаунты\n\n"
        "Выберите нужный товар",
        parse_mode="Markdown"
    )

@dp.message_handler(text="🎁 Бонусы")
async def bonus(message: types.Message):
    await message.answer("🎁 Бонусы скоро будут доступны")

@dp.message_handler(text="👤 Мой профиль")
async def profile(message: types.Message):
    await message.answer(
        f"👤 *Профиль*\n\n"
        f"ID: `{message.from_user.id}`\n"
        f"Имя: {message.from_user.first_name}",
        parse_mode="Markdown"
    )

@dp.message_handler(text="📊 Статистика")
async def stats(message: types.Message):
    await message.answer("📊 Статистика временно недоступна")

@dp.message_handler(text="ℹ️ Инфо")
async def info(message: types.Message):
    await message.answer(
        "ℹ️ *Информация*\n\n"
        "Магазин PUBG Mobile\n"
        "Поддержка: @username",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
