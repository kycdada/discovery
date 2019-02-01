vcrypt (1) - Een tool voor het coderen en decoderen van kleine hoeveelheden gegevens
===============================================================

## SYNOPSIS

Syntaxis: vcrypt --decrypt|-d  --encrypt|-e  --genkey|-g [ OPTIES ]

## BESCHRIJVING

`vcrypt` wordt voornamelijk gebruikt voor versleuteling van wachtwoorden voor gebruik door het Connector Framework.

### Een speciale opmerking over de sleutellengte

Standaard moet een Java Virtual Machine ondersteuning bieden voor implementatie van 128-bits/16-byte AES-sleutels. Als het systeem beschikt over een installatie van Java Cryptographic Extensions, kan het mogelijk 256-bits/32-bytes AES-sleutels gebruiken. Er wordt een fout gegenereerd als er een 32-bytes sleutel is opgegeven, maar deze niet wordt ondersteund door de JVM die wordt gebruikt voor het starten van `vcrypt`.

## OPDRACHTEN

### --encrypt | -e OPTIES INVOER
Gegevens versleutelen die zijn opgegeven in een bestand of in de standaard invoerbron.

### --decrypt | -d OPTIES INVOER
Gegevens decoderen die zijn opgegeven in een bestand of in de standaard invoerbron.

### --genkey | -g
Hiermee genereert u een codeersleutel die geschikt is voor gebruik met `vcrypt` naar de standaarduitvoer.

## OPTIES

### --keyfile|-k PATH/TO/ID_VCRYPT
Geef het pad op naar het bestand met de juiste met Base64 gecodeerde sleutel, waarschijnlijk gegenereerd met behulp van de opdracht `--genkey|-g` command.

## INVOER

### Coderingsmodus

    $FILE_CONTAINING_CLEARTEXT | -- $CLEARTEXT

### Decoderingmodus

    $FILE_CONTAINING_CRYPTED_TEXT | -- $CRYPTED_TEXT

## VOORBEELDEN

Een sleutel genereren en deze in het bestand `id_vcrypt` plaatsen:

    vcrypt --genkey > id_vcrypt

Een wachtwoord versleutelen vanuit standaardinvoer naar standaarduitvoer, hier geschreven via omleiding van de uitvoer naar `my_secret_data.txt`:

    ./vcrypt --encrypt --keyfile id_vcrypt -- "mijn geheime wachtwoord" > my_secret_data.txt

U kunt de uitvoer ook doorsluizen naar `xclip`, `pbcopy`, of gelijksoortige bestemming om de uitvoer op het klembord van uw besturingssysteem te plaatsen.

Een wachtwoord decoderen uit een bestand:

    vcrypt --decrypt --keyfile id_vcrypt my_secret_data.txt

## EIGENSCHAPPEN EN OMGEVINGSVARIABELEN

### Omgevingsvariabele `VCRYPT_OPTS`
Deze omgevingsvariabele kan worden gebruikt voor het doorgeven van opties aan de `java`-opdracht die wordt gebruikt voor het starten van `vcrypt`.

### Eigenschap `vcrypt.key`
Geef deze door als `-D` eigenschap in `VCRYPT_OPTS` met een tekenreeks van 16 of 32 bytes om een sleutel op de opdrachtregel te gebruiken in plaats van de optie `--keyfile | -k keyfile` door te geven.

Voorbeeldgebruik:

    VCRYPT_OPTIONS="-Dvcrypt.key='1234qwerasdfzxcv'" vcrypt --encrypt te_coderen_bestand

### Omgevingsvariabele `VIV_VCRYPT_KEY`
In `vcrypt` kunt u deze omgevingsvariabele gebruiken om de sleutel in te stellen. Deze moet bestaan uit 16 of 32 bytes.

## ZIE OOK

crawler(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
