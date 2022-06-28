import random
import telebot

from telebot import types

bot = telebot.TeleBot("5306516189:AAGR8ZIEGTrwJ4Ovv4vmo-EB5VADicfARjg")

@bot.message_handler(commands=["roll"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("d20")
    item2 = types.KeyboardButton("d10")
    item3 = types.KeyboardButton("d100")
    item4 = types.KeyboardButton("d12")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    bot.send_message(message.chat.id, "Let us roll!", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def echo(message):
    a = message.text
    a = a.lower()
    if a == "roll d20" or a == "d20":
        a = random.randint(1, 20)
        bot.send_message(message.chat.id, a)
    elif a == "roll d100" or a == "d100":
        a = random.randint(1, 100)
        bot.send_message(message.chat.id, a)
    elif a == "roll d10" or a == "d10":
        a = random.randint(1, 10)
        bot.send_message(message.chat.id, a)
    elif a == "roll d12" or a == "d12":
        a = random.randint(1, 12)
        bot.send_message(message.chat.id, a)
    else:
        bot.send_message(message.chat.id, "error")

    @bot.message_handler(commands=["maps"])
    def maps(message):
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("Waterdeep")
         item2 = types.KeyboardButton("Sword Coast")
         item3 = types.KeyboardButton("Neverwinter")
         item4 = types.KeyboardButton("Baldur´s Gate")
         markup.add(item1)
         markup.add(item2)
         markup.add(item3)
         markup.add(item4)
         bot.send_message(message.chat.id, "Choose a map!", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def echo(message):
    a = message.text
    a = a.lower()
    chat_id = message.chat.id
    if a == "Waterdeep" or a == "1":
        bot.send_photo(chat_id, "https://drive.google.com/file/d/12yJgFI9aHc3gOFudboGw6nLpx-PVeULX/view?usp=sharing")
    elif a == "Sword Coast" or a == "2":
        bot.send_photo(chat_id, "https://drive.google.com/file/d/1uMGss-7bKiqKgdHHN6Op6vIr8uDT5HSp/view?usp=sharing")
    elif a == "Neverwinter" or a == "3":
        bot.send_photo(chat_id, "https://drive.google.com/file/d/1AqG1exBRN2198n8uc-zmS4Xl3wxW5L4m/view?usp=sharing")
    elif a == "Baldur´s Gate" or a == "4":
        bot.send_photo(chat_id, "https://drive.google.com/file/d/19YNJyjuErB_PmaYncKW8O5z0xvYLlfQn/view?usp=sharing")
    else:
        bot.send_message(message.chat.id, "error")


bot.polling(none_stop=True, interval=0)

