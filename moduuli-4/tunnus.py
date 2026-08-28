user = {"tunnus": 'python', "salasana": 'rules'}
attempts = 0

while True:
    tunnus = input("Anna tunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == user["tunnus"] and salasana == user["salasana"]:
        print("Tervetuloa!")
        break
    else:
        attempts += 1
        print("Väärä tunnus tai salasana.")
        if attempts >= 3:
            print("Pääsy evätty.")
            break