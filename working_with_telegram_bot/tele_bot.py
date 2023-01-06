from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands



app = ApplicationBuilder().token("5953595197:AAFQ4dRDweB3iE-eaHwl709mM97WEuf4BLg").build()



async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Choose options that you want to calculate with\n" )
    await update.message.reply_text(f"Currently there is following commands:\n/plus\n/minus\n/mult\n/div")
    app.add_handler(CommandHandler("plus", bot_commands.sum_command))
    app.add_handler(CommandHandler("minus", bot_commands.minus_command))
    app.add_handler(CommandHandler("mult", bot_commands.multiply_command))
    app.add_handler(CommandHandler("div", bot_commands.divide_command))




app.add_handler(CommandHandler("hello", bot_commands.hello))
app.add_handler(CommandHandler("help", bot_commands.help))
app.add_handler(CommandHandler("time", bot_commands.time))
app.add_handler(CommandHandler("calc", calc_command))

print("Running")
app.run_polling()