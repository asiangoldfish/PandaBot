"""
This module contains help documentation for the converter command. It is strictly speaking not a necessity for the
program. main.py currently contains a help docs with the available_timezones function, however this could be removed.
"""

def available_timezones():
	return_string = """Available timezones:
1) UTC
2) EST

Format: [timezone from] [timezone to] [hh:mm]
Example: UTC EST 13:30"""

	return return_string


timezone_options = ["1", "2"]


def time_help_message():
	return_string = """This is the help documentation for the time converter. Currently available conversations are as follows:
- UTC to EST"""

	return return_string
