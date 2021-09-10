"""
This module contains functions for converting a user input in UTC to EST timezone.
"""

import re


def is_time_input_valid(input_time):
	"""
	Use this method to validate the input time format. The format must be as follows: hh:mm

	:param str input_time: User input time
	:return: Boolean
	"""

	# Checks if the input is in valid format: hh:mm
	valid_format = re.match("[0-9][0-9][:][0-9][0-9]", str(input_time))

	# Checks if user input length is within the format's limit
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


def convert_time(tz_from, tz_to, time):
	"""
	When differentiating two different clock times, one must ensure that minutes doesn't go over 60 minutes
	or hours don't go over 24 hours. Same goes for going under 0. This function converts time if these instances
	happen.

	:param str tz_from: Timezone from
	:param str tz_to: Timezone to
	:param str time: Time in hh:mm
	:return: New time in hh:mm format.
	"""

	# Calculates the time different between timezones
	time_dif = time_difference(tz_from, tz_to)

	# Split hour and minute into seperate variables
	hour = time.split(":")[0]
	minute = time.split(":")[1]

	# Calculate new time
	new_hour = int(hour) + time_dif

	# Converts the new time to the next or previous day in relation to the old time.
	if new_hour > 24:
		new_hour -= 24
	elif new_hour < 0:
		new_hour += 24

	return f"{new_hour}:{minute}"


def time_difference(tz_from, tz_to):
	"""
	Converts UTC to EST or vice versa. Does not consider daylight saving.

	:param str tz_from: Timezone from
	:param str tz_to: Timezone to
	:return: Time difference
	"""
	time_diff = 0

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

	return time_diff


available_tz = ["UTC", "EST"]