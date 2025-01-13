import os as brutality_ghosty
brutality_ghosty.system("pip install discord.py==1.7.3")
brutality_ghosty.system("pip install colorama")
brutality_ghosty.system('sleep 2 && clear >/dev/null 2>&1 &' if brutality_ghosty.name == 'posix' else 'timeout /t 2 >nul 2>&1 && cls')
import json as ghostop
import random as ghostyjija
from colorama import Fore, Style, init
import discord
from discord.ext import commands, tasks
import time
import sys
import asyncio as made_by_ghosty
# SKID IT 😂 || Made By Layla 
ghostyop = discord.Intents.all(); GhoStyyy = (">"); ghosty = commands.Bot(command_prefix=GhoStyyy, case_insensitive=True, self_bot=True, intents=ghostyop); ghosty.remove_command("help")
# SKID IT 😂 || Made By Layla 
running = True
pray_loop_running = True
# SKID IT 😂 || Made By Layla 
print(f"""{Fore.BLUE}

LAYLA IS BEST
{Style.RESET_ALL}""")
# SKID IT 😂 || Made By Layla 
init(autoreset=True)
print(f"{Fore.LIGHTRED_EX}\n\n > Made By Layla{Style.RESET_ALL}")
# SKID IT 😂 || Made By Layla 
@ghosty.event
async def on_ready():
    print(f"{Fore.LIGHTRED_EX} > Kết nối tool:{Style.RESET_ALL}", f"{Fore.LIGHTGREEN_EX}{ghosty.user}{Style.BRIGHT}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTRED_EX} > update{Style.RESET_ALL}")
# SKID IT 😂 || Made By Layla 
# SKID IT 😂 || Made By Layla 
@ghosty.command(aliases = ["h"])
async def help(ctx):
    ghosty_help = """
    #  RAID TOOL BY LAYLA 
Prefix: `>`

**__Main__**
 🌟 Start: *Starts The Auto*
 🛑 Stop: *Stops The Auto*

**__Made by Layla__** 
"""
    await ctx.send(ghosty_help) # SKID IT 😂 || Made By Layla 
# SKID IT 😂 || Made By Layla 
# SKID IT 😂 || Made By Layla 
@ghosty.command()
async def start(ctx):
    global running  # SKID IT 😂 || Made By Layla 
    running = True
    while True:  # SKID IT 😂 || Made By Layla 
        if not running:
            break  # SKID IT 😂 || Made By Layla 
        await ctx.send(ghostyjija.choice(["# sủa đi con lồn 🤣🤣"]))  # SKID IT 😂 || Made By Layla 
        await ctx.send(ghostyjija.choice(["# não mày úng nước ak"]))  # SKID IT 😂 || Made By Layla
        await ctx.send(ghostyjija.choice(["# cái con chó bố nè🤣🤣"]))  # SKID IT 😂 || Made By Layla
        await ctx.send(ghostyjija.choice(["# lồn hăng lên con"]))  # SKID IT 😂 || Made By Layla
        await ctx.send(ghostyjija.choice(["# đĩ đầu chó🤣🤣"]))  # SKID IT 😂 || Made By Layla
        await ctx.send(ghostyjija.choice(["# lồn con cặc"]))  # SKID IT 😂 || Made By Layla
        await ctx.send(ghostyjija.choice(["# cứt bắc kì chó🤣🤣"]))  # SKID IT 😂 || Made By Layla
        await ctx.send(ghostyjija.choice(["# lồn cay điên🤣🤣🤪"]))  # SKID IT 😂 || Made By Layla
        await ctx.send(ghostyjija.choice(["# mẹ mày chết chưa🤪🤪"]))  # SKID IT 😂 || Made By Layla
        await ctx.send(ghostyjija.choice(["# lồn ăn hại"]))  # SKID IT 😂 || Made By Layla
        await ctx.send(ghostyjija.choice(["# lồn trâu 🤣🤣"]))  # SKID IT 😂 || Made By Layla
        await ctx.send(ghostyjija.choice(["# lồn bụng bự"]))  # SKID IT 😂 || Made By Layla
def new_func():
    running = True
# SKID IT 😂 || Made By Layla 
@ghosty.command() # SKID IT 😂 || Made By Layla 
async def stop(ctx):
    global running # SKID IT 😂 || Made By Layla 
    await ctx.send("🛑 bot cute này đã dừng lại") # SKID IT 😂 || Made By Layla 
    running = False
 # SKID IT 😂 || Made By Layla 

 # SKID IT 😂 || Made By Layla 
with open("config.json", "r") as config_file: # SKID IT 😂 || Made By Layla 
    config = ghostop.load(config_file) # SKID IT 😂 || Made By Layla 

ghostyopaf = (config["TOKEN"]) # SKID IT 😂 || Made By Layla 
ghosty.run(ghostyopaf, bot=False)
# SKID IT 😂 || Made By Layla 