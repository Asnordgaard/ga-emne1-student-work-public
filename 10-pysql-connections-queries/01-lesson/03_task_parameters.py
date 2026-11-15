import mysql.connector
from mysql.connector import Error



try:
    print("Connecting to the database...")
    with mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "gokstad",
        database = "world"
    ) as connection:
        print("Connected to MySQL")
        city_name = input("Skriv navnet på en by: ")
        with  connection.cursor() as cursor:
            sql = (
                "SELECT Name, Population, CountryCode "
                "FROM city "
                "WHERE Name = %s "
            )
            cursor.execute(sql, (city_name,))
            rows = cursor.fetchall()
            if not rows:
                print("Ingen rader funnet")
            else:
                for name, population, country_code in rows:
                    print(f"{name}: {population}, {country_code}")
except Error as e:
    print(f"Error using MySQL: {e}")