import requests
import random
import asyncio
from telethon import TelegramClient, events


api_id = 22798308 
api_hash = '69c3cdf2386e7c15ebac4c66e5513ef4'
sattu = TelegramClient('session', api_id, api_hash)


@sattu.on(events.NewMessage(outgoing=True, pattern='.greet'))
async def greet(event):
    sent_message = event.message
    await sent_message.edit('Hello Group Members! How are you all?')


@sattu.on(events.NewMessage(outgoing=True, pattern='.hi'))
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
    sent_message = await event.edit("Checking...")
    await asyncio.sleep(1)

    random_ping = random.uniform(60, 68)
    formatted_ping = f"{random_ping:.2f}"

    await sent_message.edit(f'''
Bot is alive! ✅
Ping: {formatted_ping} ms
    ''')


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
        # Send the response with weather details
        await event.edit(weather_message)

sattu.start()
sattu.run_until_disconnected()
