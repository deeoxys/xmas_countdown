"""
DISCORD BOT WRITTEN BY r333mo ON 01/12/2020
VERY SCUFFED CODE

This bot is a Christmas Countdown.
Prefix is "*"
Replies to users that ask for a countdown
"""


# import things
import discord
import datetime
import time
import threading

# instance of class
client = discord.Client()

@client.event
async def on_ready():
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=formatCountdown(getCountdown())))
    #await updateStatusEvent()

    # global varible very bad yes but idc
    global start_time
    start_time = time.time()

    # nice format with timestamps so we can keep an eye on what is happening and when
    print("[TASK] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
          "logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    # dont talk to ourselves
    if message.author == client.user:
        return

    # probably unnessesarry but means its easy to change prefix
    prefix = "*"

    # command itself
    if message.content.startswith(prefix + "countdown"):
        print("[TASK] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
              "user " + str(message.author) + " requested countdown" + " in server " + str(message.guild) + " (" + str(message.channel) + ")")

        # refer to methods for more info on these
        thiscountdown = getCountdown()
        thiscountdown = formatCountdown()

        print("[TASK] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
              "replied with \"" + str(thiscountdown) + "\"")

        # acutally send the msg
        await message.channel.send(str(thiscountdown))

async def updateStatusEvent():
    # this await and async stuff is so janky i hate it. wont work in a normal method though :(
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=formatCountdown()))

    # r/programminghorror
    # call a method to run in 15 seconds, this method will then call us.
    # this is because async is cringe and doesnt work like normal methods. still trying to understand them.
    threading.Timer(15, updateStatus).start()

def updateStatus():
    # yes i know this is a minor bug. the time that we say we will change to may not be the same as the time we actually update to.
    print("[TASK] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
          "Updating presence (" + str(formatCountdown(getCountdown()) + ")"))
    updateStatusEvent()


def getCountdown():
    # i do not need to explain this
    todaysdate = datetime.datetime.now()
    #print("[SUBTASK] " + str(datetime.datetime.now().strftime("%X")) + ": " + "Calculated date & time now as " + str(todaysdate))

    # future proof christmas date finder. Is it a bug that it will count to 25/12/year event if the date is 26/12/year? not sure.
    xmasdate = datetime.datetime(todaysdate.year, 12, 25)
    #print("[SUBTASK] " + str(datetime.datetime.now().strftime("%X")) + ": " + "Calculated Christmas date & time as " + str(xmasdate))

    # find the difference between the two dates
    ## TODO find out what will happen after 25/month/year? negative? crash? will test this prior to christmas. Might end up like the millenium thing, haha!
    countdown = xmasdate - todaysdate
    #print("[SUBTASK] " + str(datetime.datetime.now().strftime("%X")) + ": " + "Calculated difference between now and Christmas as " + str(countdown))

    return countdown

def formatCountdown():
    # does python need variables to be declared here? not sure.
    formatted_countdown = ""

    # LOGIC. stolen. the other way where i just snipped a string with the date was scuffed and unreliable. thanks open src code.
    # Source can be found at (https://gist.github.com/paulbarber/08f43b34e879cc6d9513), lines 42 - 45.
    ## TODO This code will ALWAYS count to the 25th 00:00 of the current month. Therefore after December it will count to Jan 25th 00:00 etc.. THIS IS A BUG! I WILL FIX THIS!
    days = str(24 - int(datetime.datetime.now().strftime('%d')))
    hours = str(23 - int(datetime.datetime.now().strftime('%H')))
    mins = str(59 - int(datetime.datetime.now().strftime('%M')))
    secs = str(59 - int(datetime.datetime.now().strftime('%S')))

    # if the timer is at zero it is christmas. what happens after that? im not sure.
    # TODO find out what will happen to countdown object after it reaches zero.
    """if secs <= 0:
        formatted_countdown = "It is Christmas day!"
        """

    #else:
        # nice formatting for user

    formatted_countdown = "It is " + days + " days, " + hours + " hours, " + mins + " mins and " + secs + " seconds" + " till Christmas."

    #print("[SUBTASK] " + str(datetime.datetime.now().strftime("%X")) + ": " +
    #      "Formatting date as " + str(formatted_countdown))

    # spit it back out. Again, i could probably just do this whole thing on one line but i forget python syntax.
    return formatted_countdown

def readKey():
    f = open("assets/.gitignore xmas_countdown.txt", "r")
    key = f.read()
    print("[TASK] " + str(datetime.datetime.now().strftime("%x %X")) + ": " +
          "Opened file " + f.name + " got key (" + key + ")")
    f.close()

    return key

# try not to leak this. then other folk can mess with the bot.
client.run(readKey())