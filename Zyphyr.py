#bot made my Charlie, Sharkbound, and Dev
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import logging
from Config import Config
import random
import shlex
import os
import discord, chalk
from os import listdir
from pathlib import Path
import re
import pathlib
from discord.ext.commands.cooldowns import BucketType
import platform
import sys
import os
import requests
import time
import datetime

cfg = Config('config.json', foldername='Config', token='TOKEN_PLACEHOLDER', embed_role='everyone', game="type zhelp for help!", prefix="z", clr='0xff0000')


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

Z = "Zyphyr"
vers = "Current Version 1.6"
bot = commands.Bot(command_prefix=cfg['prefix'])

bot.remove_command("help")


extensions = ('Cogs.AdminCommands', 'Cogs.FunCommands', 'Cogs.InformationalCommands')
for e in extensions:
    bot.load_extension(e)


def rand_color():
    return int(''.join(random.choices('0123456789ABCDEF', k=6)), 16)

@bot.event
async def on_ready():
    print ("----------------------------------------------------")
    print ("This bot was made by Charlie and Devon")
    print ("Logged in as:")
    print (bot.user.name)
    print (bot.user.id)
    print ("----------------------------------------------------")
    await bot.change_presence(game=discord.Game(name=cfg['game']))












vers = "Current Version 1.5"

@bot.command(pass_context=True, aliases=['remove', 'delete'])
async def purge(ctx, number):
    """Bulk-deletes messages from the channel."""
    try:
        if ctx.message.author.server_permissions.manage_messages:
            mgs = []  # Empty list to put all the messages in the log
            # Converting the amount of messages to delete to an integer
            number = int(number)
            async for x in bot.logs_from(ctx.message.channel, limit=number):
                mgs.append(x)
            await bot.delete_messages(mgs)
            embed = discord.Embed(title="Done", description="Purged {} messages.".format(number), color=rand_color())
            logger.info("Purged {} messages.".format(number))
            await bot.say(embed=embed)
        else:
            await bot.say(config.err_mesg_permission)
    except:
        await bot.say(config.err_mesg)

# @bot.command(pass_context=True)
# async def roles(context):
#     """Lists the current roles on the server."""
#
#     roles = context.message.server.roles
#     result = "The roles on this server are: "
#     for role in roles:
#         result += role.name + ", "
#     embed = discord.Embed(title="Roles", description=result, color=rand_color())
#     await bot.say(embed=embed)




bot.run(cfg['token'])
