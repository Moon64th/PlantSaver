# This Script was made by Moon64th

import datetime

import discord

# main function
def main():
    class Plant:
        def __init__(self,name,date):
            self.name = name
            self.date = date

    # createplant is used to create new Plants
    def createplant():
        print("Create a new Plant:")
        name = input("Enter name for your Plant:")
        year = int(input("Enter year for watering reminder (e.g. 2025): "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day (1-31): "))
        hour = int(input("Enter hour (0-24):"))
        minute = int(input("Enter minute (0-59):"))

        date = datetime.datetime(year, month, day, hour, minute)
        return Plant(name=name, date=date)

    sf = input("Enter Software to use (Discord/Email/Whatsapp) to close the program tipe: close:")
    if sf.upper() == "DISCORD":
        # The token you will get from the discord developer Portal
        TOKEN = '<Your Token>'
        # Enter your user id
        USER_ID = int(input("Enter user ID: "))

        intents = discord.Intents.all()

        client = discord.Client(intents = intents)

        @client.event
        async def on_ready():
            print(f'✅ Logged in as {client.user}')
            try:
                user = await client.fetch_user(USER_ID)
                await user.send("Setup message, please continue in Console")
                print("📨 Message sent successfully!")
            except discord.Forbidden:
                print("❌ Cannot send message. The user might have DMs disabled or blocked the bot.")
            except discord.HTTPException as e:
                print(f"❌ Failed to send message: {e}")
            continueB = input("Do you wona add a Plant(y/n)?")
            if continueB == "n":
                await client.close()
                print("Client closed, you can now continue or end the program")
                main()
            elif continueB == "y":
                plant = createplant()
                print(plant.name,plant.date)
                try:
                    user = await client.fetch_user(USER_ID)
                    await user.send("Your plant "+plant.name+" was created!")
                    print("🌱Plant created successfully!")
                except discord.Forbidden:
                    print("❌ Cannot send message. The user might have DMs disabled or blocked the bot.")
                except discord.HTTPException as e:
                    print(f"❌ Failed to send message: {e}")
        client.run(TOKEN)

    elif sf.upper() == "EMAIL":
        print("Email")
    elif sf.upper() == "WHATSAPP":
        print("Whatsapp")
    elif sf.upper() == "CLOSE":
        return
    else:
        print("Chosen Software does not match any")

main()