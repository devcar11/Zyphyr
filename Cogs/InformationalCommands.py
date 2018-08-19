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


class Informational:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        _ping = (after - before) * 1000
        embed = discord.Embed(title=Z, description="Pong! :ping_pong:", color=rand_color())
        embed.set_footer(text="This took me {0:.0f}ms.".format(_ping))
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def userinfo(self, ctx):
        if ctx.message.mentions:
            user: Member = ctx.message.mentions[0]
        else:
            user: Member = ctx.message.author

        embed = discord.Embed(title="", color=rand_color())
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Username", value=user.name, inline=False )
        embed.add_field(name="id", value=user.id, inline=False )
        embed.add_field(name="Status", value=user.status, inline=False )
        embed.add_field(name="Highest Role", value=user.top_role, inline=False )
        embed.add_field(name="Currently Playing", value=user.game, inline=False )
        embed.add_field(name=" Joined", value= format_dt(user.joined_at), inline=False )
        embed.add_field(name="Created", value=format_dt(user.created_at), inline=False )
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def help(self, ctx):
        prefix = cfg['prefix']
        embed = discord.Embed(title="Zyphyrs help commands", color=rand_color())
        embed.add_field(name=":information_source: Informational", value=f"`{prefix}serverinfo`, `{prefix}userinfo`, `{prefix}descrim`, `{prefix}ping`, `{prefix}invite`, `{prefix}suggest`, `{prefix}changelog`, `{prefix}serverlist`, `{prefix}servers`, `{prefix}roles`", inline=False)
        embed.add_field(name=":joy: Fun", value=f"`{prefix}joke`, `{prefix}magic8ball`, `{prefix}pickup`, `{prefix}coinflip`, `{prefix}gay`, `{prefix}stroke`, `{prefix}joke`, `{prefix}hentai`, `{prefix}choose`, `{prefix}oof`, `{prefix}oceanman`, `{prefix}dice`, `{prefix}rban`, `{prefix}rape`, `{prefix}copypasta`, `{prefix}meme`, `{prefix}urban`, `{prefix}pcmaster`", inline=False)
        embed.add_field(name=":x: Moderation", value=f"`{prefix}embed`, `{prefix}purge`, `{prefix}kick`, `{prefix}ban`")
        embed.set_footer(text=f"{vers} Created by Charlie, Sharkbound, and Devon")
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def changelog(self, ctx):
        prefix = cfg['prefix']
        embed = discord.Embed(title=Z, color=rand_color())
        embed.add_field(name="Version 1.0", value=f"Made `{prefix}help` command a little bit nicer looking, as well added a bit more to the `{prefix}serverinfo` command. Added `{prefix}discrim`, `{prefix}stroke`, `{prefix}rape`", inline=False)
        embed.add_field(name="Version 1.1", value=f"Made date and time nicer thanks to Sharkbound. Also thanks to Sharkbound we have it where the color change every command", inline=False)
        embed.add_field(name="Version 1.2", value=f"Working on a suggest command. Added `{prefix}suggest`, `{prefix}copypasta`", inline=False)
        embed.add_field(name="Version 1.3", value=f"I added an embed command thanks to da532's github, if you have a role called Mod you will be able to do `{prefix}embed` and also a purge command `{prefix}purge` (text you want here)", inline=False)
        embed.add_field(name="Version 1.4", value=f"Dimitri and I added a command called `{prefix}meme` right now we are adding memes to it all the time", inline=False)
        embed.add_field(name="Version 1.5", value=f"Dimitri and I worked on the `{prefix}kick` and `{prefix}ban`", inline=False)
        embed.add_field(name="Version 1.6", value=f"Thanks to blaze bot I was able to make a `{prefix}serverlist`, `{prefix}servers`, `{prefix}urban`, `{prefix}roles` command")
        embed.set_footer(text=f"{vers}")
        await self.bot.say(embed=embed)


    @commands.command(pass_context=True)
    async def discrim(self, ctx):
        if ctx.message.mentions:
            user: Member = ctx.message.mentions[0]
        else:
            user: Member = ctx.message.author

        embed = discord.Embed(title="", color=rand_color())
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Discrimator", value=user.discriminator, inline=False)
        embed.add_field(name="Discord Name", value=user.name, inline=False)
        embed.set_footer(text="This is the users discrimator")
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        embed = discord.Embed(title="", description="", color=rand_color())
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.add_field(name="Region", value=ctx.message.server.region, inline=True)
        embed.add_field(name="Owner", value=ctx.message.server.owner, inline=True)
        embed.add_field(name="Server Id", value=ctx.message.server.id, inline=True)
        embed.add_field(name="Afk Channel", value=ctx.message.server.afk_channel, inline=True)
        embed.add_field(name="Members", value=len(ctx.message.server.members), inline=True)
        embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
        embed.add_field(name="Channels", value=len(ctx.message.server.channels), inline=True)
        embed.add_field(name="Verification level", value=ctx.message.server.verification_level, inline=True)
        embed.add_field(name="Created at", value=format_dt(ctx.message.server.created_at), inline=True)
        await self.bot.say(embed=embed)


    @commands.command(pass_context=True)
    async def invite(self, ctx):
        embed = discord.Embed(title="Invite", description="https://goo.gl/NHUwxb", color=rand_color())
        embed.set_footer(text="The invite for the bot")
        await self.bot.say(embed=embed)

    # @commands.command(pass_context=True)
    # async def about(self, ctx):
    #     embed = discord.Embed(title=Z, description="", color=rand_color())
    #     embed.add_field(name="About", value="Zyphry is a bot dedicated to random commands that would keep anyone entertained. The bot is always being updated trying to add new stuff that we think that you guys would enjoy!", inline=False)
    #     embed.add_field(name="Creators", value="The creators of the bot are Sharkbound, Dimitri, and Michael", inline=False)
    #     embed.add_field(name="test", value="test", inline=False)
    #     await self.bot.say(embed=embed)

    ###WOrk on me
    #@commands.command(pass_context=True)
    #async def test(self, ctx):
    #    embed = discord.Embed(title=Z, description=" ", color=rand_color())
    #    embed.add_field(name="Membercount", value=len(bot.get_all_members()))
    #    await self.bot.say(embed=embed)
    #bot.servers


    @commands.command(pass_context=True)
    async def suggest(self, ctx):
        embed = discord.Embed(title=Z, description="If you would like to suggest a command you can join this discord (https://discord.gg/9EzdYcx)", color=rand_color())
        embed.set_footer(text=f"{vers}")
        await self.bot.say(embed=embed)



    @commands.command(pass_context=True)
    async def serverlist(self, ctx):
        """List the servers that the bot is active on."""
        x = ', '.join([str(server) for server in self.bot.servers])
        y = len(self.bot.servers)
        print("Server list: " + x)
        if y > 40:
            embed = discord.Embed(title="Currently active on " + str(y) + " servers:",
                                  description=config.err_mesg + "```json\nCan't display more than 40 servers!```", color=rand_color())
            return await self.bot.say(embed=embed)
        elif y < 40:
            embed = discord.Embed(title="Currently active on " + str(y) +
                                  " servers:", description="\n" + x + " ", color=rand_color())
            return await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def servers(self, ctx):
        embed = discord.Embed(title=Z, description="Currently active on " + str(len(self.bot.servers)) + " servers.", color=rand_color())
        await self.bot.say(embed=embed)


    @commands.command(pass_context=True)
    async def roles(self, context):
        """Lists the current roles on the server."""

        roles = context.message.server.roles
        result = "**The roles on this server are:** "
        for role in roles:
            result += role.name + ", "
        embed = discord.Embed(title="Roles", description=result, color=rand_color())
        await self.bot.say(embed=embed)






def setup(bot):
    bot.add_cog(Informational(bot))
