def calculate_remaining_minutes():
    from datetime import datetime

    # Get current time
    now = datetime.now()

    # Calculate how many minutes passed from the last hour
    minutes_passed = now.minute

    # Calculate the remaining minutes until the next 20-minute mark
    remaining_minutes = 20 - (minutes_passed % 20)

    # Convert remaining minutes to seconds
    remaining_seconds = remaining_minutes * 60
    return remaining_seconds
