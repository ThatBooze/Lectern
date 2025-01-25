import os
import discord
from discord.ext import commands


def generate_list():
    return [f[:-3] for f in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')) if
            f.endswith('.md')]


async def parse_markdown(ctx, content, target):
    await ctx.send_followup(f"{content}", ephemeral=(target is None or target == ctx.author))


class Notes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    notes = discord.SlashCommandGroup(name="notes")

    @notes.command()
    async def share(self, ctx: discord.ApplicationContext,
                    selection: discord.Option(description="Select Note(s)", choices=generate_list(), max_values=3),
                    target: discord.Member = None):

        for note in selection:
            await parse_markdown(ctx, note, target)


def setup(bot):
    bot.add_cog(Notes(bot))
