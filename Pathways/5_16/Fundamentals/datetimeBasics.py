# Example 1: Python Datetime Basics
from datetime import datetime, timedelta, date

# Creating a datetime object
now = datetime.now()
print(f"Current date and time: {now}")

# Creating a specific datetime
specific_date = datetime(2023, 7, 15, 14, 30)  # Year, Month, Day, Hour, Minute
print(f"Specific date: {specific_date}")

# Formatting datetime objects
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date: {formatted_date}")

# Common format patterns
print(f"Date only (YYYY-MM-DD): {now.strftime('%Y-%m-%d')}")
print(f"Time only (HH:MM:SS): {now.strftime('%H:%M:%S')}")
print(f"Date (MM/DD/YYYY): {now.strftime('%m/%d/%Y')}")
print(f"Day name and month: {now.strftime('%A, %B %d')}")

# Parsing a date string to datetime
date_string = "2023-07-15"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"\nParsed date: {parsed_date}")

# Another example with a different format
date_string2 = "07/15/2023 2:30 PM"
parsed_date2 = datetime.strptime(date_string2, "%m/%d/%Y %I:%M %p")
print(f"Parsed date 2: {parsed_date2}")

# Date arithmetic
tomorrow = now + timedelta(days=1)
print(f"\nTomorrow: {tomorrow}")
yesterday = now - timedelta(days=1)
print(f"Yesterday: {yesterday}")
next_week = now + timedelta(weeks=1)
print(f"Next week: {next_week}")
two_hours_later = now + timedelta(hours=2)
print(f"Two hours later: {two_hours_later}")

# Extracting components
print(f"\nDate components:")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")
print(f"Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}")

# Get day of week (0 = Monday, 6 = Sunday)
print(f"Day of week: {now.weekday()}")  # 0-6 (Monday = 0)
print(f"Weekday name: {now.strftime('%A')}")
print(f"Day of year: {now.timetuple().tm_yday}")

# Comparing dates
date1 = datetime(2023, 5, 1)
date2 = datetime(2023, 6, 1)
print(f"\nComparing dates:")
print(f"date1 < date2: {date1 < date2}")
print(f"Difference in days: {(date2 - date1).days}")

# Creating just date objects (without time)
today = date.today()
print(f"\nToday's date (without time): {today}")
specific_date = date(2023, 12, 25)
print(f"Christmas 2023: {specific_date}")
days_until_christmas = (specific_date - today).days
print(f"Days until Christmas: {days_until_christmas}")

# Show how we can create a datetime from a date
datetime_from_date = datetime.combine(today, datetime.min.time())
print(f"\nDatetime from date: {datetime_from_date}")