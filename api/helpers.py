from datetime import datetime

def parse_date(date_string):
    return f"{date_string}T12:00:00"

def parse_location(full_location):
    return ",".join(full_location.split(',')[:2])
