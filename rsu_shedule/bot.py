import telebot
from telebot import types

bot = telebot.TeleBot("7441834795:AAGUYUoATRFSTpr5VzxY_tvQuSaZSgVSVk4") # Задаем бот

@bot.message_handler(commands=['start'])
def welcome(message): # Для кнопок внутри меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, one_time_keyboard=True) # Добавление адаптивных кнопок
    First = types.KeyboardButton('Первый')
    Second = types.KeyboardButton('Второй')
    Third = types.KeyboardButton('Третий')
    Fourth = types.KeyboardButton('Четветрый')
    markup.add(First, Second, Third, Fourth)

    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}, выбери курс", reply_markup=markup)

# Обработка нажатий кнопок
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Первый':
        first_level_choice(message) #bot.reply_to(message, "Вы выбрали первый вариант.")
    elif message.text == 'Второй':
        second_level_choice(message)
    else:
        bot.reply_to(message, "В34")

# Первая группа вложенных кнопок
def first_level_choice(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2, one_time_keyboard=True)
    btn_suboption11 = types.KeyboardButton('Подвариант 1.1')
    btn_suboption12 = types.KeyboardButton('Подвариант 1.2')
    markup.add(btn_suboption11, btn_suboption12)
    
    bot.send_message(message.chat.id, "Вы выбрали Первый вариант. Теперь выберите подвариант:", reply_markup=markup)

# Вторая группа вложенных кнопок
def second_level_choice(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    btn_suboption21 = types.KeyboardButton('9302')
    btn_suboption22 = types.KeyboardButton('9308')
    keyboard.add(btn_suboption21, btn_suboption22)
    
    bot.send_message(message.chat.id, "Выберите Вашу группу:", reply_markup=keyboard)

if __name__ == '__main__':
    bot.polling(none_stop = True, interval = 0)