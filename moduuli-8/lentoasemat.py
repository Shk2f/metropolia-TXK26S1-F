from sqlConnection import get_connection

icao_koodi = input("Anna ICAO-koodi: ")

connection = get_connection()
cursor = connection.cursor()

sql = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(sql, (icao_koodi,))

result = cursor.fetchone()

if result:
    nimi, kunta = result
    print(f"{nimi} sijaitsee kunnassa {kunta}")
else:
    print("Lentokenttää ei löytynyt annetulla ICAO-koodilla.")

cursor.close()
connection.close()