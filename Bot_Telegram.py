import telebot
from telebot import types

bot = telebot.TeleBot("6018560182:AAH9lO4OTN5IZAEW0uMnV_pbu96O_Z_2yr4")

@bot.message_handler(commands=['start'])
def welcome(message):
    # sti = open('sticker.webp', 'rb')
    # bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Ты шо не играл с нами???")
    item2 = types.KeyboardButton("Давай поиграеш с нами(((")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, f"Даров Братюня, что бы узнать все функции бота напиши /help {message.from_user.first_name}!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)



@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id, "1. /trollface, 2. /lol, /speed, Create, Play, /Night, Mouse, /weather, /anekdot, town, /maps, /google  ")





@bot.message_handler(commands=['trollface'])
def send_welcome(message):
    stiq = open('trollface-quest.webp', 'rb')
    bot.send_sticker(message.chat.id, stiq)

@bot.message_handler(commands=['lol'])
def welcome(message):
    bot.send_message(message.chat.id, "– Фима, я шубу хочу! – Софа, ты ж оливье еще не доела!")

@bot.message_handler(commands=['speed'])
def lalala(message):
    if bot.send_message(message.chat.id == "https://www.speedtest.net"):


    elif
@bot.message_handler(content_types=['Create'])
def create(message):
    message.text.lower == ("Хочешь узнать где был создан этот бот?")
    bot.send_message(message.chat.id, 'В Python')

    elif
@bot.message_handler(content_types=['Play'])
def play(message):
    message.text.lower == ("Ты поиграть хочешь?")
    bot.send_message(message.chat.id, 'https://vseigru.net')

    elif
@bot.message_handler(commands=['Night'])
def send_night(message):
    stiq = open('zvuki-nochnogo-lesa-29626.mp3', 'rb')
    bot.send_audio(message.chat.id. stiq)

    elif
@bot.message_handler(content_types=['Mouse'])
def send_link(message):
    message.text.lower == ("Моя мышка")
    bot.send_message(message.chat.id, 'https://hotline.ua/ua/computer-myshi-klaviatury/a70-bloody-crackle/')

    elif
@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.chat.id, "https://sinoptik.ua/погода-киев")

    elif
@bot.message_handler(commands=['anekdot'])
def anekdot(message):
    bot.send_message(message.chat.id, "Всё-таки это дети должны отдыхать на природе, а не природа на детях.")

    elif
@bot.message_handler(content_types=['town'])
def towm(message):
    message.text.lower == (Перевод)
    bot.send_message(message.chat.id, "town это город:)")

    elif
@bot.message_handler(commands=['maps'])
def maps(message):
    bot.send_message(message.chat.id, "https://www.google.de/maps/preview")

    elif

@bot.message_handler(commands=['google'])
def google(message):
    bot.send_message(message.chat.id, "https://www.google.com")



     else:
         bot.send_message(message.chat.id, 'Я не понимаю что ты от меня хочешь. Ты какой то странный')



        
bot.polling()