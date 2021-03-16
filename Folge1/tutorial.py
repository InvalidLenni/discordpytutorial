import discord
from discord.ext import commands
 
client = commands.Bot(command_prefix='.')
 
@client.event
async def on_ready():
    print("Der Bot ist nun online!")
 
@client.command()
async def embed(ctx):
    embed = discord.Embed(title=f'Dein erster Embed', description=f'Die Description deines Embeds', footer=f'GamerRoom')
    await ctx.send(embed=embed)
 
client.run("ODA3MjcyNTgwMjI2MjIwMDYy.YB1lLQ.q2Tm5_pcDF2SELaRmem1tAZFVEI")