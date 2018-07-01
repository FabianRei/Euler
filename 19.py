
thirtyMonths = [4, 6, 9, 11]
february = [2]
otherMonths = [1, 3, 5, 7, 8, 10, 12]

startDay = 1
startMonth = 1
startYear = 1901
startWeekDay = 1  # Tuesday

endDay = 31
endMonth = 12
endYear = 2000

sundayCount = 0
currWeekDay = startWeekDay
for year in range(startYear, endYear+1):
    for month in range(1, 12+1):
        if month in thirtyMonths:
            days = 30
        elif month in february:
            if year % 400 == 0:
                days = 29
            elif year % 100 == 0:
                days = 28
            elif year % 4 == 0:
                days = 29
            else:
                days = 28
        else:
            days = 31
        for day in range(1, days+1):
            if day < startDay and month < startMonth and year <= startYear:
                continue
            elif day > endDay and month > endMonth and year >= endYear:
                break
            else:
                if currWeekDay % 7 == 6 and day == 1:
                    sundayCount += 1
                currWeekDay += 1

print(sundayCount)
