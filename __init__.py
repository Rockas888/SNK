#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("10499690", default=None, cast=int)
API_HASH = config("87d0414dc159c10225cac921edde640a", default=None)
BOT_TOKEN = config("6507710656:AAFW_VZHa8QqQrn8E_Xs2IrF5q0IVFhSWsI", default=None)
SESSION = config("BQCt6m-i4mX2vp-AeHPzCqfmyFw6AJKCXgc1tpwx7RiDUx4gZK1V_55H_i_Oq-mnvBkB1iePZD1HA7A0ZczvdcP7qwU-D-jqzvfRZxgbijof4WZcVunCebN3rotMyPEk_PwgRC8JycS4Z9em0cdARaAvTjsUBzo1bXZsPFTtAwzlaSNCSlV6VANM_BzooJW4T2eOEcVRgnyTEB_4RXtO8BnleumMvWMno4NiGtUppQC3uLKLb1CLuyim6VvQNdugHUz-moDX-dDssnXjevxNITtnz3mnwH1y8BEuWUc_vctEr87uouZV54PM6yfXaKNWfL1pK_A4-1T5dC-phN1VBEwZfKhXOAA", default=None)
FORCESUB = config("restrictwala", default=None)
AUTH = config("2091407160", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
