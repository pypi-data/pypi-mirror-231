from datetime import datetime

def get_current_month():
    current_date = datetime.now()
    month = current_date.strftime("%m")
    return month