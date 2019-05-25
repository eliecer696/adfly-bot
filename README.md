# AdFly-Bot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AdFly-Bot** is bot created for [adf.ly](https://adf.ly/) website.

## Content

- [Content](#content)
- [Prerequisites](#prerequisites)
  - [Windows](#Prerequisites-Windows)
- [Installation](#installation)
  - [Windows](#Installation-Windows)
  - [Linux & MacOS](#Linux&MacOS)
- [Usage](#usage)
- [Documentation](#documentation)
  - [Required arguments](#required-arguments)
  - [Optional arguments](#optional-arguments)
- [Disclaimer](#disclaimer)
- [Authors](#authors)
- [Contact](#contact)
- [License](#license)

## Prerequisites

### <a name="Prerequisites-Windows">Windows

Install **Google Chrome Browser**: https://www.google.com/chrome/

Download **ChromeDriver** and move the executable to folder in your **PATH**: http://chromedriver.chromium.org/downloads

Or

Install **Mozilla Firefox Browser**: https://www.mozilla.org/en-US/firefox/new/

Download **geckodriver**, unzip and move the executable to folder in your **PATH**: https://github.com/mozilla/geckodriver/releases

## Installation

### <a name="Installation-Windows">Windows

Install Python: https://www.python.org/downloads/

```
git clone "https://github.com/DeBos99/adfly-bot.git"
cd adfly-bot
install.bat
cd ..
```

### <a name="Linux&MacOS">Linux & MacOS

```
git clone "https://github.com/DeBos99/adfly-bot.git"
cd adfly-bot
./install.sh
cd ..
```

## Usage

`python main.py ARGUMENTS`

## Documentation

### Required arguments

| Argument              | Description                                    |
| :---                  | :---                                           |
| -u URL<br>--url URL   | Sets the url of video to **URL**.              |
| -u PATH<br>--url PATH | Sets the path to the list of urls to **PATH**. |

### Optional arguments

| Argument                        | Description                                           | Default value                  |
| :---                            | :---                                                  | :---                           |
| -h<br>--help                    | Shows help message.                                   |                                |
| -t T<br>--threads T             | Sets the number of threads to **T**.                  | 15                             |
| -p PATH<br>--proxies PATH       | Sets the path to the list of proxies to **PATH**.     | Proxies list from internet.    |
| -dr DRIVER<br>--driver DRIVER   | Sets the webdriver to **DRIVER**.                     | Chrome.                        |
| -hd<br>--headless               | Sets the webdriver as headless.                       | False.                         |

## Disclaimer

**AdFly-Bot** was created for educational purposes and I'm not taking responsibility for any of your actions.

## Authors

* **Michał Wróblewski** - Main Developer - [DeBos99](https://github.com/DeBos99)

## Contact

Discord: DeBos#3292

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
