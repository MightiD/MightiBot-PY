import random
import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def onCommandError(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Missing arguments")

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.command(
        aliases=["p", "P"],
        help="Replies with Pong",
        brief="Replies with Pong"
    )
    async def ping(ctx):
        await ctx.reply("pong")

    @bot.command()
    async def say(ctx, *content):
        try:
            await ctx.reply(" ".join(content))
        except:
            await ctx.reply("What?")

    @bot.command(
        aliases=["Choose", "random", "Random"],
    )
    async def choose(ctx, *content):
        try:
            await ctx.reply(random.choice(content))
        except:
            await ctx.reply("Error")

    bot.run(settings.API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()
