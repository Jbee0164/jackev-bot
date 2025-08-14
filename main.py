import discord
from discord.ext import commands
import json
from datetime import datetime, timedelta

TOKEN = "YOUR_DISCORD_TOKEN"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="^", intents=intents)

# Load cooldown data
try:
    with open("cooldowns.json", "r") as f:
        cooldowns = json.load(f)
except FileNotFoundError:
    cooldowns = {}

@bot.command()
async def cooldown(ctx, username: str, server: str):
    # Demo reply (chưa tính toán thật)
    await ctx.send(f"Cooldown list for **{username}** on **{server}**\n```\n#Boss   Last fight   Duration\nAsh Westbrook - Ready```")

bot.run(TOKEN)
