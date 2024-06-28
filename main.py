import discord, os, keep_alive, asyncio, datetime, requests

from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  // s_b =True
)

async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=""))

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
