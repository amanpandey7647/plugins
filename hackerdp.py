import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from skull.utils import admin_cmd, edit_or_reply, sudo_cmd

COLLECTION_STRINGZ = ["hacker-background"]


async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@skull.on(admin_cmd(pattern="hackerdp ?(.*)", outgoing=True))
@skull.on(sudo_cmd(pattern="hackerdp ?(.*)", allow_sudo=True))
async def main(event):

    await edit_or_reply(
        event, "**Starting Hacker Profile Pic...\n\nDone !!! Check Your DP"
    )  # Owner MarioDevs

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(60)  # Edit this to your required needs