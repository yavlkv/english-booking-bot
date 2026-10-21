import os
from pathlib import Path

TOKEN = "8992197599:AAE_D0QlxnUrh0__fRz9l9gFIb3cXHQu4T0"
TEACHER_ID = int(os.getenv("TEACHER_ID", "778465110"))
DATA_FILE = Path(__file__).resolve().parent.parent / "bot_state.json"
TIME_SLOTS = {
    "mon":["19:00-20:00"],
    "tue":["18:00-19:00", "19:00-20:00"],
    "wed":["19:00-20:00"],
    "thu":["18:00-19:00", "19:00-20:00"],
    "sat":["10:00-11:00", "11:00-12:00", "12:00-13:00"],
}

DAY_NAMES = {
    "mon": "Понедельник",
    "tue": "Вторник",
    "wed": "Среда",
    "thu": "Четверг",
    "sat": "Суббота",
}
