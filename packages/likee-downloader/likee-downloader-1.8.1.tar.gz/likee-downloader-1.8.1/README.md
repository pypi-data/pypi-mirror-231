# Note
## Due to Likee's changes on their website, likee-downloader only works in some European countries. And, it also works in the United States.

# Likee Downloader
A program for downloading videos from Likee, given a username

[![CodeQL](https://github.com/rly0nheart/likee-downloader/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/likee-downloader/actions/workflows/codeql.yml)  [![Upload Python Package](https://github.com/rly0nheart/likee-downloader/actions/workflows/python-publish.yml/badge.svg)](https://github.com/rly0nheart/likee-downloader/actions/workflows/python-publish.yml)

![screenshot](https://user-images.githubusercontent.com/74001397/191549849-07f151c5-4f42-4c71-ae9c-ceabe24c54d3.png)

# Installation
## Install from PyPI
```
pip install likee-downloader
```
### Note
> In order to run the program, You will need to have the FireFox browser installed on your pc
>> The program is dependent on selenium, so in order to run it, you will have to download and properly setup geckodriver (setup instructions available below)

## Docker
```
docker pull rly0nheart/likee-downloader
```
### Note
> Setting up selenium/geckodriver won't be required for the docker image

# Geckodriver setup
## Linux
**1. Go to the geckodriver [releases page](https://github.com/mozilla/geckodriver/releases/). Find the latest version of the driver for your platform and download it**

**2. Extract the downloaded file**
```
tar -xvzf geckodriver*
```

**3. Make it executable**
```
chmod +x geckodriver
```

**4. Add geckodriver to your system path**
```
export PATH=$PATH:/path/to/downloaded/geckodriver
```

### Note
> If you encounter issues with the above commands, then you should run them as root (with sudo)


## Windows
**1. Go to the geckodriver [releases page](https://github.com/mozilla/geckodriver/releases/). Find the geckodriver.exe binary for your platform and download it**

**2. Move the downloaded executable to** *C:\Users\yourusername\AppData\Local\Programs\Python\Python310*

### Note
> The numbers on the directory 'Python310' will depend on the version of Python you have

## Mac OS
* [Set up Selenium & GeckoDriver (Mac)](https://medium.com/dropout-analytics/selenium-and-geckodriver-on-mac-b411dbfe61bc)


# Usage
## PyPI package
```
likee_downloader --help
```

## Docker image
```
docker run -it -v $PWD/downloads:/app/downloads rly0nheart/likee-downloader --help
```

```
usage: likee_downloader [-h] [-s] [-l LIMIT] [-d {csv,json}] [-dl] username

likee-downloader — by Richard Mwewa | https://about.me/rly0nheart

positional arguments:
  username              username

options:
  -h, --help            show this help message and exit
  -s, --screenshot      capture a screenshot of the target's profile
  -l LIMIT, --limit LIMIT
                        number of videos to get (default: 10)
  -d {csv,json}, --dump {csv,json}
                        dump video data to a specified file type
  -dl, --download       Download all returned videos

A program for downloading videos from Likee, given a username
```
# Donations
If you would like to donate, you could Buy A Coffee for the developer using the button below

<a href="https://www.buymeacoffee.com/_rly0nheart"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=_rly0nheart&button_colour=40DCA5&font_colour=ffffff&font_family=Comic&outline_colour=000000&coffee_colour=FFDD00" /></a>

![me](https://github.com/bellingcat/reddit-post-scraping-tool/assets/74001397/21e0bb33-7a84-45d6-92ba-00e40891ba31)

Your support will be much appreciated!
