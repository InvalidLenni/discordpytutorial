import discord
from discord.ext import commands
import traceback

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

initial_extensions = ['cogs.autoreact']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'{extension} konnte nicht geladen werden!')
            traceback.print_exc()


@bot.event
async def on_ready():
    print("Der Bot ist nun online!")


@bot.command()
async def embed(ctx):
    embed = discord.Embed(title=f'Dein erster Embed', description=f'Die Description deines Embeds', footer=f'GamerRoom')
    await ctx.send(embed=embed)


bot.run("ODIxMjc1NTE0Mjc4Mzc5NTIw.YFBWbQ.KjnRzu3Jpv5aFlfI-VVx2nPwdnM")