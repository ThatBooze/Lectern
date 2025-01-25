import os
import json
import discord
from verbose import logger
from discord.ext import commands


with open("configuration.json") as config_file:
    config_data = json.load(config_file)

# TODO: Intents should be defined in: ./configuration.json
bot = commands.Bot(command_prefix="", intents=discord.Intents.all())


def load_cogs():  # TODO: Replace this entire block of code...?
    for root, _, files in os.walk("cogs"):
        for file in files:
            if file.endswith(".py") and not file.endswith(".py.disabled"):
                cog_path = os.path.join(root, file).replace(os.sep, ".")[:-3]
                try:
                    bot.load_extension(cog_path)
                    logger.info(f"Initialized: {cog_path}")
                except Exception as e:
                    logger.exception(f"Failed to load {cog_path}: {e}")


load_cogs()
bot.run(config_data["TOKEN"])
