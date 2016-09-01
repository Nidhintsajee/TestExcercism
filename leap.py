year=int(input("Enter the year : "))
def is_leap_year(year):
    print year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
is_leap_year(year)
