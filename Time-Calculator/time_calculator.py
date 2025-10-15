def add_time(start, duration, day=None):
    # Days of the week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Split start time
    time, period = start.split()
    start_hour, start_minute = map(int, time.split(":"))

    # Convert start time to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    if period == "AM" and start_hour == 12:
        start_hour = 0

    # Split duration
    dur_hour, dur_minute = map(int, duration.split(":"))

    # Add duration
    total_minutes = start_minute + dur_minute
    extra_hour = total_minutes // 60
    end_minute = total_minutes % 60

    total_hours = start_hour + dur_hour + extra_hour
    days_later = total_hours // 24
    end_hour_24 = total_hours % 24

    # Convert back to 12-hour format
    if end_hour_24 == 0:
        end_hour = 12
        end_period = "AM"
    elif end_hour_24 < 12:
        end_hour = end_hour_24
        end_period = "AM"
    elif end_hour_24 == 12:
        end_hour = 12
        end_period = "PM"
    else:
        end_hour = end_hour_24 - 12
        end_period = "PM"

    # Format minute with leading zero
    end_minute_str = str(end_minute).rjust(2, "0")

    # Start building result
    new_time = f"{end_hour}:{end_minute_str} {end_period}"

    # If day of week is provided
    if day:
        day_index = days.index(day.capitalize())
        new_day = days[(day_index + days_later) % 7]
        new_time += f", {new_day}"

    # Add info about days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time