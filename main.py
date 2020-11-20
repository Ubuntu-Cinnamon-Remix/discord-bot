import discord
import logging
import datetime
from discord.utils import get

# Bot
client = discord.Client()
prefix = "uc!"
token = open('./token.txt').read()

# Our Ubuntu Cinnamon Orange Embed Colour
ubuntucinnamon = (221, 104, 42)


@client.event
async def on_connect():
    print('[TIME] Bot online with a username of [username] and operating in [server number] servers.')


async def log_message(msg):
    time = datetime.datetime.now()
    current_time = time.strftime("%H:%M:%S")

    print("[" + current_time + "] #" + msg.channel.name + " " + msg.author.name + ":          " + msg.content)

    channel = client.get_channel(734439066681999449)

    await channel.send(
        "[" + current_time + "] #" + msg.channel.name + " " + msg.author.name + ":          " + msg.content)

    logging.basicConfig(filename='./logs.txt', level=logging.INFO)
    logging.info("[" + current_time + "] #" + msg.channel.name + " " + msg.author.name + ":          " + msg.content)


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    await log_message(msg)

    if not msg.content.startswith(prefix):
        return

    msg.content.lower()

    pingid = "<@!" + str(msg.author.id) + ">"

    if msg.content == "uc!ping":
        await msg.channel.send("Work in progress-please be patient for better results")
        await msg.channel.send(pingid + ", :ping_pong: Pong! {0} ms".format(round(client.latency, 1)))

    if msg.content == "uc!notifications":
        notificationsrole = get(msg.author.guild.roles, name="Notifications")
        await msg.author.add_roles(notificationsrole)
        await msg.channel.send(":white_check_mark: " + "<@!" + pingid + ">, Sucessfully added Notifications role!")


print('[TIME] Beginning startup of Discord Bot.')

print('[TIME] Starting Discord Client Connection.')

client.run(token)
