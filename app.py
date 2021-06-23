import time

import config
from AutoVaccineChecker import AutoVaccineChecker

if __name__ == '__main__':
    birth_year = int(input('What is your year of birth?: '))
    seconds_between_requests = int(input('Set seconds between requests (60): ') or '60')
    telegram_notification = True if (input('Want to be notify on Telegram? [y]/n: ') or 'y').lower() == 'y' else False

    while not AutoVaccineChecker(config.auto_vaccine_url, birth_year, telegram_notification).available():
        time.sleep(seconds_between_requests)
