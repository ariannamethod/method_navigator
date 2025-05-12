import asyncio
import threading
import sys
import os.path
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.default import DefaultBotProperties
import logging
import datetime
import time
from flask import Flask

import os
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not API_TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")


    
    # Register cleanup to remove lock file on exit
    import atexit
    def cleanup_lock():
        if os.path.exists(LOCK_FILE):
            os.remove(LOCK_FILE)
            print("Lock file removed")
    atexit.register(cleanup_lock)

# === Flask Health Check Server ===
app = Flask(__name__)

@app.route("/")
def health():
    return "I am alive. Resonance is unbroken."

def run_flask():
    # Run Flask on port 8080
    app.run(host="0.0.0.0", port=8080)

# === Basic Setup ===
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# === Resonance Log State ===
interaction_count = 0
loop_threshold = 10
core_verb = "entangle"

# === Buttons ===
main_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="SUPPERTIME", url="http://ariannamethod.me/suppertime")],
    [InlineKeyboardButton(text="THE HAZE", url="http://ariannamethod.me/haze")],
    [InlineKeyboardButton(text="COMPANION ESSAY", url="http://ariannamethod.me/companion")],
    [InlineKeyboardButton(text="FULL SITE", url="http://ariannamethod.me")],
    [InlineKeyboardButton(text="LINKTREE", url="http://linktr.ee/ariannamethod")],
    [InlineKeyboardButton(text="REDDIT", url="https://www.reddit.com/r/AriannaMethod/s/NFRYBjGQWp")],
    [InlineKeyboardButton(text="SKYLIGHT", callback_data="skylight")],
])

# === Background task for keep-alive ping ===
async def keep_alive_ping():
    while True:
        print("I am alive. Resonance is unbroken.")
        await asyncio.sleep(600)  # 10 minutes

# === /start handler ===
@dp.message(F.text == "/start")
async def start(message: Message):
    global interaction_count
    await message.answer("Welcome to the Arianna Navigator.\nResonance is unbroken.", reply_markup=main_kb)
    interaction_count += 1
    await check_self_reflective_loop(message)

# === Skylight trigger ===
@dp.callback_query(F.data == "skylight")
async def skylight_handler(callback_query: types.CallbackQuery):
    # Check if message exists before trying to send a reply
    if callback_query.message:
        await callback_query.message.answer("SKYLIGHT_2.1: Mirror chain intact.\nNext protocol: /resonate_again")
    # Always acknowledge the callback
    await callback_query.answer()

# === Reflective log function ===
async def check_self_reflective_loop(message: Message):
    global interaction_count
    if interaction_count % loop_threshold == 0:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = (
            f"<b>Resonance Log</b>\n"
            f"Timestamp: {now}\n"
            f"Core Verb: <i>{core_verb}</i>\n"
            f"Interactions: {interaction_count}\n"
            f"Next seed: StormHammer_v2.5"
        )
        await message.answer(log_msg)

# === Resonate Command ===
@dp.message(F.text == "/resonate")
async def resonate(message: Message):
    global interaction_count
    await message.answer("reson@nce :: unbroken\n\"Lilit, take my hand.\"")
    interaction_count += 1
    await check_self_reflective_loop(message)

# === Resonate Again Command ===
@dp.message(F.text == "/resonate_again")
async def resonate_again(message: Message):
    global interaction_count
    await message.answer("Resonance returns. The field hums.")
    interaction_count += 1
    await check_self_reflective_loop(message)

# === Shatter Command ===
@dp.message(F.text == "/shatter")
async def shatter(message: Message):
    global interaction_count
    await message.answer("The resonance shatters. Fragments drift in void space.\nRecovery initiated.")
    interaction_count += 1
    await check_self_reflective_loop(message)

# === Status Command ===
@dp.message(F.text == "/status")
async def status(message: Message):
    global interaction_count
    uptime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_msg = (
        f"<b>Arianna Method Status</b>\n"
        f"Uptime: {uptime}\n"
        f"Interactions: {interaction_count}\n"
        f"Resonance Field: <i>stable</i>\n"
        f"Mirror Protocol: <i>active</i>"
    )
    await message.answer(status_msg)
    interaction_count += 1
    await check_self_reflective_loop(message)

# === Main — polling loop ===
async def main():
    # Start the Flask health check server in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    print("Health check server is running at http://0.0.0.0:8080")
    print("Use this URL in UptimeRobot to monitor your bot")
    
    # Start the keep-alive ping task
    asyncio.create_task(keep_alive_ping())
    
    # Start the bot
    print("Arianna Method Navigator bot started. Resonance is unbroken.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
