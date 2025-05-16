import discord
from Application.plant import *
from Application.timer import createTimer

def dcbot(plantArray, f):
    TOKEN = 'MTM2OTE5OTU1OTk4MDM1MTUwOA.GHxuVV.1_HHQz3UpHAqTykWa2pdECUYLbTQfjxB8stnzg'
    # Enter your user id
    check = False
    while check == False:
        user_input = input("Enter Discord user ID: ")
        if user_input.isdigit():
            USER_ID = int(user_input)
            check = True
        else:
            print("Invalid input. Please enter a numeric user ID.")
    intents = discord.Intents.all()

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')
        try:
            user = await client.fetch_user(USER_ID)
            await user.send("Setup message, please continue in Console")
            print("📨 Message sent successfully!")
        except discord.Forbidden:
            print("Cannot send message. The user might have DMs disabled or blocked the bot.")
        except discord.HTTPException as e:
            print(f"Failed to send message: {e}")
        continueB = input("Do you wona add a Plant(y/n)?")
        if continueB.upper() == "N":
            await client.close()
            client.clear()
            print("Client closed, you can now continue or end the program")
            f()
        elif continueB.upper() == "Y":
            while continueB.upper() == "Y":
                newPlant = createplant()
                try:
                    user = await client.fetch_user(USER_ID)
                    await user.send("Your plant " + newPlant.name + " was created!")
                    print("Plant created successfully!")
                except discord.Forbidden:
                    print(" Cannot send message. The user might have DMs disabled or blocked the bot.")
                except discord.HTTPException as e:
                    print(f"Failed to send message: {e}")
                plantArray.add_plants(newPlant)
                continueB = input("Do you wona add another Plant(y/n)?")
        print("Your Plants:")
        for plant in plantArray:
            print(plant.name)
            await createTimer(plant)
            try:
                user = await client.fetch_user(USER_ID)
                await user.send("Water your plant! " + plant.name)
                print("📨 Reminder was send successfully!")
            except discord.Forbidden:
                print("Cannot send message. The user might have DMs disabled or blocked the bot.")
            except discord.HTTPException as e:
                print(f"Failed to send message: {e}")
            continueC = input("Restard the timer(y/n): ")
            while continueC.upper() == "Y":
                await createTimer(plant)
                continueC = input("Restard the timer(y/n): ")
            if continueC.upper() == "N":
                await client.close()

    client.run(TOKEN)
