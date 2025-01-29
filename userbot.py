import requests
import random
import asyncio
from telethon import TelegramClient, events
from telethon import events


api_id = 22798308 
api_hash = '69c3cdf2386e7c15ebac4c66e5513ef4'
sattu = TelegramClient('session', api_id, api_hash)


'COMMAND GREET'
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


'COMMAND HI'
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


'COMMAND BYE'
@sattu.on(events.NewMessage(outgoing=True, pattern='.bye'))
async def bye(event):
    sent_message = event.message
    await sent_message.edit('''
█▄▄ █▄█ █▀▀
█▄█ ░█░ ██▄''')


'COMMAND VARSHU'
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


'COMMAND ALIVE'
@sattu.on(events.NewMessage(outgoing=True, pattern='.alive'))
async def alive(event):
    sent_message =await event.edit("Initiating bot check... 🚨")
    await asyncio.sleep(1)

    image_url = "https://www.comingsoon.net/wp-content/uploads/sites/3/2024/04/jujutsu-kaisen-jin-itadori-family-tree.png?resize=624,576"
    roast_comment = "**लगता है इस GC में किसी ने आखिरकार मुझे जगा ही लिया... 🤦‍♂️**"
    await event.edit(f"**Bot is alive! ✅**\n\n{roast_comment}\n\n**Owner:- @sattu879**\n**Developer:-** The wizard who made this magic happen. 🔮", file=image_url)


'COMMAND SPAM'
@sattu.on(events.NewMessage(outgoing=True, pattern=r'\.spam (\d+) (.+)'))
async def spam(event):
    count = int(event.pattern_match.group(1))
    message = event.pattern_match.group(2)   
    for _ in range(count):
        await event.respond(message)
        await asyncio.sleep(0.01) 

        await event.delete() 


'COMMAND CRAID'
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


'COMMAND SCRAID'
@sattu.on(events.NewMessage(outgoing=True, pattern=r'\.scraid (\d+)'))
async def scraid(event):
    number_of_craids = int(event.pattern_match.group(1))
    for _ in range(number_of_craids):
        random_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        result = random_letter * 170 
        
        await event.respond(result)
        await event.delete()


'COMMAND WEATHER'
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
         
        

'COMMAND (NIKAL) FOR KICK USERS'
@sattu.on(events.NewMessage(pattern=r'\.nikal @(\w+)'))
async def kick_user(event):
    username = event.pattern_match.group(1)
    
    roast_messages = [
        f"🚫 **{username} को ऐसे बाहर किया, जैसे आइसक्रीम गिरा दी हो! 🍦💨**",
        f"🚫 **{username}, अब जा, कहीं तो अपनी इस अकल का सही इस्तेमाल कर! 🤦‍♂️**",
        f"🚫 **तू तो कमाल का निकला! अब किसी को फेंकने की आदत हो गई क्या, {username}? 😎**",
        f"🚫 **अबे {username}, तुझसे तो वो 'फेल' ही बेहतर था! 😂**",
        f"🚫 **जैसे बिना आइसक्रीम के सर्दी, वैसे बिना तेरे के ग्रुप मजेदार! 💔🍦**",
        f"🚫 **{username}, क्या तू खुद को बड़ा समझता है? यहाँ तो किसी की भी जगह नहीं पक्की! 😜**",
        f"🚫 **जा भाई, कहीं और टाइम पे हमसे भिड़ना! 💥**",
        f"🚫 **गुस्से में क्यों हो, भाई? कुछ ज्यादा ही बिगड़ रहे हो! {username} 😂**",
        f"🚫 **{username}, यही काम करना था? लाओ कुछ और ट्रिक दिखाओ! 🙄**",
        f"✅ **{username} को ग्रुप से ऐसे बाहर किया, जैसे आइसक्रीम गिरा दी हो! 🍦💨**"
    ]
    
    try:
        user = await sattu.get_entity(username) 
        await event.reply(f"🚫 **Kicking user {username}...**")
        await event.client.kick_participant(event.chat_id, user.id)
        
        selected_roast_message = random.choice(roast_messages)
        await event.reply(selected_roast_message)
    
    except ValueError:
        await event.reply(f"❌ **User {username} not found!**")
    
    except Exception as e:
        await event.reply(f"❌ **An error occurred while kicking the user:** {str(e)}")
        
 
'COMMAND (SSPAM) FOR STICKER SPAM'       
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
        

'COMMAND (MSPAM) FOR SOMEONE MESSAGE SPAM'
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
        

'COMMAND HEHE'   
@sattu.on(events.NewMessage(pattern=r"\.hehe"))
async def hehe(event):
    emojis = [
        "😀", "😃", "😄", "😁", "😎", "😅", "🤣", "😂", 
        "😛", "😜", "🤪", "😝", "🤫", "🫡", "😶", "😆"
    ]  
    for emoji in emojis:
        await event.edit(emoji)
        await asyncio.sleep(2) 
        

'COMMAND PING'      
@sattu.on(events.NewMessage(outgoing=True, pattern='\.ping'))
async def ping(event):
    emojis = [
        "⚡", "💥", "🌟", "🔥",
    ]
    for emoji in emojis:
        await event.edit(f"{emoji}") 
        await asyncio.sleep(1.9) 
        
    random_ping = random.uniform(60, 68)
    formatted_ping = f"{random_ping:.2f}"
    await event.edit(f'🏓 **Pong!** (Ping: {formatted_ping}ms)')


'FUN COMMAND'
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


'COMMAND PHOTO'
OWNER_ID =  7605208581
@sattu.on(events.NewMessage(pattern=r"\.photo(?:\s|$)([\s\S]*)"))
async def potocmd(event):
    if event.sender_id != OWNER_ID:
        return await event.reply("`𝗢𝗡𝗟𝗬 𝑺𝒂𝒕𝒕𝒖 𝒄𝒂𝒏 𝒖𝒔𝒆 𝒕𝒉𝒊𝒔 𝒄𝒐𝒎𝒎𝒂𝒏𝒅! 💥`")

    # To get user or group profile pic
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    
    if user and user.sender:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False

    # If no specific photo number is mentioned, default to "1"
    if not uid.strip():
        uid = 1
        if uid > len(photos):
            return await event.edit("`No photo found of this NIBBA / NIBBI. Now u Die!`")
        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    
    # Show all photos
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


'COMMAND SAFAI'
@sattu.on(events.NewMessage(pattern=r"\.safai"))
async def clear_chat(event):
    if event.sender_id != OWNER_ID:
        return await event.reply("`𝗢𝗡𝗟𝗬 𝑺𝒂𝒕𝒕𝒖 𝒄𝒂𝒏 𝒖𝒔𝒆 𝒕𝒉𝒊𝒔 𝒄𝒐𝒎𝒎𝒂𝒏𝒅! 💥`")

    async for message in event.client.iter_messages(event.chat_id, limit=300):
        await message.delete()
    await event.reply("🧹 **Chat Cleared!**", delete_after=5)


'COMMAND GCAST'
gcast_message_ids = []
@sattu.on(events.NewMessage(pattern=r'\.gcast(?:\s|$)([\s\S]*)'))
async def gcast_handler(event):
    if event.sender_id != OWNER_ID:
        return await event.reply("`Only the owner can use this command! 💥`")

    if event.is_reply:
        replied_message = await event.get_reply_message()
        message_to_broadcast = replied_message.text if replied_message else "No message provided in the reply."
    else:
        message_to_broadcast = event.raw_text.split(maxsplit=1)[1] if len(event.raw_text.split()) > 1 else "No message provided"

    success_count = 0
    fail_count = 0

    async for dialog in sattu.iter_dialogs():
        try:
            if dialog.is_user or dialog.is_group:
                msg = await sattu.send_message(dialog.id, message_to_broadcast)
                gcast_message_ids.append(msg.id) 
                success_count += 1
                print(f"Message sent to {dialog.name}")
            else:
                fail_count += 1
        except Exception as e:
            print(f"Failed to send message to {dialog.name}: {e}")
            fail_count += 1
    await event.edit(f"Broadcast completed! {success_count} messages sent successfully, {fail_count} failed.")


'COMMAND DELGCAST'
@sattu.on(events.NewMessage(pattern=r'\.delgcast'))
async def delgcast_handler(event):
    if event.sender_id != OWNER_ID:
        return await event.reply("`Only the owner can use this command! 💥`")

    deleted_count = 0
    failed_count = 0

    for msg_id in gcast_message_ids:
        try:
            await sattu.delete_messages(event.chat_id, msg_id)
            deleted_count += 1
            print(f"Deleted message with ID {msg_id}")
        except Exception as e:
            print(f"Failed to delete message {msg_id}: {e}")
            failed_count += 1

    # Inform the user after deletion
    await event.edit(f"Deletion completed! {deleted_count} messages deleted successfully, {failed_count} failed.")


"""@sattu.on(events.NewMessage(pattern=r'\.zinda @(\w+)'))
async def unban_user(event):
    username = event.pattern_match.group(1)
    
    # List of fun welcome/unban messages
    welcome_messages = [
        f"✅ **{username} वो कौन आया, जिसने सबको हिलाकर रख दिया?**",
        f"✅ **{username} ग्रुप में शामिल होते ही सारा माहौल बदल गया!**",
        f"✅ **{username} आ गया राजा! अब ग्रुप में मज़ा आएगा!**",
        f"✅ **स्वागत है {username}! अब तो ग्रुप में धमाल मचाने का समय है!**",
        f"✅ **{username} ग्रुप में शामिल होते ही रंग आ गए हैं!**",
        f"✅ **{username} अब ग्रुप में और भी मज़ेदार बातें होंगी!**",
        f"✅ **{username} सुपरस्टार आ गया! अब तो ग्रुप में हर दिन नया ड्रामा होगा!**",
        f"✅ **{username} अब ग्रुप में धमाल मचाने का समय है!**",
        f"✅ **स्वागत है {username}! अब ग्रुप का स्टाइल चार चाँद लगने वाला है!**"
    ]
    
    try:
        # Fetch user details using the provided username
        user = await sattu.get_entity(username)
        
        # Attempt to unban the user
        await event.reply(f"🚫 **Unbanning user {username}...**")
        await event.client.unban(event.chat_id, user.id)
        
        # Randomly select a message to send after unbanning
        selected_message = random.choice(welcome_messages)
        await event.reply(selected_message)
    
    except ValueError:
        # User not found in the system
        await event.reply(f"❌ **User {username} not found!**")
    
    except Exception as e:
        # General error handler
        await event.reply(f"❌ **An error occurred while unbanning the user: {str(e)}**")"""

sattu.start()
sattu.run_until_disconnected()