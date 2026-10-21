import os
from pathlib import Path

TOKEN = "8992197599:AAE_D0QlxnUrh0__fRz9l9gFIb3cXHQu4T0"
TEACHER_ID = int(os.getenv("TEACHER_ID", "778465110"))
DATA_FILE = Path(__file__).resolve().parent.parent / "bot_state.json"
# Расписание для пробных занятий (например, только определенные часы)
TRIAL_SLOTS = {
    "mon": ["19:00-19:30", "19:30-20:00"],
    "tue": ["18:30-19:00"],
    "thu": ["18:00-18:30", "18:30-19:00"],
    "sat": ["10:00-10:30", "10:30-11:00"],
}

# Расписание для разовых занятий (60 минут)
REGULAR_SLOTS = {
    "tue": ["19:00-20:00"],
    "wed": ["19:00-20:00"],
    "thu": ["19:00-20:00"],
    "sat": ["11:00-12:00", "12:00-13:00"],
}
