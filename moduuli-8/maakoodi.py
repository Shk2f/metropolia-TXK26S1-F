from sqlConnection import get_connection

connection = get_connection()
cursor = connection.cursor()

maakoodi = input("Anna maakoodi: ")

cursor.execute(
    "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type ORDER BY COUNT(*) DESC",
    (maakoodi,),
)
rows = cursor.fetchall()

if not rows:
    print(f"Maakoodilla {maakoodi} ei löytynyt yhtään lentokenttää.")
else:
    print(f"\nLentokentät maassa {maakoodi} tyypeittäin:")
    for type, amount in rows:
        print(f"{type}: {amount} kpl")