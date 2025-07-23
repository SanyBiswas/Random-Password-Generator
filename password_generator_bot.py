import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

def generate_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "হ্যালো! আমি পাসওয়ার্ড জেনারেটর বট।\n"
        "পাসওয়ার্ড পেতে /generate কমান্ড লিখুন।"
    )

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    password = generate_password()
    await update.message.reply_text(f"তোমার পাসওয়ার্ড: `{password}`", parse_mode='MarkdownV2')

if __name__ == '__main__':
    TOKEN = os.getenv("BOT_TOKEN")  # Render থেকে Environment Variable নিবে

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("generate", generate))

    print("বট চলছে...")
    app.run_polling()
