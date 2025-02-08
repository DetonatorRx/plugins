from os import getenv
from strings.helpers import HELPER
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "25981592"))
API_HASH = getenv("API_HASH", "709f3c9d34d83873d3c7e76cdd75b866")
SESSION1 = getenv("SESSION1")
ALIVE_PIC = getenv("ALIVE_PIC", "https://graph.org/file/5d4a2dbf4f196fcdfe4d2.mp4")
HELP_PIC = getenv("HELP_PIC", "https://graph.org/file/e0fcedd2df8ac254bb506.jpg")
OWNER_ID = int(getenv("OWNER_ID", "6257927828"))
PM_PIC = "https://graph.org/file/bf1fdd404a82d508a7ed5.jpg"

SESSIONS = [SESSION1]
for i in range(2, 11):
    session = getenv(f"SESSION{i}")
    if session:
        SESSIONS.append(session)

SUDO_USERS = getenv("SUDO_USERS", "")
SUDO_USERS = [int(user_id) for user_id in SUDO_USERS.strip("[]").split(",") if user_id.isdigit()]

if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

SUDO_USERS.extend(HELPER)

