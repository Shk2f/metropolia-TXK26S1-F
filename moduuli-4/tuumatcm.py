while True:
    tuuma = int(input("Anna tuumamäärä: "))
    if tuuma > 0:
        cm = tuuma * 2.54
        print(f"{tuuma} tuumaa on {cm} senttimetriä.")
    else:
        break