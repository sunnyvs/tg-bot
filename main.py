import telebot
from telebot import types
import random

bot = telebot.TeleBot('')

emoji_to_text = {
    '🪨 Камень' : 'Камень',
    '📄 Бумага' : 'Бумага',
    '✂️ Ножницы' : 'Ножницы'
}

count_bot = 0
count_user = 0


#обратный словарь текст-эмодзи
text_to_emoji = {value: key for key, value in emoji_to_text.items()}

@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создание клавиатуры
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_papper = types.KeyboardButton('📄 Бумага')
    button_rock = types.KeyboardButton('🪨 Камень')
    button_scissors = types.KeyboardButton('✂️ Ножницы')
    keyboard.add(button_papper, button_rock, button_scissors)

    bot.send_message(message.chat.id,'Игра камень ножницы бумага!\nВаш ход:',reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_message(message):

    try:
        player_choice = emoji_to_text[message.text]
        bot_choose = random.choice(list(emoji_to_text.values()))
        bot.send_message(message.chat.id,f'{text_to_emoji[bot_choose]}')
        if (player_choice == 'Камень' and bot_choose == 'Ножницы') or (player_choice == 'Бумага'and bot_choose == 'Камень') or (player_choice == 'Ножницы'and bot_choose == 'Бумага'):
            bot.send_message(message.chat.id, 'Вы выиграли!')
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAENyeRnrpuLpOofIMqTXNtHeSiqOOID9wACuxEAAgRpUEhoXo8enQY6jzYE')

        elif (player_choice == bot_choose):
            bot.send_message(message.chat.id, 'Ничья!')
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAENyetnrp3opiAEGpPoTF49Mob-11Ig2gACK20AApiweUn6SxvriCHHuzYE')
        else:
            bot.send_message(message.chat.id, 'Вы проиграли!')
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAENydtnrpUOvYrLVkd9KvQdMZfDRAr0GQACXRsAAr6AYEk8jFPbEcVuTjYE')

    except KeyError:
        bot.send_message(message.chat.id, 'Введите корректное значение. Пожалуйста, используйте кнопки для выбора.')

bot.polling(none_stop=True)
