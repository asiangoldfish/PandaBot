# Setup Guide
Setting up the Discord bot requires only a few simple steps. These steps; however, depend on the operating system that you use. I personally use Debian as my development environment and therefore all commands will be for Debian-based systems, but any other Linux distributions or either Windows and MacOS will work.  
**Disclaimer:** This guide assumes that you're running a freshly installed system. If any of the steps already have been previously completed, then please ignore it.

## Setting up your own PandaBot
- Before anything, choose your installation destination. The program requires no special previliges and therefore can safely be installed in your home directory.
- Install Git...
```
sudo apt update
sudo apt install git
```
- ... and clone the repository:
```
git clone https://github.com/asiangoldfish/discordbot_py.git
```
- Install Python
```
sudo apt install python
```
- The bot utilizes third-party packages. It's therefore recommended to use a virtual environment. There are several virtual environments to choose between and is a matter of personal preference. To get you started, venv is an easy to use module to begin with.  
```
sudo apt install python3-venv
python3 -m venv venv
```
- Install pip:
```
sudo apt install python3-pip
```
- Install required packages:
```
source venv/bin/activate
pip3 install -r requirements.txt
```
- The program requires your Discord bot's token. To retrieve this token, do the following:
    - Go to the [Discord Developer Portal](https://discord.com/developers/)
    - Create a new Application if you already haven't
    - Go to the `Bot` tab and click the `Add Bot` button if this is a new application
    - There should be a `Token` field. Click the `Copy` button to copy the token. NB! This Token must *NOT* be confiscated. Please regenerate the token should it be leaked.
- To protect your token, we'll use an environment variable that is not tracked by Git.
    - Copy and rename the example env file, then assign your token to the `TOKEN` variable.
    - Replace `[YOUR TOKEN]` with your Discord bot's token.
```
cp .env.example .env
echo "TOKEN=[YOUR TOKEN]"
```
- Start the program