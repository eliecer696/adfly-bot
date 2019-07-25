# AdFly-Bot

![Made with Python](https://img.shields.io/badge/made%20with-python-0.svg?color=cc2020&labelColor=ff3030&logo=python&logoColor=white&style=for-the-badge)

![GitHub](https://img.shields.io/github/license/DeBos99/adfly-bot.svg?color=2020cc&labelColor=5050ff&style=for-the-badge)
![GitHub followers](https://img.shields.io/github/followers/DeBos99.svg?color=2020cc&labelColor=5050ff&style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/DeBos99/adfly-bot.svg?color=2020cc&labelColor=5050ff&style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/DeBos99/adfly-bot.svg?color=2020cc&labelColor=5050ff&style=for-the-badge)
![GitHub watchers](https://img.shields.io/github/watchers/DeBos99/adfly-bot.svg?color=2020cc&labelColor=5050ff&style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/DeBos99/adfly-bot.svg?color=2020cc&labelColor=5050ff&style=for-the-badge)

![GitHub commit activity](https://img.shields.io/github/commit-activity/w/DeBos99/adfly-bot.svg?color=ffaa00&labelColor=ffaa30&style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/DeBos99/adfly-bot.svg?color=ffaa00&labelColor=ffaa30&style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/DeBos99/adfly-bot.svg?color=ffaa00&labelColor=ffaa30&style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/DeBos99/adfly-bot.svg?color=ffaa00&labelColor=ffaa30&style=for-the-badge)

![GitHub issues](https://img.shields.io/github/issues-raw/DeBos99/adfly-bot.svg?color=cc2020&labelColor=ff3030&style=for-the-badge)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/DeBos99/adfly-bot.svg?color=10aa10&labelColor=30ff30&style=for-the-badge)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=NH8JV53DSVDMY)

**AdFly-Bot** is bot created for [adf.ly](https://adf.ly/) website.

## Content

- [Content](#content)
- [Features](#features)
- [Installation](#installation)
  - [Windows](#windows)
  - [Unix](#unix)
    - [Debian/Ubuntu](#apt)
    - [Arch Linux/Manjaro](#pacman)
    - [CentOS](#yum)
    - [MacOS](#homebrew)
- [Usage](#usage)
- [Documentation](#documentation)
  - [Required arguments](#required-arguments)
  - [Optional arguments](#optional-arguments)
- [Disclaimer](#disclaimer)
- [Authors](#authors)
- [Contact](#contact)
- [License](#license)

## Features

* Multi-threaded.
* Support for multiple URLs.
* IP rotation.
* User agent rotation.
* Support for chromedriver and Geckodriver.
* 3 modes of verbosity.
* Headless mode.
* Slow start mode for older machines.

## Installation

### Windows

* Install [Git](https://git-scm.com/download/win).
* Install [Python](https://www.python.org/downloads/).
* Install [Google Chrome](https://www.google.com/chrome/).
<br>Or
<br>Install [Firefox](https://www.mozilla.org/firefox/new/).
* Run following command in the command prompt:
```
git clone "https://github.com/DeBos99/adfly-bot.git"
```

### Unix

#### <a name="APT">Debian/Ubuntu based

* Run following commands in the terminal:
```
sudo apt install git python -y
git clone "https://github.com/DeBos99/adfly-bot.git"
```

#### <a name="Pacman">Arch Linux/Manjaro

* Run following commands in the terminal:
```
sudo pacman -S git python --noconfirm
git clone "https://github.com/DeBos99/adfly-bot.git"
```

#### <a name="YUM">CentOS

* Run following commands in the terminal:
```
sudo yum install git python -y
git clone "https://github.com/DeBos99/adfly-bot.git"
```

#### <a name="Homebrew">MacOS

* Run following commands in the terminal:
```
brew install git python
git clone "https://github.com/DeBos99/adfly-bot.git"
```

## Usage

`python main.py ARGUMENTS`

## Documentation

### Required arguments

| Argument              | Description                                    |
| :-------------------- | :--------------------------------------------- |
| -u URL<br>--url URL   | Sets the url of video to **URL**.              |
| -u PATH<br>--url PATH | Sets the path to the list of urls to **PATH**. |

### Optional arguments

| Argument                        | Description                                           | Default value                  |
| :------------------------------ | :---------------------------------------------------- | :----------------------------- |
| -h<br>--help                    | Shows help message.                                   |                                |
| -t T<br>--threads T             | Sets the number of threads to **T**.                  | 15                             |
| -p PATH<br>--proxies PATH       | Sets the path to the list of proxies to **PATH**.     | Proxies list from internet.    |
| -U AGENT<br>--user-agent AGENT  | Sets the user agent to **AGENT**.                     | Randomly generated user agent. |
| -U PATH<br>--user-agent PATH    | Sets the path to the list of user agents to **PATH**. | Randomly generated user agent. |
| -D DRIVER<br>--driver DRIVER    | Sets the webdriver to **DRIVER**.                     | Chrome.                        |
| -v<br>--verbose                 | Enables verbose mode.                                 | False.                         |
| -d<br>--debug                   | Enables debug mode.                                   | False.                         |
| -H<br>--headless                | Sets the webdriver as headless.                       | False.                         |
| -s<br>--slow-start              | Starts webdrivers one by one.                         | False.                         |

## Disclaimer

**AdFly-Bot** was created for educational purposes and I'm not taking responsibility for any of your actions.

## Authors

* **Michał Wróblewski** - Main Developer - [DeBos99](https://github.com/DeBos99)

## Contact

Discord: DeBos#3292

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
