
class Config(object):
    LOGGER = True

    API_ID = "12227067 " 
    API_HASH = "b463bedd791aa733ae2297e6520302fe"
    TOKEN = "6629158067:AAE8SSkEMDhyTstiCA0hDYQWqpaLhFcDEbs"  
    OWNER_ID = 5360305806 
    CHAT = "+jCS-YsVBVEE3NjQ1"
    SUPPORT_CHAT = "AM_YTSUPPORT"
    START_IMG = "https://graph.org/file/41d20249ffdb1151b8870.jpg"
    EVENT_LOGS = ("-1001908711819")
    JOIN_LOGGER = ("-1001841879487")
    MONGO_DB_URI= "mongodb+srv://DevuMusicBot:CBPNyUTcJCD1P8ZD@devumusicbot.sdqazcu.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_URL = "postgres://yone:Kushal55@yone.cirqmtrbghab.us-east-1.rds.amazonaws.com:5432/yone" 
    CASH_API_KEY = ("PNNU99H3W9KDLKVM"  )
    TIME_API_KEY = "9HK7J0H25AKQ"
    BL_CHATS = []  
    DRAGONS = [] 
    DEV_USERS = []  
    DEMONS = []  
    TIGERS = []  
    WOLVES = []  
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
