"""
Seconds in a year

Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement!
You should use constants for this exercise --
there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.
"""

DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

SECONDS_PER_YEAR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_PER_DAY * DAYS_PER_YEAR

def main():
    print("There are", SECONDS_PER_YEAR, "seconds in a year!")

if __name__ == "__main__":
    main()