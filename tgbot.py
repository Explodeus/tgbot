import telebot
import pyowm


owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language= "ru")
bot = telebot.TeleBot("774300938:AAH4EBgC1_GLetGrT8x8ksDgrmVeOx-ppO8")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    tempr = w.get_temperature('celsius')["temp"]
    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"

    answer += "Температура сейчас в районе " + str(tempr) + "\n"
    if tempr < 10:
	    answer += 'Капец как холодно, одевайся как танк!'
    elif tempr < 20:
	    answer += "Холодновато, одевайся потеплее"
    else:
	    answer += "Сейчас тепло, одевай что угодно"

	#bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)