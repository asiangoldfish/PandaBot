#!/bin/bash

NAME="discordbot.sh"
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"


function start_server() {
    if [ ! -d "$SCRIPT_PATH/venv" ]; then
        python -m venv venv
        source "$SCRIPT_PATH/venv/bin/activate"
        pip install -r requirements.txt
    else
        source "$SCRIPT_PATH/venv/bin/activate"
    fi


    python main.py

    return 0
}

# Help page
function usage() {
    echo -n "Usage: $NAME [OPTION]

Some description...

Options:
    -h, --help              this page
    -s, --start             start server
"
}

function parse_cli() {
    ###
    # Functions
    ###

    # Runs help message if no arguments were found
    if [[ $# -eq 0 ]]; then
        usage
        return 1
    fi

    # Checks for flags and runs accordingly
    for arg in "$@"; do
        case $arg in
        -h | --help) usage ;;
        -s | --start) start_server ;;
        *) usage ;;
        esac
        shift
    done
}

parse_cli "$@"
