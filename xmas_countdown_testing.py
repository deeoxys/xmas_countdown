# import things
import calendar
import datetime
from time import sleep

global date
# simulate date and time for testing
date = datetime.datetime(2020, 1, 1, 0, 0, 0)

# obsolete code
"""
def formatCountdown():
    #date = datetime.datetime.now()
    #date = datetime.datetime(2023, 1, 27, 0, 59, 59)

    # Here we can set the date and time to count down to. This is nice and modular if i ever wanna reuse this code.
    monthToCountDownTo = 12
    dayToCountDownTo = 24
    hourToCountDownTo = 23
    minToCountDownTo = 59
    secToCountDownTo = 59

    # Logic.
    months = str(monthToCountDownTo - int(date.strftime("%m")))
    days = str(dayToCountDownTo - int(date.strftime("%d")))
    hours = str(hourToCountDownTo - int(date.strftime("%H")))
    mins = str(minToCountDownTo - int(date.strftime("%M")))
    secs = str(secToCountDownTo - int(date.strftime("%S")))

    # TODO fix this jank-fest of code, ideally before Christmas
    if date.month == monthToCountDownTo and date.day > dayToCountDownTo : # and date.hour > hourToCountDownTo:
        formatted_countdown = "Wait till next year!"

    elif int(months) <= 0 and int(days) <= 0 and int(hours) <= 0 and int(mins) <= 0 and int(secs) <= 0:
        formatted_countdown = "It is Christmas day!"

    else:
        formatted_countdown = "It is " + months + " months, " + days + " days, " + hours + " hours, " + mins + " mins and " + secs + " seconds" " till Christmas."
        formatted_countdown = "It is " + months + " months, " + days + " days, " + hours + " hours, " + mins + " mins and " + secs + " seconds" + " till Christmas"

    # print("[SUBTASK] " + str(datetime.datetime.now().strftime("%X")) + ": " +
    #      "Formatting date as " + str(formatted_countdown))

    # spit it back out.
    return formatted_countdown
"""
"""
def CountdownRewrite():
    Countdown = ""
    dayOfYear = 0
    months = 0
    days = 0

    todaysdate = datetime.datetime(2020, 12, 27)
    xmasdate = datetime.datetime(todaysdate.year, 12, 25)

    fulldate = xmasdate - todaysdate
    print(xmasdate)
    print(todaysdate)
    print(fulldate.seconds)
    #Countdown = str(59 - int(datetime.datetime.now().strftime('%S')))

    months = xmasdate.month - todaysdate.month
    days = xmasdate.day - todaysdate.day
    hrs = xmasdate.hour - todaysdate.hour
    mins = xmasdate.minute - todaysdate.minute
    secs = xmasdate.second - todaysdate.second

    print(fulldate)

    return "It is " + str(days) + " days, " + str(hrs) + " hours, " + str(mins) + " mins and " + str(secs) + " seconds" + " till Christmas."

    #return Countdown
"""
def getDays():
    # variables
    dayThatXmasIs = 0
    dayOfYear = 0

    # if leap year
    if calendar.isleap(date.year):
        # these are the amount of days each month have
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # if NOT leap year
    else:
        # these are the amount of days each month have
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # loop through the array and add them up
    for month in months:
        # add the days to variable
        dayThatXmasIs += month

    # take away 6, as 31th Dec - 25th Dec = 6 days. Now we know what day of the year xmas is. Reckon this is a bit over-engineered? Perhaps.
    dayThatXmasIs -= 6

    # add up all the days from the months that have passed
    for i in range(date.month - 1):
        dayOfYear += months[i]
    # then add the current day of the month
    dayOfYear += date.day

    # return
    return dayThatXmasIs - dayOfYear

def getHrsMinsSecs():
    # get hours mins secs to midnight TODAY
    hours = str(23 - int(date.strftime('%H')))
    mins = str(59 - int(date.strftime('%M')))
    secs = str(59 - int(date.strftime('%S')))

    # return
    return hours, mins, secs

# validate
def validateCountdown():
    # if days is negative we missed it.
    if getDays() < 0:
        validate = 0 # Missed christmas

    # if days is 0 it is xmas
    elif getDays() == 0:
        validate = 1 # It is christmas

    # otherwise we are still waiting on xmas
    else:
        validate = 2 # It is not christmas yet

    return validate

# format nicely
def formatCountdown():
    # variables
    formatted_countdown = ""

    # check with function
    outcome = validateCountdown()

    # if only python had switch statements :(
    if outcome == 0:
        formatted_countdown = "Wait till next year!"

    elif outcome == 1:
        formatted_countdown = "Merry Christmas!"

    elif outcome == 2:
        # format
        formatted_countdown = "It is " + str(getDays()-1) + " days, " + str(getHrsMinsSecs()[0]) + " hours, " + str(getHrsMinsSecs()[1]) + " minutes and " + str(getHrsMinsSecs()[2]) + " seconds till Christmas."

    return formatted_countdown

# loop for testing
def loop():
    while True:
        sleep(1)
        print("[INFO] " + str(datetime.datetime.now().strftime("%x %X")) + ": "
              + formatCountdown())

# for testing
def main():
    xyz = input(">>>")

    if xyz == "*countdown" or "*cd":
        thiscountdown = formatCountdown()
        print("[INFO] " + str(datetime.datetime.now().strftime("%x %X")) + ": "
              + str(thiscountdown))
        #threading.Timer(1, main).start()

    if xyz == "go":
        loop()

# rewite this in seconds
def percent():
    # date = datetime.datetime.now()
    date = datetime.datetime(2019, 12, 25)
    months = []
    dayThatXmasIs = 0
    dayOfYear = 0

    # if leap year
    if calendar.isleap(date.year):
        # these are the amount of days each month have
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # if NOT leap year
    else:
        # these are the amount of days each month have
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # loop through the array and add them up
    for month in months:
        # add the days to variable
        dayThatXmasIs += month

    # take away 6, as 31th Dec - 25th Dec = 6 days. Now we know what day of the year xmas is. Reckon this is a bit over-engineered? Perhaps.
    dayThatXmasIs -= 6

    # add up all the days from the months that have passed
    for i in range(date.month - 1):
        dayOfYear += months[i]
    # then add the current day of the month
    dayOfYear += date.day

    percentageToXmas = dayOfYear / dayThatXmasIs

    print("It is " + str(round(percentageToXmas * 100, 2)) + "% of the way to Christmas.")

# yeajh
def readKey():
    f = open("assets/.gitignore xmas_countdown.txt", "r")
    key = f.read()
    f.close()

    return key

#percent()
# print(readKey())
#print(CountdownRewrite())
print(formatCountdown())