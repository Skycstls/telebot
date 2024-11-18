from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
allowed_user_id = int(os.getenv("ALLOWED_USER_ID"))

async def check_user(update: Update) -> bool:
    if update.effective_user.id != allowed_user_id:
        await update.message.reply_text("No tienes permiso para usar este bot.")
        return False
    return True

async def saludo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await check_user(update):
        return
    await update.message.reply_text(f"¡Hola, {update.effective_user.first_name}!")

async def random_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await check_user(update):
        return
    numero = random.randint(1, 100)
    await update.message.reply_text(f"Tu número aleatorio es: {numero}")

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await check_user(update):
        return
    await update.message.reply_text("Por favor, envía el dominio a escanear:")

async def handle_scan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await check_user(update):
        return
    domain = update.message.text
    try:
        resultados = subprocess.run(["./scan.sh", domain], capture_output=True, text=True, check=True)
        await update.message.reply_text(resultados.stdout)
    except subprocess.CalledProcessError as e:
        await update.message.reply_text(f"Error al ejecutar el script: {e.stderr}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await check_user(update):
        return
    keyboard = [
        [KeyboardButton("Saludo"), KeyboardButton("Número Aleatorio")],
        [KeyboardButton("Scan")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Elige una opción:", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await check_user(update):
        return
    text = update.message.text
    if text == "Saludo":
        await saludo(update, context)
    elif text == "Número Aleatorio":
        await random_number(update, context)
    elif text == "Scan":
        await scan(update, context)
    else:
        await handle_scan(update, context)

def main():
    app = ApplicationBuilder().token(api_key).build()
    # Comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("saludo", saludo))
    app.add_handler(CommandHandler("random", random_number))
    app.add_handler(CommandHandler("scan", scan))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("El bot está corriendo...")
    app.run_polling()

if __name__ == "__main__":
    main()