class Solution(object):
    def daysBetweenDates(self, date1, date2):
        def isLeap(year):
            return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

        def daysFrom1971(date):
            y, m, d = map(int, date.split('-'))

            days = 0

            # Add days of complete years
            for year in range(1971, y):
                days += 366 if isLeap(year) else 365

            # Add days of complete months
            month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

            for month in range(1, m):
                days += month_days[month - 1]
                if month == 2 and isLeap(y):
                    days += 1

            # Add days of current month
            days += d

            return days

        return abs(daysFrom1971(date1) - daysFrom1971(date2))