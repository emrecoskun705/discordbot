import discord
import os



TOKEN = os.environ('BOT_TOKEN')
######
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if message.content.startswith('-twitch'):
        await message.channel.send('https://www.twitch.tv/jaekiner')


client.run(TOKEN)