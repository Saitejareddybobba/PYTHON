# return a leap year using function
# divide by 400
# divide by 100
# divide by 4

year = int(input("Enter year::"))

def is_leapyear(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

print(is_leapyear(year))
