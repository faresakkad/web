import telebot
import random
from telebot import types
import requests
from bs4 import BeautifulSoup
from time import sleep

CNY = 'https://www.google.ru/search?q=юань+к+рублю&newwindow=1&sca_esv=779b01740ca52ec5&sca_upv=1&sxsrf=ACQVn0-kFLBrd-ucVrbftIwx0T9lm-A34A%3A1714048562673&ei=Mk4qZvTcKOCzwPAPvquV0AU&udm=&oq=юань&gs_lp=Egxnd3Mtd2l6LXNlcnAiCNGO0LDQvdGMKgIIADIPECMYgAQYJxiKBRhGGIICMgoQIxiABBgnGIoFMgoQIxiABBgnGIoFMgoQABiABBhDGIoFMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIKEAAYgAQYFBiHAjIFEAAYgAQyGRAAGIAEGIoFGEYYggIYlwUYjAUY3QTYAQFIyw9QAFi1A3AAeAGQAQCYAZABoAHuA6oBAzAuNLgBAcgBAPgBAZgCBKACugTCAgsQLhiABBjRAxjHAcICBRAuGIAEwgIKEC4YgAQYQxiKBZgDALoGBggBEAEYE5IHAzAuNKAH0kk&sclient=gws-wiz-serp'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0 (Edition Yx GX)'

headers = {'user agent': user_agent}

html = requests.get(CNY, headers)
soup = BeautifulSoup(html.content, 'html.parser')
price = soup.findAll('div', {'class': 'BNeawe iBp4i AP7Wnd'})
CNY_currency = float(price[0].text.split()[0].replace(',', '.'))

hjh = 0
A = ['😍', '😂', '😘', '❤️', '😊', '👋', '👍', '😁', '☺️', '😔', '😄', '😭', '😒', '😳', '😜', '😉', '😃', '😢', '😝', '😱', '😡', '😏',
     '😞', '😆', '😋', '😀', '😌', '😅', '😚', '😐', '😕', '😀', '😃', '😄', '😁', '😆', '🥹', '😅', '🙂', '😇', '😊', '☺️', '🥲', '🤣', '😂',
     '🙃', '😉', '😌', '😘', '😗', '🤪', '😝', '😜', '😋', '😚', '😙', '🤨', '🧐', '🤓', '😎', '🥸', '🤩', '🥳', '🙁', '😕', '😟', '😔', '😞',
     '😏', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😳', '🤯', '🤬', '😡', '😠', '😤', '😭', '🥵', '🥶', '😶‍🌫️', '😱', '😨', '😰', '😥',
     '🥰']
bot = telebot.TeleBot('5914652897:AAFNYcx9dQVLYseoRrYUMayayElkI5yuRrQ')
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row(types.KeyboardButton('Рассчитать стоимость 📲'), types.KeyboardButton('Актуальный курс 💹'))
menu.row(types.KeyboardButton('Срок доставки 🚘'), types.KeyboardButton('Написать менеджеру 🙎‍♂'))
menu.row(types.KeyboardButton('Инструкция и FAQ📖'), types.KeyboardButton('Отзывы 💁‍♂ 💁‍♀'))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'Привет <b>{message.from_user.first_name}</b> 👋,  этот телеграм бот🤖 предназначен для заказа через poison.  Мы надеемся,  что вы останетесь довольны нашим сервисом!😊\n\n<i>ДЛЯ ПЕРЕЗАПУСКА БОТА ВВЕДИТЕ</i> /start\n\n',
                     reply_markup=menu, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global A
    if message.text == "Рассчитать стоимость 📲":
        keyboardgostart = types.ReplyKeyboardMarkup()
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Обувь👟', 'Одежда👕']])
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Вернуться назад 🔙']])
        bot.send_message(message.chat.id, 'Выберите категорию товара', reply_markup=keyboardgostart)
    elif message.text == "Актуальный курс 💹":
        bot.send_message(message.chat.id, f'Курс на сегодня:\n\n <b>1¥</b> = <b>{CNY_currency}</b>', parse_mode='html')
    elif message.text == "Срок доставки 🚘":
        bot.send_message(message.chat.id,
                         'Среднее время доставки товара от момента покупки до его получения в Ижевске: *21 день*.\n\nСрок доставки складывается из:\n\n1. Доставка от Poizon до склада в Китае (2-6 дней).\n\nТочный срок доставки написан на кнопках в приложении. Почитать подробнее о кнопках и что они означают можно [здесь](https://teletype.in/@hfpoison/MEANINGOFBUTTONS).\n\n2. Доставка из Китая до Ижевска (17-19 дней).\n\n3. Если вы находитесь не в Ижевске, то к сроку доставки прибавится отправка из Ижевска до Вашего города СДЭКом.\n\nВесь товар изначально едет в Ижевск, мы не можем отправить товар из Китая сразу в Ваш город.',
                         parse_mode='Markdown')
    elif message.text == "Написать менеджеру 🙎‍♂":
        bot.send_message(message.chat.id,
                         'Готов оформить заказ или остались вопросы?\n\nПиши сюда @hasiip7ay3r\n\nЭто чат с нашим менеджером.\n\nДля оформления заказа тебе нужно отправить ссылку на товар + указать свой размер и написать «хочу купить»\n\n‼️ОБРАТИ ВНИМАНИЕ‼️\n\nВсе заказы осуществляются только через один аккаунт @hasiip7ay3r\n\nДругих аккаунтов у нас нет')
    elif message.text == "Инструкция и FAQ📖":
        bot.send_message(message.chat.id, '[Меню канала](https://teletype.in/@hfpoison/pNIKEGleIJW)',
                         parse_mode='Markdown')
    elif message.text == "Отзывы 💁‍♂ 💁‍♀":
        bot.send_message(message.chat.id, 'Мы собираем отзывы наших покупателей [здесь](https://t.me/hfpoisonreviews).',
                         parse_mode='Markdown')
    elif message.text == "Вернуться назад 🔙":
        bot.send_message(message.chat.id, 'Что будем делать дальше?', reply_markup=menu)
    elif message.text == "Обувь👟":
        file = open('./photo.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        msg = bot.send_message(message.chat.id, '💸 Введите стоимость вещи в юанях (бирюзовая кнопка)')
        bot.register_next_step_handler(msg, start_2)
    elif message.text == "Одежда👕":
        file = open('./photo.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        msg = bot.send_message(message.chat.id, '💸 Введите стоимость вещи в юанях (бирюзовая кнопка)')
        bot.register_next_step_handler(msg, start_1)
    else:
        bot.send_message(message.chat.id, random.choice(A))


def start_2(message):
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    chmo = 0
    for i in message.text:
        if i not in a:
            chmo = 1

    if (chmo == 0):
        bot.send_message(message.chat.id,
                         f'💸 Итоговая стоимость: *{round(int(message.text) * CNY_currency + 1500)}* 💸 рублей',
                         parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         f'Стоимость включает:\n\n<b>Курс ¥ - {CNY_currency}</b>\n\n<b>Доставка - 1500₽</b>\n\nЕсли вы находитесь не в г. Ижевск, то прибавляется доставка СДЭКом до вашего города.\n\nМы работаем по 100% предоплате\n\nГотов оформить заказ или остались вопросы?\n\nПиши сюда @hasiip7ay3r . Это чат с нашим менеджером.\n\nДля оформления заказа тебе нужно отправить ссылку на товар + указать свой размер и написать «хочу купить»\n\n‼️ОБРАТИ ВНИМАНИЕ‼️\n\nВсе заказы осуществляются только через один аккаунт @hasiip7ay3r Других аккаунтов у нас нет',
                         parse_mode='html')
    elif (message.text == 'Вернуться назад 🔙'):
        bot.send_message(message.chat.id, 'Что будем делать дальше?', reply_markup=menu)
    else:
        bot.send_message(message.chat.id, f'Вы ввели не число, попробуйте ещё раз')


def start_1(message):
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    chmo = 0
    for i in message.text:
        if i not in a:
            chmo = 1

    if (chmo == 0):
        bot.send_message(message.chat.id, f'💸 Итоговая стоимость: *{int(message.text) * CNY_currency + 1000}* 💸 рублей',
                         parse_mode='Markdown')
        bot.send_message(message.chat.id,
                         f'Стоимость включает:\n\n<b>Курс ¥ - {CNY_currency}</b>\n\n<b>Доставка - 1000₽</b>\n\nЕсли вы находитесь не в г. Ижевск, то прибавляется доставка СДЭКом до вашего города.\n\nМы работаем по 100% предоплате\n\nГотов оформить заказ или остались вопросы?\n\nПиши сюда @hasiip7ay3r Это чат с нашим менеджером.\n\nДля оформления заказа тебе нужно отправить ссылку на товар + указать свой размер и написать «хочу купить»\n\n‼️ОБРАТИ ВНИМАНИЕ‼️\n\nВсе заказы осуществляются только через один аккаунт @hasiip7ay3r Других аккаунтов у нас нет',
                         parse_mode='html')
    elif (message.text == 'Вернуться назад 🔙'):
        bot.send_message(message.chat.id, 'Что будем делать дальше?', reply_markup=menu)
    else:
        bot.send_message(message.chat.id, f'Вы ввели не число, попробуйте ещё раз')


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(15)
