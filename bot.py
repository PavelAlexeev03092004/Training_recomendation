import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery

from main import result

API_TOKEN = '7456345293:AAE2hlErQh7w-9p6thgT_kuBo7KGth1q_po'

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode='html'))
dp = Dispatcher()

sl = {}
# Хендлер для команды /start
@dp.message(CommandStart())
async def send_welcome(message: Message):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text='Начать тренировку')], [KeyboardButton(text='О проекте')]])
    await message.answer(f"Здравствуйте, {message.chat.first_name}, в этом боте, нажав на кнопку <b>Начать тренировку</b>, вам потребуется ввести ваши параметры, на основе которых вам будет предложена тренировка. Чтобы узнать подробнее о боте нажмите <b>О проекте</b>.", reply_markup=buttons)
@dp.callback_query()
async  def result_buttons(callback: CallbackQuery):
    data = callback.data.split("|")
    if data[0] == "1":
        sl[callback.message.chat.id] += data[1]
        buttons1 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Потеря веса',
                        callback_data='2|Потеря веса'
                    )
                ],
                [
                    InlineKeyboardButton(
                        text='Наращивание мышечной массы',
                        callback_data='2|Наращивание мышечной массы'
                    )
                ],
                [
                    InlineKeyboardButton(
                        text='Улучшение выносливости',
                        callback_data='2|Улучшение выносливости'
                    )
                ]
            ]
        )
        await callback.message.edit_text("Укажите цель тренировки", reply_markup=buttons1)
    elif data[0] == "2":
        sl[callback.message.chat.id] += ", " + data[1]
        l = []
        for name in ["Без ограничений", "Пресс", "Приводящие мышцы", "Отводящие мышцы", "Бицепсы", "Икроножные мышцы", "Грудные мышцы",
                "Предплечья", "Ягодичные мышцы", "Подколенные сухожилия", "Широчайшие мышцы спины",
                "Нижняя часть спины", "Средняя часть спины",
                "Шея",
                "Квадрицепсы",
                "Плечи",
                "Трапеции",
                "Трицепсы"]:
            l.append( [InlineKeyboardButton(
                        text=name,
                        callback_data=f'3|{name}'
                    )])
        buttons = InlineKeyboardMarkup(inline_keyboard=l)
        await callback.message.edit_text("Выберите ограничение по здоровью",reply_markup=buttons)
    elif data[0] == "3":
        sl[callback.message.chat.id] += ", " + data[1]
        l = []
        for name in range (1, 6):
            l.append([InlineKeyboardButton(
                text=str(name),
                callback_data=f'4|{name}'
            )])
        buttons = InlineKeyboardMarkup(inline_keyboard=l)
        await callback.message.edit_text("Укажите ваш уровень усталости", reply_markup=buttons)
    elif data[0] == "4":
        sl[callback.message.chat.id] += ", " + data[1]
        l = []
        for name in ["1-10", "10-30","30-60","60-90", "90-120", "120+"]:
            if name == "120+":
                cd = "150"
            else:
                cd = name.split("-")
                cd = (int(cd[1]) + int(cd[0]))//2
            l.append([InlineKeyboardButton(
                text=name,
                callback_data=f'5|{cd}'
            )])
        buttons = InlineKeyboardMarkup(inline_keyboard=l)
        await callback.message.edit_text("Укажите время тренировки", reply_markup=buttons)
    elif data[0] == "5":
        sl[callback.message.chat.id] += ", " + data[1]
        l = []
        for name in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10+"]:
            l.append([InlineKeyboardButton(
                text=name,
                callback_data=f'6|{name if "+" not in name else 15} '
            )])
        buttons = InlineKeyboardMarkup(inline_keyboard=l)
        await callback.message.edit_text("Укажите количество упражнений", reply_markup=buttons)
    elif data[0] == "6":
        sl[callback.message.chat.id] += ", " + data[1]
        l = []
        for name in ["Кардио", "Олимпийские поднятия весов", "Плиометрика", "Паверлифтинг", "Силовая", "Растяжка", "Стронгман"]:
            l.append([InlineKeyboardButton(
                text=name,
                callback_data=f'7|{name}'
            )])
        buttons = InlineKeyboardMarkup(inline_keyboard=l)
        await callback.message.edit_text("Укажите тип тренировки", reply_markup=buttons)
    elif data[0] == "7":
        sl[callback.message.chat.id] += ", " + data[1]
        l = []
        for name in ["Пресс", "Приводящие мышцы", "Отводящие мышцы", "Бицепсы", "Икроножные мышцы", "Грудные мышцы",
                "Предплечья", "Ягодичные мышцы", "Подколенные сухожилия", "Широчайшие мышцы спины",
                "Нижняя часть спины", "Средняя часть спины",
                "Шея",
                "Квадрицепсы",
                "Плечи",
                "Трапеции",
                "Трицепсы"]:
            l.append([InlineKeyboardButton(
                text=name,
                callback_data=f'8|{name}'
            )])
        buttons = InlineKeyboardMarkup(inline_keyboard=l)
        await callback.message.edit_text("Укажите желаемую часть тела для тренировки", reply_markup=buttons)
    elif data[0] == "8":
        sl[callback.message.chat.id] += ", " + data[1]
        l = []
        for name in [
        "Резинки",
        "Штанга",
        "Собственный вес",
        "Кроссовер",
        "Гантели",
        "Изогнутый гриф",
        "Гимнастический мяч",
        "Пенопластовый ролик",
        "Гиря",
        "Тренажер",
        "Медицинский мяч",
        "Другое",
        "Без инвентаря"
    ]:
            l.append([InlineKeyboardButton(
                text=name,
                callback_data=f'9|{name}'
            )])
        buttons = InlineKeyboardMarkup(inline_keyboard=l)
        await callback.message.edit_text("Укажите имеющийся инвентарь", reply_markup=buttons)
    elif data[0] == "9":
        sl[callback.message.chat.id] += ", " + data[1]
        l = []
        for name in ["Начинающий", "Эксперт", "Продвинутый"]:
            l.append([InlineKeyboardButton(
                text=name,
                callback_data=f'10|{name}'
            )])
        buttons = InlineKeyboardMarkup(inline_keyboard=l)
        await callback.message.edit_text("Укажите ваш уровень", reply_markup=buttons)
    elif data[0] == "10":
        sl[callback.message.chat.id] += ", " + data[1]
        wishes = sl[callback.message.chat.id]
        wishes_list = wishes.split(", ")
        await callback.message.delete()
        waiting = await callback.message.answer("Данные обрабатываются...")
        try:
            data = result([], wishes_list)
            await waiting.delete()
            for name, video in data:
                buttons = InlineKeyboardMarkup(
                    inline_keyboard=[[InlineKeyboardButton(text='Перейти к видео', url=video)]])
                await callback.message.answer(f'Тренировка: <b>{name}</b>', reply_markup=buttons)
        except Exception as e:
            await waiting.delete()
            await callback.message.answer(f"Тренировка не найдена, попробуйте еще раз")
# Хендлер для получения пожеланий
@dp.message(lambda message: message.text)
async def handle_wishes(message: Message):
    if message.text == 'Начать тренировку':
        sl[message.chat.id] = ''
        buttons1 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Верх',
                        callback_data='1|Верх'
                    ),
                    InlineKeyboardButton(
                        text='Низ',
                        callback_data='1|Низ'
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text='Смешанная',
                        callback_data='1|Смешанная'
                    )
                ]
            ]
        )
        await message.answer("Выберите тип тренировки", reply_markup=buttons1)

    elif message.text == 'О проекте':
        buttons1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Перейти на GitHub', url="https://github.com/PavelAlexeev03092004/Training_recomendation")]])
        await message.answer("""Меня зовут Алексеев Павел Александрович. Я часто занимаюсь в тренажерном зале, и передо мной встала проблема составления своего плана тренировок. 

В связи с этим я разработал свою модель системы рекомендаций с использованием MegaGymDataset на основе модели Ridge, которая рекомендует упражнения на основе доступного оборудования, ограничений физической подготовки, здоровья и т.д.""", reply_markup=buttons1)



if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))