import telebot
from telebot import types
import os
import platform
import socket
import pyautogui
import ctypes


bot =telebot.TeleBot("TOKEN")
my_screenshot =open("screenshot.png", encoding="utf-8")

@bot.message_handler(commands=["start"])
def main(message):
    if message.from_user.first_name != "Vesel4ak":
        bot.send_message(message.chat.id,f"Добро пожаловать, {message.from_user.first_name}.Чтобы увидеть мои команды,пропишите команду /show")
        return
@bot.message_handler(commands=["show"])
def show(message):
    markup = types.ReplyKeyboardMarkup()

    button_1 = types.KeyboardButton("Завершение работы")
    button_2 = types.KeyboardButton("Перезагрузка")
    button_3 = types.KeyboardButton("Блокировка компьютера")

    button_4 = types.KeyboardButton("Снимок экрана")
    button_5 = types.KeyboardButton("Системная информация")
    button_6 = types.KeyboardButton("Открыть командную строку")

    button_7 = types.KeyboardButton("Свернуть все окна")
    button_8 = types.KeyboardButton("Закрыть текущую вкладку")
    button_9 = types.KeyboardButton("Открыть быстрые настройки")


    markup.row(button_1, button_2, button_3)  # 1 ряд

    markup.row(button_4, button_5, button_6)

    markup.row(button_7, button_8, button_9)
    bot.send_message(message.chat.id, "Показзываю все мои команды:",reply_markup=markup)
    return


@bot.message_handler()
def on_click(message):
    if message.text == "Завершение работы":
        os.system("shutdown /s /t 1")
        bot.send_message(message.chat.id, "Устройство выключено")
        return
    elif message.text == "Перезагрузка":
        os.system("shutdown /r /t 1")
        bot.send_message(message.chat.id, "Перезагрузка уже началась")
        return
    elif message.text == "Блокировка компьютера":
        ctypes.windll.user32.LockWorkStation()
        bot.send_message(message.chat.id,"Компьютер заблокирован!")
        return


    elif message.text == "Снимок экрана":
        my_screenshot = pyautogui.screenshot("screenshot.png")
        bot.send_photo(message.chat.id, my_screenshot)
        bot.send_message(message.chat.id,"Вот снимок экрана,только что сделаный на устройстве")
    elif message.text == "Системная информация":
        bot.send_message(message.chat.id, "Информация о твоём компьютере следующая:\n"
                                          f"\nИмя компьютера: {socket.gethostname()}"
                                          f"\nИмя пользователя: {socket.getfqdn()}"
                                          f"\nВаша опперационная система: {platform.system()}"
                                          f"\nВерсия вашей операционной системы: {platform.version()}"
                                          f"\nАрхитектура вашей системы: {platform.architecture()[0]}"
                                          f"\nВаш процессор: {platform.processor()}"
                                          f"\nПлатформа: {platform.platform()}"
                                          f"\nНомер и дата сборки: {platform.python_build()}"
                                          f"\nВаш компилятор: {platform.python_compiler()}")
        return
    elif message.text == "Открыть командную строку":
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("cmd")
        bot.send_message(message.chat.id, "Командная строка открыта!")
        return


    elif message.text == "Свернуть все окна":
        pyautogui.hotkey("winleft", "m")
        bot.send_message(message.chat.id, "Все окна свернуты!")
        return
    elif message.text == "Закрыть текущую вкладку":
        pyautogui.hotkey("alt","f4")
        bot.send_message(message.chat.id, "Текущая вкладка закрыта")
        return
    elif message.text == "Открыть быстрые настройки":
        pyautogui.hotkey("winleft","a")
        bot.send_message(message.chat.id, "Текущая вкладка закрыта")
        return

bot.infinity_polling()
