from discord.ext import commands
from discord.ext.commands import bot
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
from discord.ext import commands
from random import choices


def rand_color():
    return int(''.join(choices('0123456789ABCDEF', k=6)), 16)

def format_dt(dt):
    return dt.strftime('%a, %b/%d/%Y %I:%M %p')

class Fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hug(self, ctx, *, member: discord.Member = None):
        if member is None:
            embed = discord.Embed(title="Us bots love you humans too", description=f"{ctx.message.author.mention} has been hugged", color=rand_color())
            await self.bot.say(embed=embed)
        elif member.id == ctx.message.author.id:
            embed = discord.Embed(title="It's fine, I love you still", description=f"{ctx.message.author.mention} hugged themself", color=rand_color())
            await self.bot.say(embed=embed)
        else:
            embed = discord.Embed(title="Yay you have been hugged", description=f"{member.mention} has been hugged by {ctx.message.author.mention}!", color=rand_color())
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def gay(self, ctx, user):
        embed = discord.Embed(title=" ", description=" ", color=rand_color())
        n = random.randint(0,100)
        if n >= 100:
            embed.add_field(name=f"Zyphyr", value=f"{ctx.message.author.mention} is **{n}%**  gay! :gay_pride_flag:")
            embed.set_footer(text="You are the gay lord of the server!")
        elif n <= 1:
            embed.add_field(name=f"Zyphyr", value=f"{ctx.author.mention} is **{n}%**  gay! :open_mouth:")
            embed.set_footer(text="You are 0%  gay(Seems a little far-fetched)")
        elif n < 50:
            embed.add_field(name=f"Zyphyr", value=f"{user.name} is **{n}%**  gay! :wink:")
            embed.set_footer(text="You are a little bit gay")
        else:
            embed.add_field(name=f"Zyphyr", value=f"{ctx.message.author.mention} is **{n}%**  gay! :gay_pride_flag:")
            embed.set_footer(text="You are pretty gay, and that's alright")
            await self.bot.say(embed=embed)

        @commands.command(pass_context=True)
        async def stroke(self, ctx, user: discord.Member):
            if not ctx.message.mentions:
                embed = discord.Embed(title=Z, description="Please specify a user!", color=rand_color())
            else:
                user = ctx.message.mentions[0]
                embed = discord.Embed(title=Z, description=f"{ctx.author.mention} walkes up behing {ctx.user.mention} and strokes them softly", color=rand_color())
                await self.bot.say(embed=embed)

        @commands.command(pass_context=True)
        async def coinflip(ctx: Context, self):
            embed= discord.Embed(title=" ", description=" ", color=rand_color())
            frames = '-/|\\'
            msg = await self.bot.say(f'flipping coin... ')
            for i in range(0, 7):
                await self.bot.edit_message(msg, msg.content + " " + frames[i%len(frames)])
                await asyncio.sleep(.4)

                await self.bot.edit_message(msg, f'the coins shows {choice(["heads", "tails"])}')



def setup(bot):
    bot.add_cog(Fun(bot))
