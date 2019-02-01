# De Data Crawler configureren

Voor opties van de `crawler` is een configuratiebestand vereist. Voorbeelden van configuratie vindt u in de directory `share` in de installatiedirectory van de `crawler`. Kopieer deze voorbeelden en wijzig ze. *Breng geen wijzigingen ter plekke in de voorbeelden aan.*

Het bestand `crawler.conf` bevat informatie die de crawler instrueert welke bestanden moeten worden gebruikt voor het crawlen (invoeradapter), waar de verzameling van gecrawlde bestanden naartoe verzonden wordt als de crawl voltooid is (uitvoeradapter) en andere opties voor het beheren van crawls.

**Opmerking**: Alle paden zijn relatief ten opzichte van de directory `config`, behalve waar aangegeven.

De opties die in dit bestand kunnen worden ingesteld, zijn:

## Invoeradapter
*  **class** - Alleen intern gebruik; definieert de invoeradapterklasse van Data Crawler. De standaardwaarde is: `com.ibm.watson.crawler.connectorframeworkinputadapter.Crawl`.
*  **config** - Alleen intern gebruik; definieert de configuratie van het Connector Framework. De standaard configuratiesleutel in dit blok die wordt doorgegeven aan de gekozen invoeradapter is: `connector_framework`. **Opmerking** - Het connectorframework maakt het mogelijk om met uw gegevens te communiceren. Dit kunnen interne gegevens binnen het bedrijf zijn, of externe gegevens op het web of in de cloud. De connectors geven toegang tot een aantal verschillende gegevensbronnen. Het maken van de verbinding wordt feitelijk bestuurd door het crawlproces.
  -  **BELANGRIJK** - Gegevens die door de Connector Framework Input Adapter worden opgehaald, worden in de lokale cache opgeslagen. Ze worden niet versleuteld opgeslagen. Standaard worden de gegevens in cache geplaatst in een tijdelijke directory die moet worden gewist bij het opstarten en die alleen mag worden gelezen door de gebruiker die de crawlopdracht heeft uitgevoerd. Er is een kans dat deze directory de crawler overleeft als het connectorframework zou verdwijnen voordat het een opschoonbewerking zou uitvoeren. U moet de locatie van cachegegevens zorgvuldig overwegen - u kunt ze op een versleuteld bestandssysteem zetten, maar houd er in dat geval rekening mee dat dat ten koste van de prestaties kan gaan. Alleen u kunt de juiste balans tussen snelheid en beveiliging van uw crawls bepalen.
*  **crawl_config_file** - Het configuratiebestand dat moet worden gebruikt voor het crawlproces. De standaardwaarde is: `connectors/filesystem.conf`.
*  **crawl_seed_file** - Het crawlseedbestand dat moet worden gebruikt voor het crawlproces. De standaardwaarde is: `seeds/filesystem-seed.conf`.
*  **id_vcrypt_file** - Het sleutelbestand dat door de crawler wordt gebruikt om gegevens te versleutelen; de standaardsleutel die in de crawler is opgenomen is `id_vcrypt`.
Gebruik het script vcrypt in de map `bin` als u een nieuw id_vcrypt_file wilt genereren.
*  **crawler_temp_dir** - De tijdelijke crawlermap voor connectorlogboeken. Er is een standaardwaarde, `tmp`, beschikbaar. Als de map `tmp` nog niet aanwezig is, wordt hij in de actieve directory gemaakt.
*  **extra_jars_dir** - Alleen intern gebruik; voegt extra JAR-bestanden toe aan het klassenpad van het Connector Framework.
Deze waarde moet `oakland` zijn bij gebruik van de SharePoint-connector en `database` wanneer u de databaseconnector gebruikt. U kunt hem leeg laten (d.w.z. een lege string "") als u andere connectors gebruikt. **Opmerking**: Relatief ten opzichte van de directory `lib/java` van het connectorframework.
*  **urls_to_filter** - Door terugloop-met-nieuwe-regel gescheiden goedgekeurde lijst van URL's die gecrawld worden, in de vorm van een expressie. De Data Crawler crawlt alleen URL's die overeenkomen met een van de expressies. De domeinlijst bevat de meest voorkomende domeinen van het hoogste niveau; indien nodig kunt u items toevoegen. De lijst met bestandsextensietypen bevat de extensies van bestanden die de Orchestration Service ondersteunt, vanaf deze release van de Data Crawler. Zorg ervoor dat het domein van de seed-URL door het filter wordt toegestaan. Als de seed-URL er bijvoorbeeld als volgt uitziet `http://testdomain.test.in`, voegt u "`in`" toe aan het domeinfilter. Zorg ervoor dat de seed-URL niet door een filter wordt uitgesloten, anders kan de crawler vastlopen.
*  **max_text_size** - De maximumgrootte, in bytes, van een document voordat het door het Connector Framework wordt weggeschreven naar een lokale schijf. Het aanpassen van deze waarde naar een hogere waarde vermindert de hoeveelheid documenten die naar schijf worden geschreven, maar vergroot het vereiste geheugen.
*  **extra_vm_params** - Hiermee voegt u extra Java-parameters toe aan de opdracht die wordt gebruikt voor het starten van het Connector Framework.
*  **bootstrap_logging** - Schrijft het opstartlogboek van het connectorframework; dit is alleen nuttig bij geavanceerde foutopsporing. Waarden zijn `true` of `false`. Het logbestand wordt weggeschreven naar `crawler_temp_dir`.

## Opslagadapter

Hiermee kunt u de interne status van de crawler opslaan in een database. Deze instelling is vereist om de opties `opnieuw starten` en `hervatten` voor het crawlproces correct te laten werken.

```javascript
storage_adapter {
 config = "storage_in_db"
  storage_in_db {
    include "storage/database_storage.conf"
  } 
}
```
Het bestand waarnaar wordt verwezen, `storage/database_storage.conf`, gebruikt standaard een H2-database. U kunt elke database met een JDBC-stuurprogramma gebruiken in plaats van de standaardwaarden. Raadpleeg de documentatie bij uw JDBC-stuurprogramma om specifieke informatie over een aantal van deze instellingen op te zoeken. De standaardopties kunnen rechtstreeks worden gewijzigd door het openen van het bestand `config/storage/database_storage.conf` en de volgende waarden voor uw gebruiksvoorbeeld te wijzigen:

*  **class** - Deze klasse verwijst naar de databaseadapterklasse die u wilt gebruiken. De standaardwaarde is `com.ibm.watson.crawler.storageadapters.DatabasePersistAdapter`
*  **driver** - De klasse voor het JDBC-stuurprogramma. De standaardwaarde is `org.h2.Driver` voor het gebruik van H2
*  **erl** - Zie de JDBC-opties voor uw stuurprogramma. Dit is de URL-prefix voor de JDBC-verbindingsreeks. De standaardwaarde is `jdbc:h2:file:`
*  **database_location** - De locatie waar uw database zich moet bevinden. Dit geldt alleen voor databases op basis van bestanden, zoals sqlite en H2. De standaardwaarde is `./storage/database`
*  **database_name** - Naam van de database. De standaardwaarde is`ActivityDB`
*  **table_name** - Naam van de tabel die moet worden gebruikt. De standaardwaarde is `Ledger`
*  **username** - Gebruikersnaam om verbinding te maken met de database
*  **password** - Wachtwoord om verbinding te maken met de database

De standaardconfiguratie voldoet voor de meeste activiteiten

## Uitvoeradapter

Er is een aantal *uitvoeradapters* waaruit u kunt kiezen. Stel de uitvoeradapter in door `output_adapter.class` in `crawler.conf` in te stellen. De opties zijn:

*  **class** - Definieert de uitvoeradapterklasse van de Data Crawler. De standaardwaarde is `com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter`
*  **config** - Geeft aan welke configuratiesleutel aan de uitvoeradapter moet worden doorgegeven. De tekenreeks moet overeenkomen met een sleutel in dit configuratieobject. Zie het volgende codevoorbeeld:
```javascript
  orchestration_service {
    include "orchestration_service.conf"
  },
  test {
    output_directory = "/tmp/crawler-test-output"
  }
}
```
de configuratiesleutel is `orchestration_service`. De standaardwaarde is `discovery_service`
U moet een uitvoeradapter selecteren door het opgeven van de parameter `class` en de sleutel `config`.

* **Orchestration Service-uitvoeradapter**: Hiermee uploadt u gecrawlde documenten naar de Orchestration Service van Watson Developer Cloud. Selecteer deze adapter door de parameter `class` en de sleutel `config` als volgt in te stellen: 
```javascript
  class = "com.ibm.watson.crawler.orchestrationserviceoutputadapter.oneatatime.OrchestrationServiceOutputAdapter"
  config = "orchestration_service"
  orchestration_service {
    include "orchestration/orchestration_service.conf"
  }
```
* **Discovery Service-uitvoeradapter**: Hiermee uploadt u gecrawlde documenten naar de Discovery Service van Watson Developer Cloud. Selecteer deze adapter door de parameter `class` en de sleutel `config` als volgt in te stellen:
```javascript
  class = "com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter"
  config = "discovery_service"
  discovery_service {
    include "discovery/discovery_service.conf"
  }
```
* **Watson Test-uitvoeradapter**: Schrijft een weergave van de gecrawlde bestanden naar schijf op een opgegeven locatie. Selecteer deze adapter door de parameter `class` en de sleutel `config` als volgt in te stellen:

**Opmerking** - Met een extra parameter, `output_directory`, selecteert u de directory waarin de weergave van de gecrawlde gegevens moet worden geschreven.
```javascript
  class = "com.ibm.watson.crawler.testoutputadapter.TestOutputAdapter"
  config = "test"
  output_directory = "/tmp/crawler-test-output"
```
* **retry** - Geeft de opties aan voor nieuwe pogingen als er mislukte pogingen zijn geweest om items naar de uitvoeradapter te pushen. 
  * max_attempts - Maximumaantal nieuwe pogingen. De standaardwaarde is `10`
  * delay - Minimale vertraging tussen pogingen, in seconden. De standaardwaarde is `2`
  * exponent_base - Factor die de groei van de vertragingstijd vaststelt met betrekking tot elke mislukte poging. De standaardwaarde is `2`

 De formule is:
```
 d(aantal_nieuwe_pogingen) = vertraging * (exponentbasis ^ aantal_nieuwe_pogingen)
```

 Als de vertraging bijvoorbeeld 1 seconde is bij een exponentbasis van 2, is de tweede nieuwe poging - de derde poging dus - 2 seconden vertraagd in plaats van 1, en de volgende is 4 seconden vertraagd.
 ```
 d(0) = 1 * (2 ^ 0) = 1 seconde
 d(1) = 1 * (2 ^ 1) = 2 seconden
 d(2) = 1 * (2 ^ 2) = 4 seconden
```
Met de standaardinstellingen wordt een ingezonden item tot maximaal tien keer opnieuw geprobeerd, en wordt er gewacht tot ongeveer 1.022 seconden (iets meer dan 17 minuten). Deze tijd is bij benadering aangegeven, omdat er extra tijd toegevoegd wordt om te vermijden dat meerdere nieuwe inzendingen gelijktijdig uitgevoerd worden. Deze extra tijd kan oplopen tot 10%, , waardoor de laatste nieuwe poging in het vorige voorbeeld een vertraging tot 4,4 seconden kan krijgen. De wachttijd is exclusief de tijd die is besteed aan het maken van verbinding met de service, het uploaden van gegevens, of het wachten op een antwoord.

 *Waarschuwing:* het verminderen van de wachttijd door het verlagen van een van deze standaardwaarden kan ertoe leiden dat documenten niet via de geconfigureerde uitvoeradapter worden geüpload. Bewijs hiervoor bij het gebruik van Watson Developer Cloud Services ziet u in de vorm van RetryFailure-berichten in het logboek waarbij een snelheidsbeperking vanwege "429 Too Many Requests" genoemd wordt. 
 
## Foutopsporingsopties
*  **full_node_debugging** - Hiermee activeert u de foutopsporingsmodus; mogelijke waarden zijn `true` of `false`. **Waarschuwing**: Hiermee worden de volledige gegevens van elk gecrawld document in logbestanden geplaatst.
*  **heartbeat_wait_time** - Tijdsinterval in milliseconden tussen opnamestatistieken voor rapportagedocumenten (alleen foutopsporingsmodus). De standaardwaarde is 1000 milliseconden.

## Opties voor logboekregistratie
*  **configuration_file** - Het configuratiebestand dat moet worden gebruikt voor logboekregistratie. In het voorbeeldbestand `crawler.conf` is deze optie gedefinieerd in `logging.log4j` en is de standaardwaarde ervan `log4j_custom.properties`.
Deze optie moet op soortgelijke wijze gedefinieerd worden - ofwel met een `.properties`-bestand of met een `.conf`-bestand.

## Aanvullende opties voor het beheren van crawls
*  **shutdown_timeout** - Hiermee geeft u de timeoutwaarde in minuten aan, voordat de toepassing wordt afgesloten. De standaardwaarde is `10`.
*  **output_limit** - Het hoogste aantal indexeerbare items dat de crawler probeert tegelijkertijd naar de uitvoeradapter te sturen. Dit aantal kan verder worden beperkt door het aantal kernen dat beschikbaar is om het werk uit te voeren. Het geeft aan dat er op een bepaald tijdstip niet meer dan "x" indexeerbare items die naar de uitvoeradapter zijn gezonden, wachten op retourzending. De standaardwaarde is `10`.
*  **input_limit** - Beperkt het aantal URL's dat in één keer kan worden aangevraagd vanaf de connector. De standaardwaarde is `3`.
*  **output_timeout** - Het aantal seconden voordat de Data Crawler een aanvraag voor de uitvoeradapter staakt en vervolgens het item uit de wachtrij van de uitvoeradapter verwijdert; hierdoor kan er meer verwerkt worden. De standaardwaarde is `1200`. **Opmerking** - Er dient aandacht te worden besteed aan de voorwaarden die door de uitvoeradapter opgelegd worden, aangezien deze voorwaarden betrekking kunnen hebben op de limieten die hier gedefinieerd zijn. De `output_limit` die hierboven is gedefinieerd, heeft alleen betrekking op de hoeveelheid indexeerbare objecten die tegelijk naar de uitvoeradapter kunnen worden verzonden. Als een indexeerbaar object eenmaal naar de uitvoeradapter is verzonden, wordt "de klok gezet" zoals gedefinieerd door de variabele `output_timeout`. Het kan zijn dat de uitvoeradapter zelf een snelheidsregeling heeft die voorkomt dat hij evenveel invoeritems verwerkt als dat hij ontvangt. De Orchestration Output Adapter kan bijvoorbeeld een verbindingspool hebben die geconfigureerd kan worden voor HTTP-verbindingen met de service. Als de standaardwaarde bijvoorbeeld 8 is en u de
`output_limit` instelt op een getal dat hoger is dan 8, zijn er processen op de klok die wachten op hun beurt om uitgevoerd te worden. U kunt dan timeouts krijgen.
*  **num_threads** - Het aantal parallelle threads dat tegelijk kan worden uitgevoerd. Deze waarde kan een geheel getal zijn dat het aantal parallelle threads rechtstreeks aangeeft, of een tekenreeks met de indeling "xNUM", die de vermenigvuldigingsfactor van het aantal beschikbare processors aangeeft, bijvoorbeeld "x1.5". De standaardwaarde is `"30"`.

## ZIE OOK

crawler(1)

vcrypt(1)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
