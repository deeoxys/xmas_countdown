"""
DISCORD BOT WRITTEN BY r333mo ON 01/12/2020
VERY SCUFFED CODE

This bot is a Christmas Countdown.
Prefix is "*".
Replies to users that ask for a countdown.

Stuff i need to do:
TODO 1. Add presence with countdown, but avoid being rate-limited.
TODO 2. Send a message when we join a server.
TODO 3. Fix janky code (lines 106 - 114).
"""

# import things
import calendar

import discord
from discord import *
import datetime
import time
#import threading

# instance of class
client = discord.Client()

@client.event
async def on_ready():
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=formatCountdown(getCountdown())))
    # await updateStatusEvent()

    # global varible very bad yes but idc
    global start_time
    start_time = time.time()

    # nice format with timestamps so we can keep an eye on what is happening and when
    print("[INFO] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
          "logged in as {0.user}".format(client) + ".")

@client.event
async def on_message(message):
    # dont talk to ourselves
    if message.author == client.user:
        return

    # probably unnessesarry but means its easy to change prefix
    prefix = "*"

    # command itself
    if message.content == (prefix + "countdown") or message.content == (prefix + "cd"):
        print("[INFO] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
              "user " + str(message.author) + " requested countdown" + " in server " + str(message.guild) + " (" + str(message.channel) + ").")

        # refer to methods for more info on these
        thiscountdown = formatCountdown()

        print("[INFO] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
              "replied with \"" + str(thiscountdown) + "\"")

        # acutally send the msg
        await message.channel.send(str(thiscountdown))

    elif message.content == (prefix + "percentage") or message.content == (prefix + "pc"):
        print("[INFO] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
              "user " + str(message.author) + " requested percentage" + " in server " + str(message.guild) + " (" + str(message.channel) + ").")

        print("[INFO] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
              "replied with \"" + percent() + "\"")

        # acutally send the msg
        await message.channel.send(percent())



# lots of unused code here. for future.
"""
@client.event
async def on_guild_join(server):
    for textchannel in server.channels:
        if "general" in textchannel.name:
            await message.channel.send("Hello I am r333mo's Christas Countdown bot.\nYou can use *countdown or *cd to see how long it is till Christmas.")
"""
"""
async def updateStatusEvent():
    # this await and async stuff is so janky i hate it. wont work in a normal method though :(
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=formatCountdown()))

    # r/programminghorror
    # call a method to run in 15 seconds, this method will then call us.
    # this is because async is cringe and doesnt work like normal methods. still trying to understand them.
    threading.Timer(15, updateStatus).start()
"""
"""
def updateStatus():
    # yes i know this is a minor bug. the time that we say we will change to may not be the same as the time we actually update to.
    print("[TASK] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
          "Updating presence (" + str(formatCountdown() + ")"))
    updateStatusEvent()
"""
def formatCountdown():
    # does python need variables to be declared here? not sure.
    formatted_countdown = ""

    # find what datetime it is right now.
    date = datetime.datetime.now()

    # Here we can set the date and time to count down to. This is nice and modular if i ever wanna reuse this code.
    monthToCountDownTo = 12
    dayToCountDownTo = 24
    hourToCountDownTo = 23
    minToCountDownTo = 59
    secToCountDownTo = 59
    millisecToCountDownTO = 1000

    # Logic. Compare the date we are counting to, to datetime that we got on line 91.
    months = str(monthToCountDownTo - int(date.strftime("%m")))
    days = str(dayToCountDownTo - int(date.strftime("%d")))
    hours = str(hourToCountDownTo - int(date.strftime("%H")))
    mins = str(minToCountDownTo - int(date.strftime("%M")))
    secs = str(secToCountDownTo - int(date.strftime("%S")))
    # millisecs = str(secToCountDownTo - int(date.strftime("%f")))

    # fix this jank-fest of code, ideally before Christmas
    if date.month == monthToCountDownTo and date.day > dayToCountDownTo and date.hour > hourToCountDownTo:
        formatted_countdown = "Wait till next year!"

    elif int(months) <= 0 and int(days) <= 0 and int(hours) <= 0 and int(mins) <= 0 and int(secs) <= 0:
        formatted_countdown = "It is Christmas day!"

    else:
        formatted_countdown = "It is " + months + " months, " + days + " days, " + hours + " hours, " + mins + " mins and " + secs + " seconds" " till Christmas."
    #    formatted_countdown = "It is " + months + " months, " + days + " days, " + hours + " hours, " + mins + " mins, " + secs + " seconds and " + millisecs[:-3] + " milliseconds" + " till Christmas"
    # print("[SUBTASK] " + str(datetime.datetime.now().strftime("%X")) + ": " +
    #      "Formatting date as " + str(formatted_countdown))

    # spit it back out.
    return formatted_countdown

def percent():
    #date = datetime.datetime.now()
    date = datetime.datetime(2019, 12, 5, 13, 40, 55)
    months = []
    dayThatXmasIs = 0
    dayOfYear = 0

    # Here we can set the date and time to count down to. This is nice and modular if i ever wanna reuse this code.
    dayToCountDownTo = 259

    # if leap year
    if calendar.isleap(date.year):
        # these are the amount of days each month have
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # loop through the array and add them up
        for month in months:
            # add the days to variable
            dayThatXmasIs += month

        # take away 6, as 31 - 25 = 6. Now we know what day of the year xmas is. Reckon this is a bit over-engineered? Perhaps.
        dayThatXmasIs - 6

    # if NOT leap year
    elif not calendar.isleap(date.year):
        # these are the amount of days each month have
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # loop through the array and add them up
        for month in months:
            # add the days to variable
            dayThatXmasIs += month

        # take away 6, as 31 - 25 = 6. Now we know what day of the year xmas is. Reckon this is a bit over-engineered? Perhaps.
        dayThatXmasIs - 6

    # add up all the days from the months that have passed
    for i in range(date.month - 1):
        dayOfYear += months[i]
    # then add the current day of the month
    dayOfYear + date.day

    percentageToXmas = dayOfYear / dayThatXmasIs

    return "It is " + str(round(percentageToXmas * 100, 2)) + "% of the way to Christmas."

# so folk cant scoop the bot.
def readKey():
    f = open("assets/.gitignore xmas_countdown.txt", "r")
    key = f.read()
    print("[INFO] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
          "Opened file " + f.name + " got key (" + key + ").")
    f.close()

    return key

# start bot up.
client.run(readKey())