# This code has been modified by @Safaridev
# Please do not remove this credit
import re
import os
from os import environ, getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', "29870283")
API_HASH = environ.get('API_HASH', "e803aa1882327dc35bb0276279a849c2")
BOT_TOKEN = environ.get('BOT_TOKEN', "")
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled((environ.get('USE_CAPTION_FILTER', 'True')), True)
PICS = (environ.get('PICS', '')).split()
WELCOME_VID = environ.get("WELCOME_VID", "https://telegra.ph/file/451f038b4e7c2ddd10dc0.mp4")

#premium imag
REFFER_PIC = environ.get('REFFER_PIC', '')
PREMIUM_PIC = environ.get('SUBSCRIPTION', '')
QR_CODE = environ.get('QR_CODE', '') # Scanner Code image 
#refer time, or feffer count
REFERAL_TIME = int(environ.get('REFERAL_USER_TIME', "2592000")) # set in seconds | already seted 1 month premium
REFFER_POINT = int(environ.get('USER_POINT', "50")) # Set Referel point Count 
#premium Users Satuts
premium = environ.get('PREMIUM_LOGS', '-1002080161079')
PREMIUM_LOGS = int(premium) if premium and id_pattern.search(premium) else None
# lock file, set file limit 
FILE_LIMITE = int(environ.get('FILE_LIMITE', 15))
SEND_ALL_LIMITE = int(environ.get('SEND_ALL_LIMITE', 3))
LIMIT_MODE = is_enabled((environ.get('LIMIT_MODE', 'True')), False)

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6522991984').split()]
OWNER_USER_NAME = environ.get("OWNER_USER_NAME", "wrrohit02") # widout 👉 @
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002149802025').split()]
# post channel auto post new movie
POST_CHANNELS = list(map(int, (channel.strip() for channel in environ.get('POST_CHANNELS', '--1002080161079').split(','))))
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '0'))
AUTH_REQ_CHANNEL = int(environ.get('AUTH_REQ_CHANNEL', '0'))
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'True')), False)

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://modes10542:XyHc63deIs6fFSSM@cluster0.geelpoy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'wrrohit02')

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'sharedisklinks.com'))
STREAM_API = (environ.get('STREAM_API', '587f94f0e0b1813a52aed61290af6ea79d6ee464'))
STREAM_HTO = (environ.get('STREAMHTO', 'https://t.me/wrrohit02'))
STREAM_MODE = is_enabled((environ.get('STREAM_MODE', "False")), False)


#verify site api and url
IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'False')), False)
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
VERIFY_URL = environ.get('VERIFY_URL', 'sharedisklinks.com')
VERIFY_API = (environ.get('VERIFY_API', '587f94f0e0b1813a52aed61290af6ea79d6ee464'))

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "600"))
VERIFY_URL2 = environ.get('VERIFY_URL2', 'sharedisklinks.com')
VERIFY_API2 = (environ.get('VERIFY_API2', '587f94f0e0b1813a52aed61290af6ea79d6ee464'))
 
THIRD_VERIFY_GAP = int(environ.get('THIRD_VERIFY_GAP', "600"))
VERIFY_URL3 = environ.get('VERIFY_URL3', 'sharedisklinks.com')
VERIFY_API3 = (environ.get('VERIFY_API3', '587f94f0e0b1813a52aed61290af6ea79d6ee464'))
 
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/shdjekkw')
TUTORIAL2 = environ.get('TUTORIAL2', 'https://t.me/hejejje')
TUTORIAL3 = environ.get('TUTORIAL3', 'https://t.me/safabsovhwi3')

# auto files delete
AUTO_FILE_DELETE = is_enabled((environ.get('AUTO_FILE_DELETE', "True")), False)

DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1001998895377').split()]
MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/wrbackup')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/wrmovies')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1002162269855))
GROUP_VERIFY_LOGS = int(environ.get('GROUP_VERIFY_LOGS', -1002162269855)) # Group verify stats 
REQ_CHANNEL = int(environ.get('REQ_CHANNEL', -1002162269855)) # movies request channel, else log channel
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'motumovies')
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
PM_FILTER = is_enabled((environ.get('PM_FILTER', "True")), False)

SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)

REACTION = ["🔥", "❤️", "😍", "⚡", "👍", "❤", "🔥", "🥰", "👏", "😁", "🎉", "🤩", "🙏", "👌", "🕊", "❤‍🔥", "⚡", "😇", "🤗", "😘", "🙊", "😎"]

# Streaming
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", "-1002162269855")) 
PORT = int(environ.get('PORT', 8080))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'safaribotts'))
MULTI_CLIENT = False
name = str(environ.get('name', 'safaribotts'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "https://{}/".format(FQDN)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

