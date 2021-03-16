import discord
from discord.ext import commands


class AutoReact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 821273878424059927:
            await message.add_reaction("👍")
            await message.add_reaction("<a:ja:821277827697475614>")
            await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(AutoReact(bot))