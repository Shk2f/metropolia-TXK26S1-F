import random
randomint = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku väliltä 1-10: "))
    if arvaus > randomint:
        print("Luku on pienempi.")
    elif arvaus < randomint:
        print("Luku on suurempi.")
    else:
        print("Arvasit oikein!")
        break