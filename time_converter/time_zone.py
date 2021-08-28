"""
This module contains functions for converting a user input in UTC to EST timezone.
It is developed by a complete new programmer.

Last edited in June 2021.
"""

import re
import datetime
import discord
from discord.ext import commands


# Checks if user input is valid [HH:MM]
def is_time_input_valid(input_time):
  
  # Checks if the input is in valid format
  valid_format = re.match("[0-9][0-9][:][0-9][0-9]", str(input_time))

  # Checks if user input length is valid
  if len(input_time) == 5:
    valid_len = True
  else:
    valid_len = False

  # If both checks are valid...

  if valid_format and valid_len:
    is_format_valid = True
  else:
    is_format_valid = False

  return is_format_valid


# Format time from user input UTC to EST
def convert_time(tz_from, tz_to, time):

  # Time difference
  time_dif = time_difference(tz_from, tz_to)

  # Split time
  hour = time.split(":")[0]
  minute = time.split(":")[1]

  # Calculate new time
  new_hour = int(hour) + time_dif

  if new_hour > 24:
    new_hour -= 24
  elif new_hour < 0:
    new_hour += 24
  
  return f"{new_hour}:{minute}"


# Time difference between time zones
def time_difference(tz_from, tz_to):
  
  result = 0

  # From UTC
  if tz_from.upper() == "UTC":
    # To EST
    if tz_to.upper() == "EST":
      result = -4
  
  # From EST
  elif tz_from.upper() == "EST":
    # To UTC
    if tz_to.upper() == "UTC":
      result = 4
  
  return result

available_tz = ["UTC", "EST"]

def valid_tz(timezone):
  if isinstance(timezone, available_tz):
    return True
  else:
    return False