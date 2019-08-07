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
* Support for ChromeDriver and GeckoDriver.
* Headless mode.
* Slow start mode for older machines.
* IP and User agent rotation.
* Debug mode.

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

| Argument       | Description                  |
| :------------- | :--------------------------- |
| -u, --url URL  | Sets url of video.           |
| -u, --url PATH | Sets path to file with urls. |

### Optional arguments

| Argument                      | Description                         | Default value                  |
| :---------------------------- | :---------------------------------- | :----------------------------- |
| -h, --help                    | Shows help message and exits.       |                                |
| -t, --threads N               | Sets number of threads.             | 15                             |
| -D, --driver {chrome,firefox} | Sets webdriver.                     | chrome                         |
| -H, --headless                | Enables headless mode.              | False                          |
| -s, --slow-start              | Enables slow start mode.            | False                          |
| -p, --proxies PATH            | Sets path to file with proxies.     | Proxies list from internet.    |
| -U, --user-agent AGENT        | Sets user agent.                    | Randomly generated user agent. |
| -U, --user-agent PATH         | Sets path to file with user agents. | Randomly generated user agent. |
| -d, --debug                   | Enables debug mode.                 | False                          |

## Disclaimer

**AdFly-Bot** was created for educational purposes and I'm not taking responsibility for any of your actions.

## Authors

* **Michał Wróblewski** - Main Developer - [DeBos99](https://github.com/DeBos99)

## Contact

* Discord: DeBos#3292
* Reddit: [DeBos99](https://www.reddit.com/user/DeBos99)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
