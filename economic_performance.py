import requests
from bs4 import BeautifulSoup

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'accept': '*/*'
}
params = None


# Еженедельная добыча нефти
def oil():
    url = 'https://ru.investing.com/economic-calendar/eia-crude-oil-inventories-75'
    r = requests.get(url, headers=HEADERS, params=params)
    soup = BeautifulSoup(r.content, 'lxml')

    oil_prod = soup.find('div', id='releaseInfo').find_all('span')
    a = []
    for i in oil_prod:
        a.append(i.find('div').text)

    return f"Последний выпуск: {a[0]}\nФакт.: {a[1]}\nПрогноз: {a[2]}\nПред.: {a[3]}"


# print(oil())


# Уровень безработицы в США
def unemployment():
    url = 'https://ru.investing.com/economic-calendar/unemployment-rate-300'
    r = requests.get(url, headers=HEADERS, params=params)
    soup = BeautifulSoup(r.content, 'lxml')

    unpl = soup.find('div', id='releaseInfo').find_all('span')
    a = []
    for i in unpl:
        a.append(i.find('div').text)
    return f"Последний выпуск: {a[0]}\nФакт.: {a[1]}\nПрогноз: {a[2]}\nПред.: {a[3]}"


# print(unemployment())


# Решение по процентной ставке ФРС США
def rate():
    url = 'https://ru.investing.com/economic-calendar/interest-rate-decision-168'
    r = requests.get(url, headers=HEADERS, params=params)
    soup = BeautifulSoup(r.content, 'lxml')

    rate = soup.find('div', id='releaseInfo').find_all('span')
    a = []
    for i in rate:
        a.append(i.find('div').text)
    return f"Последний выпуск: {a[0]}\nФакт.: {a[1]}\nПрогноз: {a[2]}\nПред.: {a[3]}"


# print(rate())

# ВВП США
def GDP():
    url = 'https://ru.investing.com/economic-calendar/gdp-375'
    r = requests.get(url, headers=HEADERS, params=params)
    soup = BeautifulSoup(r.content, 'lxml')

    gdp = soup.find('div', id='releaseInfo').find_all('span')
    a = []
    for i in gdp:
        a.append(i.find('div').text)
    return f"Последний выпуск: {a[0]}\nФакт.: {a[1]}\nПрогноз: {a[2]}\nПред.: {a[3]}"


# print(GDP())


import telebot

# Кнопки
keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Добыча 🛢', 'Безработица 🤷‍♂️', 'Ставка 📍', 'ВВП 📊')
bot = telebot.TeleBot('TOKEN')


# приветствие для пользователя после команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, что тебе интересно?', reply_markup=keyboard)


# Команды на кнопки
@bot.message_handler(content_types=['text'])
def any_key(message):
    if message.text == 'Добыча 🛢':
        bot.send_message(message.chat.id, oil())
    elif message.text == 'Безработица 🤷‍♂️':
        bot.send_message(message.chat.id, unemployment())
    elif message.text == 'Ставка 📍':
        bot.send_message(message.chat.id, rate())
    elif message.text == 'ВВП 📊':
        bot.send_message(message.chat.id, GDP())
    else:
        bot.send_message(message.chat.id, 'Выберете команду')


bot.polling(none_stop=True)

