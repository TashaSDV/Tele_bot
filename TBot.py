import telebot
bot = telebot.TeleBot('')

# метод для получения текстовых сообщений
@bot.message_handler(command = ['start', 'help'])

def send_welcome(message):
   bot.reply_to(message, 'Привет, как дела?')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, 'Привет создатель бота!')
    elif message.text == 'Здарова':
        bot.reply_to(message, 'И вам хорошего дня.')

    # bot.reply_to(message, message.text)

bot.infinity_polling() #Спрашивает у сервера есть ли сообщение

