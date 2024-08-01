import random
print("welkom")
user=0
megic=random.randint(1,100)
while megic!=user:
    user=int(input(" ведіть чесло:"))
    if megic>user:
        print("більше")
    elif megic<user:
        print("меньше")
print("ти переміга:),перемога буде:)")50