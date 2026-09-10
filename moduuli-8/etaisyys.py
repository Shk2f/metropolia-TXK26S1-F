from sqlConnection import get_connection
from geopy.distance import geodesic
connection = get_connection()
cursor = connection.cursor()

icao_koodi_1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao_koodi_2 = input("Anna toisen lentokentän ICAO-koodi: ")

cursor.execute(
    "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s",
    (icao_koodi_1,),
)
koordinaatit_1 = cursor.fetchone()

cursor.execute(
    "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s",
    (icao_koodi_2,),
)
koordinaatit_2 = cursor.fetchone()

if koordinaatit_1 is None or koordinaatit_2 is None:
    print("Yhtä tai molempia lentokenttiä ei löytynyt tietokannasta.")
else:
    etaisyys = geodesic(koordinaatit_1, koordinaatit_2).kilometers
    print(f"Etäisyys lentokenttien välillä: {etaisyys:.2f} km")
    
cursor.close()
connection.close()