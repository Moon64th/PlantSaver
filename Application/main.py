from Application.token import BOT_TOKEN

sf = input("enter Software to use (Discord/Email/Whatsapp)")
if sf == "Discord":
   print("Discord")
elif sf == "Email":
    print("Email")
elif sf == "Whatsapp":
    print("Whatsapp")
else:
    print("Chosen Software does not match any")