# Data Crawler konfigurieren

`crawler` erfordert eine Konfigurationsdatei für seine Optionen. Beispiele für Konfigurationsdateien stehen im Verzeichnis `share` im Installationsverzeichnis von `crawler`zur Verfügung. Kopieren Sie diese Beispiele und ändern Sie sie. *Ändern Sie nicht die Beispiele selbst!*

Die Datei `crawler.conf` enthält Informationen, die dem Crawler mitteilen, welche Dateien er für seinen Suchlauf verwenden soll (Eingabeadapter), wohin die Zusammenstellung von Dateien der Crawlersuche gesendet werden soll, sobald der Suchlauf abgeschlossen ist (Ausgabeadapter), und weitere Verwaltungsoptionen der Crawlersuche. 

**Hinweis**: Alle Dateipfade sind relativ zum Verzeichnis `config`, sofern nichts anderes angegeben ist.

Die Optionen, die in dieser Datei definiert werden können, sind: 

## Eingabeadapter
*  **class** - Nur zur internen Verwendung. Definiert die Eingabeadapterklasse von Data Crawler. Der Standardwert lautet: `com.ibm.watson.crawler.connectorframeworkinputadapter.Crawl`.
*  **config** - Nur zur internen Verwendung. Definiert die Konfiguration von Connector-Framework. Der Standardkonfigurationsschlüssel innerhalb dieses Blocks zum Übergeben des ausgewählten Eingabeadapters lautet: `connector_framework`. **Hinweis** - Das Connector-Framework ermöglicht Ihnen, mit Ihren Daten zu "sprechen". Es können interne Daten innerhalb des Unternehmens oder externe Daten im Web oder in der Cloud sein. Die Konnectoren ermöglichen Zugriff auf eine Reihe von unterschiedlichen Datenquellen, während die Verbindung tatsächlich durch den Prozess der Crawlersuche gesteuert wird. 
  -  **WICHTIG** - Daten, die vom Eingabeadapter das Connector-Frameworks abgerufen werden, werden lokal im Cache gespeichert. Die Daten werden nicht verschlüsselt gespeichert. Die Daten werden standardmäßig in einem temporären Verzeichnis zwischengespeichert, das beim Warmstart bereinigt werden sollte. Die Daten sollten nur von dem Benutzer gelesen werden können, der den crawler-Befehl ausgeführt hat. Es besteht die Möglichkeit, dass dieses Verzeichnis den Crawler überdauert, falls das Connector-Framework verschwindet, bevor es sich selbst bereinigen kann. Denken Sie daher sorgfältig über die Position Ihrer zwischengespeicherten Daten nach. Sie können sie in ein verschlüsseltes Dateisystem stellen. Dabei sind jedoch Auswirkung auf die Leistung zu bedenken. Nur Sie können die Entscheidung über die richtige Balance zwischen Geschwindigkeit und Sicherheit für Ihre Crawlersuchen treffen.
*  **crawl_config_file** - Die Konfigurationsdatei für die Crawlersuche. Der Standardwert lautet: `connectors/filesystem.conf`.
*  **crawl_seed_file** - Die Seeddatei für die Crawlersuche. Der Standardwert lautet: `seeds/filesystem-seed.conf`.
*  **id_vcrypt_file** - Die Schlüsseldatei, die für die Datenverschlüsselung durch den Crawler verwendet wird. Der Standardschlüssel für den Crawler lautet `id_vcrypt`.
Verwenden Sie das Script im Ordner `bin`, wenn Sie eine neue Datei 'id_vcrypt_file' generieren müssen.
*  **crawler_temp_dir** - Der temporärer Ordner des Crawlers für Konnektorprotokolle. Der Standardwert `tmp` wird bereitgestellt. Wenn der Ordner `tmp` noch nicht vorhanden ist, wird er im aktuellen Arbeitsverzeichnis erstellt. 
*  **extra_jars_dir** - Nur zur internen Verwendung. Fügt weitere JARs zum Klassenpfad des Connector-Frameworks hinzu.
Dieser Wert muss `oakland` lauten, wenn er den SharePoint-Konnektor verwendet, und `database`, wenn er den Datenbankconnector verwendet. Sie können diesen Wert leer lassen, (z. B. eine leere Zeichenfolge "" angeben), wenn Sie andere Konnectoren verwenden. **Hinweis**: Relativ zum Verzeichnis `lib/java` des Connector-Frameworks. 
*  **urls_to_filter** - Durch einen Zeilenumbruch getrennte Whitelist von URLs für die Crawlersuche in Form von regulären Ausdrücken. Data Crawler durchsucht nur URLs, die einem der bereitgestellten regulären Ausdrücke entsprechen. Die Domänenliste enthält die häufigsten Domänen der höchsten Ebene (Top-Level Domains). Fügen Sie bei Bedarf weitere hinzu. Die Liste der Dateierweiterungstypen enthält die Dateierweiterungen, die der Orchestration Service in diesem Release von Data Crawler unterstützt. Stellen Sie sicher, dass Ihre Seed-URL-Domäne vom Filter zugelassen wird. Falls die Seed-URL zum Beispiel `http://testdomain.test.in` lautet, fügen Sie im Domänenfilter "`in`" hinzu. Stellen Sie sicher, dass Ihre Seed-URL nicht von einem Filter ausgeschlossen wird, da der Crawler sonst blockiert. 
*  **max_text_size** - Die maximale Größe (in Byte), die ein Dokument annehmen kann, bevor es vom Connector-Framework auf die Platte geschrieben wird. Die Anpassung mit einem höheren Wert führt dazu, dass weniger Dokumente auf die Platte geschrieben werden. Dabei erhöht sich jedoch der Speicherbedarf. 
*  **extra_vm_params** - Ermöglicht Ihnen weitere Java-Parameter zu dem Befehl hinzuzufügen, der das Connector-Framework startet. 
*  **bootstrap_logging** - Schreibt das Startprotokoll von Connector-Framework. Diese Option ist nur für die professionelle Fehlerbehebung sinnvoll. Die Werte lauten `true` oder `false`. Die Protokolldatei wird in das Verzeichnis `crawler_temp_dir` geschrieben.

## Speicheradapter

Ermöglicht das Speichern interner Status der Crawlersuche in einer Datenbank. Diese Einstellung ist für die Optionen `restart` und `resume` der Crawlersuche notwendig, damit diese korrekt funktionieren. 

```javascript
storage_adapter {
 config = "storage_in_db"
  storage_in_db {
    include "storage/database_storage.conf"
  } 
}
```
Die referenzierte Datei `storage/database_storage.conf` verwendet standardmäßig eine H2-Datenbank. Sie können eine beliebige Datenbank anstelle der bereitgestellten Standardwerte mit einem JDBC-Treiber verwenden. Lesen Sie die Dokumentation zu Ihrem JDBC-Treiber, um spezifische Informationen über einige dieser Einstellungen herauszufinden. Die Standardoptionen können direkt durch Öffnen der Datei `config/storage/database_storage.conf` und Ändern der folgenden anwendungsfallspezifischen Werte geändert werden:

*  **class** - Diese Klasse zeigt auf die zu verwendende Datenbankadapterklasse. Der Standardwert lautet `com.ibm.watson.crawler.storageadapters.DatabasePersistAdapter`.
*  **driver** - Die Klasse für den JDBC-Treiber. Der Standardwert lautet `org.h2.Driver` für die Verwendung von H2.
*  **url** - Verwenden Sie die JDBC-Optionen für Ihren Treiber. Dies ist das URL-Präfix für die JDBC-Verbindungszeichenfolge. Der Standardwert lautet: `jdbc:h2:file:`
*  **database_location** - Die Position, an der Ihre Datenbank sich befinden soll. Dies gilt nur für dateibasierte Datenbanken wie 'sqlite' und H2. Der Standardwert lautet: `./storage/database`
*  **database_name** - Der Name der Datenbank. Der Standardwert lautet `ActivityDB`
*  **table_name** - Der Name der zu verwendenden Tabelle. Der Standardwert lautet: `Ledger`
*  **username** - Der Benutzername für die Verbindung zur Datenbank.
*  **password** - Das Kennwort für die Verbindung zur Datenbank.

Die Standardkonfiguration ist für die meisten Aktivitäten ausreichend. 

## Ausgabeadapter

Es gibt eine Reihe von *Ausgabeadaptern* aus denen Sie auswählen können. Legen Sie den Ausgabeadapter durch die Definition von `output_adapter.class`
in `crawler.conf` fest. Die Optionen sind: 

*  **class** - Definiert die Ausgabeadapterklasse von Data Crawler. Der Standardwert lautet: `com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter`
*  **config** - Definiert, welcher Konfigurationsschlüssel an den Ausgabeadapter übergeben werden soll. Die Zeichenfolge muss einem Schlüssel innerhalb des Konfigurationsobjekts entsprechen. Es folgt ein Codebeispiel: 
```javascript
  orchestration_service {
    include "orchestration_service.conf"
  },
  test {
    output_directory = "/tmp/crawler-test-output"
  }
}
```
In diesem Beispiel lautet der Konfigurationsschlüssel `orchestration_service`. Der Standardwert lautet `discovery_service`.

Sie müssen einen Ausgabeadapter auswählen, indem Sie seinen Klassenparameter `class` und seinen Konfigurationsschlüssel `config` angeben. 

* **Orchestration Service-Ausgabeadapter**: Lädt durchsuchte Dokumente auf den Orchestration Service der Watson Developer Cloud hoch. Wählen Sie diesen Adapter aus, indem Sie für den Parameter `class` und den Schlüssel `config` Folgendes festlegen:  
```javascript
  class = "com.ibm.watson.crawler.orchestrationserviceoutputadapter.oneatatime.OrchestrationServiceOutputAdapter"
  config = "orchestration_service"
  orchestration_service {
    include "orchestration/orchestration_service.conf"
  }
```
* **Discovery Service-Ausgabeadapter**: Lädt durchsuchte Dokumente auf den Discovery Service der Watson Developer Cloud hoch. Wählen Sie diesen Adapter aus, indem Sie für den Parameter `class` und den Schlüssel `config` Folgendes festlegen: 
```javascript
  class = "com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter"
  config = "discovery_service"
  discovery_service {
    include "discovery/discovery_service.conf"
  }
```
* **Watson Test-Ausgabeadapter**: Schreibt eine Darstellung der durchsuchten Dateien an eine bestimmte Position. Wählen Sie diesen Adapter aus, indem Sie für den Parameter `class` und den Schlüssel `config` Folgendes festlegen: 

**Hinweis** - Ein weiterer Parameter, `output_directory`, wählt das Verzeichnis, in das die Darstellung der durchsuchten Daten geschrieben werden soll. 
```javascript
  class = "com.ibm.watson.crawler.testoutputadapter.TestOutputAdapter"
  config = "test"
  output_directory = "/tmp/crawler-test-output"
```
* **retry** - Gibt die Optionen zum Wiederholen für den Fall eines fehlgeschlagenen Versuchs, den Ausgabeadapter mit einer Push-Operation zu übertragen, an. 
  * max_attempts - Maximale Anzahl der Wiederholungsversuche. Der Standardwert lautet: `10`
  * delay - Mindestdauer der Verzögerung zwischen den Versuchen in Sekunden. Der Standardwert lautet: `2`
  * exponent_base - Faktor, der das Wachstum der Verzögerungszeit bei jedem fehlgeschlagenen Versuch bestimmt. Der Standardwert lautet: `2`

 Die Formel lautet: 
```
 d(nth_retry) = delay * (exponent_base ^ nth_retry)
```

 Die Einstellung mit einer Verzögerung von 1 Sekunde und einem Exponenten mit der Basis 2, führt dazu, dass die zweite Wiederholung bzw.. der dritte Versuch insgesamt, mit einer Verzögerung von 2 Sekunden anstatt mit einer Verzögerung von 1 Sekunde erfolgt. Der nächste Versuch erfolgt dann mit einer Verzögerung von 4 Sekunden. 
 ```
 d(0) = 1 * (2 ^ 0) = 1 second
 d(1) = 1 * (2 ^ 1) = 2 seconds
 d(2) = 1 * (2 ^ 2) = 4 seconds
```
 Auf diese Weise wird mit den Standardeinstellungen eine Übermittlung bis zu 10 Mal versucht, wobei ungefähr 1022 Sekunden (etwas über 17 Minuten) lang gewartet wird. Die Angabe dieser Zeitdauer kann nur näherungsweise berechnet werden, da weitere Wartezeit hinzugefügt wird, um zu vermeiden, dass mehrere erneute Übergaben gleichzeitig ausgeführt werde. Diese variable Zeitdauer beträgt bis zu 10%, so dass der letzte Versuch im vorherigen Beispiel eine Verzögerung von bis zu 4,4 Sekunden aufweisen kann. Die Wartezeit umfasst nicht die Zeit, die zum Verbinden mit dem Service, zum Hochladen von Daten oder zum Warten auf eine Antwort benötigt wird.
 *Warnung:* Das Verringern der Wartezeit durch Reduzierung einer dieser Standardwerte kann dazu führen, dass Dokumente über den konfigurierten Ausgabeadapter nicht erfolgreich hochgeladen werden. Ein Hinweis darauf ist es, wenn bei der Verwendung von Watson Developer Cloud-Services RetryFailure-Nachrichten im Protokoll mit "429 Too Many Requests" auf das Überschreiten der Begrenzung hinweisen. 
 
## Debugoptionen
*  **full_node_debugging** - Aktiviert den Debugmodus. Mögliche Werte sind: `true` oder `false` **Warnung**: Damit werden die vollständigen Daten jedes durchsuchten Dokuments in die Protokolle gestellt. 
*  **heartbeat_wait_time** - Zeitintervall in Millisekunden zwischen dem Berichten der Dokumentaufnahmestatistik (nur im Debugmodus). Der Standardwert lautet: 

## Protokollierungsoptionen
*  **configuration_file** - Die Konfigurationsdatei für die Protokollierung. In der Beispieldatei `crawler.conf` ist diese Option in `logging.log4j` definiert und der zugehörige Standardwert lautet `log4j_custom.properties`.
Diese Option muss bei Verwendung einer `.properties`-Datei oder einer `.conf`-Datei auf ähnliche Weise definiert werden. 

## Weitere Verwaltungsoptionen der Crawlersuche
*  **shutdown_timeout** - Gibt das Zeitlimit bei Systemabschluss der Anwendung in Minuten an. Der Standardwert lautet `10`.
*  **output_limit** - Die höchste Zahl der indexierbaren Elemente, die der Crawler gleichzeitig an den Ausgabeadapter sendet. Dieser Wert kann weiter durch die Anzahl zentraler Bestandteile begrenzt werden, die für die Ausführung von Arbeiten verfügbar sind. Es heißt, dass zu jedem beliebigen Zeitpunkt nicht mehr als "x" indexierbare Elemente an den Ausgabeadapter gesendet werden und auf die Rückgabe warten. Der Standardwert lautet `10`.
*  **input_limit** - Begrenzt die Anzahl der URLs, die zu einem Zeitpunkt angefordert werden können. Der Standardwert lautet `3`.
*  **output_timeout** - Die Zeitdauer in Sekunden, bevor der Data Crawler bei einer Anforderung an den Ausgabeadapter aufgibt und anschließend das Element aus der Warteschlange des Ausgabeadapters entfernt, um die weitere Verarbeitung fortsetzen zu können. Der Standardwert lautet `1200`. **Hinweis** - Den Beschränkungen, die durch den Ausgabeadapter bestehen, sollte Beachtung geschenkt werden, da diese Beschränkungen mit den hier definierten Begrenzungen zusammenhängen könnten. Das oben definierte `output_limit` bezieht sich nur auf die Anzahl der indexierbaren Objekte, die gleichzeitig an den Ausgabeadapter gesendet werden können. Sobald ein indexierbares Objekt an den Ausgabeadapter gesendet wird, ist es wie in der Variablen `output_timeout` definiert gezählt worden. Es ist möglich, dass der Ausgabeadapter selbst über eine Drosselung verfügt, die es verhindert, dass er so viele Eingaben verarbeitet, wie er empfängt. Die Orchestrierungsausgabeadapter können über einen Verbindungspool verfügen, der für HTTP-Verbindungen zum Service konfigurierbar ist. Wenn dieser zum Beispiel den Standardwert 8 annimmt und wenn Sie für `output_limit` eine Zahl definiert haben, die größer als 8 ist, dann werden Sie (gezählte) Prozesse haben, die auf ihre Ausführung warten. In diesem Fall kann es zu Zeitlimitüberschreitungen kommen. 
*  **num_threads** - Die Anzahl der parallelen Threads, die gleichzeitig ausgeführt werden können. Dieser Wert kann entweder eine ganze Zahl sein, die die Anzahl der parallelen Threads direkt angibt, oder es kann eine Zeichenfolge mit dem Format"xNUM" sein, die den Multiplikationsfaktor der Anzahl der verfügbaren Prozessoren angibt. Zum Beispiel: "x1.5". Der Standardwert lautet `"30"`.

## Weitere Informationen

crawler(1)

vcrypt(1)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
