#!/usr/bin/env python3
# Copyright (C) 2020 Joshua Peisach <itzswirlz2020@outlook.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA.

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

# Time, for logging and such
time = datetime.datetime.now()
current_time = time.strftime("%H:%M:%S")


@client.event
async def on_connect():
    print('[' + current_time + '] Bot online with a username of [username] and operating in [server number] servers.')


async def log_message(msg):
    # Reinitialize these variables or the time will be the same as the start time
    logtime = datetime.datetime.now()
    current_logtime = logtime.strftime("%H:%M:%S")

    print("[" + current_logtime + "] #" + msg.channel.name + " " + msg.author.name + ":          " + msg.content)

    channel = client.get_channel(734439066681999449)

    await channel.send(
        "[" + current_logtime + "] #" + msg.channel.name + " " + msg.author.name + ":          " + msg.content)

    logging.basicConfig(filename='./logs.txt', level=logging.INFO)
    logging.info("[" + current_logtime + "] #" + msg.channel.name + " " + msg.author.name + ":          " + msg.content)


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


print('[' + current_time + '] Beginning startup of Discord Bot.')
print('[' + current_time + '] Starting Discord Client Connection.')

client.run(token)
