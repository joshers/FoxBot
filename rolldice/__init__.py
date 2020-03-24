"""Package for Rolldice cog."""
from .rolldice import *

def setup(bot):
    """Load Rolldice."""
    cog = Rolldice()
    bot.add_cog(cog)
