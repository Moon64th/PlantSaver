import asyncio
from time import sleep


def createTimer(plant):
    timer = 0
    timer_started = True
    print(f"Timer set for {plant.time} minute/s, you will get a reminder on your chosen platform when the timer runs out")
    while timer_started:
        sleep(1)
        timer += 1
        if timer >= plant.time * 60:
            timer_started = False
            print("Message Reminder sent, water your plant!")
