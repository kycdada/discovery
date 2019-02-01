# De Discovery-service configureren
De Discovery-service instrueert de crawler hoe deze gecrawlde bestanden moet beheren bij gebruik van de IBM Watson Discovery-service. Standaardopties kunnen rechtstreeks worden gewijzigd door het openen van het bestand `config/discovery/discovery_service.conf` en de volgende waarden voor uw gebruiksvoorbeeld te wijzigen:

*  **http_timeout** - De timeout, in seconden, voor de lees/indexeerbewerking; de standaardwaarde is `125`.
*  **concurrent_upload_connection_limit** - Het aantal gelijktijdige verbindingen dat is toegestaan voor het uploaden van documenten; de standaardwaarde is `2`. Als u gebruik maakt van de Orchestration Service Output Adapter, moet dit getal groter zijn dan, of gelijk zijn aan, de `output_limit` die is ingesteld bij het configureren van de crawlopties.
*  **base_url** - De URL waarnaar de gecrawlde documenten worden verzonden. Voor de huidige release van de Discovery service is de waarde `https://gateway.watsonplatform.net/discovery/api`.
*  **environment_id** - De locatie van uw verzameling van gecrawlde documenten op de `base-url`.
*  **collectie-ID** - Naam van de documentcollectie die u instelt in de Discovery-service.
*  **configuration_id** - De bestandsnaam van het configuratiebestand dat de Discovery-service gebruikt.
*  **check_for_completion** - Controleert of het document op het eindpunt is verwerkt. Dit vermindert de waargenomen performance van de crawler, maar leidt tot betrouwbare melding van een geslaagde upload en conversie van documenten. De waarde is `true` of `false`.  
**BELANGRIJK** - Bij het inschakelen van deze parameter is het verstandig om de `concurrent_upload_connection_limit` in te stellen op meer dan, of gelijk aan de `output_limit` die is ingesteld bij het configureren van crawlopties; zo kunt u volledig gebruikmaken van de resources die voor u beschikbaar zijn.

Geef uw legitimatiegegevens voor de Discovery Service op:
*  **username** - Gebruikersnaam voor verificatie bij de locatie van uw verzameling van gecrawlde documenten.
*  **password** - Wachtwoord voor verificatie bij de locatie van uw verzameling van gecrawlde documenten.

De Discovery Service Output Adapter kan statistieken naar IBM verzenden om diens gebruikers beter te begrijpen en van dienst te zijn. De volgende opties kunnen worden ingesteld voor de variabele `send_stats`:
*  **jvm** - Statistieken over de JVM (Java Virtual Machine) die worden verstuurd zijn onder andere de leverancier en de Java-versie, zoals gemeld door de JVM die wordt gebruikt voor het uitvoeren van de Data Crawler. De waarde is `true` of `false`.
*  **os** - Statistieken over het besturingssysteem die worden verstuurd zijn onder andere de naam, versie en architectuur van het besturingssysteem, zoals gemeld door de JVM die wordt gebruikt voor het uitvoeren van de Data Crawler. De waarde is `true` of `false`.

*  **api_version** - Alleen voor intern gebruik. Datum van de laatste wijziging van de API-versie.

# Configuratie van de opslag voor het volgen van URL's
De map `config/discovery` bevat ook een configuratiebestand dat kan worden gebruikt voor interne toewijzing van crawler-URL's en document-ID's. De standaardopties kunnen rechtstreeks worden gewijzigd door het openen van het bestand `config/discovery/uri_tracking_storage.conf` en de volgende waarden voor uw specifieke gebruiksvoorbeeld te wijzigen:

*  **driver** - De JDBC H2-stuurprogrammaklasse van uw database. De standaardwaarde is `org.h2.Driver`
*  **url** - Dit is de URL-prefix voor de JDBC-verbindingsreeks. De indeling is `jdbc:h2:[file:]`. **OPMERKING** Het voorvoegsel `file:` is optioneel. Als er geen pad, of alleen een relatief pad wordt gebruikt voor `database_location`, wordt de huidige werkdirectory gebruikt als uitgangspunt. De standaardwaarde is `jdbc:h2:file:`
*  **database_location** - De locatie op de schijf waar de database is opgeslagen, bijvoorbeeld `./storage/database` of `~/storage/database`. De standaardwaarde is `./storage/database`
*  **database_name** - Naam van de database. De standaardwaarde is`ActivityDB`
*  **table_name** - Naam van de tabel die moet worden gebruikt. De standaardwaarde is `UriTracker`
*  **username** - Gebruikersnaam om verbinding te maken met de database
*  **password** - Wachtwoord om verbinding te maken met de database

## ZIE OOK

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
