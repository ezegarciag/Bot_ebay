import telebot
import time


# Configura tu token de acceso del bot
token = ""
bot = telebot.TeleBot(token)  # La clase se llama TeleBot, no Telebot

# Envía un mensaje
chat_id = ''
mensaje = 'Alerta! producto: '





def alerta(precio,enlace,tiempo):
    print("ALERTA")
    mensaje = 'Alerta! producto: '
    mensaje = mensaje + enlace
    bot.send_message(chat_id, mensaje)  # Corregir el parámetro chat_id
