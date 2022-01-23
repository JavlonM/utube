import os


class Config:

    BOT_TOKEN = 5137083191:AAGjLLIFdsGCcgYmXBzkJuBBHy0X9UDvUSg

    SESSION_NAME = 1

    API_ID = 9314947

    API_HASH = 0b5efbc3295a6e8941abaed9760afb7c

    CLIENT_ID = 351121494353-o8ckvdia7ss2n6cnteeg39m3l4v75jpu.apps.googleusercontent.com

    CLIENT_SECRET = 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

    BOT_OWNER = 5021325274

    AUTH_USERS_TEXT = 5021325274

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
