import discord
from discord.ext import commands, tasks
import random
import datetime
import os
from tarot_data import LUCKY_CONTENT # Import dữ liệu từ file riêng

# --- CẤU HÌNH BIẾN MÔI TRƯỜNG ---
# Bot Token: Nên dùng 'DISCORD_TOKEN' hoặc 'BOT_TOKEN'
BOT_TOKEN = os.environ.get('DISCORD_TOKEN') 

# Channel ID
try:
    # Lấy ID kênh từ biến môi trường và chuyển sang kiểu số nguyên
    CHANNEL_ID = int(os.environ.get('CHANNEL_ID'))
except (TypeError, ValueError):
    print("LỖI: Không thể lấy hoặc chuyển đổi CHANNEL_ID. Vui lòng kiểm tra lại biến môi trường.")
    CHANNEL_ID = None

# --- CẤU HÌNH BOT VÀ TASKS ---

# Cần Intents cao hơn để đảm bảo khả năng mở rộng
intents = discord.Intents.default()
intents.message_content = True # Cần thiết nếu bot phải đọc tin nhắn, nhưng nên bật cho an toàn
intents.members = True         # Hữu ích cho các lệnh trong tương lai

bot = commands.Bot(command_prefix='!', intents=intents)

# Thiết lập múi giờ (UTC+7 cho Việt Nam)
VN_TZ = datetime.timezone(datetime.timedelta(hours=7))
# Thiết lập thời gian chạy task (Ví dụ: 3 giờ 00 phút sáng VN)
schedule_time = datetime.time(hour=3, minute=0, tzinfo=VN_TZ)

@tasks.loop(time=schedule_time)
async def daily_lucky_draw():
    """Hàm chạy mỗi ngày vào lúc 3:00 sáng (VN)"""
    
    if CHANNEL_ID is not None:
        # Lấy kênh qua ID
        channel = bot.get_channel(CHANNEL_ID)
        
        if channel:
            min_num = 1
            max_num = len(LUCKY_CONTENT)
            lucky_number = random.randint(min_num, max_num)
            
            # Lấy nội dung lá bài, sử dụng .get() để tránh lỗi nếu thiếu số
            message_content = LUCKY_CONTENT.get(lucky_number, "Có lỗi xảy ra khi lấy thông báo.")

            try:
                # Tách Tên Lá Bài ra khỏi Nội Dung để làm tiêu đề Embed đẹp hơn
                title_end_index = message_content.find('.')
                card_title = message_content[:title_end_index] if title_end_index != -1 else "Lá Bài May Mắn"
                card_description = message_content[title_end_index+1:].strip() if title_end_index != -1 else message_content

                embed = discord.Embed(
                    title=f"🔮 LÁ BÀI TAROT NGÀY: {card_title} 🔮",
                    description=f"**Con số ngẫu nhiên: {lucky_number}/78**\n\n{card_description}",
                    color=discord.Color.gold()
                )
                embed.set_footer(text=f"Ngày: {datetime.date.today().strftime('%d/%m/%Y')} | Thời gian: {datetime.datetime.now(VN_TZ).strftime('%H:%M:%S')}")
                
                await channel.send(embed=embed)
                print(f"[{datetime.datetime.now()}] Đã gửi thông báo số {lucky_number} thành công.")
            except Exception as e:
                print(f"Lỗi khi gửi tin nhắn: {e}")
        else:
            print(f"Không tìm thấy kênh với ID: {CHANNEL_ID}. Kiểm tra lại ID kênh hoặc quyền của Bot.")
    else:
        print("CHANNEL_ID không hợp lệ, không thể thực hiện tác vụ.")


# Sự kiện khi Bot đã sẵn sàng
@bot.event
async def on_ready():
    """Hàm chạy khi Bot kết nối thành công"""
    print(f'🤖 Bot đã đăng nhập với tên: {bot.user}')
    await bot.change_presence(activity=discord.Game(name="Xem bói Tarot mỗi ngày"))
    
    # Bắt đầu vòng lặp task khi bot sẵn sàng
    if not daily_lucky_draw.is_running():
        # Đợi Bot sẵn sàng (kết nối Discord hoàn tất) trước khi bắt đầu Task
        # Điều này giúp hàm get_channel() hoạt động tốt hơn
        daily_lucky_draw.start()
        print(f'⏳ Task quay số đã được lên lịch lúc {schedule_time.strftime("%H:%M:%S")} (VN).')

# Khởi chạy Bot
if __name__ == "__main__":
    if BOT_TOKEN:
        try:
            bot.run(BOT_TOKEN)
        except Exception as e:
             print(f"LỖI: Không thể chạy bot. Kiểm tra lại DISCORD_TOKEN và Intents của bot. Chi tiết: {e}")
    else:
        print("LỖI: DISCORD_TOKEN không được thiết lập. Vui lòng kiểm tra lại Biến Môi Trường.")
