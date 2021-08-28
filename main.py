import os
import discord
from discord.ext import commands
from dice import *
from time_converter import time_zone, time_help
from config.config import *
import random
import time

client = commands.Bot(command_prefix=";panda ", help_command=None)


# On starting up the bot
@client.event
async def on_ready():
    print(STARTUP_MESSAGE)

    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=";panda help "))

    print("\nGuilds currently joined:\n")
    for guild in client.guilds:
        print(guild)
        await guild.me.edit(nick=DEFAULT_NICKNAME)

    print("\n" + STARTUP_COMPLETE_MESSAGE + "\n")

# Help documentation
@client.group(name="help", invoke_without_command=True)
async def help(ctx):
  # Initialize the embedded message
  embed=discord.Embed(description="This bot is in BETA. For more info about a command, use `;panda help <name of command>`",
color=0xFF5733)

  # Include more fields to the embed
  embed.set_author(name=PANDA_HELP_NAME, icon_url=PANDA_HELP_ICON)
  embed.add_field(name="Utilities", value=EMBED_UTILS, inline=False)
  embed.add_field(name="Games:", value=EMBED_GAMES, inline=False)
  embed.set_footer(text="More commands and functionalities are on the way. Hang on tight!")

  await ctx.send(embed=embed)


@help.command(name="ping")
async def ping_subcommand(ctx):
  embed=discord.Embed(description="Ping the server and check for the response time.", color=EMBED_COLOR)
  embed.set_author(name=PANDA_HELP_NAME, icon_url=PANDA_HELP_ICON)
  embed.add_field(name="How To Use", value="Simply type `;panda ping` and get a pong back in milliseconds.", inline=False)
  embed.set_footer(text=EMBED_MORE_HELP)
  await ctx.send(embed=embed)


@help.command(name="convert")
async def convert_subcommand(ctx):
  embed=discord.Embed(description="Time converter.", color=EMBED_COLOR)
  embed.set_author(name=PANDA_HELP_NAME, icon_url=PANDA_HELP_ICON)
  embed.add_field(name="How To Use", value="The format for the command is as follows: [timezone from] [timezone to] [hh:mm]. Example: `;panda convert UTC EST 13:30`", inline=False)
  embed.add_field(name="Available Timezones", value="UTC, EST", inline=False)
  embed.set_footer(text=EMBED_MORE_HELP)
  await ctx.send(embed=embed)


@help.command(name="clear")
async def clear_subcommand(ctx):
  embed=discord.Embed(description="Use this command to clear messages. **NOTE**: Only available to admins.")
  embed.set_author(name=PANDA_HELP_NAME, icon_url=PANDA_HELP_ICON)
  embed.add_field(name="How To Use", value="Clear a number of messages in the particular channel between 1 and 100. Example: `;panda clear 20`.")
  embed.set_footer(text=EMBED_MORE_HELP)
  await ctx.send(embed=embed)

@help.command(name="dice")
async def dice_subcommand(ctx):
  embed=discord.Embed(description="Roll the dice against the bot and see who wins!", color=EMBED_COLOR)
  embed.set_author(name=PANDA_HELP_NAME, icon_url=PANDA_HELP_ICON)
  embed.add_field(name="How To Use", value="Roll the dice! Command: `;panda dice`")
  embed.set_footer(text=EMBED_MORE_HELP)
  await ctx.send(embed=embed)


@help.command(name="8ball")
async def ball8_subcommand(ctx):
  embed=discord.Embed(description="See what I think about your yes or no questions.", color=EMBED_COLOR)
  embed.set_author(name=PANDA_HELP_NAME, icon_url=PANDA_HELP_ICON)
  embed.add_field(name="How To Use", value="Use the command, followed by a yes or no question. Example: `;panda 8ball is the panda bot not the best bot ever?`")
  embed.set_footer(text=EMBED_MORE_HELP)
  await ctx.send(embed=embed)


# Dice game
@client.command()
async def dice(ctx):
    player_roll = roll_dice()
    bot_roll = roll_dice()

    await ctx.send(f"Your roll is {player_roll}. My roll is {bot_roll}.")
    if player_roll > bot_roll:
        await ctx.send("You won!")
    elif player_roll < bot_roll:
        await ctx.send("I won!")
    else:
        await ctx.send("Draw!")


# Ping command
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


# 8ball game
@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question=None):
    responses = [
        "It is Certain.", "It is decidedly so.", "Without a doubt.",
        "Yes definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
        "My sources say no.", "Outlook not so good.", "Very doubtful."
    ]
    if question == "help":
        await ctx.send("Ask me a yes or no question and I will answer it.")
    else:
        await ctx.send(f"{random.choice(responses)}")


# Convert time
@client.command(aliases = ["c"])
async def convert(ctx, *,input_time= ""):

  # Help doc
  if input_time.casefold() == 'help':
    await ctx.send(f"{time_help.available_timezones()}")
  else:
  
    split_input_time = input_time.split(" ")
    available_tz = time_zone.available_tz

    from_time = False
    to_time = False
    clock_time = False

    error_msg = 'Please refer to the help doc for formatting rules. Command: ";convert help"'

    # Checks if the format is valid
    if split_input_time[0].upper() in available_tz:  # Checks from-time
      from_time = True

      if split_input_time[1].upper() in available_tz and split_input_time[1] != split_input_time[0]:  # Checks to_time
        to_time = True
    
        if time_zone.is_time_input_valid(split_input_time[2]):  # Checks hour and min
          clock_time = True

        else:
          await ctx.send(error_msg)
      
      else:
        await ctx.send(error_msg)

    else:
      await ctx.send(error_msg)


    # Convert time
    if from_time and to_time and clock_time:
      output_time = time_zone.convert_time(split_input_time[0], split_input_time[1], split_input_time[2])

      await ctx.send(f"Time in {split_input_time[1].upper()} is: {output_time}.")

# Clear messages
@client.command()
async def clear(ctx, amount = 0):
  if ctx.message.author.guild_permissions.administrator:
    if amount <= 0: # Makes sure that the number is positive
      await ctx.send("Specify how many messages to clear")
    elif amount in range(1, 100):
      await ctx.channel.purge(limit = amount + 1, check = lambda msg: not msg.pinned)
    elif amount > 100:
      await ctx.send("Due to safety reasons, this is limited to only 100.")
  
  else:

    await ctx.send("ERROR: Admin only command.")
    time.sleep(3)
    await ctx.channel.purge(limit = 2)


my_secret = os.environ['token']
client.run(my_secret)
