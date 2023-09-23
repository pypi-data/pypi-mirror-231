from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .admin import *

PAID_TEXTZ = "Pay Money To Use This Bot"

PAID_BUTTONZ = InlineKeyboardMarkup([[InlineKeyboardButton("Pay Now", url="https://t.me/DKBOTZHELP")],])

try:
    from config import EXPIRE_TEXT
except:
    try:
        from configs import EXPIRE_TEXT
    except:
        try:
            from paid import EXPIRE_TEXT
        except:
            EXPIRE_TEXT = "**User Id:** `{user_id}`\n\n**User Name:** @{user_name}\n\n**Plan Validity:** `{paid_duration}` Days\n\n**Joined On** : `{paid_on}`\n\n👋 Your Paid Plan Has Expired On {will_expire}\n\n||**Need More HELP Contact To Our Developer :- @DKBOTZ**||"


try:
    from config import ALREAY_PAID_PLAN_TEXT
except:
    try:
        from configs import ALREAY_PAID_PLAN_TEXT
    except:
        try:
            from paid import ALREAY_PAID_PLAN_TEXT
        except:
            ALREAY_PAID_PLAN_TEXT = "***Your Plan Deatails**\n\n**User Id:** `{user_id}`\n\n**User Name:** @{user_name}\n\nPlan Type : `Paid`\n\n**Plan Validity:** `{paid_duration}` Days\n\n**Plan Buy On** : `{paid_on}`\n\n**Plan Discription** : `{paid_reason}`\n\nDate :- `{current_date}`\n\n👋 Your Paid Plan Has Expired On {will_expire}"

try:
    from config import NOT_PAID_PLAN_TEXT
except:
    try:
        from configs import NOT_PAID_PLAN_TEXT
    except:
        try:
            from paid import NOT_PAID_PLAN_TEXT
        except:
            NO_PAID_PLAN_TEXT = "**Your Plan Deatails**\n\n**User Id:** `{user_id}`\n\n**User Name:** @{user_name}\n\nPlan : `Free`\n\n**Plan Validity:** `Lifetime`\n\nDate :- {current_date}"

try:
    from config import PAID_TEXT
except:
    try:
        from configs import PAID_TEXT
    except:
        try:
            from paid import PAID_TEXT
        except:
            PAID_TEXT = PAID_TEXTZ


try:
    from config import PAID_BUTTONS
except:
    try:
        from configs import PAID_BUTTONS
    except:
        try:
            from paid import PAID_BUTTONS
        except:
            PAID_BUTTONS = PAID_BUTTONZ


try:
    from config import MANGODB_URL
except:
    try:
        from configs import MANGODB_URL
    except:
        try:
            from paid import MANGODB_URL
        except:
            MANGODB_URL = "mongodb+srv://great:great@cluster0.vixtby6.mongodb.net/?retryWrites=true&w=majority"





try:
    from config import SESSION_NAME
except:
    try:
        from configs import SESSION_NAME
    except:
        try:
            from paid import SESSION_NAME
        except:
            SESSION_NAME = "dkbotz"


try:
    from config import PAID_BOT
except:
    try:
        from configs import PAID_BOT
    except:
        try:
            from paid import PAID_BOT
        except:
            PAID_BOT = "NO"




