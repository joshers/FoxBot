from redbot.core import commands
#from redbot.core.i18n import Translator, cog_i18n
import dice

#_ = Translator("Rolldice", __file__)

class Rolldice(commands.Cog):
    """Rolldice Cog
        A simple cog to glue Python's dice module together to Redbotv3.
    """

    max_dice_sets = 8

    @commands.command()
    async def rolldice(self, ctx, *to_roll: str):
        if not to_roll:
            to_roll = ['1d6']
        if len(to_roll > self.max_dice_sets):
            await ctx.send(f'Too many dice sets to roll, max is {max_dice_sets}')

        res = []
        for dice_set in to_roll:
            try:
                res += (dice_set, dice.roll(dice_set))
            except dice.DiceBaseException as e:
                #pretty_e = e.pretty_print().replace('\n', '\n\t')
                #res += (dice_set, f'Invalid dice syntax:\n\t{pretty_e}')
                res += (dice_set, 'Dice string error')
            except Exception as e:
                res += (dice_set, 'Input error')
        
        await ctx.send('\n'.join([f'{k}: {v}' for k,v in res]))

