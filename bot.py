import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os



TOKEN = os.environ['BOT_TOKEN']
######
Client = discord.Client()
client =commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if message.content.startswith('-twitch'):
        await message.channel.send('https://www.twitch.tv/jaekiner')

    if message.content.startswith('-sil'):
        data = message.content.split()
        count = 6
        if len(data) > 1:
            try:
                count = int(data[1]) + 1
                if(int(data[1]) > 21):
                    await message.channel.send('En fazla 20 mesajı bir anda silebilirsin!')
                    return
            except:
                await message.channel.send('Örnek: "-sil" veya "-sil 10"')
                return
        
        await message.channel.purge(limit=count)
    





client.run(TOKEN)
