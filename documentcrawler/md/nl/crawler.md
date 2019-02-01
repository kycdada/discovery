crawler (1) - Een crawler voor het verplaatsen van gegevens van A naar B
====================================================================

## SYNOPSIS

Syntaxis: crawler [ crawl | testit | restart | resume | refresh | summary ][ options ]

## BESCHRIJVING

De Data Crawler wordt gebruikt voor het crawlen van verschillende repository's van gegevens, zoals contentbeheersystemen en bestandssystemen en om de resulterende documenten naar een service op afstand te pushen.

## ALGEMENE OPTIES

    --version
        De versie van het programma afbeelden
    --help
        Deze tekst over gebruik afbeelden

## OPDRACHTEN

### crawl [ opties ]

Hiermee wordt een crawl met de huidige configuratie uitgevoerd

    -c <waarde> | --config <waarde>  # Geeft het te gebruiken configuratiebestand aan. De standaardwaarde is "config/crawler.conf".
    --pii-checking <waarde>         # Schakelt controle van PII in/uit

### testit [ opties ]

Hiermee wordt een testcrawl uitgevoerd, waarbij alleen de seed-URL wordt gecrawld en de in de wachtrij geplaatste URL's worden afgebeeld. Als de seed-URL resulteert in indexeerbare content (bijvoorbeeld een document), wordt deze content verzonden naar de uitvoeradapter en wordt de content op het scherm afgebeeld. Als het ophalen van de seed-URL ertoe leidt dat URL's in de wachtrij geplaatst worden, worden deze URL's afgebeeld en wordt er geen content naar de uitvoeradapter verzonden. Standaard worden er vijf in de wachtrij geplaatste URL's afgebeeld.

    -c <waarde> | --config <waarde>  # Geef het te gebruiken configuratiebestand aan. De standaardwaarde is "config/crawler.conf".
    -l <n> | --limit <n>           # Begrenst het aantal in de wachtrij geplaatste URL's die afgebeeld worden.
    --pii-checking <waarde>         # Schakelt controle van PII in/uit

### restart [ opties ]

Hiermee voert u het starten van de crawl opnieuw uit; er wordt een nieuwe crawl met de huidige configuratie uitgevoerd.

    -c <waarde> | --config <waarde>  # Geeft het te gebruiken configuratiebestand aan.
    --pii-checking <waarde>         # Schakelt controle van PII in/uit

### resume [ opties ]

Hiermee wordt het crawlen hervat vanaf het punt waar deze was gestopt.

    -c <waarde> | --config <waarde>  # Geeft het te gebruiken configuratiebestand aan.
    --pii-checking <waarde>         # Schakelt controle van PII in/uit

### refresh [ opties ]

Hiermee vernieuwt u een eerdere crawl.

    -c <waarde> | --config <waarde>  # Geeft het te gebruiken configuratiebestand aan.
    --pii-checking <waarde>         # Schakelt controle van PII in/uit

### summary [ opties ]

Hiermee genereert u een crawlrapport.

    --submitted                    # Query op alle ingezonden documenten
    --processed                    # Query op alleen de documenten met geslaagde verwerking
    --failed                       # Query op alleen de documenten met mislukte verwerking
    --group-id <waarde>            # Query op de crawluitvoering voor een opgegeven groep. Een groep bestaat uit een eerste crawl en alle hervatte, vernieuwde, of opnieuw gestart items van de eerste crawl. Als de waarde niet is opgegeven, behelst deze query standaard de meest recente gecrawlde groep.
    --show-content                 # Hiermee beeldt u alle aanvullende content af die is gekoppeld aan een query
    --filter                       # Filtert het queryresultaat op URL en hashID

## VOORBEELDEN

Voer het crawlen uit met behulp van het configuratiebestand op `config/crawler.conf`:

    crawler crawl

Voer een test uit met behulp van het configuratiebestand op `config/crawler.conf`:

    crawler testit

Voer het crawlen uit met behulp van het configuratiebestand op `/home/watson/office-share.conf`:

    crawler crawl --config /home/watson/office-share.conf

Start het crawlen opnieuw met behulp van het configuratiebestand op `/home/watson/office-share.conf`:

    crawler restart --config /home/watson/office-share.conf

Haal overzichtsinformatie over mislukte documenten op met een groeps-ID van `2`

    crawler summary --failed --group-id 2 --show-content

Gebruik afbeelden, inclusief versie:

    crawler --help

## CONFIGURATIE

Voor opties van de `crawler` is een configuratiebestand vereist. Voorbeelden van configuratiebestanden vindt u in de directory `share` in de installatiedirectory van de `crawler`. Kopieer deze voorbeelden en wijzig ze. *Breng geen wijzigingen ter plekke in de voorbeelden aan.*

Als de optie `--config | -c` niet is opgegeven, kijkt de `crawler` voor zijn configuratie in de directory `config` van de directory waarin `crawler` gestart is. Dat wil zeggen:  `crawler` zoekt naar `config/crawler.conf`.

## DIAGNOSE

Met deze functies kunt u een diagnose maken van problemen.

### Fouten opsporen

Hiermee activeert u de foutopsporingswerkstand. Stel het volgende in het bestand `crawler.conf` in:

    debugging.full_node_debugging = true

### Logboekregistratie

Hiermee schakelt u logboekregistratie in. Stel het volgende in het bestand `log4j_custom.properties` in:

    log4j.rootLogger=INFO, Console, Log

Dit is het standaard logboekniveau voor de bestandsuitvoer. Voor het consolelogboek is de standaardwaarde:

    log4j.appender.Console.Threshold=WARN

Logboekniveaus kunnen worden ingesteld op de volgende waarden:

    OFF - Het hoogst mogelijke niveau, hiermee schakelt u logboekregistratie uit.
    FATAL - Geeft zeer ernstige foutevents aan die er waarschijnlijk toe leiden dat de toepassing  afgebroken wordt.
    ERROR - Geeft foutevents aan waarbij de toepassing nog voortgezet kan worden.
    WARN - Hiermee worden mogelijk schadelijke situaties aangegeven.
    INFO - Geeft informatieberichten aan over de voortgang van de toepassing op weinig gedetailleerd niveau.
    DEBUG - Geeft gedetailleerde informatieve events aan die relevant zijn om fouten op te sporen in een toepassing.
    TRACE - Geeft nog gedetailleerdere informatieve events aan dan bij DEBUG.
    ALL - Het laagst mogelijke niveau, hiermee schakelt u alle logboekregistraties in.

## VERSNELLING/VERTRAGING

Hiermee definieert u beperkingen in grootte, voor het beheren van de doorvoer. Stel het volgende in het bestand `crawler.conf` in:

`shutdown_timeout` Hier geeft u de timeoutwaarde in minuten aan, voordat de toepassing wordt afgesloten; de standaardwaarde is 10

    shutdown_timeout = <n>

`output_limit` is het grootste aantal indexeerbare items die de draagbare crawler tegelijkertijd naar de uitvoeradapter stuurt, waarna retourzending wordt afgewacht; de standaardwaarde is 10. Dit aantal kan verder worden beperkt door het aantal kernen dat beschikbaar is om het werk uit te voeren.

    output_limit = <n>

`input_limit` Beperkt het aantal URL's dat in één keer kan worden aangevraagd vanaf de connector; de standaardwaarde is 3.

    input_limit = <n>

`output_timeout` is het aantal seconden voordat de draagbare crawler een aanvraag voor de uitvoeradapter staakt en vervolgens het item uit de limietwachtrij verwijdert; hierdoor kan er meer verwerkt worden. De standaardwaarde is 150.

    output_timeout = <n>

Er dient aandacht te worden besteed aan de voorwaarden die door de uitvoeradapter opgelegd worden, aangezien deze voorwaarden betrekking kunnen hebben op de limieten die hier gedefinieerd zijn. De `output_limit` die hierboven is gedefinieerd, heeft alleen betrekking op de hoeveelheid indexeerbare objecten die tegelijk naar de uitvoeradapter kunnen worden verzonden. Als een indexeerbaar object eenmaal naar de uitvoeradapter is verzonden, wordt "de klok gezet" zoals gedefinieerd door de variabele `output_timeout`. Het kan zijn dat de uitvoeradapter zelf een snelheidsregeling heeft die voorkomt dat hij evenveel invoeritems verwerkt als dat hij ontvangt.
De Orchestration Output Adapter kan bijvoorbeeld een verbindingspool hebben die geconfigureerd kan worden voor HTTP-verbindingen met de service. Als de standaardwaarde bijvoorbeeld 8 is en u de
`output_limit` instelt op een getal dat hoger is dan geconfigureerd voor die verbindingspool, zijn er processen op de klok die wachten op hun beurt om uitgevoerd te worden.
U kunt dan timeouts krijgen.

`num_threads` Het aantal parallelle threads dat tegelijk kan worden uitgevoerd. Deze waarde kan een geheel getal zijn dat het aantal parallelle threads rechtstreeks aangeeft, of een tekenreeks met de indeling `"xNUM"`, die de vermenigvuldigingsfactor van het aantal beschikbare processors aangeeft. De standaardwaarde is "x1.5", oftewel 1,5 keer het aantal beschikbare processors (op basis van `Runtime.availableProcessors`).

    num_threads = <n>

De formule voor het berekenen van de parallelle verwerking in de Data Crawler-pool is: `min(maxThreads, max(minThreads, numThreads))`.

## OMGEVINGSVARIABELE `CRAWLER_OPTS` 

Hieronder vindt u eigenschappen die kunnen worden doorgegeven aan `crawler` via de omgevingsvariabele `CRAWLER_OPTS`, samen met standaardwaarden.

Geef deze als volgt door:

    CRAWLER_OPTS="-Dproperty=waarde -Dproperty=waarde" crawler

Deze mag alleen worden gewijzigd voor het opsporen van fouten en alleen op verzoek van IBM Support.

### cfa.java_bin

`cfa.java_bin` kan de `java`-opdracht wijzigen die wordt gebruikt voor het starten van de Connector Framework Input Adapter. Standaard gebruikt `crawler` hetzelfde `java`-programma dat wordt gebruikt voor het starten van de `crawler` zelf.

Dit kan ook worden gewijzigd door de eigenschap `java.home` in te stellen; deze eigenschap kan daarna worden gebruikt voor het berekenen van het pad naar het uitvoerbare `java`-bestand.

### cfa.lib_dir

`cfa.lib_dir` wijzigt het pad naar de directory `lib` van het Connector Framework. Normaal gesproken hoeft dit slechts zelden te worden gewijzigd. Standaard gebruikt `crawler` de directory `lib` binnen het berekende pad naar het Connector Framework, in het algemeen simpelweg `connectorFramework`.

### cfa.framework_jars_dir

`cfa.framework_jars_dir` wijzigt het pad naar de jars-directory van het Connector Framework dat zich standaard bevindt in `connectorFramework/<version>/lib/java`.

### cfa.plugins_dir

`cfa.plugins_dir` geeft het pad aan naar de plugins-directory van het Connector Framework, waarin de feitelijke connectors zijn opgeslagen.
Standaard wordt dit opgebouwd vanuit de `framework_jars_dir` en is het `connectorFramework/<version>/lib/java/plugins`.

## BEKENDE BEPERKINGEN

Hier vindt u bekende beperkingen in de huidige release van de Data Crawler

* De Data Crawler kan vastlopen bij het uitvoeren van de connector voor het bestandssysteem met een ongeldige of ontbrekende URL.
* Configureer de waarde `urls_to_filter` in het bestand `config/crawler.con` zodanig dat alle URL's of RegExes in de goedgekeurde lijst worden opgenomen in een enkele RegEx-expressie.
* Het pad naar het configuratiebestand dat wordt doorgegeven aan de optie `--config | -c` moet een gekwalificeerd pad zijn. Dit betekent dat het de relatieve indelingen `config/crawler.conf` of `./crawler.conf` moet hebben, of het absolute pad `/path/to/config/crawler.conf`. Het opgeven van alleen `crawler.conf` is alleen mogelijk als bestanden waarnaar wordt verwezen met behulp van `include` in het bestand `crawler.conf` inline worden gezet in plaats van `include` te gebruiken. Bijvoorbeeld: `discovery/discovery_service.conf` is met een `include` opgenomen om de configuratie eenvoudiger te kunnen lezen. De content moet worden gekopieerd naar `crawler.conf` in de sleutel `output_adapter.discovery_service` om een niet-gekwalificeerde pad in de optie config te kunnen gebruiken.

## WIJZIGINGSLOGBOEK

Raadpleeg het bestand `changelog.txt` in uw installatiedirectory voor een lijst met wijzigingen in deze release.

## AUTEUR

IBM Watson - https://www.ibm.com/smarterplanet/us/en/ibmwatson/

Gemaakt door yinz in Pittsburgh.

## ZIE OOK

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
