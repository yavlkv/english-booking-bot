from datetime import datetime, timedelta
from html import escape

from .config import DAY_NAMES
from .state import user_names


def parse_slot(slot):
    return slot.split("_", 1)


def format_slot(slot, prefix="• "):
    day, time_range = slot.split("_", 1)
    from .config import DAY_NAMES 
    
    date_str = get_next_date(day) 
    return f"{prefix}{DAY_NAMES[day]} ({date_str}) {time_range}"


def format_slot_list(slots, prefix="- "):
    return "\n".join(format_slot(slot, prefix=prefix) for slot in slots)


def get_slot_datetime(day, time_range):
    today = datetime.today()
    weekday_map = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5}

    start_str = time_range.split("-", 1)[0]
    hour_part, minute_part = start_str.split(":")
    hour = int(hour_part)
    minute = int(minute_part)

    days_ahead = (weekday_map[day] - today.weekday()) % 7
    slot_date = (today + timedelta(days=days_ahead)).date()
    slot_datetime = datetime(slot_date.year, slot_date.month, slot_date.day, hour, minute, 0, 0)

    if days_ahead == 0 and slot_datetime <= today:
        slot_datetime += timedelta(days=7)

    return slot_datetime


def format_user_label(user_id):
    display_name = escape(user_names.get(user_id, f"ID {user_id}"))
    if user_id in user_names:
        return f'<a href="tg://user?id={user_id}">{display_name}</a>'
    return display_name

from datetime import datetime, timedelta

def get_next_date(day_code):
    """Возвращает строку с датой ближайшего указанного дня недели."""
    weekday_map = {
        "mon": 0, "tue": 1, "wed": 2, "thu": 3, 
        "fri": 4, "sat": 5, "sun": 6
    }
    
    today = datetime.now()
    target_weekday = weekday_map[day_code]
    
    days_ahead = target_weekday - today.weekday()
    
    if days_ahead < 0:
        days_ahead += 7
        
    next_date = today + timedelta(days=days_ahead)
    return next_date.strftime("%d.%m") 
