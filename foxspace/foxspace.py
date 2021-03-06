from redbot.core import commands

"""import launchlibrary as ll"""
import asyncio
import discord
import urllib.request
import json
import datetime

class FoxSpace(commands.Cog):
    """FoxSpace Commands"""

    @commands.command()
    async def nextlaunch(self, ctx):
        """Displays Next Rocket Launch from LaunchLibrary API"""
        """api = ll.Api(retries=10)     
        next_launch = ll.Launch.next(api, 1)
        launch_loc = next_launch[0].location
        launch_start = next_launch[0].windowstart
        launch_end = next_launch[0].windowend
        launch_name = next_launch[0].name
        launch_status = next_launch[0].status"""
        with urllib.request.urlopen("https://launchlibrary.net/1.4/launch/next/1") as url:
            launch = json.load(url)
        launch_status = launch["launches"][0]["status"]
        launch_start = launch["launches"][0]["windowstart"]
        launch_end = launch["launches"][0]["windowend"]
        launchws_unix = launch["launches"][0]["wsstamp"]
        launch_loc = launch["launches"][0]["location"]
        launch_name = launch["launches"][0]["name"]
        launch_image = launch["launches"][0]["rocket"]["imageURL"]
        launch_pad = launch["launches"][0]["location"]["pads"][0]["name"]
        launch_mission = launch["launches"][0]["missions"][0]["description"]
        status = "Undetermined"
        color = 0x0000FF
        if launch_status == 1:
            status = "Green"
            color = 0x00FF00
        if launch_status == 2:
            status = "Red"
            color = 0xFF0000
        launch_time = datetime.datetime.fromtimestamp(launchws_unix)
        current_time_utc = datetime.datetime.utcnow()
        ttl = launch_time - current_time_utc
        embed = discord.Embed(
            title="Next Upcoming Rocket Launch", description=launch_name, color=color
        )
        embed.add_field(name="Mission", value=launch_mission, inline="false")
        embed.add_field(name="Pad", value=launch_pad, inline="false")
        embed.add_field(name="Time To Launch Window", value=ttl, inline="false")
        embed.add_field(name="Window Begin", value=launch_start, inline="false")
        embed.add_field(name="Window End", value=launch_end, inline="false")
        embed.set_thumbnail(url=launch_image)
        await ctx.send(embed=embed)