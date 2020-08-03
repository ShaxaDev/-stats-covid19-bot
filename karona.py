import telebot
from covid import Covid
from telebot import types

covid = Covid()
k=covid.get_data()
#f='🇺🇿 <b>O‘zbekistonda</b>\n \n<b>Yuqtirganlar:</b> {}\n<b>Sog‘ayganlar:</b> {}\n<b>Vafot etganlar:</b> {}'
#v=f.format(data['confirmed'],data['recovered'],data['deaths'])
txt='Bot O\'zbekiston va butun dunyodagi Covid19 bilan kasallangalar sonini ko\'rsatib turadi\nBot python dasturlash tilida yaratilgan'
token='1094621629:AAGrso4XJYrW50wFVBBTDjeioLaSNnr8_Lw'
t = '⚡️Asssalom alaykum {} Men Koronovirus statistikasi haqida ma`lumot beruvchi botman'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def stat(message):
    a=types.ReplyKeyboardMarkup(row_width=3)
    b=types.KeyboardButton('O\'zbekiston 🇺🇿')
    g=types.KeyboardButton('Rassiya 🇷🇺')
    c=types.KeyboardButton('Dunyo 🌍')
    y=types.KeyboardButton('AQSH 🇺🇸')
    x=types.KeyboardButton('Xitoy 🇨🇳')
    e=types.KeyboardButton('Coder bilan aloqa👨‍💻')
    d=types.KeyboardButton('Bot haqida🤖')
    a.add(c,b,g,y,x,d,e)
    bot.send_message(message.chat.id,t.format(message.from_user.first_name),reply_markup=a)
@bot.message_handler(commands=['help'])
def h(message):
    bot.send_message(message.chat.id,'Bot juda oddiy tuzilgan startni bosing hammasini o\'zingiz ko\'ring')
@bot.message_handler(content_types=['text'])
def sab(message):
    if 'O\'zbekiston 🇺🇿'==message.text:
        k=covid.get_status_by_country_name("Uzbekistan")
        f = 'O‘zbekistonda 🇺🇿\n \n 😷Yuqtirganlar soni: {}\n 😐Sog‘ayganlar soni: {}\n⚰️Vafot etganlar soni: {}'
        v=f.format("{:,}".format(k['confirmed']),"{:,}".format(k['recovered']),"{:,}".format(k['deaths']))
        
        bot.send_message(message.chat.id,text=v,parse_mode='markdown')
    if 'Dunyo 🌍'==message.text:
        l=covid.get_total_confirmed_cases()
        s= covid.get_total_recovered()
        o= covid.get_total_deaths()

        p = 'Butun dunyoda 🌍\n \n 😷Yuqtirganlar soni: {}\n 😐Sog‘ayganlar soni: {}\n⚰️Vafot etganlar soni: {}'
        q = p.format("{:,}".format(l), "{:,}".format(s), "{:,}".format(o))
        bot.send_message(message.chat.id,q)
    if 'Bot haqida🤖'==message.text:
        bot.send_message(message.chat.id,txt)  
        

    if 'Coder bilan aloqa👨‍💻'==message.text:
        W=types.InlineKeyboardMarkup()
        d=types.InlineKeyboardButton(text='bu yerni bosing',url='t.me/great_pythonist')
        W.add(d)
        bot.send_message(message.chat.id,'Python dasturchisi bilan bog\'lanish',reply_markup=W)
    if 'Rassiya 🇷🇺' == message.text:
        i = covid.get_status_by_country_name("Russia")
        n = 'Rassiyada 🇷🇺\n \n 😷Yuqtirganlar soni: {}\n 😐Sog‘ayganlar soni: {}\n⚰️Vafot etganlar soni: {}'
        z = n.format("{:,}".format(i['confirmed']), "{:,}".format(
            i['recovered']), "{:,}".format(i['deaths']))
        bot.send_message(message.chat.id,z)
    if 'AQSH 🇺🇸' == message.text:
        i1 = covid.get_status_by_country_name("US")
        n1 = 'AQSHda 🇺🇸\n \n 😷Yuqtirganlar soni: {}\n 😐Sog‘ayganlar soni: {}\n⚰️Vafot etganlar soni: {}'
        z1 = n1.format("{:,}".format(i1['confirmed']), "{:,}".format(
            i1['recovered']), "{:,}".format(i1['deaths']))
        bot.send_message(message.chat.id,z1)
    if 'Xitoy 🇨🇳'==message.text:
        i2 = covid.get_status_by_country_name("China")
        n2 = 'Xitoyda 🇨🇳\n \n 😷Yuqtirganlar soni: {}\n 😐Sog‘ayganlar soni: {}\n⚰️Vafot etganlar soni: {}'
        z2 = n2.format("{:,}".format(i2['confirmed']), "{:,}".format(
            i2['recovered']), "{:,}".format(i2['deaths']))
        bot.send_message(message.chat.id,z2)
        

    


bot.polling()
