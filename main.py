import discord
from googletrans import Translator
import json

json_open = open('password.json', 'r')
json_load = json.load(json_open)

token = json_load['discord']['token']

client = discord.Client()
translator = Translator()

guild = client.get_guild(841936352077414410)

@client.event
async def on_ready():
    print("run")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    lang = translator.detect(message.content).lang

    if lang == "ja":
        channel = client.get_channel(841949669248598046)
        trans_text = translator.translate(message.content, src = lang, dest = "en").text
        await channel.send(trans_text)

    elif lang == "en":
        channel = client.get_channel(841949627142111232)
        trans_text = translator.translate(message.content, src = lang, dest = "ja").text
        await channel.send(trans_text)

client.run(token)
