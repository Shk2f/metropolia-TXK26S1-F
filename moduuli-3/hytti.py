hyttisi = input('Anna hyttisi luokka: ')

if hyttisi.upper() == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif hyttisi.upper() == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif hyttisi.upper() == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hyttisi.upper() == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka')