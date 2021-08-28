import os
import discord
from discord.ext import commands
from dice import *
from time_converter import time_zone, time_help
from config.config import *
import random
import time

client = commands.Bot(command_prefix=";")


# On starting up the bot
@client.event
async def on_ready():
    print(STARTUP_MESSAGE)

    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=";help "))

    print("\nGuilds currently joined:\n")
    for guild in client.guilds:
        print(guild)
        await guild.me.edit(nick=DEFAULT_NICKNAME)

    print("\n" + STARTUP_COMPLETE_MESSAGE)


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
  
  else:

    await ctx.send("ERROR: Admin only command.")
    time.sleep(3)
    await ctx.channel.purge(limit = 2)


my_secret = os.environ['token']
client.run(my_secret)
