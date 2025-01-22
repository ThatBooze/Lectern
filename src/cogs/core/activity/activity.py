import os
import random
import discord
from discord.ext import commands, tasks


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "splashes.txt"), encoding="utf-8") as s:
    SPLASHES = [line.strip() for line in s.readlines() if line.strip()]


class Activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update_status.start()

    @tasks.loop(minutes=10)
    async def update_status(self):
        await self.bot.change_presence(activity=discord.Game(name=random.choice(SPLASHES)))

    @update_status.before_loop
    async def before_update_status(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(Activity(bot))
