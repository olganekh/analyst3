from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from analyst_bot.settings import TOKEN_TELEGRAM_BOT_API
from bot.bot_work.start_command import start, cancel, help, goal, date, income, DATE, INCOME, GOAL, ready_to_chat


def run_bot():
    """Основа бота: прокинули токен, подкючили команду старт, создали пулинг"""
    updater = Updater(TOKEN_TELEGRAM_BOT_API)
    dp = updater.dispatcher
    # dp.add_handler(CommandHandler('goal', goal))
    # dp.add_handler(CommandHandler('help', help))

    dp.add_handler(CommandHandler('start', start))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('ready_to_chat', ready_to_chat)],
        states={
            GOAL: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, goal)],
            DATE: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, date)],
            INCOME: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, income)],

        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler('help', help))
    updater.start_polling()
    updater.idle()
