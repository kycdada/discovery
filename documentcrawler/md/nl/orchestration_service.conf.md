# De Orchestration-service configureren
De Orchestration-service instrueert de crawler hoe deze gecrawlde bestanden moet beheren. Standaardopties kunnen rechtstreeks worden gewijzigd door het openen van het bestand `config/orchestration/orchestration-service.conf` en de volgende waarden voor uw specifieke gebruiksvoorbeeld te wijzigen:

*  **http_timeout** - De timeout, in seconden, voor de lees/indexeerbewerking; de standaardwaarde is `585`.
*  **concurrent_upload_connection_limit** - Het aantal gelijktijdige verbindingen dat is toegestaan voor het uploaden van documenten; de standaardwaarde is `10`. In het algemeen moet dit getal groter zijn dan, of gelijk zijn aan, de `output_limit` die is ingesteld bij het configureren van de crawlopties. 
*  **base_url** - De URL waarnaar de gecrawlde documenten worden verzonden.
*  **endpoint** - De locatie van uw verzameling van gecrawlde documenten op de `base-url`.
*  **username** - De gebruikersnaam voor verificatie bij de locatie van `endpoint`. 
*  **password** - Het wachtwoord voor verificatie bij de locatie van `endpoint`. **Belangrijk** - Maak **GEEN** gebruik van het programma vcrypt dat bij de Data Crawler is geleverd voor het versleutelen van dit wachtwoord.
*  **config_file** - Het configuratiebestand dat de Orchestration-service gebruikt.

De Orchestration Service Output Adapter kan statistieken naar IBM verzenden om diens gebruikers beter te begrijpen en van dienst te zijn. De volgende opties kunnen worden ingesteld voor de variabele `send_stats`:
*  **jvm** - Statistieken over de JVM (Java Virtual Machine) die worden verstuurd zijn onder andere de leverancier en de Java-versie, zoals gemeld door de JVM die wordt gebruikt voor het uitvoeren van de Data Crawler. De waarde is `true` of `false`.
*  **os** - Statistieken over het besturingssysteem die worden verstuurd zijn onder andere de naam, versie en architectuur van het besturingssysteem, zoals gemeld door de JVM die wordt gebruikt voor het uitvoeren van de Data Crawler. De waarde is `true` of `false`.

## ZIE OOK

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
