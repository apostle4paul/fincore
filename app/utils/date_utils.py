from datetime import date, datetime

def today()-> str:
    return date.today().isoformat()

def current_time()-> str:
    return datetime.now().isoformat(timespec="seconds")