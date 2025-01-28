import os
from asyncio import sleep
from multiprocessing import Event
from telethon.client import chats
from telethon.sync import TelegramClient, events
#from config import api_hash, api_id
import time
from telethon.tl.types import Chat, Photo # type: ignore
import asyncio
from telethon import events
import os
import asyncio
from telethon import TelegramClient, events , functions
import contextlib
from telethon.tl import types


import random
from io import BytesIO
import textwrap
import requests
import json



def load_config(config_file='config.json'):
     with open(config_file, 'r')as f:
          config = json.load(f)
          return config
     
config = load_config()     

api_id = config.get('api_id')
api_hash = config.get('api_hash')

kio = TelegramClient('session' , api_id , api_hash)

@kio.on(events.NewMessage(pattern=r"\.hi"))
async def greeting(event):
        await event.edit("""
        ⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣿⡿⠗⠀⠠⠄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⡜⠁⠀⠀⠀⠀⠀⠈⠑⢶⣶⡄
⢀⣶⣦⣸⠀⢼⣟⡇⠀⠀⢀⣀⠀⠘⡿⠃
⠀⢿⣿⣿⣄⠒⠀⠠⢶⡂⢫⣿⢇⢀⠃⠀
⠀⠈⠻⣿⣿⣿⣶⣤⣀⣀⣀⣂⡠⠊⠀⠀
⠀⠀⠀⠃⠀⠀⠉⠙⠛⠿⣿⣿⣧⠀⠀⠀
⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀
⠀⠀⠀⣷⣄⡀⠀⠀⠀⢀⣴⡟⠿⠃⠀⠀
⠀⠀⠀⢻⣿⣿⠉⠉⢹⣿⣿⠁⠀⠀⠀⠀ HELLO GUYSIS
⠀⠀⠀⠀⠉⠁⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
        """)


@kio.on(events.NewMessage(pattern=r"\.hello"))
async def greeting(event):
        await event.edit("""
╔┓┏╦━━╦┓╔┓╔━━╗
║┗┛║┗━╣┃║┃║╯╰║     
║┏┓║┏━╣┗╣┗╣╰╯║      
╚┛┗╩━━╩━╩━╩━━╝⠀⠀⠀
        """)
        
@kio.on(events.NewMessage(pattern=r"\.fuck"))
async def greeting(event):
        await event.edit("F*ck You Baby 🖕")
        time.sleep(2)  
        await event.edit("Baby, Ohh.. Yes 👅")
        time.sleep(2)  
        await event.edit("""
 ⢀⣴⡿⠿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡿⣀⠠⠇⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢷⠀⢀⣀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⣇⠉⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⢾⡄⠀⠀⠀⢻⠞⠓⢺⠉⠓⣦⡀⠀⠀⠀
⠀⣠⡾⢂⣱⠐⠛⠭⠀⢃⠀⠀⠡⡀⠈⠳⣄⠀⠀
⣴⠫⠛⠀⠈⢇⠀⠀⠀⠀⠆⠀⠀⢡⠀⠀⠘⣆⠀
⣇⢇⠀⠀⠀⠀⢆⠀⠀⠀⠈⡄⠀⠀⢧⠀⠀⢸⡆
⢻⠸⡀⠀⠀⠀⢸⡆⠀⠀⠀⠐⠀⠀⠀⠀⢀⡞⠀
⢸⠀⢳⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⣣⠾⠀⠀
⠈⠳⣄⢆⠀⠀⠀⠀⠆⠀⠀⠀⣠⡦⠞⠃⠀F*CK YOU
⠀⠀⠈⠛⠷⠤⠤⠖⠚⠒⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀
        """)

@kio.on(events.NewMessage(pattern=r"\.gn"))
async def greeting(event):
        await event.edit("""
∩――――∩     ˗ˏˋ ★ ˎˊ˗
|    ∧  ﾍ        |
|    (* ´ ▽`)     |  < ᴳᵒᵒᵈᴺⁱᵍʰᵗ   ♡
|ﾉ^⌒⌒づ￣  ＼
(　ノ　　⌒ ヽ ＼
＼　　|￣￣￣￣￣|
　 ＼,ﾉ| ⠀⠀⠀⠀⠀⠀⠀
        """)

@kio.on(events.NewMessage(pattern=r"\.bear"))
async def greeting(event):
        await event.edit(""" KESA HE SAFED BHAKU """)
        time.sleep(2)
        await event.edit("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣦⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⠟⠋⠉⠀⠀⠀⠀⠉⠑⠢⣄⡀⠀⠀⠀⠀⠀                
⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣦⡀                
⠀⣀⠀⠀⢀⡏⠀⢀⣴⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠇
⣾⣿⣿⣦⣼⡀⠀⢺⣿⣿⡿⠃⠀⠀⠀⠀⣠⣤⣄⠀⠀⠈⡿⠋⠀
⢿⣿⣿⣿⣿⣇⠀⠤⠌⠁⠀⡀⢲⡶⠄⢸⣏⣿⣿⠀⠀⠀⡇⠀⠀
⠈⢿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠈⠉⠓⠂⠀⠙⠛⠛⠠⠀⡸⠁⠀⠀
⠀⠀⠻⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⠀⠀⠀⠀⠑⠀⣠⠞⠁⠀⠀⠀
⠀⠀⠀⢸⡏⠉⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⢿⣿⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⢷  @ice_bear526⠈⢻⣿⣿⣿⣿⡀⠀⠀⠀
⠀⠀⠀⢸⣆⠀⠀⠀⠀⠀      ⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⢸⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠻⠿⠟⡀⠀⠀⠀
⠀⠀ ⠀⣿⣿⣿⣿⣶⠶⠤⠤⢤⣶⣾⣿⣿⡇⠀
⠀⠀⠀⠀⠹⣿⣿⣿⠏⠀⠀⠀⠈⢿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠉⠉⠀
        """)

@kio.on(events.NewMessage(pattern=r"\.gm"))
async def greeting(event):
        await event.edit("""
Good morning!
     へ   +        —̳͟͞͞💗
૮  -   ̫ ՛ )つ  —̳͟͞͞ 💗         —̳͟͞͞💗 +
(つ    <                —̳͟͞͞💗
｜  _   つ      +  —̳͟͞͞💗         —̳͟͞͞💗 ˚
`し´⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)

@kio.on(events.NewMessage(pattern=r"\.sleep"))
async def greeting(event):
        await event.edit("😴🥱😴🥱")
        time.sleep(2)
        await event.edit("🥱😴🥱😴")
        time.sleep(2)
        await event.edit("😴🥱😴🥱")
        time.sleep(2)
        await event.edit("🥱😴🥱😴")
        time.sleep(2)
        await event.edit("😴🥱😴🥱")
        time.sleep(2)
        await event.edit("🥱😴🥱😴")
        time.sleep(2)
        await event.edit("""
∩――――∩     ˗ˏˋ ★ ˎˊ˗
|    ∧  ﾍ        |
|    (* ´ ▽`)     |  < ᴳᵒᵒᵈᴺⁱᵍʰᵗ   ♡
|ﾉ^⌒⌒づ￣  ＼
(　ノ　　⌒ ヽ ＼
＼　　|￣￣￣￣￣|
　 ＼,ﾉ| ⠀⠀⠀⠀⠀⠀⠀
      """)

@kio.on(events.NewMessage(pattern=r"\.hehe"))
async def greeting(event):
        await event.edit("😀")
        time.sleep(2)
        await event.edit("😃")
        time.sleep(2)
        await event.edit("😄")
        time.sleep(2)
        await event.edit("😁")
        time.sleep(2)
        await event.edit("😎")
        time.sleep(2)
        await event.edit("😅")
        time.sleep(2)
        await event.edit("🤣")
        time.sleep(2)
        await event.edit("😂")
        time.sleep(2)
        await event.edit("😛")
        time.sleep(2)
        await event.edit("😜")
        time.sleep(2)
        await event.edit("🤪")
        time.sleep(2)
        await event.edit("😝")
        time.sleep(2)
        await event.edit("🤫")
        time.sleep(2)
        await event.edit("🫡")
        time.sleep(2)
        await event.edit("😶")
        time.sleep(2)
        await event.edit("😆")
       
@kio.on(events.NewMessage(pattern=r"\.hack"))
async def greeting(event):
        await event.edit("trying to get the weakness...")
        time.sleep(2)
        await event.edit("Found Some INFORMATION...")
        time.sleep(2)
        await event.edit("[Processing...                     ] 5%")
        time.sleep(1)
        await event.edit("[Processing.....                   ] 10%")
        time.sleep(1)
        await event.edit("[Processing.......                 ] 15%")
        time.sleep(1)
        await event.edit("[Processing.........               ] 20%")
        time.sleep(1)
        await event.edit("[Processing..........              ] 35%")
        time.sleep(1)
        await event.edit("[Processing...........             ] 45%")
        time.sleep(1)
        await event.edit("[Processing.............           ] 50%")
        time.sleep(1)
        await event.edit("[Processing...............         ] 60%")
        time.sleep(1)
        await event.edit("[Processing.................       ] 70%")
        time.sleep(1)
        await event.edit("[Processing....................    ] 80%")
        time.sleep(1)
        await event.edit("[Processing....................... ] 90%")
        time.sleep(1)
        await event.edit("[Processing........................] 100%")
        time.sleep(1)
        await event.edit("gained access...")
        time.sleep(1)
        await event.edit("You are HAcked Buddy...")
        time.sleep(1)
      
@kio.on(events.NewMessage(pattern=r"\.alive"))
async def greeting(event):
        photo_path = r"C:\Users\LENOVO\Desktop\KIO\USERBOT\Kio_xd_ketty_5260.jpg" #photo.jpg path of you pc/device
        await event.edit(
            file=photo_path,
            text="""
Yes Boss, I Am Alive.
How Can I Help You?

Owner    = 
Developer = 
            """
        )
        await asyncio.sleep(10)
        await kio.delete_messages(event.chat_id, [event.id])

@kio.on(events.NewMessage(pattern=r"\.sad"))
async def greeting(event):
        await event.edit("🙂")
        time.sleep(2)
        await event.edit("🙃")
        time.sleep(2)
        await event.edit("🥲")
        time.sleep(2)
        await event.edit("😐")
        time.sleep(2)
        await event.edit("😕")
        time.sleep(2)
        await event.edit("🙁")
        time.sleep(2)
        await event.edit("☹️")
        time.sleep(2)
        await event.edit("😰")
        time.sleep(2)
        await event.edit("😥")
        time.sleep(2)
        await event.edit("😢")
        time.sleep(2)
        await event.edit("😭")
        time.sleep(2)
        await event.edit("😣")
        time.sleep(2)
        await event.edit("😞")
        time.sleep(2)
        await event.edit("😩")
        
@kio.on(events.NewMessage(pattern=r"\.heart"))
async def greeting(event):
        await event.edit("💌")
        time.sleep(2)
        await event.edit("💘")
        time.sleep(2)
        await event.edit("💝")
        time.sleep(2)
        await event.edit("💖")
        time.sleep(2)
        await event.edit("💗")
        time.sleep(2)
        await event.edit("💓")
        time.sleep(2)
        await event.edit("💞")
        time.sleep(2)
        await event.edit("💕")
        time.sleep(2)
        await event.edit("💟")
        time.sleep(2)
        await event.edit("❣️")
        time.sleep(2)
        await event.edit("❤️‍🔥")
        time.sleep(2)
        await event.edit("❤️‍🩹")
        time.sleep(2)
        await event.edit("❤️")
        time.sleep(2)
        await event.edit("🩷")
        time.sleep(2)
        await event.edit("🧡")
        time.sleep(2)
        await event.edit("💛")
        time.sleep(2)
        await event.edit("💚")
        time.sleep(2)
        await event.edit("💙")
        time.sleep(2)
        await event.edit("🩵")
        time.sleep(2)
        await event.edit("💜")
        time.sleep(2)
        await event.edit("🤎")
        time.sleep(2)
        await event.edit("🖤")
        time.sleep(2)
        await event.edit("🩶")
        time.sleep(2)
        await event.edit("🤍")
        time.sleep(2)
        await event.edit("You Are So Cute 🙈")



####################################################################################################################################################################################

# Replace with your own Telegram user ID
BOT_OWNER_ID =           # Your Telegram user ID

# Global dictionary to track ongoing spam sessions
spam_sessions = {}

@kio.on(events.NewMessage(pattern=r"\.spam (\d+)(.*)?"))
async def spam(event):
    """
    Function to send a message, sticker, or replied object multiple times to the chat.
    Only the bot owner can use this command.
    :param event: The event object containing message details.
    """
    # Debug: Log the sender ID
    print(f"Sender ID: {event.sender_id}")

    # Check if the sender is the bot owner
    if event.sender_id != BOT_OWNER_ID:
        await event.reply("You are not authorized to use this command.")
        return

    match = event.pattern_match
    count = int(match.group(1))  # First group is count
    text = match.group(2).strip() if match.group(2) else None  # Second group is text, optional

    # Get the chat and replied message
    chat = await event.get_chat()
    reply_message = await event.get_reply_message()

    # Generate a unique session ID for this spam operation (based on chat ID and user ID)
    session_id = f"{chat.id}_{event.sender_id}"

    # Check if there's an active spam session
    if session_id in spam_sessions and spam_sessions[session_id]['active']:
        await event.reply("You are already spamming! Please stop the current spam first using `.stop`.")
        return

    # Validate input and reply_message
    if not text and not reply_message:
        await event.reply("Please specify text to spam or reply to a message/sticker.")
        return

    # Create a new session in the spam_sessions dictionary
    spam_sessions[session_id] = {
        'active': True,
        'count': count,
        'chat': chat,
        'current_count': 0  # Track how many messages have been sent
    }

    # Start sending the spam messages
    for _ in range(count):
        if not spam_sessions[session_id]['active']:  # Check if spam was stopped
            await event.reply("Spam has been stopped.")
            break

        # Spam the appropriate object
        if text:
            await kio.send_message(chat, text)  # Send the specified text
        elif reply_message:
            if reply_message.sticker:  # Spam the sticker
                await kio.send_file(chat, reply_message.media)
            else:  # Spam the replied message
                await kio.send_message(chat, reply_message.message)

        spam_sessions[session_id]['current_count'] += 1
        await asyncio.sleep(0.1)  # Optional delay between messages

    # After spamming is complete, mark the session as inactive
    spam_sessions[session_id]['active'] = False
    await event.reply(f"Successfully spammed {spam_sessions[session_id]['current_count']} times!")

@kio.on(events.NewMessage(pattern=r"\.stop"))
async def stop_spam(event):
    """
    Stop the ongoing spam session.
    Only the bot owner can use this command.
    :param event: The event object containing message details.
    """
    # Debug: Log the sender ID
    print(f"Sender ID: {event.sender_id}")

    # Check if the sender is the bot owner
    if event.sender_id != BOT_OWNER_ID:
        await event.reply("You are not authorized to use this command.")
        return

    # Generate the session ID for the user in the chat
    session_id = f"{event.chat_id}_{event.sender_id}"

    # Check if there's an active spam session to stop
    if session_id not in spam_sessions or not spam_sessions[session_id]['active']:
        await event.reply("No active spam session found to stop.")
        return

    # Mark the session as inactive to stop it
    spam_sessions[session_id]['active'] = False
    await event.reply("Spam session has been successfully stopped.")

#####################################################################################################################################
OWNER_ID =    # Replace with your own Telegram user ID

@kio.on(events.NewMessage(pattern=r"\.photo(?:\s|$)([\s\S]*)"))
async def potocmd(event):
    # Check if the user is the bot owner
    if event.sender_id != OWNER_ID:
        return await event.reply("`𝐨𝐧𝐥𝐲 𝐊𝐢𝐨 🦅 ✇【✘𝗗™】𝐂𝐀𝐋𝐋 ➣ 𝐒𝐢𝐆𝐍 『 KΣƬƬY 』 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐜𝐨𝐦𝐦𝐚𝐧𝐝`")

    "To get user or group profile pic"
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user and user.sender:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if not uid.strip():
        uid = 1
        if uid > len(photos):
            return await event.edit("`No photo found of this NIBBA / NIBBI. Now u Die!`")
        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    elif uid.strip() == "all":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await event.edit("`This user has no photos to show you`")
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await event.edit("```number Invalid!``` **Are you Comedy Me ?**")
                return
        except ValueError:
            await event.edit("`Are you comedy me ?`")
            return
        if uid > len(photos):
            return await event.edit("`No photo found of this NIBBA / NIBBI. Now u Die!`")

        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    await event.delete()

kio.start()
kio.run_until_disconnected()