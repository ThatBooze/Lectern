import discord
from discord.ext import commands


class Tags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tags = discord.slashCommandGroup(name="tags")

    @tags.command
    async def share(self, ctx: ApplicationContext, ):
        await ctx.send_response("Surprise! It's a [placeholder](https://www.google.com/search?q=placeholder)!")


def setup(bot):
    bot.add_cog(Tags(bot))
