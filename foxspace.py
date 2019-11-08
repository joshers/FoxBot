from redbot.core import commands

class FoxSpace(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def nextlaunch(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Next Rocket Launch Will Display Here")