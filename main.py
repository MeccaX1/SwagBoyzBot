from discord.ext import commands
import os

TOKEN = os.environ['TOKENBOT']
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


@client.command()
async def nw(ctx):
    await ctx.send("ToDo")


client.run(TOKEN)