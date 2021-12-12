#!/usr/bin/python3
# -*- Coding: utf-8 -*-
bot.remove_webhook()
from telebot import TeleBot
from telebot import types


bot = TeleBot('1498467565:AAFaJoWM19P8pcbX8G7qz8lr_eO6is83Icw')

@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
	markup = types.InlineKeyboardMarkup()
	btn_my_site= types.InlineKeyboardButton(text='🔥 НАЛИЧИЕ ТАБАКА/LISTA SMAKÓW 🔥', url='https://t.me/HookahHub_Wroclaw_presens')
	markup.add(btn_my_site)
	btn_my_site4= types.InlineKeyboardButton(text='🛍 АКСЕССУАРЫ/AKCESORIA 🛍', url='https://t.me/HookahHub_Wroclaw_ace')
	markup.add(btn_my_site4)
	btn_my_site5= types.InlineKeyboardButton(text='💨 КАЛЬЯНЫ/FAJKI WODNE 💨', url='https://t.me/HookahHub_wroclaw_hookah')
	markup.add(btn_my_site5)
	btn_my_site6= types.InlineKeyboardButton(text='💸 КОЛБЫ/WAZONY 💸', url='https://t.me/HookahHub_Wroclaw')
	markup.add(btn_my_site6)
	btn_my_site7= types.InlineKeyboardButton(text='☄️ ОДНОРАЗКИ/E-PODS ☄️', url='https://instagram.com/hookahhub_wroclaw?utm_medium=copy_link')
	markup.add(btn_my_site7)
	btn_my_site2= types.InlineKeyboardButton(text='💸 ЗАКАЗАТЬ/ZAMÓWIĆ 💸', url='https://t.me/HookahHub_Wroclaw')
	markup.add(btn_my_site2)
	btn_my_site3= types.InlineKeyboardButton(text='📸 INSTAGRAM 📸', url='https://instagram.com/hookahhub_wroclaw?utm_medium=copy_link')
	markup.add(btn_my_site3)
	first_name = message.new_chat_members[0].first_name
	bot.send_message(message.chat.id, "Добро пожаловать 👋, {0}! Рады приветствовать вас в HookahHub_Wroclaw. \nУ нас вы найдете только лучшие табаки и кальяны. Вас ждёт много акций и приятных сюрпризов🎁!!!\n Посмотреть наличие и сделать заказ можно по кнопкам ниже. Также подписывайтесь на наш Инстаграмм что бы не пропустить акции и поднять себе настроение! \nВсем дымного 💨💨💨 ".format( first_name), reply_markup=markup)


if __name__ == '__main__':
	bot.polling(none_stop=True)

