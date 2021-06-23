import requests
import json
from datetime import datetime

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
        print('Checking...')

        response = requests.get(
            url=self.URL
        )

        end_date = datetime.strptime(response.json()['dFin_Birthday'], '%d/%m/%Y')

        if end_date.year == self.birth_year:
            self.notify('You can make an appointment now to COVID-19 vaccination')
            return True

        return False

    def notify(self, message):
        print(message)

        if self.telegram_notifications:
            TelegramBot.send_message(message)
