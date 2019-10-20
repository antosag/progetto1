# ANTONIETTA SAGGESE 119112807
# 18 Oct 2019
# Code with a function to print a calendar given a month and a year, a function that returns how many days
# contained in a given month, and a function that returns which is the first day in a given month


# Su Mo Tu We Th Fr Sa
#  0  1  2  3  4  5  6



def cal (month, year):
    
    # function that prints out a calendar page for a given month and year, taken as input parameters two integer values (month, year)
    
    print (" Su Mo Tu We Th Fr Sa ")
    first_day = start_day(month, year)            # day of the week on which the first of the month falls
    days_in_month = num_days(month, year)         # number of days in a given month
    count_day = 0                                 # variable containing the number of the day to print in the calendar
    
    no_print=0                                    # variable counting the number of days before the day of the week on
                                                  # which the first of the month falls
                                                  
    week= first_day                               # variable containing the corresponding day of week
    while(count_day != days_in_month):
        
        if no_print<first_day:
            print("%3c" %" ", end="")
            no_print = no_print + 1
        else:
            count_day=count_day+1
            week=week+1
            if (week==7):
                print("%3d" %count_day)
                week=0
            else:
                print("%3d" %count_day, end="")


def start_day (month, year):
    
    # function that returns the day of the week on which the first of the month falls
    # the function has as input parameters the two integer values; month, year
    
    week_day=6                                         # day of the week for 1 Jennuary 2000 is Saturday (6)
  #  days_in_month= 0

    
    for i in range (2000, 2100):                       # from 2020 to 2099
        

        for j in range (1, 13):                        # from 1 to 12 months
            if ((i==year)&(j==month)):
                return week_day
            else:
                days_in_month=num_days(j,i)
                for k in range (1, days_in_month+1):   # from 1 to number of days in the month
                    week_day=week_day+1
                    if week_day==7:
                        week_day=0
    return week_day


def num_days (month, year):
    
    # function that returns the number of day in given a month
    # the input integer parameters are: month, year 
    # MONTH                   1   2   3   4   5   6   7   8   9  10  11  12   
    # NUMBER OF DAYS         31  28  31  30  31  30  31  31  30  31  31  31
    # (leap year)                29

    days_in_month=31
    if ((month==4) | (month==6) | (month==9) | (month==11)) :
        days_in_month=30
    elif (month == 2 )& (year%4 ==0):              #leap year
        days_in_month=29
    elif (month == 2 )& (year%4 !=0):
        days_in_month=28
    return days_in_month


def next_day(day,month,year):
    
    # additional functions that returns the next day date
    # not used here for the other functions
   
    num_day=num_days(month, year)
   
    if ((num_day==31) & (day!= 31)) | ((num_day==30) & (day!=30)) | ((num_day==29) & (day!=29)) | ((num_day==28) & (day!=28)):
        next_d=day+1
        next_m=month
        next_y=year
    else:
        next_d=1
        if (month!=12):
            next_m= month+1
            next_y=year
        elif (month==12):
            next_m=1
            next_y=year+1
    return next_d, next_m, next_y
