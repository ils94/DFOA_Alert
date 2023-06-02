import datetime


def event_get_time():
    current_time = datetime.datetime.now().time()

    event_start_minutes = [6, 36]

    event_duration = datetime.timedelta(minutes=30)

    closest_start_time = None
    closest_time_diff = datetime.timedelta(hours=1)

    for start_minute in event_start_minutes:
        start_time = datetime.datetime.combine(datetime.date.today(), datetime.time(current_time.hour, start_minute))

        if current_time >= start_time.time():
            time_diff = datetime.datetime.combine(datetime.date.today(), current_time) - start_time
        else:
            time_diff = start_time - datetime.datetime.combine(datetime.date.today(), current_time)

        if time_diff < closest_time_diff:
            closest_start_time = start_time
            closest_time_diff = time_diff

    started_time = closest_start_time.strftime("%H:%M")

    remaining_time = closest_start_time + event_duration - datetime.datetime.now()

    remaining_seconds = int(remaining_time.total_seconds())

    return int(remaining_seconds), started_time
