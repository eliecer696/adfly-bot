# AdFly-Bot

**AdFly-Bot** is bot created for [adf.ly](https://adf.ly/) website.

## Content

- [Content](#content)
- [Prerequisites](#prerequisites)
  - [Windows](#Prerequisites-Windows)
- [Installation](#installation)
  - [Windows](#Installation-Windows)
  - [Linux & MacOS](#Linux&MacOS)
- [Usage](#usage)
- [TODO](#todo)
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

Show help:

`python main.py --help`

Set url of the link to **URL**:

`python main.py --url URL`

Set the path of the urls list to **PATH**:

`python main.py --url PATH`

Set number of the threads to **T** (default: 15):

`python main.py --url URL --threads T`

Set the driver as headless:

`python main.py --headless`

Set the path of proxies list to **PATH** (default: proxies loaded from web):

`python main.py --url URL --proxies PATH`

Set the driver for the bot to chrome:

`python main.py --url URL --driver chrome`

Set the driver for the bot to firefox:

`python main.py --url URL --driver firefox`

## Disclaimer

**AdFly-Bot** was created for educational purposes and I'm not taking responsibility for any of your actions.

## Authors

* **Michał Wróblewski** - Main Developer - [DeBos99](https://github.com/DeBos99)

## Contact

Discord: DeBos#3292

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
