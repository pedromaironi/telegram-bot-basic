from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):

    update.message.reply_text('Hola humano')


if __name__ == '__main__':
    TOKEN = '1628014222:AAElsm7zvdVtiwktnPOAalTdDmCmJFa55dE';
    updater = Updater(TOKEN,use_context=True)

    # dispatcher = send actions
    dp = updater.dispatcher

    # add handler = manejador | This handler it executable when de user goes an action
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()