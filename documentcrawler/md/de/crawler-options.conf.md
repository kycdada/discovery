# Optionen für die Crawlersuche konfigurieren
Der Data Crawler erfasst Rohdaten, die möglicherweise verwendet werden, um Suchergebnisse für den Service IBM Watson Retrieve and Rank zu bilden. 

Der Datencrawler bietet aktuell Konnektoren zur Unterstützung der Datenerfassung von den folgenden Repositorys an: 

*	Dateisystem
*	Datenbank über JDBC
*	CMIS (Content Management Interoperability Services)
*	SMB (Server Message Block, CIFS (Common Internet Filesystem) oder gemeinsam genutzte Samba-Dateien
*	SharePoint und SharePoint Online
*	Box

Ferner wird eine Konfigurationsschablone zur Verfügung gestellt. Diese ermöglicht es Ihnen, einen Konnektor anzupassen.

## Erste Schritte:
Bei der Crawlersuche über Datenrepositorys beginnt der Crawler bei einer benutzerdefinierten Ausgangs-Seed-URL damit, Seiten mit Daten herunterzuladen. Der Crawler lokalisiert ferner Links in den heruntergeladenen Seiten und terminiert weitere Crawlersuchen für die neu erkannten Seiten. 

Konfigurationsdaten werden verwendet, um festzulegen, welche Seiten durchsucht werden müssen und wie diese Crawlersuche erfolgen soll. Diese Datei erläutert die Optionen, die Sie für jeden Konnektor konfigurieren können.

**Hinweis**: Jeder Konnektor verfügt ferner über eine entsprechende Seed-Konfigurationsdatei. Die Optionen für die Seed-Konfiguration werden gesondert beschrieben. 

### Dateisystemkonnektor konfigurieren
Der Dateisystemkonnektor ermöglicht Ihnen, Dateien lokal an der Position der Data Crawler-Installation zu durchsuchen. Es folgen die Basiskonfigurationsoptionen, die für die Verwendung des Dateisystemkonnektors erforderlich sind. Um diese Werte festzulegen, öffnen Sie die Datei `config/connectors/filesystem.conf` und ändern die folgenden Werte, die für Ihre Anwendungsfälle spezifisch sind: 

*  **protocol** - Der Name des für die Crawlersuche verwendeten Konnektorprotokolls. Verwenden Sie für diesen Konnektor `sdk-fs`. 
*  **collection** - Dieses Attribut wird verwendet, um temporäre Dateien zu entpacken. 
*  **logging-config** - Gibt die Datei an, die für die Konfiguration der Protokollierungsoption verwendet wird. Diese muss als XML-Zeichenfolge `log4j` formatiert sein. 
*  **classname** - Java-Klassenname für den Konnektor. Der Wert für die Verwendung dieses Konnektors muss `plugin:filesystem.plugin@filesystem` lauten.

### Datenbankkonnektor konfigurieren
Der Datenbankkonnektor ermöglicht Ihnen, eine Crawlersuche für eine Datenbank über einen angepassten SQL-Befehl auszuführen und ein Dokument pro Zeile (Datensatz) und ein Inhaltselement pro Spalte (Feld) zu erstellen. Sie können eine Spalte angeben, die als eindeutiger Schlüssel verwendet wird, sowie eine Spalte mit einer Zeitmarke, die das letzte Änderungsdatum jedes Datensatzes darstellt. Der Konnektor ruft alle Datensätze von der angegebenen Datenbank ab und kann auch auf bestimmte Tabellen, Joins usw. in der SQL-Anweisung beschränkt werden. 

Der Datenbankkonnektor ermöglicht Ihnen, eine Crawlersuche für die folgenden Datenbanken durchzuführen:

*  IBM DB2
*  MySQL
*  Oracle
*  PostgreSQL
*  Microsoft SQL Server
*  Sybase
*  Andere SQL-konforme Datenbanken über einen JDBC 3.0-konformen Treiber

Der Konnektor ruft alle Datensätze von der angegebenen Datenbank und Tabelle ab. 

**JDBC-Treiber**
Der Datenbankkonnektor wird mit dem Oracle JDBC-Treiber (Java Database Connectivity) Version 1.5 ausgeliefert. Alle JDBC-Treiber anderer Anbieter, die mit Data Crawler ausgeliefert werden befinden sich im Verzeichnis `/lib/java/database` Ihrer Data Crawler-Installation. Sie können diese Treiber bei Bedarf hinzufügen, entfernen oder ändern. Sie können auch die Einstellung `extra_jars_dir` in der Datei `crawler.conf` nutzen, um eine andere Position anzugeben.

***DB2 JDBC-Treiber***
Data Crawler wird aufgrund von Lizenzierungsproblemen nicht mit den JDBC-Treibern für DB2 ausgeliefert. Alle DB2-Installationen, in denen Sie JDBC-Unterstützung installiert haben, enthalten  jedoch die JAR-Dateien, die für Data Crawler erforderlich sind, um eine Crawlersuche über eine DB2-Installation durchzuführen. Um eine Crawlersuche für eine DB2-Instanz durchzuführen, müssen Sie diese Dateien in das entsprechende Verzeichnis in Ihrer Data Crawler-Installation kopieren, so dass der Datenbankkonnektor sie verwenden kann. 

Um Data Crawler die Crawlersuche über eine DB2-Installation zu ermöglichen, suchen Sie `db2jcc.jar` und JAR-Lizenzdateien (in der Regel `db2jcc_license_cu.jar`) in Ihrer DB2-Installation und kopieren diese Dateien in das Unterverzeichnis `lib/java` Ihres Installationsverzeichnisses von Data Crawler oder Sie verwenden die Einstellung `extra_jars_dir` in der Datei `crawler.conf`, um eine andere Position anzugeben.

***MySQL JDBC-Treiber***
Data Crawler wird nicht mit den JDBC-Treibern für MySQL ausgeliefert, da es möglicherweise zu Lizenzproblemen kommen könnte, wenn diese als Teil des Produkts ausgeliefert werden. Es ist jedoch sehr einfach, die JAR-Datei herunterzuladen, die die MySQL JDBC-Treiber enthält und diese JAR-Datei in Ihre Installation von Data Crawler zu integrieren:

1.	Verwenden Sie einen Web-Browser, um zur Download-Site von MySQL zu gelangen. Suchen Sie hier die Quelle und den binären Download-Link für das Archivformat, das Sie verwenden möchten (in der Regel 'zip' bei Systemen mit Microsoft Windows oder eine mit 'gzip' komprimiert TAR-Datei bei Linux-Systemen). Klicken Sie auf den Link zum Initialisieren des Downloadprozesses. Eine Registrierung kann erforderlich sein. 

2.	Verwenden Sie den entsprechenden Befehl `unzip archive-file-name` oder `tar zxf archive-file-name`, um den Inhalt des Archivs auf Grundlage des Archivtyps und -namens der heruntergeladenen Archivdatei zu extrahieren. 

3.	Wechseln Sie in das Verzeichnis, das aus der Archivdatei extrahiert wurde, und kopieren Sie die JAR-Datei aus diesem Verzeichnis in das Unterverzeichnis `lib/java` Ihres Installationsverzeichnisses von Data Crawler oder Sie verwenden die Einstellung `extra_jars_dir` in der Datei `crawler.conf`, um eine andere Position anzugeben.

Es folgen die Basiskonfigurationsoptionen, die für die Verwendung des Datenbankkonnektors erforderlich sind. Um diese Werte festzulegen, öffnen Sie die Datei `config/connectors/database.conf` und ändern die folgenden Werte, die für Ihre Anwendungsfälle spezifisch sind: 

*  **protocol** - Der Name des für die Crawlersuche verwendeten Konnektorprotokolls. Der Wert für diesen Konnektor basiert auf dem Datenbanksystem, auf das zugegriffen werden soll. 
*  **collection** - Dieses Attribut wird verwendet, um temporäre Dateien zu entpacken. 
*  **classname** - Java-Klassenname für den Konnektor. Der Wert für die Verwendung dieses Konnektors muss `plugin:database.plugin@database` lauten.
*  **logging-config** - Gibt die Datei an, die für die Konfiguration der Protokollierungsoption verwendet wird. Diese muss als XML-Zeichenfolge `log4j` formatiert sein. 

### CMIS-Konnektor konfigurieren
Der CMIS-Konnektor (CMIS, Content Management Interoperability Services) ermöglicht Ihnen für CMIS-aktivierte CMS-Repositorys (CMS, Content Management System) wie beispielsweise Alfresco, Documentum oder IBM Content Manager zu durchsuchen sowie einen Index der darin enthaltenen Daten zu erstellen. 

Es folgen die Basiskonfigurationsoptionen, die für die Verwendung des CMIS-Konnektors erforderlich sind. Um diese Werte festzulegen, öffnen Sie die Datei `config/connectors/cmis.conf` und ändern die folgenden Werte, die für Ihre Anwendungsfälle spezifisch sind: 

*  **protocol** - Der Name des für die Crawlersuche verwendeten Konnektorprotokolls. Verwenden Sie für diesen Konnektor `cmis`. 
*  **collection** - Dieses Attribut wird verwendet, um temporäre Dateien zu entpacken. 
*  **dns** - Nicht verwendete Option.
*  **classname** - Java-Klassenname für den Konnektor. Der Wert für die Verwendung dieses Konnektors muss `plugin:cmis-v1.1.plugin@connector` lauten.
*  **logging-config** - Gibt die Datei an, die für die Konfiguration der Protokollierungsoption verwendet wird. Diese muss als XML-Zeichenfolge `log4j` formatiert sein. 
*  **endpoint** - Die Serviceendpunkt-URL eines CMIS-konformen Repositorys. Die URL-Strukturen für SharePoint lauten zum Beispiel: 
   *  Für AtomPub-Binding:   
      http://<server>:<port>/_vti_bin/cmis/rest?getRepositories
   *  Für WebServices-Binding:   
      http://<server>:<port>/_vti_bin/cmissoapwsdl.aspx

*  **username** - Der Benutzername des CMIS-Repositorybenutzers, der für den Zugriff auf den Inhalt verwendet wird. Dieser Benutzer muss Zugriff auf alle Zielordner und -dokumente erhalten, die durchsucht oder indexiert werden sollen. 
*  **password** - Das Kennwort für das CMIS-Repository, das für den Zugriff auf den Inhalt verwendet wird. Das Kennwort darf NICHT verschlüsselt werden. Es sollte als unverschlüsselter Text angegeben werden. 
*  **repositoryid** - Die ID des CMIS-Repositorys, die für den Zugriff auf den Inhalt für dieses spezifische Repository verwendet werden soll. 
*  **bindingtype** - Gibt an, welcher Bindungstyp verwendet werden soll, um eine Verbindung zum CMIS-Repository herzustellen. Der Wert lautet entweder `AtomPub` oder `WebServices`.
*  **authentication** - Gibt an, welcher Typ von Authentifizierungsmechanismus während der Verbindung zu einem CMIS-kompatiblen Repository verwendet werden soll: `Basic HTTP Authentication`, `NTLM` oder `WS-Security(Username token)`.
*  **enable-acl** - Ermöglicht das Abrufen von ACLs für durchsuchte Daten. Wenn Sie keine Bedenken hinsichtlich der Sicherheit der Dokumente in dieser Zusammenstellung haben, können Sie durch Ausschalten dieser Option die Leistung erhöhen, indem Sie diese Informationen nicht mit dem Dokument abrufen und diese Daten nicht verschlüsseln. Der Wert lautet entweder `true` oder `false`.
*  **user-agent** - Ein Header, der an den Server gesendet wird, wenn Dokumente durchsucht werden. 
*  **method** - Die Methode (`GET` oder `POST`) mit der Parameter übergeben werden. 
*  **url-logging** - Der Bereich, in dem durchsuchte URLs protokolliert werden. Mögliche Werte sind: 

   *  ***full-logging*** - Alle Informationen über die URL protokollieren. 
   *  ***refined-logging*** - Nur die Informationen protokollieren, die zum Anzeigen des Crawlerprotokolls und für die korrekte Funktion des Konnektors erforderlich sind. Dies ist der Standardwert. 
   *  ***minimal-logging*** - Nur ein Minimum an Informationen protokollieren, die für die korrekte Funktion des Konnektors erforderlich sind. 

   Durch das Festlegen dieser Option auf 'minimal-logging', wird die Größe des Protokoll reduziert und eine leichte Leistungssteigerung erzielt, da die E/A bezüglich der geringeren zu protokollierenden Datenmenge kleiner ist.
*  **ssl-version** - Gibt eine SSL-Version an, die für die HTTPS-Verbindungen verwendet werden soll. Standardmäßig wird das stärkste verfügbare Protokoll verwendet. 

### SMB/CIFS/Samba-Konnektor konfigurieren
Der Samba-Konnektor ermöglicht Ihnen, gemeinsam genutzte SMB-Dateien (Server Message Block) und CIFS-Dateien (Common Internet Filesystem) zu durchsuchen. Dieser Typ gemeinsam genutzter Dateien ist in Windows-Netzen häufig und wird ebenfalls vom Open-Source-Projekt [Samba](https://www.samba.org/) zur Verfügung gestellt.

Es folgen die Basiskonfigurationsoptionen, die für die Verwendung des Samba-Konnektors erforderlich sind. Um diese Werte festzulegen, öffnen Sie die Datei `config/connectors/samba.conf` und ändern die folgenden Werte, die für Ihre Anwendungsfälle spezifisch sind: 

*  **protocol** - Der Name des für die Crawlersuche verwendeten Konnektorprotokolls. Der Wert für die Verwendung dieses Konnektors muss `smb` lauten.
*  **collection** - Dieses Attribut wird verwendet, um temporäre Dateien zu entpacken. 
*  **classname** - Java-Klassenname für den Konnektor. Der Wert für die Verwendung dieses Konnektors muss `plugin:smb.plugin@connector` lauten.
*  **logging-config** - Gibt die Datei an, die für die Konfiguration der Protokollierungsoption verwendet wird. Diese muss als XML-Zeichenfolge `log4j` formatiert sein. 
*  **username** - Der Samba-Benutzername für die Authentifizierung. Wenn dieser angegeben ist, müssen Domäne und Kennwort ebenfalls angegeben werden. Wenn dieser nicht angegeben ist, wird das Gastkonto verwendet. 
*  **password** - Das Samba-Kennwort für die Authentifizierung. Falls der Benutzername angegeben ist, ist das Kennwort erforderlich. Das Kennwort muss mithilfe der VCrypt-Bibliothek verschlüsselt werden, die mit Data Crawler ausgeliefert wird. 
*  **archive** - Aktiviert den Samba-Konnektor zum Durchsuchen und Indexieren von Dateien, die in Archivdateien komprimiert wurden. Der Wert lautet entweder `true` oder `false`. Der Standardwert lautet `false`.
*  **max-policies-per-handle** - Gibt die maximale Anzahl an LSA-Richtlinien (LSA, Local Security Authority) an, die für ein einziges RPC-Handle geöffnet werden können. Diese Richtlinien definieren die Zugriffsberechtigungen, die für die Abfrage oder Änderung eines bestimmten Systems unter verschiedenen Bedingungen erforderlich sind. Der Standardwert für diese Option lautet `255`.
*  **crawl-fs-metadata** - Das Aktivieren dieser Option führt dazu, dass Data Crawler ein VXML-Dokument mit verfügbaren Dateisystem-Metadaten über die Datei hinzufügt (Erstellungsdatum, Datum der letzten Änderung, Dateiattribute etc.)
*  **enable-arc-connector** - Nicht verwendete Option.
*  **disable-indexes** - Durch einen Zeilenumbruch getrennte Liste von zu inaktivierenden Indizes. Dies kann zu einer schnelleren Crawlersuche führen. Zum Beispiel: 

   *  disable-url-index
   *  disable-error-state-index
   *  disable-crawl-time-index
*  **exact-duplicates-hash-size** - Legt die Größe der Hashtabelle fest, die für das Auflösen doppelter Werte verwendet wird. Seien Sie sehr vorsichtig, wenn Sie diese Größe ändern. Der Wert, den Sie auswählen, sollte gut überlegt sein. Größere Werte können zu schnelleren Suchläufen führen, erfordern jedoch mehr Speicherplatz. Kleinere Werte dagegen können Suchläufe verlangsamen, reduzieren aber die Speichernutzung wesentlich. 
*  **user-agent** - Nicht verwendete Option.
*  **timeout** - Nicht verwendete Option.
*  **n-concurrent-requests** - Die Anzahl der Anforderungen, die parallel an eine einzige IP-Adresse gesendet werden. Der Standard lautet `1`.
*  **enqueue-persistence** - Nicht verwendete Option.

### SharePoint-Konnektor konfigurieren
Der SharePoint-Konnektor ermöglicht Ihnen, Objekte von SharePoint Server und SharePoint Online zu durchsuchen und die Daten, die diese enthalten, zu indexieren. Ein Objekt wie zum Beispiel ein Dokument, ein Benutzerprofil, eine Siteerfassung, ein Blog, ein Listeneintrag, eine Mitgliederliste, eine Verzeichnisseite usf. kann mit seinen zugehörigen Metadaten indexiert werden. Bei Listeneinträgen und Dokumenten können die Indizes zudem Anhänge enthalten. 

**Hinweis**: Der SharePoint-Konnektor respektiert das `noindex`-Attribut bei allen SharePoint-Objekten, unabhängig von deren bestimmtem Typ (Blogs, Dokumente, Benutzerprofile usw.). Für jedes Ergebnis wird ein einzelnes Dokument zurückgegeben. 

**Wichtig**: Das SharePoint-Konto, das Sie für die Crawlersuche über Ihre SharePoint-Sites verwenden, muss mindestens über die vollständigen Leseberechtigungen verfügen.

Es folgen die Basiskonfigurationsoptionen, die für die Verwendung das SharePoint-Konnektors erforderlich sind. Um diese Werte festzulegen, öffnen Sie die Datei `config/connectors/sharepoint.conf` und ändern die folgenden Werte, die für Ihre Anwendungsfälle spezifisch sind:

*  **protocol** - Der Name des für die Crawlersuche verwendeten Konnektorprotokolls. Verwenden Sie für diesen Konnektor `io-sp`. 
*  **collection** - Dieses Attribut wird verwendet, um temporäre Dateien zu entpacken. 
*  **classname** - Java-Klassenname für den Konnektor. Der Wert für die Verwendung dieses Konnektors muss `plugin:io-sharepoint.plugin@connector` lauten.
*  **logging-config** - Gibt die Datei an, die für die Konfiguration der Protokollierungsoption verwendet wird. Diese muss als XML-Zeichenfolge `log4j` formatiert sein. 
*  **seed-url-type** - Gibt den Typ des SharePoint-Objekts an, auf den die bereitgestellte Seed-URL zeigt: Siteerfassungen oder Webanwendungen (auch als virtuelle Server bekannt). 

   *  ***Site Collections*** - Wenn für den Seed-URL-Typ `Site Collections` angegeben ist, dann werden nur die untergeordneten Elemente der durch die URL referenzierten Siteerfassung durchsucht. 
   *  ***Web Applications*** - Wenn für den Seed-URL-Typ `Web Applications` angegeben ist, dann werden alle Siteerfassungen (und deren untergeordnete Elemente), die zu der durch die URL referenzierten Webanwendung gehören, durchsucht. 
*  **auth-type** - Der Authentifizierungsmechanismus, der für die Verbindung zum SharePoint-Server verwendet werden soll: `BASIC`, `NTLM2`, `KERBEROS` oder `CBA`. Der Standardauthentifizierungstyp lautet `NTLM2`.
*  **spUser** - Der Benutzername des SharePoint-Benutzers, der für den Zugriff auf den Inhalt verwendet werden wird. Dieser Benutzer muss Zugriff auf alle  Zielsites und -listen erhalten, die durchsucht und indexiert werden soll. Ferner muss er in der Lage sein, die zugehörigen Berechtigungen abzurufen und aufzulösen. Es wird empfohlen, mit dem Domänennamen zuzugreifen. Zum Beispiel: `MYDOMAIN\\Administrator`.
*  **spPassword** - Das Kennwort des SharePoint-Benutzers, das für den Zugriff auf den Inhalt verwendet werden wird. Das Kennwort muss mit dem Programm 'vcypt' verschlüsselt werden, das mit Data Crawler ausgeliefert wird.
*  **cba-sts** - Die URL für den STS-Endpunkt (STS, Security Token Service), an dem versucht wird, den Benutzer des Crawlers zu authentifizieren. Bei einem lokalen SharePoint mit ADFS sollte dies Ihr ADFS-Endpunkt sein. Falls für den Authentifizierungstyp `CBA` (Claims Based Authentication) angegeben ist, ist dieses Feld erforderlich. 
*  **cba-realm** - Die Vertrauenskennung des Relaisteilnehmers, die beim Abrufen eines Sicherheitstokens vom STS verwendet wird. Dies wird manchmal auch als "AppliesTo"-Wert oder "Realm" bezeichnet. Bei SharePoint Online sollte dies die URL zum Stammverzeichnis der SharePoint Online-Instanz sein (zum Beispiel: `https://mycompany.sharepoint.com`). Bei ADFS ist dies der Wert für die Vertrauenskennung des Relaisteilnehmers (Relying Party Trust) zischen SharePoint und ADFS (zum Beispiel `"urn:SHAREPOINT:adfs"`).
*  **everyone-group** - Falls angegeben wird dieser Gruppenname in den ACLs verwendet, wenn jedem Zugriff gegeben wird. Das Feld ist erforderlich, wenn das Durchsuchen von Benutzerprofilen aktiviert wird. **Hinweis** - Sicherheit wird von den Services Retrieve und Rank noch nicht beachtet. 
*  **user-profile-master-url** - Die Basis-URL, die der Konnektor verwendet, um Links zu Benutzerprofilen zu erstellen. Diese sollte konfiguriert werden, um auf die Anzeigeform für Benutzerprofile zu zeigen. Falls das Token `%FIRST_SEED%` gefunden wird, wird es durch die erste Seed-URL-ersetzt. Das Feld ist erforderlich, wenn die Crawlersuche über Benutzerprofile aktiviert wird. 
*  **urls** - Eine durch Zeilenumbruch getrennte Liste von HTTP-URLs von SharePoint-Webanwendungen oder Siteerfassungen für die Crawlersuche. 
*  **ehcache-config** - Nicht verwendete Option.
*  **method** - Die Methode (`GET` oder `POST`) mit der Parameter übergeben werden. 
*  **cache-types** - Nicht verwendete Option.
*  **cache-size** - Nicht verwendete Option.
*  **enable-acl** - Ermöglicht die Crawlersuche über SharePoint-Benutzerprofile. Die Werte sind `true` oder `false`. Der Standardwert lautet `false`. 

### Box-Konnektor konfigurieren
Der Box-Konnektor ermöglicht Ihnen, Ihre Enterprise Box-Instanz zu durchsuchen und die enthaltenen Informationen zu indexieren. Es folgen einige Basiskonfigurationsoptionen, die für die Verwendung des Box-Konnektors erforderlich sind. Um diese Werte festzulegen, öffnen Sie die Datei `config/connectors/box.conf` und ändern die folgenden Werte, die für Ihre Anwendungsfälle spezifisch sind: 

*  **protocol** - Der Name des für die Crawlersuche verwendeten Konnektorprotokolls. Verwenden Sie für diesen Konnektor `box`. 
*  **classname** - Java-Klassenname für den Konnektor. Der Wert für die Verwendung dieses Konnektors muss `plugin:box.plugin@connector` lauten.
*  **logging-config** - Gibt die Datei an, die für die Konfiguration der Protokollierungsoption verwendet wird. Diese muss als XML-Zeichenfolge `log4j` formatiert sein. 
*  **box-crawl-seed-url** - Die Basis-URL für Box. Der Wert für diesen Konnektor lautet `box://app.box.com/`. Sie können unterschiedliche URL-Typen durchsuchen. Zum Beispiel: 

   *  ***Zum Durchsuchen eines gesamten Unternehmens***: `box://app.box.com/`
   *  ***Zum Durchsuchen eines bestimmten Ordners***: `box://app.box.com/user/USER_ID/folder/FOLDER_ID/FolderName`
   *  ***Zum Durchsuchen eines bestimmten Benutzers***: `box://app.box.com/user/USER_ID/`
*  **client-id** - Geben Sie die Client-ID ein, die von Box zur Verfügung gestellt wird, wenn Sie Ihre Box-Anwendung erstellt haben.
*  **client-secret** - Geben Sie den geheimen Clientschlüssel ein, der von Box zur Verfügung gestellt wird, wenn Sie Ihre Box-Anwendung erstellt haben. 
*  **path-to-private-key** - Dies ist die Position des privaten Schlüssels, der Teil des Schlüsselpaares (privater Schlüssel/öffentlicher Schlüssel) ist, auf Ihrem lokalen Dateisystem, das für die Kommunikation mit Box generiert wurde. 
*  **kid** - Geben Sie die ID für den öffentlichen Schlüssel an. Dies ist die andere Hälfte des Schlüsselpaares (privater Schlüssel/öffentlicher Schlüssel), das für die Kommunikation mit Box generiert wurde. 
*  **enterprise-id** - Das Unternehmen, in dem Ihre Anwendung autorisiert wurde. Die Unternehmens-ID wird auf der Hauptseite der Administratorkonsole von Box aufgelistet. 
*  **enable-acl** - Nur zur internen Verwendung. Ermöglicht das Abrufen von ACLs für durchsuchte Daten. 
*  **user-agent** - Ein Header, der an den Server gesendet wird, wenn Dokumente durchsucht werden. 
*  **method** - Die Methode (`GET` oder `POST`) mit der Parameter übergeben werden. 
*  **url-logging** - Der Bereich, in dem durchsuchte URLs protokolliert werden. Mögliche Werte sind: 

   *  ***full-logging*** - Alle Informationen über die URL protokollieren. 
   *  ***refined-logging*** - Nur die Informationen protokollieren, die zum Anzeigen des Crawlerprotokolls und für die korrekte Funktion des Konnektors erforderlich sind. Dies ist der Standardwert. 
   *  ***minimal-logging*** - Nur ein Minimum an Informationen protokollieren, die für die korrekte Funktion des Konnektors erforderlich sind. 

   Durch das Festlegen dieser Option auf 'minimal-logging', wird die Größe des Protokoll reduziert und eine leichte Leistungssteigerung erzielt, da die E/A bezüglich der geringeren zu protokollierenden Datenmenge kleiner ist.
*  **ssl-version** - Gibt eine SSL-Version an, die für die HTTPS-Verbindungen verwendet werden soll. Standardmäßig wird das stärkste verfügbare Protokoll verwendet. 

Der Box-Konnektor weist einige Beschränkungen auf: 

* Kommentare oder Tasks zu Dateien werden nicht abgerufen.
* Der Notes-Inhaltshauptteil wird als JSON abgerufen. Eine weitere Konversion von Note-Daten ist möglicherweise erforderlich.
* Einzelne Dokumente können über TestIt nicht abgerufen werden. Nur Seed-URLs, Ordner-URLs und Benutzer-URLs können über TestIt abgerufen werden.


## Weitere Informationen

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
