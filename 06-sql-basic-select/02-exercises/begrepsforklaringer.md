## Oppgave 2.1 Hva gjør de ulike delene
*Forklar med egne ord hva en database, et DBMS og SQL er. Knytt begrepene til World og MySQL. Forklar
deretter hvilken rolle DataGrip og Docker har i oppsettet vårt.*


En database er strukturen som holder selve datasettet
* En DBMS er systemet som administrerer databaser (MySQL, MS SQL Server, Oracle etc)
* SQL er syntaks som benyttes for å utføre operasjoner på data i en database. Dette kan være spørringer, inserts, oppdatering etc.

* Datagrip er et verktøy for å kunne koble til databaser, se innhold (data), kolonner, rettigheter ved å benytte SQL syntaks.
Det er en IDE for databaser.
* Docker er for å kunne administtrere og kjøre applikasjoner i dedikerte kontainere på lokal maskin.
Det gjør at man slipper å installer f.eks MySQL lokalt for å kjøre databasen. En kontainer
bruker svært lite minne, og kan slås på og av ved behov.


## Oppgave 2.2 Tabell rad og kolonne
*Åpne strukturen til city i DataGrip. Hva representerer én rad? Hva beskriver kolonnene Name, CountryCode,
District og Population?
Finn datatypene til ID, Name og Population. Forklar hvorfor navn og folketall trenger forskjellige datatyper.*

* En rad representerer én instans av et datasett.
* Name = Bavn på byen
* CountryCode = 3 bokstavs landkode
* District = Område/fylke
* Population = Antall innbyggere 

* ID = INT, Name = Char(35) som betyr at navnet er begrenset til 35 bokstaver, Population = INT
* Navn på by må kunne skrives slik de er, derfor må dette være en tekststreng
* Innbyggertall må kunne benyttes til beregninger (<, >, sum) og må derfor være tall. De er INT da det ikke finnes halve innbyggere.
* 