import os
import discord

from discord import Activity
from discord.ext import tasks, commands
from mcstatus import MinecraftServer
from aioconsole import aprint
client = discord.Client()

IP = "127.0.0.1:25565" # Minecraft server IP (if you are running the server and bot on same server, do not change the defaults)
REFRESH_RATE = 5 # Status refresh rate in seconds
STATUS_TYPE = discord.activity.ActivityType.watching # Types: watching, playing, listening & streaming
TOKEN = ":D" # Your bot token

@client.event
async def on_ready():
    if Status_Update.is_running():
        pass
    else:
        Status_Update.start()
    os.system("clear") # If you are using Windows, change it to "cls"
    await aprint(f"Ready! ({client.user})")

@tasks.loop(seconds=REFRESH_RATE)
async def Status_Update():
    try:
        server = MinecraftServer.lookup(IP)
        sstatus = server.status()
        await client.change_presence(activity=Activity(type=STATUS_TYPE, name=f"{sstatus.players.online} Players"))
    except Exception as e:
        await aprint(f"Error: {e}")
        return

if __name__ == '__main__':
    client.run(TOKEN)
