import requests
import json
from zoneinfo import ZoneInfo
from datetime import datetime, timezone

import config
from TelegramBot import TelegramBot


class AutoVaccineChecker:
    URL = ''
    telegram_notifications = False
    birth_year = ''

    def __init__(self, auto_vaccine_url, birth_year, telegram_notifications):
        self.birth_year = birth_year
        self.telegram_notifications = telegram_notifications
        self.URL = auto_vaccine_url

    def available(self):
        current_date = datetime.now().replace(tzinfo=timezone.utc).astimezone(ZoneInfo("Europe/Madrid"))

        print(f'[{current_date.strftime("%Y-%m-%d %H:%M:%S")}] Checking...')

        response = requests.get(
            url=self.URL
        )

        end_date = datetime.strptime(response.json()['dFin_Birthday'], '%d/%m/%Y')

        print(f'Current limit year: {end_date.year}')

        if end_date.year == self.birth_year:
            self.notify('You can make an appointment now to COVID-19 vaccination')
            return True

        return False

    def notify(self, message):
        print(message)

        if self.telegram_notifications:
            TelegramBot.send_message(message)
