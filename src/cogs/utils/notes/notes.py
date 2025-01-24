import discord
from discord.ext import commands

async def parse_markdown(ctx, content):
    await ctx.send_response(content)


class Notes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    notes = discord.SlashCommandGroup(name="notes")

    @notes.command()
    async def share(self, ctx: discord.ApplicationContext):
        parse_markdown(ctx, "This is where I start writing the method for markdown.")


def setup(bot):
    bot.add_cog(Notes(bot))
