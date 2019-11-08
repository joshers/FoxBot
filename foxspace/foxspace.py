from redbot.core import commands

import launchlibrary as ll
import asyncio
import discord

class FoxSpace(commands.Cog):
    """FoxSpace Commands"""

    @commands.command()
    async def nextlaunch(self, ctx):
        """Displays Next Rocket Launch from LaunchLibrary API"""
        api = ll.Api(retries=10)     
        next_launch = ll.Launch.next(api, 1)
        launch_loc = next_launch[0].pad
        launch_name = next_launch[0].name
        embed = discord.Embed(
            title="Next Launch", description="Upcoming Rocket Launch Information", color=0xFF0000
        )
        embed.add_field(name="Mission", value=launch_name)
        embed.add_field(name="Launch Window Begin", value="November 11, 2019 14:51:00 UTC")
        embed.add_field(name="Launch Window End", value="November 11, 2019 15:02:00 UTC")
        embed.add_field(name="Launch Pad", value=launch_loc)

        await ctx.send(embed=embed)