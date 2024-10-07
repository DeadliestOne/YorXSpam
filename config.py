import logging
from os import getenv
from telethon import TelegramClient
from JARVIS.data import FRIDAY

# Configure logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# Environment variables and constants
API_ID = 26416419
API_HASH = "c109c77f5823c847b1aeb7fbd4990cc4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
MONGO_DB_URI = getenv("MONGO_DB_URI")

# Bot tokens
BOT_TOKENS = [
    getenv("7413239375:AAFH20aY3Ie4g1-x9DUrKWoKgUxhJ24AyX8", default=None),
    getenv("7598334054:AAGvkVothxrXAAd0srj7BcITdRrGb6DkOl0", default=None),
    getenv("7919258912:AAERMqgdLT6T0ZO60ZUrs7NfU2E_iZJEfcM", default=None),
    getenv("7821644897:AAHkTCyJzcFLYUBuy_F73qQMLOd_bn92Qro", default=None),
    getenv("7750937190:AAHtO17eyY-s4aEe1oKUTvYcjbTV6Olrnqw", default=None),
    getenv("8000395612:AAGh9U1H5voOMFXINBKWbyTYrsalbwS3e7w", default=None),
    getenv("7393018825:AAFUujEyJoXJhoYTjnEFxXUgMl7iddQvufA", default=None),
    getenv("7830693639:AAG3hCHeB4QlZnIEUtHlg7573PZcWB-BgHU", default=None),
    getenv("7988315589:AAHlFHkhrEa_NrfWw7MpTsH0ftiFEjUBBqQ", default=None),
    getenv("BOT_TOKEN10", default=None),
]

# Sudo users and owner ID
SUDO_USERS = list(map(int, getenv("SUDO_USERS", default="6748827895").split()))
SUDO_USERS.extend(FRIDAY)
OWNER_ID = int(getenv("OWNER_ID", default="6209871909"))
SUDO_USERS.append(OWNER_ID)

# Initialize Telegram clients
clients = []
for idx, bot_token in enumerate(BOT_TOKENS, start=1):
    if bot_token:
        client = TelegramClient(f'X{idx}', API_ID, API_HASH).start(bot_token=bot_token)
        clients.append(client)
        logging.info(f'Initialized bot X{idx}')

# Assign clients to specific variables for convenience
X1, X2, X3, X4, X5, X6, X7, X8, X9, X10 = clients[:10]

