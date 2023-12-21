import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.command(
        aliases=["p", "P"],
        help="Replies with Pong",
        brief="Replies with Pong"
    )
    async def ping(ctx):
        """Answers with Pong"""
        await ctx.reply("pong")

    bot.run(settings.API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()
