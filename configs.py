import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "13290427"))
    API_HASH = os.environ.get("API_HASH", "c33b2f280810fc2f60a6387a4c4217f2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5894919927:AAHTPcseEL_HRJE7ik2SVGKa0nhKCqXSkE0")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOLsBu7SJS71LBT0H9mAGqMi1hvPRLSO_zDQL3GwMwoGhx_0F21cOxz_AAMIVDMSTBSh0oz7FISaWAdrnwKyZX3iOsupa4Fp-v8BTkPy71k6J-vMEFqJXn2UKNqbRFs2I2HhVCkrHHsRefxBHOdOKU5P18RHaZ4OCdMWzAQrr_MLsz9cn1LK7dfRGhO3SV4TpIL7R9UtzTLZP4wCz_y6IgLwWu3pDoEI_FII8534WJUUVrexaOpBeCSxeTlZ7SdMcPY4INhNqcsFAaji82kah6Hb8dNw15SQuDVPxFiU4dLdhy2mBDb3MkGENsfBOnUaHq3dpM9vpfmXtBe9NWskPzOHrrFA=")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001711211283"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mdisk_search_ary_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5079629749"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aryan1082:aryan_1082@cluster0.jmqpi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <b> Link Search Bot </b>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='render.com'>Render</a>

👨‍💻 Created By: <a href='https://t.me/starkownerbot'>Stark Owner Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/starkownerbot'>Stark Owner Bot</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @starkownerbot</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @starkownerbot</a></b>
"""

