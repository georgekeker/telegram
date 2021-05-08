from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardRemove
from telegram import ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import Updater 
from telegram.ext import Filters
from telegram.ext import MessageHandler

button_dz_1 = "дз на 1 марта "


def message_handler(update: Update, context:CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text=button_dz_1),
            ],
            
        ],
        resize_keyboard=True,
    )

    update.message.reply_text(
        text="1+2=3 ,3+76 = 79 , 545+455=1000",
        reply_markup=reply_markup,
        )

def main():
    updater=Updater(
        token ="1740318020:AAF1pIZguJv2U6JK8duZPvSPQXYSqoSeV68",
        use_context=True,              #обновляет
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle() 

if __name__=="__main__":
    main()
