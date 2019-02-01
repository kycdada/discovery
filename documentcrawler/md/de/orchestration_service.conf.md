# Orchestrierungsservice konfigurieren
Der Orchestrierungsservice informiert den Crawler darüber, wie die durchsuchten Dateien zu verwalten sind. Die Standardoptionen können direkt durch Öffnen der Datei `config/orchestration/orchestration-service.conf` und Ändern der folgenden anwendungsfallspezifischen Werte geändert werden: 

*  **http_timeout** - Das Zeitlimit in Sekunden für die Lese- und Indexieroperation für Dokumente. Der Standardwert lautet `585`.
*  **concurrent_upload_connection_limit** - Die Anzahl der gleichzeitigen Verbindungen, die für das Hochladen von Dokumenten zulässig ist. Der Standardwert lautet `10`. Im Allgemeinen sollte diese Zahl größer als der oder gleich dem Wert für `output_limit` sein, der beim Konfigurieren der Optionen für die Crawlersuche definiert wurde. 
*  **base_url** - Die URL, an die Ihre durchsuchten Dokumente gesendet werden.
*  **endpoint** - Die Position Ihrer Sammlung durchsuchter Dokumente unter `base-url`.
*  **username** - Der Benutzername zur Authentifzierung der Position `endpoint`.
*  **password** - Das Kennwort zur Authentifzierung der Position `endpoint`. **Wichtig** - Verwenden Sie **NICHT** das Programm 'vcrypt', das mit Data Crawler geliefert wird, um dieses Kennwort zu verschlüsseln. 
*  **config_file** - Die Konfigurationsdatei, die der Orchestrierungsservice verwendet.

Der Ausgabeadapter des Orchestrierungsservice kann Statistikdaten senden, damit IBM seinen Kundenservice verbessern kann. Die folgenden Optionen können für die Variable `send_stats` definiert werden:
*  **jvm** - Gesendete JVM-Statistikdaten (JVM, Java Virtual Machine) umfassen den Java-Anbieter und die Java-Version, so wie diese von der für die Ausführung von Data Crawler verwendeten JVM berichtet werden. Der Wert lautet entweder `true` oder `false`.
*  **os** - Gesendete Betriebssystemstatistikdaten (OS, Operating System) umfassen den Namen, die Version und die Architektur des Betriebssystems, so wie diese von der für die Ausführung von Data Crawler verwendeten JVM berichtet werden. Der Wert lautet entweder `true` oder `false`.

## Weitere Informationen

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
