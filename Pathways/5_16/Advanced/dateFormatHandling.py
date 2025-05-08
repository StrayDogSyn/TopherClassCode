# Advanced Date Format Handling and Frequency Examples
# Time Series Basics - Session 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Part 1: Handling Different Date Formats
# -----------------------------------------------------------------------------
print("PART 1: HANDLING DIFFERENT DATE FORMATS")
print("=" * 70)

# Common date formats in real-world data
date_formats = [
    '2023-07-15',            # ISO format
    '15/07/2023',            # European format
    'July 15, 2023',         # Text format
    '7/15/23',               # US format
    '2023.07.15',            # Period separated
    '20230715',              # Compact format
    '15-Jul-2023'            # Abbreviated month format
]

# Converting all formats to datetime using pandas's flexible parser
print("Converting different date formats to datetime:")
for date_str in date_formats:
    dt = pd.to_datetime(date_str)
    print(f"Original: {date_str:<15} → Converted: {dt} (Type: {type(dt)})")

# Handling ambiguous formats with format specification
print("\nHandling ambiguous formats with format specification:")
ambiguous_date = '01-02-2023'  # Could be Jan 2 or Feb 1
# Specify the format to ensure correct parsing
jan_2 = pd.to_datetime(ambiguous_date, format='%d-%m-%Y')  # Day-Month-Year
feb_1 = pd.to_datetime(ambiguous_date, format='%m-%d-%Y')  # Month-Day-Year
print(f"Original: {ambiguous_date}")
print(f"As Day-Month-Year (%d-%m-%Y): {jan_2}")
print(f"As Month-Day-Year (%m-%d-%Y): {feb_1}")

# Common format codes reference
print("\nCommon format codes reference:")
format_codes = {
    '%Y': 'Year with century (2023)',
    '%y': 'Year without century (23)',
    '%m': 'Month as number (01-12)',
    '%d': 'Day of month (01-31)',
    '%B': 'Full month name (January)',
    '%b or %h': 'Abbreviated month name (Jan)',
    '%A': 'Full weekday name (Monday)',
    '%a': 'Abbreviated weekday name (Mon)',
    '%H': 'Hour (24-hour clock, 00-23)',
    '%I': 'Hour (12-hour clock, 01-12)',
    '%p': 'AM/PM',
    '%M': 'Minute (00-59)',
    '%S': 'Second (00-59)',
    '%f': 'Microsecond (000000-999999)'
}

for code, description in format_codes.items():
    print(f"{code:<10} {description}")

# Handling errors in date parsing
print("\nHandling errors in date parsing:")
problematic_dates = ['2023/13/01',  # Invalid month
                   'February 30, 2023',  # Invalid day
                   'Not a date',  # Not a date
                   '2023-07']  # Incomplete date

# Method 1: Using errors='coerce' to set invalid dates to NaT (Not a Time)
print("Using errors='coerce':")
for date_str in problematic_dates:
    dt = pd.to_datetime(date_str, errors='coerce')
    print(f"Original: {date_str:<20} → Result: {dt}")

# Method 2: Using try-except to handle errors
print("\nUsing try-except:")
for date_str in problematic_dates:
    try:
        dt = pd.to_datetime(date_str)
        print(f"Original: {date_str:<20} → Result: {dt}")
    except Exception as e:
        print(f"Original: {date_str:<20} → Error: {str(e)}")

# Method 3: Using a custom parser function
print("\nUsing a custom parser function:")
def safe_parse_date(date_str):
    try:
        # Try standard parsing
        return pd.to_datetime(date_str)
    except:
        # Try with a different format if the first attempt fails
        try:
            # For incomplete dates like '2023-07', append a day
            if len(date_str.split('-')) == 2:
                return pd.to_datetime(date_str + '-01')
            return None  # Return None if can't parse
        except:
            return None

for date_str in problematic_dates:
    dt = safe_parse_date(date_str)
    print(f"Original: {date_str:<20} → Result: {dt}")

# Part 2: Working with Different Time Frequencies
# -----------------------------------------------------------------------------
print("\n\nPART 2: WORKING WITH DIFFERENT TIME FREQUENCIES")
print("=" * 70)

# Creating time series with different frequencies
frequencies = [
    ('Hourly', 'H', 24),
    ('Daily', 'D', 10),
    ('Weekly', 'W', 5),
    ('Monthly', 'M', 6),
    ('Quarterly', 'Q', 4),
    ('Annual', 'Y', 3),
    ('Business Days', 'B', 10),
    ('Business Month End', 'BM', 6),
    ('Semi-Month', 'SM', 6),  # 15th and end of month
    ('Business Quarter End', 'BQ', 4)
]

print("Example date ranges with different frequencies:")
for name, freq, periods in frequencies:
    date_range = pd.date_range(start='2023-01-01', periods=periods, freq=freq)
    print(f"{name:<20} ('{freq}'): {list(date_range)}")

# Creating custom business day frequency
print("\nCustom business day (excluding holidays):")
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

# Create a calendar with US federal holidays
calendar = USFederalHolidayCalendar()

# Get the holidays for 2023
holidays = calendar.holidays(start='2023-01-01', end='2023-12-31')
print(f"2023 US Federal Holidays: {holidays[:3]}...")  # Show first 3

# Create a custom business day excluding these holidays
custom_bd = CustomBusinessDay(calendar=calendar)

# Create a date range that skips holidays and weekends
business_days = pd.date_range(start='2023-01-01', end='2023-01-15', freq=custom_bd)
print(f"Business days (excluding US holidays): {business_days}")

# Part 3: Time Offset and Shifting Operations
# -----------------------------------------------------------------------------
print("\n\nPART 3: TIME OFFSET AND SHIFTING OPERATIONS")
print("=" * 70)

# Create a sample time series
dates = pd.date_range(start='2023-01-01', periods=10, freq='D')
values = np.random.normal(10, 2, 10)  # Random values around 10
ts = pd.Series(values, index=dates)
print("Original time series:")
print(ts)

# Shifting data forwards and backwards in time
print("\nShifting data in time:")
print("Shifted forward 2 days:")
print(ts.shift(periods=2))
print("\nShifted backward 2 days:")
print(ts.shift(periods=-2))

# Using frequency offsets
print("\nUsing time offsets:")
from pandas.tseries.offsets import Day, MonthEnd, QuarterEnd

# Shift index by different offsets
print("Original index + 1 Day:")
print(ts.index + Day(1))
print("\nOriginal index + 1 MonthEnd:")
print(ts.index + MonthEnd(1))  # Shift to the end of the month
print("\nOriginal index + 1 QuarterEnd:")
print(ts.index + QuarterEnd(1))  # Shift to the end of the quarter

# Creating an example of lag features for time series analysis
print("\nCreating lag features for time series analysis:")
df = pd.DataFrame({'value': values}, index=dates)
df['lag_1'] = df['value'].shift(1)  # Value from previous day
df['lag_2'] = df['value'].shift(2)  # Value from 2 days ago
df['lead_1'] = df['value'].shift(-1)  # Value from next day
print(df)

# Visualizing original and shifted time series
plt.figure(figsize=(10, 6))
plt.plot(ts.index, ts.values, 'o-', label='Original')
plt.plot(ts.index, ts.shift(2).values, 's--', label='Lag 2')
plt.plot(ts.index, ts.shift(-2).values, '^--', label='Lead 2')
plt.title('Time Series Shifting Example')
plt.legend()
plt.grid(True)
plt.xlabel('Date')
plt.ylabel('Value')
plt.tight_layout()
plt.savefig('time_shifting_example.png')

print("\nPlot saved as 'time_shifting_example.png'")