# Auto vaccine appointment checker

Bot to check if there are available to make an appointment to COVID-19 vaccine in Madrid.

## Requirements

- Docker.
- Python >= 3.7 (if you don't use docker).

## Instructions

- Copy environment file example .env.example to .env and fill it:
    - `AUTO_VACCINE_URL`: Url to check the init and end dates allowed to make an appointment
    
    - Telegram vars:
        - `TELEGRAM_BOT_TOKEN`: Telegram bot token (view telegram instructions)
        - `TELEGRAM_BOT_ID`: Telegram bot id (view telegram instructions)
    
        
*Docker usage instructions*
- Build docker image: `docker image build -t madrid_autovaccine_checker .`

*Python command line usage instructions*
- Install dependencies: `pip install -r requirements.txt`

## Telegram instructions

To get telegram notifications, you must follow create your own bot following this instructions:

- Search @BotFather on Telegram.
- Send `/start` to join it.
- Send `/newbot` to create your own bot.
- Enter a bot name.
- Enter a unique bot username (it has to end with `_bot`).
- Copy the `token` and join to it with your account (search it by username).
- To get the `id`, join to it and on same session (browser), navigate to `https://api.telegram.org/bot<token>/getUpdates` and search the `id` on json.

## Usage

- Using docker: `docker container run app python app.py`.
- Using python command line: `python app.py`.
- Follow the instructions.

## Disclaimers

- This script works only on healthcare system.
- Use only for study purposes.
- Use under your own risk.