import datetime


def generate_slots(start_time, time_duration, no_of_slots):
    slots = []
    start_time = datetime.datetime.strptime(start_time, "%H:%M")
    for i in range(int(no_of_slots)):
        end_time = (start_time + datetime.timedelta(minutes=int(time_duration)))
        slots.append((str(start_time.time()), str(end_time.time())))
        start_time = end_time
    return slots


def generate_selected_dates(current_date, end_date, weekdays):
    selected_dates = []
    while current_date <= end_date:
        if current_date.weekday() in weekdays:
            selected_dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += datetime.timedelta(days=1)
    # print("selected_dates: ", selected_dates)
    return selected_dates
