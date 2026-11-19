# Struktur på koden

## config_local.py
<code>config_local.py</code> inneholder selve tilkoblingsinfoen til DB.

Her settes all info som python mysql.connector er avhengig av:

```
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "YOUR_DB_USER",
    "password": "YOUR_DB_PASS",
    "database": "world"
}
```

## database.py
Importerer settinger fra config_local.py og definerer spørring mpt DB. 
I dette tilfellet er det en SELECT som kjøres