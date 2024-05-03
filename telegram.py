import telebot
import time


# Configura tu token de acceso del bot
token = "6748261723:AAGMdMHtf-BUT17a1E3KJ86DOjpUxWn1zD4"
bot = telebot.TeleBot(token)  # La clase se llama TeleBot, no Telebot

# Envía un mensaje
chat_id = '6491419713'
mensaje = 'Alerta! producto: '





def alerta(precio,enlace,tiempo):
    print("ALERTA")
    mensaje = 'Alerta! producto: '
    mensaje = mensaje + enlace
    bot.send_message(chat_id, mensaje)  # Corregir el parámetro chat_id
