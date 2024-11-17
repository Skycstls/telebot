from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

async def saludo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"¡Hola, {update.effective_user.first_name}!")

async def random_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    numero = random.randint(1, 100)
    await update.message.reply_text(f"Tu número aleatorio es: {numero}")

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    domain = context.args[0]
    try:
        resultados = subprocess.run(["./scan.sh", domain], capture_output=True, text=True, check=True)
        await update.message.reply_text(resultados.stdout)
    except subprocess.CalledProcessError as e:
        await update.message.reply_text(f"Error al ejecutar el script: {e.stderr}")

def main():
    app = ApplicationBuilder().token(api_key).build()
    # Comandos
    app.add_handler(CommandHandler("saludo", saludo))
    app.add_handler(CommandHandler("random", random_number))
    app.add_handler(CommandHandler("scan", scan))
    print("El bot está corriendo...")
    app.run_polling()

if __name__ == "__main__":
    main()