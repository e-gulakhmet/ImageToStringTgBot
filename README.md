This Telegram bot is designed to extract text from images. Follow the steps below to set up and run the bot.

![Example](./docs/example.jpg)

## Prerequisites

**Telegram Bot Token:** Obtain a Telegram Bot Token from BotFather. Set it as the `BOT_TOKEN` environment variable.
```bash
export BOT_TOKEN=<Your Telegram Bot Token>
```

**System Dependencies:** Install Tesseract OCR to your system.

**Python Dependencies:** Install the required dependencies using `pip`.
```bash
pip install -r requirements.txt
```

## Running the Bot

Execute the `main.py` file to start the bot.

```bash
python main.py
```

## How to Use

1. Start a chat with your bot on Telegram.
2. Send an image to the bot.
3. The bot will process the image and reply with the extracted text. The first reply may be long (downloading models for text recognition).
