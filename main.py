import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# 🔑 Environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
ACR_API_KEY = os.getenv("ACR_API_KEY")
ACR_HOST = "identify-eu-west-1.acrcloud.com"  # Default region

async def start(update: Update, context):
    await update.message.reply_text(
        "👋 হ্যালো! আমি Song Finder Bot 🎶\n"
        "আমাকে যেকোনো ভিডিও লিংক পাঠাও (যেমন YouTube, TikTok, Instagram), আমি বলে দেব কোন গানটা ব্যবহার হয়েছে!"
    )

async def find_song(update: Update, context):
    user_msg = update.message.text
    await update.message.reply_text("🔍 গান খোঁজা হচ্ছে... একটু অপেক্ষা করো 🎧")

    # ডেমো হিসেবে আমরা শুধু টেক্সট show করছি, অডিও extract করার কোড চাইলে পরে যুক্ত করা যাবে
    # এখানে সরাসরি API তে পাঠানো যেতে পারে যদি তোমার কাছে audio bytes থাকে

    # For now:
    await update.message.reply_text(
        "⚠️ বর্তমানে demo মোড চলছে। Audio analysis কোড যুক্ত করলে আমি গান চিনে ফেলব!"
    )

async def help_command(update: Update, context):
    await update.message.reply_text("ℹ️ শুধু ভিডিও লিংক পাঠাও, আমি বলে দেব কোন গান চলছে 🎶")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, find_song))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
