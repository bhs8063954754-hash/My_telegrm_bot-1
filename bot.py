from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

app = Client(
    "file_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

keyboard = ReplyKeyboardMarkup(
    [
        ["📤 Upload File", "📂 Check Files"],
        ["📊 Statistics"]
    ],
    resize_keyboard=True
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "📤 Universal File Upload Bot\n\nSend me any file.",
        reply_markup=keyboard
    )

@app.on_message(filters.document | filters.video | filters.audio | filters.photo)
async def upload(client, message):
    msg = await message.reply_text("⏳ Uploading...")
    path = await message.download(file_name=DOWNLOAD_DIR)
    await msg.edit_text(f"✅ File uploaded:\n`{path}`")

app.run()
