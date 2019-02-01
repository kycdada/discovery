# Discovery-Service konfigurieren
Der Discovery Service informiert den Crawler darüber, wie die durchsuchten Dateien zu verwalten sind, wenn der Service IBM Watson Discovery verwendet wird. Die Standardoptionen können direkt durch Öffnen der Datei `config/discovery/discovery_service.conf` und Ändern der folgenden anwendungsfallspezifischen Werte geändert werden: 

*  **http_timeout** - Das Zeitlimit in Sekunden für die Lese- und Indexieroperation für Dokumente. Der Standardwert lautet `125`.
*  **concurrent_upload_connection_limit** - Die Anzahl der gleichzeitigen Verbindungen, die für das Hochladen von Dokumenten zulässig ist. Falls der Standardwert `2` lautet. Wenn der Ausgabeadapter des Orchestration Service verwendet wird, sollte diese Anzahl größer als der oder gleich dem Wert für `output_limit` sein, der bei der Konfiguration der Optionen für die Crawlersuche festgelegt wurde.
*  **base_url** - Die URL, an die Ihre durchsuchten Dokumente gesendet werden. Für das aktuelle Release von Discovery Service lautet der Wert `https://gateway.watsonplatform.net/discovery/api`.
*  **environment_id** - Die Position Ihrer Sammlung durchsuchter Dokumente unter `base-url`.
*  **collection_id** - Der Name der Dokumentsammlung, den Sie im Discovery Service definiert haben.
*  **configuration_id** - Der Dateiname der Konfigurationsdatei, die der Discovery Service verwendet.
*  **check_for_completion** - Überprüft, ob das Dokument am Endpunkt erfolgreich verarbeitet wurde. Dies reduziert die  wahrgenommene Leistung des Crawlers, führt jedoch zu verlässlichen Benachrichtigungen bei einem erfolgreichen Hochladen und einer erfolgreichen Konvertierung von Dokumenten. Der Wert lautet entweder `true` oder `false`.  
**WICHTIG** - Beim Aktivieren dieses Parameters ist es von Vorteil, für `concurrent_upload_connection_limit` einen Wert festzulegen, der größer als der oder gleich dem Wert ist, der bei der Konfiguration der Crawleroptionen für `output_limit` festgelegt wurde, um die Ihnen verfügbaren Ressourcen vollständig auszunutzen.

Stellen Sie Ihre Berechtigungsnachweise für Discovery Service bereit:
*  **username** - Der Benutzername für die Authentifizierung an der Position Ihrer Dokumentenzusammenstellung der Crawlersuche.
*  **password** - Das Kennwort zur Authentifizierung an der Position Ihrer Dokumentenzusammenstellung der Crawlersuche.

Der Ausgabeadapter des Discovery Service kann Statistikdaten senden, damit IBM seinen Kundenservice verbessern kann. Die folgenden Optionen können für die Variable `send_stats` definiert werden:
*  **jvm** - Gesendete JVM-Statistikdaten (JVM, Java Virtual Machine) umfassen den Java-Anbieter und die Java-Version, so wie diese von der für die Ausführung von Data Crawler verwendeten JVM berichtet werden. Der Wert lautet entweder `true` oder `false`.
*  **os** - Gesendete Betriebssystemstatistikdaten (OS, Operating System) umfassen den Namen, die Version und die Architektur des Betriebssystems, so wie diese von der für die Ausführung von Data Crawler verwendeten JVM berichtet werden. Der Wert lautet entweder `true` oder `false`.

*  **api_version** - Nur zur internen Verwendung. Das Datum der letzten Änderung der API-Version.

# URL-Trackingspeicher konfigurieren
Der Ordner `config/discovery` enthält ferner eine Konfigurationsdatei, die für die interne Zuordnung von Crawler-URLs und Dokument-IDs verwendet werden kann. Die Standardoptionen können direkt durch Öffnen der Datei `config/discovery/uri_tracking_storage.conf` und Ändern der folgenden anwendungsfallspezifischen Werte geändert werden: 

*  **driver** - JDBC-H2--Treiberklasse Ihrer Datenbank. Der Standardwert lautet `org.h2.Driver`
*  **url** - Dies ist das URL-Präfix für die JDBC-Verbindungszeichenfolge. Das Format lautet `jdbc:h2:[file:]`. **HINWEIS** Das Präfix `file:` ist optional. Fall kein oder nur ein relativer Pfad für `database_location` verwendet wird, wird das aktuelle Arbeitsverzeichnis als Ausgangspunkt verwendet. Der Standardwert lautet `jdbc:h2:file:`
*  **database_location** - Die Position auf der Platte, an der die Datenbank gespeichert ist. Zum Beispiel: `./storage/database` oder `~/storage/database`. Der Standardwert lautet `./storage/database`
*  **database_name** - Der Name der Datenbank. Der Standardwert lautet `ActivityDB`
*  **table_name** - Der Name der zu verwendenden Tabelle. Der Standardwert lautet `UriTracker`
*  **username** - Der Benutzername für die Verbindung zur Datenbank.
*  **password** - Das Kennwort für die Verbindung zur Datenbank.

## Weitere Informationen

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
