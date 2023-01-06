from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands



app = ApplicationBuilder().token("5953595197:AAFQ4dRDweB3iE-eaHwl709mM97WEuf4BLg").build()



async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Choose options that you want to calculate with\n"
                                    "1.+\n"
                                    "2.-\n"
                                    "3.*\n"
                                    "4./\n")
    msg = update.message.text

    if msg == '1':
        app.add_handler(CommandHandler("calc", bot_commands.sum_command))
    elif msg == '2':
        app.add_handler(CommandHandler("calc", bot_commands.minus_command))
    elif msg == '3':
        app.add_handler(CommandHandler("calc", bot_commands.multiply_command))
    elif msg == 4:
        app.add_handler(CommandHandler("calc", bot_commands.devide_command))




app.add_handler(CommandHandler("hello", bot_commands.hello))
app.add_handler(CommandHandler("help", bot_commands.help))
app.add_handler(CommandHandler("time", bot_commands.time))
app.add_handler(CommandHandler("calc", calc_command))

print("Running")
app.run_polling()