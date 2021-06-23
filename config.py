import dotenv
import os

dotenv.load_dotenv()

auto_vaccine_url = os.getenv('AUTO_VACCINE_URL')
telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
telegram_chat_id = os.getenv('TELEGRAM_BOT_ID')
