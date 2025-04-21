
import os
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")
COINS_FILE = "coins.json"

# Load or initialize coin data
def load_coins():
    if os.path.exists(COINS_FILE):
        with open(COINS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_coins(coins):
    with open(COINS_FILE, "w") as f:
        json.dump(coins, f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey kanka, InstaTrim'e hoş geldin! Coinlerin hazır, başlıyor muyuz?")

async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    coins = load_coins()
    current = coins.get(user_id, 0)
    await update.message.reply_text(f"{update.effective_user.first_name}, şu an {current} coin'in var.")

async def giris(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    coins = load_coins()
    current = coins.get(user_id, 0)
    coins[user_id] = current + 5
    save_coins(coins)
    await update.message.reply_text("Giriş yaptın! Bugünlük +5 coin cebe yazıldı.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("coin", coin))
    app.add_handler(CommandHandler("giris", giris))
    app.run_polling()

if __name__ == "__main__":
    main()
