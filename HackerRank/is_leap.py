def is_leap(year):
    leap = False

    # A year is a leap year if:
    # it's evenly divisible by 4 unless:
    # the year can be evenly divided by 100, it is NOT a leap year, unless:
    # the year is also evenly divisible by 400. Then it is a leap year.
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 400 == 0:
        leap = True
    else:
        leap = False

    return leap

    year = int(input())
    print(is_leap(year))
