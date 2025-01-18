#import
import telebot
from telebot import types
import os
import platform
import socket
import pyautogui
import ctypes


bot =telebot.TeleBot("TOKEN")
my_screenshot =open("screenshot.png", encoding="utf-8")

#crate main function for command "start"

@bot.message_handler(commands=["start"])
def main(message):
    if message.from_user.first_name != "Vesel4ak":
        bot.send_message(message.chat.id,f"Welcome, {message.from_user.first_name}.To see my commands, write the command /show")
        return

#crate main function for command "show"

@bot.message_handler(commands=["show"])
def show(message):
    markup = types.ReplyKeyboardMarkup()
    

    button_1 = types.KeyboardButton("Shutdown")
    button_2 = types.KeyboardButton("Reboot")
    button_3 = types.KeyboardButton("Computer lock")
    
    button_4 = types.KeyboardButton("Screenshot")
    button_5 = types.KeyboardButton("System Information")
    button_6 = types.KeyboardButton("Open Command Prompt")
    
    button_7 = types.KeyboardButton("Minimize all windows")
    button_8 = types.KeyboardButton("Close current tab")
    button_9 = types.KeyboardButton("Open Quick Settings")


    markup.row(button_1, button_2, button_3)  # 1 ряд

    markup.row(button_4, button_5, button_6)

    markup.row(button_7, button_8, button_9)
    bot.send_message(message.chat.id, "Показзываю все мои команды:",reply_markup=markup)
    return

#crate main function for events

@bot.message_handler()
def on_click(message):
    if message.text == "Shutdown":
        os.system("shutdown /s /t 1")
        bot.send_message(message.chat.id , "Device is off")
        return
    elif message.text == "Reboot":
        os.system("shutdown/r/t 1")
        bot.send_message(message.chat.id , "Reboot has already started")
        return
    elif message.text == "Computer lock":
        ctypes.windll.user32.LockWorkStation()
        bot.send_message(message.chat.id ,"Computer is locked!")
        return
    
    
    elif message.text == "Screenshot":
        my_screenshot = pyautogui.screenshot("screenshot.png")
        bot.send_photo(message.chat.id , my_screenshot)
        bot.send_message(message.chat.id "Here is a screenshot just taken on the device")
    elif message.text == "System information":
        bot.send_message(message.chat.id "The information about your computer is as follows:\n"
         f"\Computer name: {socket.gethostname()}"


bot.infunity_polling()
