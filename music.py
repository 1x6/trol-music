import discord
from discord.ext import commands, tasks
import json
import os
import asyncio
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from discord.utils import get


client = commands.Bot(command_prefix='!') # , self_bot=True

queue = []

@client.event
async def on_ready():
    print('Bot is ready.')
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="my botnet"))

@client.command()
async def connect(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        vc = await channel.connect()


@client.command()
async def disconnect(ctx):
    for vc in client.voice_clients:
        if vc.guild == ctx.guild:
            await vc.disconnect()

@client.command()
async def vibe(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        try:
            vc = await channel.connect()
        except:
            pass
    voice = get(client.voice_clients, guild=ctx.guild)
    source = FFmpegPCMAudio(source='botnet.mp3', executable='ffmpeg')
    player = voice.play(source)
    await ctx.send(f"now playing sex song <a:catkiss:869202118890881034>")


@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    player = voice.pause()

@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    player = voice.resume()

@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    player = voice.stop()

    #await ctx.send("I'm not connected to a voice channel on this server!")


client.run("cock") # , bot=False
