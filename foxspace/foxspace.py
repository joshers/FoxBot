from redbot.core import commands

import launchlibrary as ll
import asyncio

class FoxSpace(commands.Cog):
    """FoxSpace Commands"""

    @commands.command()
    async def nextlaunch(self, ctx):
        """Displays Next Rocket Launch from LaunchLibrary API"""
        # Then initialize an API object
		embed = discord.Embed(
            title="Next Launch", description="Upcoming Rocket Launch Information", color="red"
        )
		embed.add_field(name="Rocket", value="Falcon 9 Block 5 | Starlink 1")
		embed.add_field(name="Launch Window Begin", value="November 11, 2019 14:51:00 UTC")
		embed.add_field(name="Launch Window End", value="November 11, 2019 15:02:00 UTC")
		embed.add_field(name="Launch Pad", value="Space Launch Complex 40, Cape Canaveral, FL")

        await ctx.send(embed=embed)