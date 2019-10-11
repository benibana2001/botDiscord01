import discord
# import setting
import os

# Set Token from dotenv file

# For debug @local
# TOKEN = setting.APIKEY01

# For release @Heroku
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
    if message.content == '/hana':
        await message.channel.send('にゃーん')
    # メンバーのリストを取得して表示
    if message.content == '/members':
        await message.channel.send(message.guild.members)
        print(message.guild.members)
    # 役職のリストを取得して表示
    if message.content == '/roles':
        print(message.guild.roles)
    # テキストチャンネルのリストを取得して表示
    if message.content == '/text_channels':
        print(message.guild.text_channels)
    # ボイスチャンネルのリストを取得して表示
    if message.content == '/voice_channels':
        print(message.guild.voice_channels)
    # カテゴリチャンネルのリストを取得して表示
    if message.content == '/category_channels':
        print(message.guild.categories)

# Run
client.run(TOKEN)


