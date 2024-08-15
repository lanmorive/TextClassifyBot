import telebot
import joblib
import warnings
import os
import numpy as np
import util

warnings.filterwarnings('ignore')

os.chdir(r'C:\Users\lanmo\Desktop\tg_bot\data')
model = joblib.load('log1.pkl')
vec = joblib.load('vec1.pkl')
bot = telebot.TeleBot() # Тут должен быть ваш token

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'начать':
        bot.send_message(message.from_user.id, "Введите комментарий к фильму на английском:")
        bot.register_next_step_handler(message, preobraz)
    else:
        bot.send_message(message.from_user.id, 'Напиши: Начать')


def preobraz(message):
    text = message.text
    print(text)
    our_text = np.array([util.lemma(util.delt_stop_words(util.chist(text)))])
    transform = vec.transform(our_text)
    num = model.predict(transform)[0]

    if num == 1:
        bot.send_message(message.from_user.id, "Вы оставили положительный комментарий!")
    else:
        bot.send_message(message.from_user.id, "Вы оставили негативный комментарий!")

    # Спрашиваем, хочет ли пользователь продолжить
    bot.send_message(message.from_user.id, "Хотите продолжить? Напишите Да или Нет.")
    bot.register_next_step_handler(message, continue_or_not)


def continue_or_not(message):
    if message.text.lower() == 'да':
        bot.send_message(message.from_user.id, "Введите комментарий к фильму на английском:")
        bot.register_next_step_handler(message, preobraz)
    else:
        bot.send_message(message.from_user.id,
                         "Спасибо за использование! Если хотите начать заново, напишите 'Начать'.")


bot.polling(none_stop=True, interval=0)
