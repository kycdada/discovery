crawler(1) - Ein Crawler zum Verschieben von Daten von Punkt A nach Punkt B
====================================================================

## Übersicht

Verwendung: crawler [ crawl | testit | restart | resume | refresh | summary ][ options ]

## Beschreibung

Data Crawler wird verwendet, um verschiedene Datenrepositorys wie Content-Management-Systeme und Dateisysteme zu durchsuchen und anschließend die Ergebnisdokumente mit der Push-Operation an einen fernen Service zu übertragen.

## Globale Optionen

    --version
        Anzeigen der Programmversion
    --help
        Anzeigen dieses Texts zur Verwendung

## Befehle

### crawl [ optionen ]

Führt eine Crawlersuche mit der aktuellen Konfiguration durch.

    -c <wert> | --config <wert>    # Gibt die zu verwendende Konfigurationsdatei an. Standardwert: "config/crawler.conf".
    --pii-checking <wert>          # Aktivieren/Inaktvieren der PII-Überprüfung

### testit [ optionen ]

Führt einen Test der Crawlersuche durch, der nur die Seed-URL durchsucht und alle eingereihten URLs anzeigt. Falls die Seed-URL zu einem indexierbaren Inhalt führt, (z.B. ein Dokument), dann wird der Inhalt an den Ausgabeadapter gesendet und am Bildschirm angezeigt. Falls die Abfrage der Seed-URL dazu führt, dass URLs eingereiht werden, dann werden diese URLs angezeigt und es wird kein Inhalt an den Ausgabeadapter gesendet. Standardmäßig werden fünf eingereihte URLs angezeigt. 

    -c <wert> | --config <wert>    # Gibt die zu verwendende Konfigurationsdatei an. Standardwert: "config/crawler.conf".
    -l <n> | --limit <n>           # Begrenzt die Anzahl der eingereihten URLs, die angezeigt werden.
    --pii-checking <wert>          # Aktivieren/Inaktvieren der PII-Überprüfung

### restart [ optionen ]

Führt eine Crawlersuche erneut aus; startet eine neue Crawlersuche mit der aktuellen Konfiguration.

    -c <wert> | --config <wert>    # Gibt die zu verwendende Konfigurationsdatei an.
    --pii-checking <wert>          # Aktivieren/Inaktvieren der PII-Überprüfung

### resume [ optionen ]

Nimmt eine Crawlersuche an dem Punkt wieder auf, an dem sie stoppte.

    -c <wert> | --config <wert>    # Gibt die zu verwendende Konfigurationsdatei an.
    --pii-checking <wert>          # Aktivieren/Inaktvieren der PII-Überprüfung

### refresh [ optionen ]

Aktualisiert eine vorherige Crawlersuche.

    -c <wert> | --config <wert>    # Gibt die zu verwendende Konfigurationsdatei an.
    --pii-checking <wert>          # Aktivieren/Inaktvieren der PII-Überprüfung

### summary [ optionen ]

Generiert einen Crawlersuchbericht.

    --submitted                    # Fragt alle übergebenen Dokumente ab.
    --processed                    # Fragt nur die Dokumente ab, die erfolgreich verarbeitet wurden.
    --failed                       # Fragt nur die Dokumente ab, die nicht erfolgreich verarbeitet wurden.
    --group-id <value>             # Fragt die Ausführung der Crawlersuche für eine bestimmte Gruppe ab. Eine Gruppe besteht aus einer Anfangssuche und allen wiederaufgenommenen, aktualisierten oder neu gestarteten Crawlersuchen dieser Anfangssuche. Falls kein Wert angegeben wird, wird für diese Abfrage standardmäßig die aktuellste Gruppe durchsucht.
    --show-content                 # Zeigt allen zusätzlichen Inhalt an, der einer Abfrage zugeordnet ist.
    --filter                       # Filtert dieses Abfrageergebnis auf der URL und hashID.

## Beispiele

Führt eine Crawlersuche mithilfe der Konfigurationsdatei unter `config/crawler.conf` aus:

    crawler crawl

Führt einen Test aus, bei dem die Konfigurationsdatei unter `config/crawler.conf` verwendet wird:

    crawler testit

Führt eine Crawlersuche mit der Konfigurationsdatei unter `/home/watson/office-share.conf` aus:

    crawler crawl --config /home/watson/office-share.conf

Startet eine Crawlersuche mit der Konfigurationsdatei unter `/home/watson/office-share.conf`:

    crawler restart --config /home/watson/office-share.conf

Ruft Ergebnistexte für fehlgeschlagene Dokumente mit der Gruppen-ID `2` ab:

    crawler summary --failed --group-id 2 --show-content

Zeigt die Verwendung einschließlich der Version an:

    crawler --help

## KONFIGURATION

`crawler` erfordert eine Konfigurationsdatei für seine Optionen. Beispiele für Konfigurationsdateien stehen im Verzeichnis `share` im Installationsverzeichnis von `crawler` zur Verfügung. Kopieren Sie diese Beispiele und ändern Sie sie. *Ändern Sie nicht die Beispiele selbst!*

Ohne die Angabe der Option `--config | -c` sucht `crawler` im Verzeichnis `config` des Verzeichnisses, in dem `crawler` gestartet wurde, nach seiner Konfiguration. Das heißt, `crawler` sucht nach `config/crawler.conf`.

## Diagnose

Verwenden Sie diese Komponenten, um Probleme zu diagnostizieren. 

### Fehlerbehebung

Aktiviert den Debugmodus. Legen Sie in der Datei `crawler.conf` Folgendes fest:

    debugging.full_node_debugging = true

### Protokollierung

Aktiviert die Protokollierung. Legen Sie in der Datei `log4j_custom.properties` Folgendes fest:

    log4j.rootLogger=INFO, Console, Log

Dies ist die Standardprotokollierungsstufe für die Dateiausgabe. Für das Konsolenprotokoll lautet der Standard: 

    log4j.appender.Console.Threshold=WARN

Für Protokollebenen können die folgenden Werte festgelegt werden:

    OFF - Die höchstmögliche Ebene, diese ist zum Abschalten der Protokollierung gedacht.
    FATAL - Kennzeichnet sehr schwerwiegender Fehlerereignisse, die vermutlich zu einem Abbruch der Anwendung führen.
    ERROR - Kennzeichnet Fehlerereignisse, bei denen die Anwendung weiter ausgeführt werden kann.
    WARN - Kennzeichnet möglicherweise schädliche Situationen.
    INFO - Kennzeichnet Informationsnachrichten, die den Fortschritt der Anwendung auf einer allgemeinen Ebene hervorheben.
    DEBUG - Kennzeichnet differenzierte Informationsereignisse, die bei der Fehlerbehebung bei Anwendungen hilfreich sind.
    TRACE - Kennzeichnet differenziertere Informationsereignisse als DEBUG.
    ALL - Die niedrigste Ebene, die zum Einschalten der Protokollierung gedacht ist.

## Regulierung

Definiert Dimensionierungsbegrenzungen, die bei der Verwaltung des Durchsatzes helfen. Legen Sie in der Datei `crawler.conf` Folgendes fest: 

`shutdown_timeout` Gibt den Zeitlimitwert in Minuten an, bevor die Anwendung heruntergefahren wird. Der Standardwert lautet 10. 

    shutdown_timeout = <n>

`output_limit` ist die höchste Zahl der indexierbaren Elemente, die der portierbare Crawler gleichzeitig an den Ausgabeadapter in Erwartung einer Antwort sendet. Der Standardwert lautet 10. Dieser Wert kann weiter durch zentrale Bestandteile begrenzt werden, die für die Ausführung von Arbeiten verfügbar sind. 

    output_limit = <n>

`input_limit` Begrenzt die Anzahl der URLs, die zu einem Zeitpunkt angefordert werden können. Der Standardwert lautet 3. 

    input_limit = <n>

`output_timeout` Dies ist die Zeitdauer in Sekunden, bevor der portierbare Crawler bei einer Anforderung an den Ausgabeadapter aufgibt und anschließend das Element aus der  Begrenzungswarteschlange entfernt, um die Verarbeitung fortsetzen zu können. Der Standardwert lautet 150.

    output_timeout = <n>

Den Beschränkungen, die durch den Ausgabeadapter bestehen, sollte Beachtung geschenkt werden, da diese Beschränkungen mit den hier definierten Begrenzungen zusammenhängen könnten. Das oben definierte `output_limit` bezieht sich nur auf die Anzahl der indexierbaren Objekte, die gleichzeitig an den Ausgabeadapter gesendet werden können. Sobald ein indexierbares Objekt an den Ausgabeadapter gesendet wird, ist es wie in der Variablen `output_timeout` definiert gezählt worden. Es ist möglich, dass der Ausgabeadapter selbst über eine Drosselung verfügt, die es verhindert, dass er so viele Eingaben verarbeitet, wie er empfängt. Die Orchestrierungsausgabeadapter können über einen Verbindungspool verfügen, der für HTTP-Verbindungen zum Service konfigurierbar ist. Wenn dieser zum Beispiel den Standardwert 8 annimmt und wenn Sie für `output_limit` eine Zahl definiert haben, die über der für diesen Verbindungspool konfigurierten Zahl liegt, dann werden Sie (gezählte) Prozesse haben, die auf ihre Ausführung warten. In diesem Fall kann es zu Zeitlimitüberschreitungen kommen. 

`num_threads` Die Anzahl der parallelen Threads, die gleichzeitig ausgeführt werden können. Dieser Wert kann entweder eine ganze Zahl sein, die die Anzahl der parallelen Threads direkt angibt, oder es kann eine Zeichenfolge mit dem Format `"xNUM"` sein, die den Multiplikationsfaktor der Anzahl der verfügbaren Prozessoren angibt. Der Standardwert lautet "x1.5" oder 1,5 x die Anzahl der verfügbaren Prozessoren (die mit `Runtime.availableProcessors` erfasst wurde).

    num_threads = <n>

Die Formel für die Berechnung der Parallelität im Data Crawler-Pool lautet: `min(maxThreads, max(minThreads, numThreads))`.

## Umgebungsvariable `CRAWLER_OPTS` 

Folgende Eigenschaften können an `crawler` mithilfe der Umgebungsvariable `CRAWLER_OPTS` übergeben werden. Sie werden hier mit Standardwerten aufgelistet.

Übergeben Sie diese wie folgt:

    CRAWLER_OPTS="-Dproperty=value -Dproperty=value" crawler

Sie sollten nur für die Fehlerbehebung geändert werden und ausschließlich auf Anweisung von IBM Support.

### cfa.java_bin

`cfa.java_bin` kann den Befehl `java` ändern, der für den Start des Eingabeadapters des Connector-Frameworks verwendet wird. Standardmäßig verwendet `crawler` dieselbe `java`-Binärdatei, die auch für den Start von `crawler` selbst verwendet wird.

Dies kann auch durch Festlegen der Eigenschaft `java.home` geändert werden, die dann verwendet wird, um den Pfad zur ausführbaren `java`-Datei zu berechnen. 

### cfa.lib_dir

`cfa.lib_dir` ändert den Pfad zum Verzeichnis `lib` von Connector-Framework. Diese Änderung sollte sehr selten vorzunehmen sein. Standardmäßig verwendet `crawler` das Verzeichnis `lib` innerhalb des berechneten Pfades zum Connector-Framework. In der Regel ist dies einfach `connectorFramework`.

### cfa.framework_jars_dir

`cfa.framework_jars_dir` ändert den Pfad zum jar-Verzeichnis von Connector-Framework, das sich standardmäßig im Verzeichnis `connectorFramework/<version>/lib/java` befindet.

### cfa.plugins_dir

`cfa.plugins_dir` gibt den Pfad zum Plugins-Verzeichnis des Connector-Frameworks an, in dem die tatsächlichen Konnectoren gespeichert sind.
Standardmäßig wird dieser Pfad vom Verzeichnis `framework_jars_dir` erstellt und lautet `connectorFramework/<version>/lib/java/plugins`.

## Bekannte Einschränkungen

Details zu bekannten Einschränkungen im aktuellen Release von Data Crawler

* Data Crawler kann blockieren, wenn der Dateistystemkonnektor mit einer ungültigen oder fehlenden URL ausgeführt wird.
* Konfigurieren Sie den Wert `urls_to_filter` in der Datei `config/crawler.conf`, so dass alle Whitelist-URLs oder RegExes in einem einzigen RegEx-Ausdruck enthalten sind.
* Der Pfad zur Konfigurationsdatei, der in der Option `--config | -c` übergeben wurde, muss ein qualifizierter Pfad sein. Das heißt, er muss sich in den relativen Formaten `config/crawler.conf` oder `./crawler.conf` oder dem absoluten Pfad `/path/to/config/crawler.conf` befinden. Die alleinige Angabe von `crawler.conf` ist möglich, aber nur dann, wenn die mithilfe von `include` in der Datei `crawler.conf` referenzierten Dateien integriert (in-lined) und nicht mit `include` einbezogen wurden. So wurde zum Beispiel `discovery/discovery_service.conf` mit `include` einbezogen, um das Lesen der Konfiguration zu vereinfachen. Der zugehörige Inhalt muss in `crawler.conf` innerhalb des Schlüssels `output_adapter.discovery_service` kopiert werden, um einen nicht qualifizierten Pfad in der Konfigurationsoption verwenden zu können. 

## Änderungsprotokoll

Eine Liste mit Änderungen in diesem Release finden Sie in der Datei `changelog.txt` in Ihrem Installationsverzeichnis. 

## Autor

IBM Watson - https://www.ibm.com/smarterplanet/us/en/ibmwatson/

Made by yinz in Pittsburgh.

## Weitere Informationen

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
