from http import client
import discord
from discord.ext import commands
from discord.utils import get
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'images/{file_name}')
            result = get_class(model="keras_model.h5", labels="labels.txt", image=f'images/{file_name}')
            await ctx.send(result)
            if result == 'lichi':
                await ctx.send('Личи - экзотический фрукт родом из Китая.')
            elif result == 'marakuja':
                await ctx.send('Маракуя - фрукт, плод ряда тропических лиан.')
            elif result == 'papaya':
                await ctx.send('Папайя - дынное дерево, древесное растение.')

    else:
        await ctx.send('You forgot to add the picture!')

bot.run("")
