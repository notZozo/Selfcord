import discord
from discord.ext import commands
import os

bot_prefix = "s!"
bot = commands.Bot(f"{bot_prefix}", self_bot=True)
bot.remove_command('help')

#Shows an error if the command doesn't meet the requirements
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        user=ctx.message.author
        await ctx.send(f'Please pass in all requirements. :rolling_eyes: For help, use `{bot_prefix}help <command>`.')
        print(f'@{user} tried to use a command but missed an arguent!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.message.delete()
        user=ctx.message.author
        await ctx.send("You don't have the necessary permissions! :angry:")
        print(f'@{user} tried to use a command without necessary permissions!')
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        user=ctx.message.author
        await ctx.send(f'Command not found! :flushed: For help, use `{bot_prefix}help`.')
        print(f'@{user} tried to use an inexistent command!')

#When the bot is connected, it prints a message and the prefix
@bot.event
async def on_ready():
    os.system("clear")
    print("Selfcord is running ( ͡° ͜ʖ ͡°)")
    print(f"The bot prefix is [{bot_prefix}]")

#Command to get some help
@bot.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send("**Commands:**\n    -`prefix`: **Allows you to get the bot prefix**\n    -`rpc`: **Allows you to change your rich presence status**\n         *Included Options:* `playing` + `name`, `streaming` + `name` + `url`, `watching` + `name`, `listening` + `name`\n    -`trylater`: **Allows you to send an** `I'll try later` **message if you're too lazy to type one**\n         *Included Options:* `FR` *(French Prefix)*, `EN` *(English Prefix)*")

#Command to get the prefix
@bot.command()
async def prefix(ctx):
    await ctx.message.delete()
    await ctx.send(f"The bot prefix is `{bot_prefix}`")

#Command to change the rich presence status
@bot.command()
async def rpc(ctx, rpc, rpc_name, rpc_url=None):
    await ctx.message.delete()
    if rpc == "playing":
        await bot.change_presence(activity=discord.Game(f'{rpc_name}'))
        await ctx.send(f"Rpc changed to {rpc} {rpc_name}")
    if rpc == "streaming":
        await bot.change_presence(activity=discord.Streaming(name=f'{rpc_name}', url=f'{rpc_url}'))
        await ctx.send(f"Rpc changed to {rpc} {rpc_name} with the following url <{rpc_url}>")
    if rpc == "watching":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{rpc_name}'))
        await ctx.send(f"Rpc changed to {rpc} {rpc_name}")
    if rpc == "listening":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{rpc_name}'))
        await ctx.send(f"Rpc changed to {rpc} {rpc_name}")

#Command to send an "I'll try later" message
@bot.command()
async def trylater(ctx, lang):
    await ctx.message.delete()
    if lang == "FR":
        await ctx.send("J'essayerais plus tard...\n[Réponse envoyée depuis un selfbot]")
    if lang == "EN":
        await ctx.send("I'll try it later...\n[Answer sent from a selfbot]")

bot.run("OTkwMDM0MzU4MjgwNzg1OTMw.GWWJz3.rn2217zCaVg8pPod_oufVapi-Oxf10O1pvbuw8", bot=False)
