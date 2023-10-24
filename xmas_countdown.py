"""
DISCORD BOT WRITTEN ON 01/12/2020
VERY SCUFFED CODE

This bot is a Christmas Countdown.
Prefix is "*".
Replies to users that ask for a countdown.

Stuff i need to do:
TODO 1. Add presence with countdown, but avoid being rate-limited.
TODO 2. Send a message when we join a server.
"""

# import things
import calendar

import discord
from discord import *
import datetime
import time
#import threading

# instance
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
              "replied with \"" + formatPercentage() + "\"")

        # acutally send the msg
        await message.channel.send(formatPercentage())


# lots of unused code here. for future.
"""
@client.event
async def on_guild_join(server):
    for textchannel in server.channels:
        if "general" in textchannel.name:
            await message.channel.send("Hello I am Christas Countdown bot.\nYou can use *countdown or *cd to see how long it is till Christmas.")
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
def getDays():
    # variables
    dayThatXmasIs = 0
    dayOfYear = 0

    # if leap year
    if calendar.isleap(datetime.datetime.now().year):
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
    for i in range(datetime.datetime.now().month - 1):
        dayOfYear += months[i]
    # then add the current day of the month
    dayOfYear += datetime.datetime.now().day

    # return
    return dayThatXmasIs - dayOfYear

def getHrsMinsSecs():
    # get hours mins secs to midnight TODAY
    hours = str(23 - int(datetime.datetime.now().strftime('%H')))
    mins = str(59 - int(datetime.datetime.now().strftime('%M')))
    secs = str(59 - int(datetime.datetime.now().strftime('%S')))

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

def calculatePercentage():
    # date = datetime.datetime.now()
    #date = datetime.datetime(2019, 12, 24, 23, 0, 0)
    dayOfYear = 0

    # if leap year
    if calendar.isleap(datetime.datetime.now().year):
        # these are the amount of days each month have
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        secThatXmasIs = 31104000

    # if NOT leap year
    else:
        # these are the amount of days each month have
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        secThatXmasIs = 31017600

    # add up all the days from the months that have passed
    for i in range(datetime.datetime.now().month - 1):
        dayOfYear += months[i]
    # then add the current day of the month
    dayOfYear += datetime.datetime.now().day

    secOfYear = (dayOfYear * 24 * 60 * 60) + (datetime.datetime.now().hour * 60 * 60) + (datetime.datetime.now().minute * 60) + datetime.datetime.now().second

    percentageToXmas = secOfYear / secThatXmasIs

    return percentageToXmas

def validatePercentage():
    outcome = calculatePercentage()

    if outcome > 100.00:
        validate = True

    elif outcome <= 100.00:
        validate = False

    # boolean to say if we missed chistmas or not
    return validate

def formatPercentage():
    formattedPercentage = ""
    outcome = validatePercentage()

    if outcome:
       formattedPercentage = "Wait till next year!"

    else:
        formattedPercentage = "It is " + str(round(calculatePercentage() * 100, 5)) + "% of the way to Christmas."

    return formattedPercentage


# so folk cant scoop the bot.
def readKey():
    f = open("key.txt", "r")
    key = f.read()
    print("[INFO] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
          "Opened file " + f.name + " got key (" + key + ").")
    f.close()

    return key

# start bot up.
client.run(readKey())