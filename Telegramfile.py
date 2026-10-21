import telebot
import yt_dlp

TOKEN = '8602163038:AAHetAj4njlGtM4MaKkzRXVWYPALO8Add1E'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "হ্যালো! আমি আপনার ভিডিও ডাউনলোডার বট।")


@bot.message_handler(func=lambda message: True)
def download_video(message):
    bot.reply_to(message, "অনুগ্রহ করে অপেক্ষা করুন, আমি ভিডিওটি ডাউনলোড করছি।")
    url = message.text
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        with open('video.mp4', 'rb') as video:
            bot.send_video(message.chat.id, video)
    except Exception as e:
        bot.reply_to(message, f"ভিডিওটি ডাউনলোড করতে সমস্যা হয়েছে: {e}")


bot.polling()
