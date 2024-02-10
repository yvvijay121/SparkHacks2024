from datetime import datetime, timedelta

def generate_events(start_date, end_date, event_count):
    events = []
    date_format = "%Y-%m-%d"
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)

    number_of_days = (end - start).days

    for i in range(number_of_days):
        start_of_day = start + timedelta(days=i)
        for j in range(event_count):
            events.append({
                "start_date": start_of_day + j * timedelta(hours=24 / event_count) - timedelta(minutes=15),
                "end_date": start_of_day + j * timedelta(hours=24 / event_count) + timedelta(minutes=15)
            })
    
    return events

print(generate_events("2024-01-01", "2024-01-02", 3))