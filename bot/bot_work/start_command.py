from logging import Logger
from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from db_analyst.models import User_verification, Purposes
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger: Logger = logging.getLogger(__name__)


machine, apartment, vacation, another_target = range(4)

GOAL, DATE, INCOME = range(3)


def start(update, context, button=None):
    chat = update.effective_chat
    name = update.message.chat.first_name
    User_verification.objects.get_or_create(user_id=chat.id, activating_bot=True, name=name, goal=True, price=True, income=True, data=True)
    button = ReplyKeyboardMarkup([['/ready_to_chat'], ['/cancel'], ['/help']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Я бот, который позволит тебе проанализировать бюджет при постановки цели.\n'
             'При нажатии "/ready_to_chat" подтверждаете , что у вас есть цель.\n'
             'Если нет цели, нажмите "/cancel", распрощаемся.\n'
             'Если возникнут вопросы, то ты всегда можешь нажать "/help".\n'.format(name),
        reply_markup=button
    )


def ready_to_chat(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    price = int()
    User_verification.objects.get_or_create(user_id=chat.id, price=price)
    context.bot.send_message(
        chat_id=chat.id,
        text="Какая сумма нужна для реализации цели? (формат записи-> 200000) \n"
        "Команда /cancel, чтобы прекратить разговор.".format(name),

    )
    return GOAL


def help(update, context, button=None):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/ready_to_chat'], ['/cancel']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Давай расскажу тебе подробнее чем я занимаюсь: \n'
             'Команда ready_to_chat необходима для того, чтобы запустить процесс расчета твоих финансовых трат. \n'
             'Врезультате получите отчет как правельно распорядится своим доходом \n'
             'Eсли интересно нажатии команды "/ready_to_chat", готов к общению.\n'
             'Если нет, нажатии команды "/cancel", распрощаемся.\n'.format(name),
        reply_markup=button
    )


def cancel(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text='Досвидания! {}'.format(name),

    )


def goal(update, context):
    income = int()
    User_verification.objects.get_or_create(income=income)
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=
        "Укажите доход в месяц? (формат записи-> 200) \n"
        "Команда /cancel, чтобы прекратить разговор."
    )
    return DATE


def date(update, context):
    date= int()
    User_verification.objects.get_or_create(date=date)
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=
        "Какая дата цели? (формат записи-> 12.12.23)\n"
        "Команда /cancel, чтобы прекратить разговор.")
    return INCOME


def income(update, context):
    income(int)
    User_verification.objects.get_or_create(income=income)
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text="Какай у вас доход в месяц? (формат записи-> 100)\n"
             "Команда /cancel, чтобы прекратить разговор.")
    return ConversationHandler.END
