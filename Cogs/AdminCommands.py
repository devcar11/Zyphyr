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

class Moderation:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx):
        if member == ctx.message.author:
            return
        try:
            await self.bot.ban(member)
            embed = discord.Embed(title=Z, description=f"{member.mention} has been banned", color=rand_color())
            await self.bot.say(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(title=Z, description="Sorry, you don't have the permission to do that.", color=rand_color())
            await self.bot.say(embed=embed)

    @ban.error
    async def ban_error(error, err, ctx):
          if isinstance(error, commands.CheckFailure):
              embed = discord.Embed(title=Z, description="Sorry, you don't have the permission to do that.", color=rand_color())
              await self.bot.say(embed=embed)
          elif isinstance(error, commands.MissingRequiredArgument):
               embed = discord.Embed(title=Z, description="")


    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member):
        if member == ctx.message.author:
            return
        try:
            await self.bot.kick(member)
            embed = discord.Embed(title=Z, description=f"{member.mention} has been kicked", color=rand_color())
            await self.bot.say(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(title=Z, description="Sorry, you don't have the permission to do that.", color=rand_color())
            await self.bot.say(embed=embed)

    @kick.error
    async def kick_error(error, err, ctx):
          if isinstance(error, commands.CheckFailure):
              embed = discord.Embed(title=Z, description="Sorry, you don't have the permission to do thats.", color=rand_color())
              await self.bot.say(embed=embed)
          elif isinstance(error, commands.MissingRequiredArgument):
               embed = discord.Embed(title=Z, description="Please specify a user!.", color=rand_color())
               await self.bot.say(embed=embed)


    @commands.command(pass_context=True)
    async def embed(self, ctx, *, a_sMessage):
        if ctx.message.author.server_permissions.embed_links:
            embed = discord.Embed(description=a_sMessage, color=rand_color())
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.set_author(name=f"{ctx.message.author.name} says..")
            # embed.set_footer(text=f"{vers}")
            await self.bot.delete_message(ctx.message)
            await self.bot.say(embed=embed)
        else:
            embed = discord.Embed(title=Z, description="Sorry, you don't have the permission to do that.")
            await self.bot.say(embed=embed, delete_after=5 )



def setup(bot):
    bot.add_cog(Moderation(bot))
