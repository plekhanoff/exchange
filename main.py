

import telebot

TOKEN = "6523102768:AAGprogp1UDnCeUDfPqjTVxBZP0K8gv5w0s"

bot = telebot.TeleBot(TOKEN)


bot.polling(none_stop=True)
import telebot

TOKEN = "6523102768:AAGprogp1UDnCeUDfPqjTVxBZP0K8gv5w0s"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(filter)
def function_name(message):
    bot.reply_to(message, "This is a message handler")
    import telebot
    bot = telebot.TeleBot("TOKEN")


    @bot.message_handler(commands=['start', 'help'])
    def handle_start_help(message):
        pass


    @bot.message_handler(content_types=['voice', 'audio'])
    def handle_docs_audio(message):
        bot.send_massage(massage.chat.id,"Голос как у алкаша")


    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.send_message(message.chat.id, f"Привет, {message.chat.username}")
        import telebot

        bot = telebot.TeleBot('TOKEN')

        @bot.message_handler(content_types=['photo', ])
        def say_lmao(message: telebot.types.Message):
            bot.reply_to(message, 'Nice meme XDD')

        bot.polling(none_stop=True)