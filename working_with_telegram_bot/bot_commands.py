from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import log

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Currently there is following commands:\n/hello\n/help\n/time\n/sum')

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Current time is: {datetime.datetime.now().time()}')

async def sum_command (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items [2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def minus_command (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} - {y} = {x-y}')

async def multiply_command (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    await log(update,context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await  update.message.reply_text(f'{x} * {y} = {x*y}')
    
async def devide_command (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    await log(update,context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} / {y} = {x/y}')
    

