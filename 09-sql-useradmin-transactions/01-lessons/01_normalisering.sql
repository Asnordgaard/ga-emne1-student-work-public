-- Normalisering handler om å sørge for at en database har god struktur
-- med tanke på innlegging, endring og sletting.

-- UNF: Unormalisert form (ikke egnet for MySQL db
-- NF1: Normalisert form 1 - Data ER på et format som kan legges inn i en database (eks. ikke to verdier i samme "celle")
-- NF2: Normalisert form 2 - Fjerne delvis avhengighet Eks. personnummer er determinant for person og adresse
-- regnr. er determinant for bil og modell. Redundans er fjernet.

-- NF3: Vi kan ikke ha kolonner som (rely on) noe utenfor primærnøkkel. Ingen transitiv avhengighet.
-- Eks. Kolonne C kan ikke være avhengig av både kolonne B OG A.

