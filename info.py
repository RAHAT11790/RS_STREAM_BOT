import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Rs_link_bots')
API_ID = int(environ.get('API_ID', '25976192')) ##api id fot t.me.org
API_HASH = environ.get('API_HASH', '8ba23141980539b4896e5adbc4ffd2e2') #api hash fot t.me.org
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Bot settings
PORT = environ.get("PORT", "8080") #your hosting site port or use default port

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "") #hosting site URL

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003504080537')) #LOG channel id
ADMINS = [6621572366] #replace with your ID

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://RAHAT1132:RAHAT11a@rahat.txn4lkk.mongodb.net/?appName=Rahat") #mongo DB URL
DATABASE_NAME = environ.get('DATABASE_NAME', "rs_fllink_bot")

# Shortlink Info
SHORTLINK = "False" # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'api.shareus.io')
SHORTLINK_API = environ.get('SHORTLINK_API', 'hRPS5vvZc0OGOEUQJMJzPiojoVK2')
