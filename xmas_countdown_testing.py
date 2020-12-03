# import things
import datetime
import time
import threading

def formatCountdown():
    # does python need variables to be declared here? not sure.
    ## TODO This code will ALWAYS count to the 25th 00:00 of the current month. Therefore after December it will count to Jan 25th 00:00 etc.. THIS IS A BUG! I WILL FIX THIS!


    date = datetime.datetime.now()
    #date = datetime.datetime(2019, 12, 5, 13, 40, 55)

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
    if date.month == monthToCountDownTo and date.day > dayToCountDownTo and date.hour > hourToCountDownTo:
        formatted_countdown = "Wait till next year!"

    elif int(months) <= 0 and int(days) <= 0 and int(hours) <= 0 and int(mins) <= 0 and int(secs) <= 0:
        formatted_countdown = "It is Christmas day!"

    else:
        formatted_countdown = "It is " + months + " months, " + days + " days, " + hours + " hours, " + mins + " mins and " + secs + " seconds" + " till Christmas"

    # print("[SUBTASK] " + str(datetime.datetime.now().strftime("%X")) + ": " +
    #      "Formatting date as " + str(formatted_countdown))

    # spit it back out. Again, i could probably just do this whole thing on one line but i forget python syntax.
    return formatted_countdown

def main():
    for i in range(5):
        xyz = input(">>>")

        if xyz == "*countdown" or "*cd":
            thiscountdown = formatCountdown()
            print("[INFO] " + str(datetime.datetime.now().strftime("%x %X")) + ": "
                  + str(thiscountdown))
            #threading.Timer(1, main).start()

def readKey():
    f = open("assets/.gitignore xmas_countdown.txt", "r")
    key = f.read()
    f.close()

    return key

main()
print(readKey())