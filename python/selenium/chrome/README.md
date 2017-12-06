# Headless Web Scraping with Python, Selenium + chromedriver, Google Chrome on Ubuntu 16.04

## Setup

1. Install Google Chrome:
   1. Edit the apt sources list with `sudo nano /etc/apt/sources.list`.
   1. Add the text `deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' as a line at the bottom of the file.
   1. Download the signing key for the repository by running `wget https://dl.google.com/linux/linux_signing_key.pub`, and add this to the system keyring with `sudo apt-key add linux_signing_key.pub`.
   1. Update the package index with `sudo apt update`.
   1. Install Google Chrome with `sudo apt install google-chrome-stable`.
1. Clone this repository/gist and change directory into it.
1. Create a new virtual environment with `virtualenv -p python3 venv` and activate it with `source venv/bin/activate`.
1. Install the required modules with `pip install -r requirements.txt`.
1. Run `get_chromedriver.sh` to download and unzip the current `chromedriver` executable.
1. Given a NetID `abc123` run the script with `python nudirectory.py abc123` to print the full details from the NU Directory as a Python dictionary.
