import discord
from discord.ext import commands


class Tags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    tags = discord.SlashCommandGroup(name="tags")

    @tags.command()
    async def share(self, ctx: discord.ApplicationContext):
        await ctx.respond("meals!")


def setup(bot):
    bot.add_cog(Tags(bot))
