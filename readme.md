
# X (formerly Twitter) Auto Like Bot using SeleniumBase

This Python bot automates the process of logging into X (formerly Twitter) and liking posts using SeleniumBase. Due to the recent changes in X's API, which is no longer free, this bot provides an alternative way to automate interactions with X without relying on the official API.

## Features
- Automatically logs into X using a provided username and password.
- Navigates through posts and likes them.
- Handles potential errors and retries the login process.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.7+
- Google Chrome or Chromium browser installed
- Chromedriver (SeleniumBase handles this automatically)

### Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/x-auto-like-bot.git
   cd x-auto-like-bot
   ```

2. **Install the required packages**:
   You can install SeleniumBase using pip:
   ```bash
   pip install seleniumbase
   ```

3. **Update the credentials**:
   In the script, replace the following variables with your X (formerly Twitter) username and password:
   ```python
   username = "your_username"
   password = "your_password"
   ```

### Usage

1. **Run the bot**:
   After updating your credentials, simply run the script:
   ```bash
   python like_bot.py
   ```

2. **How it works**:
   - The bot will open the X login page.
   - It will automatically enter the username and password.
   - After logging in, the bot will search for posts and automatically like them.

### YouTube Tutorial

Watch the full tutorial on how to set up and run this bot on YouTube:

[![Watch the tutorial](https://img.youtube.com/vi/C70jwFemBFs/maxresdefault.jpg)](https://www.youtube.com/watch?v=C70jwFemBFs)


### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute and enhance the project! Pull requests are welcome.
