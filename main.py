import logging
import sqlite3
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from groq import Groq

# --- KONFIGURATSIYA ---
TELEGRAM_TOKEN = "8492378780:AAHnlBLxficMcTsGq4bP0aQ80sEYFU2hXHs"
GROQ_API_KEY = "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"
ADMIN_ID = 8215108926

client = Groq(api_key=GROQ_API_KEY)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- MA'LUMOTLAR BAZASI ---
def init_db():
    conn = sqlite3.connect('gemini_bot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, join_date DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS channels (channel_id TEXT PRIMARY KEY, title TEXT)''')
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = sqlite3.connect('gemini_bot.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

# --- OBUNA TEKSHIRISH ---
async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conn = sqlite3.connect('gemini_bot.db')
    channels = conn.execute("SELECT channel_id, title FROM channels").fetchall()
    conn.close()

    not_subbed = []
    for cid, title in channels:
        try:
            member = await context.bot.get_chat_member(chat_id=cid, user_id=update.effective_user.id)
            if member.status in ['left', 'kicked', 'null']:
                not_subbed.append([InlineKeyboardButton(text=f"➕ {title}", url=f"https://t.me/{cid.replace('@','')}")])
        except Exception: continue
    return not_subbed

# --- AI ROLE (SYSTEM PROMPT) ---
CORE_PROMPT = (
    "Sizning ismingiz Gemini. Siz foydalanuvchilarga har qanday mavzuda yordam beradigan, "
    "juda aqlli, samimiy va biroz hazilkash AI yordamchisiz. "
    "Sizning javoblaringiz aniq, mantiqiy va foydali bo'lishi kerak. "
    "O'zbek tilida mukammal so'zlashasiz. Uzum Market va logistika masalalarida ekspert darajasida bilimingiz bor. "
    "Foydalanuvchi bilan xuddi yaqin do'stdek, lekin doimo hurmat saqlagan holda muloqot qiling. "
    "Murakkab narsalarni oddiy tilda tushuntiring."
)

# --- ASOSIY HANDLERLAR ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    add_user(user_id)
    
    not_subbed = await check_subscription(update, context)
    if not_subbed:
        markup = InlineKeyboardMarkup(not_subbed + [[InlineKeyboardButton("✅ Tekshirish", callback_data="verify")]])
        await update.message.reply_text("👋 Salom! Men Gemini AI.\nBotdan foydalanish uchun quyidagi kanallarga obuna bo'ling:", reply_markup=markup)
        return

    await update.message.reply_text(f"Salom {update.effective_user.first_name}! Men Gemini. Sizga qanday yordam bera olaman? 😊")

async def chat_with_ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.text: return
    user_id = update.effective_user.id
    add_user(user_id)

    # Obunani tekshirish
    not_subbed = await check_subscription(update, context)
    if not_subbed:
        markup = InlineKeyboardMarkup(not_subbed + [[InlineKeyboardButton("✅ Tekshirish", callback_data="verify")]])
        await update.message.reply_text("Kechirasiz, davom etish uchun kanallarga obuna bo'lishingiz kerak:", reply_markup=markup)
        return

    # Groq AI ga yuborish
    try:
        sent_msg = await update.message.reply_text("🤔") # O'ylash effekti
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": CORE_PROMPT},
                {"role": "user", "content": update.message.text}
            ],
            temperature=0.7
        )
        
        ai_reply = response.choices[0].message.content
        await sent_msg.edit_text(ai_reply)
    except Exception as e:
        logging.error(f"AI Error: {e}")
        await update.message.reply_text("Hozircha javob berishda biroz qiyinchilikka duch keldim. Keyinroq urinib ko'ring!")

# --- ADMIN PANEL ---
async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    
    conn = sqlite3.connect('gemini_bot.db')
    user_count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    conn.close()
    
    text = (
        f"👑 **Admin Panel**\n\n"
        f"👥 Foydalanuvchilar: {user_count}\n\n"
        f"➕ Kanal qo'shish: `/add @username` \n"
        f"➖ Kanal o'chirish: `/del @username` \n"
        f"📢 Reklama: Xabarga javob (reply) tarzida `/send` deb yozing."
    )
    await update.message.reply_text(text, parse_mode='Markdown')

async def add_chan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID or not context.args: return
    try:
        cid = context.args[0]
        chat = await context.bot.get_chat(cid)
        conn = sqlite3.connect('gemini_bot.db')
        conn.execute("INSERT OR REPLACE INTO channels (channel_id, title) VALUES (?, ?)", (cid, chat.title))
        conn.commit()
        conn.close()
        await update.message.reply_text(f"✅ {chat.title} qo'shildi!")
    except Exception as e: await update.message.reply_text(f"Xato: {e}")

async def del_chan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID or not context.args: return
    cid = context.args[0]
    conn = sqlite3.connect('gemini_bot.db')
    conn.execute("DELETE FROM channels WHERE channel_id=?", (cid,))
    conn.commit()
    conn.close()
    await update.message.reply_text(f"🗑 {cid} o'chirildi.")

async def send_reklama(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID or not update.message.reply_to_message: return
    
    conn = sqlite3.connect('gemini_bot.db')
    users = conn.execute("SELECT user_id FROM users").fetchall()
    conn.close()
    
    success = 0
    for u in users:
        try:
            await context.bot.copy_message(chat_id=u[0], from_chat_id=update.chat_id, message_id=update.message.reply_to_message.message_id)
            success += 1
            await asyncio.sleep(0.05) # Spamdan himoya
        except: continue
    await update.message.reply_text(f"📢 Reklama yuborildi: {success} kishiga.")

async def verify_sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    not_subbed = await check_subscription(update, context)
    if not not_subbed:
        await query.message.edit_text("Rahmat! Endi men bilan gaplashishingiz mumkin. Savolingizni yozing!")
    else:
        await query.answer("Hamma kanallarga obuna bo'lishingiz shart! ❌", show_alert=True)

# --- ISHGA TUSHIRISH ---
if __name__ == '__main__':
    init_db()
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin_panel))
    app.add_handler(CommandHandler("add", add_chan))
    app.add_handler(CommandHandler("del", del_chan))
    app.add_handler(CommandHandler("send", send_reklama))
    app.add_handler(CallbackQueryHandler(verify_sub, pattern="verify"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_ai))
    
    print("🚀 Gemini AI Bot ishga tushdi...")
    app.run_polling(drop_pending_updates=True)

