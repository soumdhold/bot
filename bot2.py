#!/usr/bin/python3
# -*- Coding: utf-8 -*-
from telebot import TeleBot
from telebot import types


bot = ('1498467565:AAFaJoWM19P8pcbX8G7qz8lr_eO6is83Icw')


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
	markup = types.InlineKeyboardMarkup()
	btn_my_site= types.InlineKeyboardButton(text='🔥 Наличие 🔥', url='https://t.me/SmokeLab_Wro_presence')
	markup.add(btn_my_site)
	btn_my_site4= types.InlineKeyboardButton(text='🛍 Аксесуары 🛍', url='https://t.me/sl_wroclaw_accessories')
	markup.add(btn_my_site4)
	btn_my_site2= types.InlineKeyboardButton(text='💸 Заказать 💸', url='https://t.me/SmokeLaboratory_Wroclaw')
	markup.add(btn_my_site2)
	btn_my_site3= types.InlineKeyboardButton(text='📸 Инстаграмм 📸', url='https://instagram.com/smokelaboratory_wroclaw?igshid=1hi8r8o228cjz')
	markup.add(btn_my_site3)
	first_name = message.new_chat_members[0].first_name
	bot.send_message(message.chat.id, "Добро пожаловать 👋, {0}! Рады приветствовать вас в SmokeLaboratory_Wroclaw. \n    У нас вы найдете только лучшие табаки и кальяны. \nПосмотреть наличие и сделать заказ можно по кнопкам ниже. Также подписывайтесь на наш Инстаграмм что бы не пропустить акции и поднять себе настроение! \nВсем дымного 💨💨💨 ".format( first_name), reply_markup=markup)


if __name__ == '__main__':
	bot.polling(none_stop=True)

