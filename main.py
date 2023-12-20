import settings
import discord
from discord.ext import commands

def run():
    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user}, IS READY")

    bot.run(settings.API_TOKEN)

if __name__ == "__main__":
    run()
