import openai
import telegrampy
from telegrampy.ext import Updater, CommandHandler, MessageHandler, Filters

# Initialize OpenAI API key
openai.api_key = "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"

# Define the Telegram bot token
token = "6137184657:AAGQVBWMQOGzd_Bq5Isgthxz3tGBN0xx3Iw"

# Initialize the bot and the updater
bot = telegram.Bot(token)
updater = Updater(token, use_context=True)

# Define the handler function for the chatbot
def chatbot(update, context):
    # Get the user's message
    user_message = update.message.text

    # Use OpenAI to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="How can I help you with " + user_message + "?",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    # Send the response back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Add the handler to the dispatcher
updater.dispatcher.add_handler(MessageHandler(Filters.text, chatbot))

# Start the bot
updater.start_polling()
