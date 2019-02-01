# Seedwerte für Crawlersuche konfigurieren

Seedwerte sind die Ausgangspunkte von Crawlersuchen und werden von Datencrawlern verwendet, um Daten von einer Ressource abzurufen, die durch den jeweiligen Seedwert gekennzeichnet ist. In der Regel konfigurieren Seedwerte URLs, um auf protokollbasierte Ressourcen wie gemeinsame Dateizugriffe, gemeinsame SMB-Zugriffe, Datenbanken und andere Datenrepositorys zuzugreifen, die über verschiedene Webprotokolle zur Verfügung stehen. Darüber hinaus haben unterschiedliche Seed-URLs unterschiedliche Leistungsmerkmale.

Seedwerte können auch repositoryspezifisch sein, um die Crawlersuche bestimmter Anwendungen von Drittanbietern wie beispielsweise CRM-Systemen (CRM, Customer Relationship Management), PLC-Systemen (PLC, Product Life Cycle), CMS-Systemen (CMS,Content Management System), cloudbasierten Anwendungen und Webdatenbankanwendungen zu ermöglichen.

Der Datencrawler bietet aktuell Seedwerte, die Dateiverbindungen für die folgenden Repository-Typen unterstützen:

*	Dateisystem
*	Datenbank über JDBC
*	CMIS (Content Management Interoperability Services)
*	SMB (Server Message Block), CIFS (Common Internet Filesystem) oder gemeinsam genutzte Samba-Dateien
*	SharePoint und SharePoint Online
*	Box

Eine Konfigurationsschablone für die Seedwerte der Crawlersuche wird ebenfalls zur Verfügung gestellt. Diese ermöglicht es Ihnen, Seedwerte für die Crawlersuche an einen benutzerdefinierten Konnektor anzupassen.

## Erste Schritte:

Bei der Crawlersuche über Datenrepository, beginnt der Crawler bei einer benutzerdefinierten Ausgangs-URL damit, Seiten mit Daten herunterzuladen. Der Crawler lokalisiert ferner Links in den heruntergeladenen Seiten und terminiert weitere Crawlersuchen für die neu erkannten Seiten. 

Konfigurationsdaten werden verwendet, um festzulegen, welche Seiten durchsucht werden müssen und wie diese Crawlersuche erfolgen soll. Diese Datei erläutert die Optionen, die Sie für jede Seeddatei der Crawlersuche des Konnektors konfigurieren können. 

**Hinweis**: Jede Konfigurationsdatei der Crawlersuche funktioniert mit einer entsprechenden Konfigurationsdatei für den Dateikonnektor. Optionen für den Dateikonnektor  werden gesondert beschrieben. 

### Seedwert für die Dateisystemcrawlersuche konfigurieren

Die folgenden Werte können für die Seeddatei der Dateisystemcrawlersuche konfiguriert werden. Um diese Werte festzulegen, öffnen Sie die Datei `config/seeds/filesystem-seed.conf` und geben die folgenden Werte an, die für Ihre Anwendungsfälle spezifisch sind: 

*  **url** - Eine durch Zeilenumbruch getrennte Liste von Dateien und Ordnern für die Crawlersuche. UNIX-Benutzer verwenden einen Pfad wie beispielsweise `/usr/local/`.
Die URLs müssen mit `sdk-fs://` beginnen. Um zum Beispiel eine Crawlersuche für `/home/watson/mydocs` durchzuführen, würde der Wert dieser URL `sdk-fs:///home/watson/mydocs` lauten - der dritte Schrägstrich `/` ist dabei erforderlich!
**Hinweis**: Der Dateisystemkonnektor verwendet das benutzerdefinierte Protokoll `sdk-fs://`, um eine gültige URL zu erstellen. Stellen Sie den aufgelisteten Pfaden nicht `file://` voran. Die URLs müssen mit `sdk-fs://` beginnen.
*  **hops** - Nur zur internen Verwendung.
*  **default-allow** - Nur zur internen Verwendung.

### Seedwerte für Datenbankcrawlersuche konfigurieren

Die folgenden Werte können für die Seeddatei der Datenbankcrawlersuche konfiguriert werden. Um diese Werte festzulegen, öffnen Sie die Datei `config/seeds/database-seed.conf` und geben die folgenden Werte an, die für Ihre Anwendungsfälle spezifisch sind: 

*  **url** - Die URL der Tabelle oder Ansicht, die abgerufen werden soll. Definiert die Seed-URL ihrer angepasste SQL-Datenbank. Die Struktur lautet: 

   	`database-system://host:port/database?[per=num]&[sql=SQL]`

   Der Test einer Seed-URL zeigt alle eingereihten URLs an. Beispiel für das Testen der folgenden URL für eine Datenbank mit 200 Datensätzen:

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=100&sql=select%20*%20from%20vessel&`

   zeigt die folgenden eingereihten URLs an:

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=0&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=100&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=200&`

   Beim Testen der folgenden URL werden die Daten angezeigt, die aus Zeile 43 abgerufen wurden:

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=1&key-val=43`
*  **hops** - Nur zur internen Verwendung.
*  **default-allow** - Nur zur internen Verwendung.
*  **user-password** - Berechtigungsnachweise für das Datenbanksystem. Der Benutzername und das Kennwort müssen durch einen Doppelpunkt `:` voneinander getrennt sein und das Kennwort muss mit dem Programm 'vcrypt' verschlüsselt werden, das mit Data Crawler ausgeliefert wird. Beispiel: `username:[[vcrypt/3]]passwordstring`.
*  **max-data-size** - Maximale Größe der Daten für ein Dokument. Dies ist der größte Speicherblock, der geladen wird. Erhöhen Sie diesen Grenzwert nur dann, wenn Sie über ausreichend Speicherplatz auf Ihrem Computer verfügen. 
*  **filter-exact-duplicates** - Nur zur internen Verwendung.
*  **jdbc-class** (Extender-Option) - Bei Angabe dieser Option überschreibt diese Zeichenfolge die JDBC-Klasse, die vom Konnektor verwendet wird, wenn `(other)` als Datenbanksystem ausgewählt wurde.
*  **connection-string** (Extender-Option) - Bei Angabe dieser Option, überschreibt diese Zeichenfolge die automatisch generierte Zeichenfolge der JDBC-Verbindung. Dies ermöglicht Ihnen, eine detaillierte Konfiguration der Datenbankverbindung wie beispielsweise Lastausgleich oder SSL-Verbindungen. Beispiel: `jdbc:netezza://127.0.0.1:5480/databasename`.
*  **save-frequency-for-resume** (Extender-Option) - Diese Option gibt den Namen einer Spalte oder einer zugehörigen Beschriftung an, um eine Crawlersuche fortsetzen zu können oder um eine Teilaktualisierung durchzuführen. Der Seedwert speichert den  Namen dieser Spalte regelmäßig im Laufe der Crawlersuche und speichert ihn erneut, sobald die letzte Zeile der Datenbank durchsucht wurde. Bei der Wiederaufnahme der Crawlersuche oder bei ihrer Aktualisierung, beginnt die Crawlersuche mit der Zeile, die dem in diesem Feld gespeicherten Wert entspricht.

### Seedwert für CMIS-Crawlersuche konfigurieren

Die folgenden Werte können für die Seeddatei der CMIS-Crawlersuche konfiguriert werden. Um diese Werte festzulegen, öffnen Sie die Datei `config/seeds/cmis-seed.conf` und ändern die folgenden Werte, die für Ihre Anwendungsfälle spezifisch sind: 

*  **url** - Die URL eines Ordners vom CMIS-Repository, die als Ausgangspunkt für die Crawlersuche verwendet wird. Zum Beispiel: 

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=workspace://SpacesStore/guid`
   Um eine Crawlersuche vom Stammordner aus durchzuführen, müssen Sie die URL wie folgt angeben: 

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=`
*  **at** - Nicht verwendete Option.
*  **default-allow** - Nur zur internen Verwendung.

### Seedwert für die Samba-Crawlersuche konfigurieren

Die folgenden Werte können für die Samba-Crawlersuche konfiguriert werden. Um diese Werte festzulegen, öffnen Sie die Datei `config/seeds/samba-seed.conf` und ändern die folgenden Werte, die für Ihre Anwendungsfälle spezifisch sind: 

*  **url** - Eine durch Zeilenumbruch getrennte Liste gemeinsam genutzter Werte für die Crawlersuche. Zum Beispiel: 

   *  `smb://share.test.com/office`
   *  `smb://share.test.com/cash/money/change`
   *  `smb://share.test.com/C$/Program Files`

*  **hops** - Nur zur internen Verwendung.
*  **default-allow** - Nur zur internen Verwendung.

### Seedwert für die SharePoint-Crawlersuche konfigurieren

Die folgenden zusätzlichen Werte können für die Seeddatei der SharePoint-Crawlersuche verwendet werden. Um diese Werte festzulegen, öffnen Sie die Datei `config/seeds/sharepoint-seed.conf` und ändern die folgenden Werte, die für Ihre Anwendungsfälle spezifisch sind: 

*  **url** - Eine durch Zeilenumbruch getrennte Liste von SharePoint-Webanwendungen oder Siteerfassungen für die Crawlersuche. Zum Beispiel: 

   *  `io-sp://a.com`
   *  `io-sp://b.com:83/site`
   *  `io-sp://c.com/site2`

   Die untergeordneten Sites dieser Sites werden ebenfalls durchsucht (es sei denn, sie werden durch andere Crawlersuchregeln ausgeschlossen).
*  **filter-url** - Eine durch Zeilenumbruch getrennte Liste von SharePoint-Webanwendungen oder Siteerfassungen für die Crawlersuche. Zum Beispiel: 

   *  `http://a.com`
   *  `http://b.com:83/site`
   *  `http://c.com/site2`

*  **hops** - Nur zur internen Verwendung.
*  **n-concurrent-requests** - Nur zur internen Verwendung.
*  **delay** - Nur zur internen Verwendung.
*  **default-allow** - Nur zur internen Verwendung.
*  **seed-protocol** - Legt das Seedprotokoll für untergeordnete Elemente der Siteerfassung fest. Dies ist erforderlich, wenn das Protokoll der Siteerfassung das Format SSL, HTTP oder HTTPS aufweist. Dieser Wert muss auf denselben Wert wie das Protokoll der Siteerfassung festgelegt werden. 

### Seedwert für Box konfigurieren

Die folgenden Werte können für die Seeddatei der Box-Crawlersuche konfiguriert werden. Um diese Werte festzulegen, öffnen Sie die Datei `config/seeds/box-seed.conf` und geben die folgenden Werte, die für Ihre Anwendungsfälle spezifisch sind: 

*  **url** - Die URL, die als Ausgangspunkt der Crawlersuche verwendet werden soll. Der Standardwert lautet `box://app.box.com/`.
*  **default-allow** - Nur zur internen Verwendung.

## Weitere Informationen

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

orchestration_service.conf(5)
