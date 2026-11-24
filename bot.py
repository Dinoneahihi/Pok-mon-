import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1529370748182069360

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Đã đăng nhập với tên: {client.user}")
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Bot đã chạy thành công từ GitHub Actions!")
    await client.close()

client.run(TOKEN)
