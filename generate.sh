#!/bin/bash

# run as sudo
[ "$UID" -eq 0 ] || exec sudo bash "$0" "$@"

# ensure python venv is installed
if ! dpkg -s python3.12-venv &>/dev/null; then
    apt install -y python3.12-venv
fi

# activate the virtual environment
/usr/bin/python3 -m venv env
source env/bin/activate

# install dependencies
apt-get install -y latexmk
apt-get install -y texlive-latex-extra
apt-get install -y texlive-luatex
python env/bin/pip install -r requirements.txt

# generate PDFs
python example.py

# exit
deactivate