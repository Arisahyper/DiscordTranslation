import discord
from googletrans import Translator
import json

json_open = open('password.json', 'r')
json_load = json.load(json_open)

# シークレットトークンの定義
token = json_load['discord']['token']

# 略
client = discord.Client()
translator = Translator()

# サーバーIDの取得
guild = client.get_guild(841936352077414410) # microsoft dev server




@client.event
async def on_ready():
    # 起動時メッセージ
    print("run")

@client.event
async def on_message(message):
    # botの発言には反応しない
    if message.author.bot:
        return

    # 言語判別
    lang = translator.detect(message.content).lang

    # if 言語が日本語だったら
    if lang == "ja":
        #チャンネル指定
        channel = client.get_channel(841949669248598046) # en-text-manage
        # 変換
        trans_text = translator.translate(message.content, src = lang, dest = "en").text
        # 送信
        await channel.send(trans_text)

    # if 言語が英語だったら
    elif lang == "en":
        #チャンネル指定
        channel = client.get_channel(841949627142111232) # ja-text-manage
        # 変換
        trans_text = translator.translate(message.content, src = lang, dest = "ja").text
        # 送信
        await channel.send(trans_text)




client.run(token)
