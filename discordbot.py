# インストールした discord.py を読み込む
import discord
import os

# Set Token from dotenv file
# TOKEN = setting.APIKEY01
TOKEN = os.environ.get('API_KEY_01')
# os.environ.get('CHROME_DRIVER_PATH')
# Create Client instance
client = discord.Client()

# Trigger
@client.event
async def on_ready():
    # Print for std out
    print('ログインしました')

# when get message
@client.event
async def on_message(message):
    # Ignore message from the other bot
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」
    if message.content == '/neko':
        await message.channel.send('にゃーん')

# Run
client.run(TOKEN)


