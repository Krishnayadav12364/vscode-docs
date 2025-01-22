import logging
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Replace with your bot token
BOT_TOKEN = 6755738221:AAEFAM92xuOYj7KyF77yFKQQO9MxyFXt42g"YOUR_BOT_TOKEN_HERE"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
        )

        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
            """Send a message when the command /start is issued."""
                user = update.effective_user
                    await update.message.reply_html(
                            rf"Hi {user.mention_html()}!",
                                    reply_markup=ForceReply(selective=True),
                                        )

                                        async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                            """Send a message when the command /help is issued."""
                                                await update.message.reply_text("Help!")

                                                async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                                    """Echo the user message."""
                                                        await update.message.reply_text(update.message.text)


                                                        def main():
                                                            """Start the bot."""
                                                                application = ApplicationBuilder().6755738221:AAEFAM92xuOYj7KyF77yFKQQO9MxyFXt42g(BOT_TOKEN).build()

                                                                    application.add_handler(CommandHandler("start", start))
                                                                        application.add_handler(CommandHandler("help", help_command))
                                                                            application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

                                                                                application.run_polling()


                                                                                if __namae__ == '__main__':
       han(hellohe)                                                                        main()

name
anshika
koun
