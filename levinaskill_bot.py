import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

API_TOKEN = "7595960746:AAFEl9Ncx8fe01-OmROD8xgWfuMKtCHUZAk"

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Обработка команды /start
@dp.message(F.text == "/start")
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Рада вас видеть 🌟\n"
        "Благодарю за проявленный интерес к моей программе обучения!\n\n"
        "💳 Вот еквизиты для оплаты курса CRYPTO WORK:\n"
        "IBAN: UA203220010000026007340113213\n"
        "Банк: УНІВЕРСАЛ БАНК\n"
        "Получатель: ФОП Лєвіна Тетяна Юріївна\n"
        "ЄДРПОУ: 21133352\n\n"
        "После оплаты пришлите скриншот сюда, и вы получите доступ к программе🙌"
   )

# Если хочешь — можно оставить эхо-обработчик
# @dp.message()
# async def echo(message: types.Message):
#     await message.answer(f"Вы написали: {message.text}")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # Удаляем webhook
    await dp.start_polling(bot)  # Запускаем polling

if __name__ == "__main__":
    asyncio.run(main())
