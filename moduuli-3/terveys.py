sukupuoli = input("Anna sukupuolesi (mies/nainen): ")
hemoglobiiniarvo = int(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli.upper() == "MIES":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvosi on liian alhainen. Sinulla voi olla anemia.")
    elif hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvosi on liian korkea. Sinulla voi olla polycytemia.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli.upper() == "NAINEN":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvosi on liian alhainen. Sinulla voi olla anemia.")
    elif hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvosi on liian korkea. Sinulla voi olla polycytemia.")
    else:
        print("Hemoglobiiniarvosi on normaali.")