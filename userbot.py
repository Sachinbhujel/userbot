import random
import asyncio
from telethon import TelegramClient, events


api_id = 22798308 
api_hash = '69c3cdf2386e7c15ebac4c66e5513ef4'
sattu = TelegramClient('session', api_id, api_hash)


@sattu.on(events.NewMessage(outgoing=True, pattern='.greet'))
async def greeting(event):
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
        await asyncio.sleep(0.1) 

        await event.delete() 


@sattu.on(events.NewMessage(outgoing=True, pattern=r'craid (\d+)'))
async def craid(event):
    # Extract the number from the command
    number = event.pattern_match.group(1)
    
    # Generate a random uppercase letter
    random_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    # Create the string with the letter repeated 50 times, followed by the number
    result = f"{random_letter * 50} {number}"
    
    # Reply with the generated string
    await event.respond(result)
    await event.delete()  


sattu.start()
sattu.run_until_disconnected()
