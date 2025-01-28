import requests
import random
import asyncio
from telethon import TelegramClient, events
from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.types import User


api_id = 22798308 
api_hash = '69c3cdf2386e7c15ebac4c66e5513ef4'
sattu = TelegramClient('session', api_id, api_hash)


@sattu.on(events.NewMessage(outgoing=True, pattern='.greet'))
async def greet(event):
    sent_message = event.message
    wishes = [
        "Aaj ka din badhiya ho, doston! 💪",
        "Let's make today awesome together! 🌟",
        "Keep the good vibes going! 🌸",
        "Aaj kuch zabardast karte hain! 🎉"
    ]
    random_wish = random.choice(wishes)
    await sent_message.edit(f'''
👋 **Hello Group Members!** 👋

How's everyone doing today? 😊

{random_wish}
''')   


@sattu.on(events.NewMessage(outgoing=True, pattern='^\.hi$'))
async def hi(event):
    sent_message = event.message
    await sent_message.edit('''
██╗░░██╗██╗
██║░░██║██║
███████║██║
██╔══██║██║
██║░░██║██║
╚═╝░░╚═╝╚═╝''')


@sattu.on(events.NewMessage(outgoing=True, pattern='.bye'))
async def bye(event):
    sent_message = event.message
    await sent_message.edit('''
█▄▄ █▄█ █▀▀
█▄█ ░█░ ██▄''')


@sattu.on(events.NewMessage(outgoing=True, pattern='.varshu'))
async def varshu(event):
    sent_message = event.message
    await sent_message.edit('''
╭╮╱╱╭╮╱╱╱╱╱╱╭╮
┃╰╮╭╯┃╱╱╱╱╱╱┃┃
╰╮┃┃╭┻━┳━┳━━┫╰━┳━━╮
╱┃╰╯┃╭╮┃╭┫━━┫╭╮┃╭╮┃
╱╰╮╭┫╭╮┃┃┣━━┃┃┃┃╭╮┃
╱╱╰╯╰╯╰┻╯╰━━┻╯╰┻╯╰╯
''')


@sattu.on(events.NewMessage(outgoing=True, pattern='.alive'))
async def alive(event):
    sent_message =await event.edit("Initiating bot check... 🚨")
    await asyncio.sleep(1)

    image_url = "https://www.comingsoon.net/wp-content/uploads/sites/3/2024/04/jujutsu-kaisen-jin-itadori-family-tree.png?resize=624,576"
    roast_comment = "**लगता है इस GC में किसी ने आखिरकार मुझे जगा ही लिया... 🤦‍♂️**"
    await event.edit(f"**Bot is alive! ✅**\n\n{roast_comment}\n\n**Owner:- @sattu879**\n**Developer:-** The wizard who made this magic happen. 🔮", file=image_url)


@sattu.on(events.NewMessage(outgoing=True, pattern=r'\.spam (\d+) (.+)'))
async def spam(event):
    count = int(event.pattern_match.group(1))
    message = event.pattern_match.group(2)   
    for _ in range(count):
        await event.respond(message)
        await asyncio.sleep(0.01) 

        await event.delete() 


@sattu.on(events.NewMessage(outgoing=True, pattern=r'\.craid (\d+)'))
async def craid(event):
    number_of_craids = int(event.pattern_match.group(1))

    replied_user = await event.get_reply_message()
    if replied_user:
        if replied_user.sender.username:
            sender_name = f"@{replied_user.sender.username}"
        else:
            sender_name = f"[{replied_user.sender.first_name}](tg://user?id={replied_user.sender.id})"

        for _ in range(number_of_craids):
            random_letter = random.choice("ABCDEFGHJKLMNOPQRSTUVWXYZ")
            result = f"{sender_name} " + (random_letter * 170)
            await event.respond(result)
    
    await event.delete()


@sattu.on(events.NewMessage(outgoing=True, pattern=r'\.scraid (\d+)'))
async def scraid(event):
    number_of_craids = int(event.pattern_match.group(1))
    for _ in range(number_of_craids):
        random_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        result = random_letter * 170 
        
        await event.respond(result)
        await event.delete()


@sattu.on(events.NewMessage(pattern=r'\.weather (.+)'))
async def weather(event):
    city = event.pattern_match.group(1)
    api_key = "08b2a9ece1deb607c45a0ef084d7e7e4"
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    
    if response["cod"] == 404:
        await event.respond(f"❌ **City '{city}' not found!** Please check the city name and try again.")
    else:
        main = response["main"]
        weather = response["weather"][0]["description"]
        temperature = main["temp"] - 273.15
        humidity = main["humidity"]
        pressure = main["pressure"]
        wind_speed = response["wind"]["speed"]
        icon_code = response["weather"][0]["icon"]

        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

        weather_message = f"""
**🌍 Weather in {city}:**

🌀 **Condition**: {weather.capitalize()}
🌡️ **Temperature**: {temperature:.2f}°C
💨 **Wind Speed**: {wind_speed} m/s
💧 **Humidity**: {humidity}%
🌬️ **Pressure**: {pressure} hPa

🔍 **More Info**:
- 🌤️ **Weather Icon**: ![Icon]({icon_url})

Stay safe and have a great day! ☀️
"""
        await event.edit(weather_message)
         
        
@sattu.on(events.NewMessage(pattern=r'\.nikal @(\w+)'))
async def kick_user(event):
    username = event.pattern_match.group(1)
    
    try:
        user = await sattu.get_entity(username) 
        await event.reply(f"🚫 **Kicking user {username}...**")
        await event.client.kick_participant(event.chat_id, user.id)
        await event.reply(f"✅ **{username} को ग्रुप से ऐसे बाहर किया, जैसे आइसक्रीम गिरा दी हो! 🍦💨**")
    
    except ValueError:
        await event.reply(f"❌ **User {username} not found!**")
    
    except Exception as e:
        await event.reply(f"❌ **An error occurred while kicking the user:** {str(e)}")
        
        
@sattu.on(events.NewMessage(pattern=r'\.sspam (\d+)\s*$'))
async def spam_stickers(event):
    count = int(event.pattern_match.group(1))
    replied_message = await event.get_reply_message() 
    if replied_message and replied_message.sticker: 
        sticker = replied_message.sticker 
        for _ in range(count):
            await event.respond(file=sticker) 
            await asyncio.sleep(0.5) 
        await event.delete() 
    else:
        await event.reply("❌ Please reply to a sticker to spam it.")
        
        
@sattu.on(events.NewMessage(pattern=r'\.mspam (\d+)\s*$'))
async def spam_messages(event):
    count = int(event.pattern_match.group(1))
    replied_message = await event.get_reply_message() 
    if replied_message and replied_message.text: 
        message = replied_message.text
        for _ in range(count):
            await event.respond(message) 
            await asyncio.sleep(0.3) 
        await event.delete() 
    else:
        await event.reply("❌ Please reply to a text message to spam it.")
        
        
@sattu.on(events.NewMessage(pattern=r"\.hehe"))
async def hehe(event):
    emojis = [
        "😀", "😃", "😄", "😁", "😎", "😅", "🤣", "😂", 
        "😛", "😜", "🤪", "😝", "🤫", "🫡", "😶", "😆"
    ]  
    for emoji in emojis:
        await event.edit(emoji)
        await asyncio.sleep(2) 
        
        
@sattu.on(events.NewMessage(outgoing=True, pattern='\.ping'))
async def ping(event):
    emojis = [
        "⚡", "💥", "🌟", "🔥",
    ]
    for emoji in emojis:
        await event.edit(f"{emoji}") 
        await asyncio.sleep(1.2) 
        
    random_ping = random.uniform(60, 68)
    formatted_ping = f"{random_ping:.2f}"
    await event.edit(f'🏓 **Pong!** (Ping: {formatted_ping}ms)')


@sattu.on(events.NewMessage(pattern=r"\.hack"))
async def greeting(event):
    await event.edit("🔓 Trying to get the weakness...")
    await asyncio.sleep(1.5)
    
    await event.edit("🔍 Searching for vulnerabilities...")
    await asyncio.sleep(2)
    
    await event.edit("[Processing.                     ] 5%")
    await asyncio.sleep(0.5)
    await event.edit("[Processing...                   ] 10%")
    await asyncio.sleep(0.5)
    await event.edit("[Processing.....                 ] 25%")
    await asyncio.sleep(1)
    await event.edit("[Processing........              ] 40%")
    await asyncio.sleep(0.5)
    await event.edit("[Processing.........             ] 50%")
    await asyncio.sleep(0.5)
    await event.edit("[Processing...........           ] 60%")
    await asyncio.sleep(1)
    await event.edit("[Processing.............         ] 75%")
    await asyncio.sleep(0.5)
    await event.edit("[Processing..................    ] 85%")
    await asyncio.sleep(1)
    await event.edit("[Processing..................... ] 95%")
    await asyncio.sleep(0.5)
    await event.edit("[Processing......................] 100%")
    
    await asyncio.sleep(1)
    await event.edit("Access granted. Connection established.")
    await asyncio.sleep(1)
    await event.edit("System breach confirmed. Vulnerable.")
    await asyncio.sleep(1.5)
    await event.edit("WARNING: Intrusion detected now.")
    await asyncio.sleep(1)
    await event.edit("Your data compromised completely.")
    await asyncio.sleep(1.5)
    await event.edit("Accessing private information now.")
    await asyncio.sleep(1.5)
    await event.edit("System corruption in progress.")
    await asyncio.sleep(2)
    await event.edit("Prepare for consequences ahead.")
    await asyncio.sleep(2)
    await event.edit("System override complete. Done.🔴")


sattu.start()
sattu.run_until_disconnected()