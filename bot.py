import discord
from discord.ext.commands import Bot
from discord.ext import commands
import youtube_dl
import os


TOKEN = os.environ['BOT_TOKEN']
######
bot =commands.Bot(command_prefix='-')

players = {}

@bot.command()
async def twitch(ctx):
    await ctx.send('https://www.twitch.tv/jaekiner')
    


@bot.command(aliases=['join'])
async def join_voice(ctx):
    channel = ctx.author.voice.channel
    if channel:
        await channel.connect()

@bot.command(aliases=['leave'])
async def leave_voice(ctx):
    server = ctx.message.guild.voice_client
    if server:
        await server.disconnect()







    



    
#@bot.event
#def ondsfsd_message(message):

 #   if message.author == bot.user:
  #      return
    #-twitch
    #if message.content.startswith('-twitch'):
     #   await message.channel.send('https://www.twitch.tv/jaekiner')

    #-sil
   # if message.content.startswith('-sil'):
    #    data = message.content.split()
     #   count = 6
      #  if len(data) > 1:
       #     try:
        #        count = int(data[1]) + 1
         #       if(int(data[1]) > 21):
                    #await message.channel.send(colour('En fazla 20 mesajı bir anda silebilirsin!'))
          #          return
           # except:
                #await message.channel.send('Örnek: "-sil" veya "-sil 10"')
            #    return
        
       # await message.channel.purge(limit=count)

    #-help
    #if message.content.startswith('-help'):
        #await message.channel.send(helpMessage())

def colour(comment):
    comment = "```css\n" + comment + "```"
    return comment

def helpMessage():
    string = f"""
        {colour('-twitch')} {colour('-sil')}
    """
    return string
        
    





bot.run(TOKEN)
