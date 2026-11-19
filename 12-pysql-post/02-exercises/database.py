import mysql.connector
from config_local import DB_CONFIG

from models import City

def get_cities(code):
    sql = (
        "SELECT ID, Name, CountryCode, District,Population "
        "FROM city "
        "WHERE CountryCode = %s "
        "ORDER BY Name ASC"
    )

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, (code,))
            return cursor.fetchall()


def get_city(city_id):
    sql = (
        "SELECT Name, CountryCode, District, Population "
        "FROM city "
        "WHERE ID = %s"
    )
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, (city_id,))
            row = cursor.fetchone()
    if row is None:
        return None
    return City(city_id, row[0], row[1], row[2], row[3])


def get_countries(region):
    sql = (
        "SELECT Name, Population "
        "FROM country "
        "WHERE Region = %s "
        "ORDER BY Name ASC"
    )

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, (region, ))
            return cursor.fetchall()


def get_country_code():
    sql = (
        "SELECT DISTINCT Code, Name "
        "FROM country "
        "ORDER BY Name ASC"
    )

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()


def get_country_name(code):
    sql = (
        "SELECT DISTINCT Name "
        "FROM country "
        "WHERE Code = %s "
        "ORDER BY Name ASC"
    )

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, (code, ))
            row = cursor.fetchone()
    if row is None:
        return '"Unknown country name"'
    return row[0]


def insert_city(name, countrycode, district, population):
    sql = (
        "INSERT INTO city "
        "(Name, CountryCode, District, Population) "
        "VALUES (%s, %s, %s, %s)"
    )
    params = (name, countrycode, district, population)

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        connection.commit()



def update_city(city_id, name, countrycode, district, population):
    sql = (
        "UPDATE city "
        "SET Name = %s, "
        "CountryCode = %s, "
        "District = %s, "
        "Population = %s "
        "WHERE ID = %s"
    )
    params = (name, countrycode, district, population, city_id)

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        connection.commit()



def delete_city(city_id):
    sql = (
        "DELETE FROM city "
        "WHERE ID = %s"
    )
    params = (city_id,)
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
        connection.commit()