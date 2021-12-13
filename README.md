# PandaBot

Welcome to the Panda bot GitHub page! The bot was developed as method to learn Python, which has worked brilliantly.
Panda's source codes comes with a lot of docstrings and comments to clarify and explain how each block of code works.
This will hopefully make it less daunting and more friendly for new Pythonistas.

If you are experienced in programming, then this bot will appear utterly basic to you. For new programmers, however,
I hope this will become helpful as you are learning Python, just like I am!

## How to use the bot

It comes with a few commands:
- *;panda help* - Help/documentation command
- *;panda ping* - Ping command to check server latency
- *;panda 8ball* - 8ball game
- *;panda dice* - Dice game
- *;panda convert* - Converts time. Check the help command for more info about available timezones.
- *;panda clear* - Command for clearing messages in current channel.

## Setting up your own PandaBot

- The bot utilizes third-party packages. It's therefore recommended to use a virtual environment. There are several virtual environments to choose between and is a matter of personal preference. To get you started, `venv` is an easy to use module to begin with.  
Linux (Debian-based):
```
sudo apt update
sudo apt install python3-venv
python3 -m venv venv
```
- Install pip (if you don't already have):  
Linux (Debian-based):
```
sudo apt install python3-pip
```
- Install required packages:
```
source venv/bin/activate
pip3 install -r requirements.txt
```
- Start the PandaBot:
```
python3 main.py
```
