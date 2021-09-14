import discord
from discord.ext import commands
import json
import os


bot = commands.Bot(command_prefix="z$")
bot.remove_command ("help")

@bot.event
async def on_ready():
    print("CZav is ready, Guardian.")

@bot.command(pass_context=True)
async def help(ctx):
    await ctx.send("https://sites.google.com/view/czavlist/home")

@bot.command(pass_context=True)
async def valus(ctx):
    await ctx.send("Whether we wanted it or not, we've stepped into a war with the Cabal on Mars. So let's get to taking out their command, one by one. Valus Ta'aurc. From what I can gather he commands the Siege Dancers from an Imperial Land Tank outside of Rubicon. He's well protected, but with the right team, we can punch through those defenses, take this beast out, and break their grip on Freehold.")

@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Hello, Guardian.")

@bot.command(pass_context=True)
async def tokens(ctx):
    await ctx.send("No tokens. Only reputation.")

@bot.command(pass_context=True)
async def pnotes(ctx):
    await ctx.send("https://sites.google.com/view/czavlist/patch-notes")

@bot.command(pass_context=True)
async def stasis(ctx):
    await ctx.send("Guardians must not use Stasis. That is the Vanguard's official stance on this.")

@bot.command(pass_context=True)
async def fireteam(ctx):
    await ctx.send("I need my fireteam. I need Ikora and Cayde.")

@bot.command(pass_context=True)
async def indeed(ctx):
    await ctx.send("Indeed.")
    
bot.run("token")
