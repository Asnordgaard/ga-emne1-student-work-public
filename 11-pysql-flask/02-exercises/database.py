import mysql.connector
from config_local import DB_CONFIG

def get_cities(code):
    sql = (
        "SELECT Name, District, Population "
        "FROM city "
        "WHERE CountryCode = %s "
        "ORDER BY Name ASC"
    )
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, (code,))
            return cursor.fetchall()


def get_regions():
    sql = (
        "SELECT DISTINCT Region "
        "FROM country "
        "ORDER BY Region ASC"
    )
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()


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
