import random
print("вітаємо:)")
user_choice=0
bot_choice=0
user_skore=0
bot_skore=0
for x in range(5):
    print("raund",x+1)
    bot_choice=random.choice(["k","p","n"])
    user_choice=input("ваш вибір:")
    print("вибір бота",bot_choice,"x"," ваш вибір",user_choice)
    if user_choice==bot_choice:
        print("nichua")
    elif user_choice=="k":
        if bot_choice=="n":
            print("win it raund")
            user_skore+=1
        else:
            print("bot win it raund ")
            bot_skore+=1
    elif user_choice=="p":
        if bot_choice=="k":
            print("win it raund")
            user_skore+=1
        else:
            print("bot win it raund ")
            bot_skore += 1
    elif user_choice == "n":
        if bot_choice == "p":
            print("win it raund")
            user_skore += 1
        else:
            print("bot win it raund ")
            bot_skore += 1
if user_skore==bot_skore:
    print("resait nichua")
elif user_skore>bot_skore:
    print("uo=win")
    print(user_skore,":",bot_skore)
else:
    print("botwin")
    print(user_skore, ":", bot_skore)