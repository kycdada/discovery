# Crawlopties configureren
De gegevenscrawler verzamelt de onbewerkte gegevens die uiteindelijk worden gebruikt voor het vormen van de zoekresultaten voor de service IBM Watson Retrieve and Rank.

De gegevenscrawler beschikt op dit moment over connectors voor het verzamelen van gegevens uit de volgende repository's:

*	Bestandssysteem
*	Databases, via JDBC
*	CMIS (Content Management Interoperability Services)
*	Bestandsshares van SMB (Server Message Block), CIFS (Common Internet Filesystem) of Samba
*	SharePoint en SharePoint Online
*	Box

Er is ook een configuratiesjabloon voor connectors beschikbaar, waarmee u wijzigingen in een connector kunt aanbrengen.

## Aan de slag:
Bij het crawlen van gegevensrepository's begint de crawler met een door de gebruiker opgegeven seed-URL en begint met het downloaden van pagina's met informatie. De crawler zoekt ook links in de gedownloade pagina's en plant de nieuw gevonden pagina's voor verdere crawls.

Er worden configuratiegegevens gebruikt om te bepalen welke pagina's moeten worden gecrawld en hoe u crawlt. In dit bestand vindt u een overzicht van de opties die u voor elke connector kunt configureren. 

**Opmerking**: Elke connector heeft een bijbehorend seedconfiguratiebestand; opties voor het seedconfiguratiebestand worden afzonderlijk beschreven.

### De connector voor het bestandssysteem configureren
Met de connector voor het bestandssysteem kunt u bestanden crawlen die zich lokaal in de installatie van de gegevenscrawler bevinden. Hieronder vindt u de opties voor de basisconfiguratie die vereist zijn voor het gebruik van de connector voor het bestandssysteem. Om deze waarden in te stellen, opent u het bestand `config/connectors/filesystem.conf` en wijzigt u de volgende waarden voor uw gebruiksvoorbeelden:

*  **protocol** - De naam van het connectorprotocol dat voor het crawlproces wordt gebruikt. Gebruik `sdk-fs` voor deze connector.
*  **collection** - Dit kenmerk wordt gebruikt voor het uitpakken van tijdelijke bestanden.
*  **logging-config** - Hiermee geeft u het bestand aan dat wordt gebruikt voor het configureren van opties voor logboekregistratie; het moet worden opgemaakt als een `log4j` XML-tekenreeks.
*  **classname** - De java-klassennaam voor de connector. De waarde die voor deze connector moet worden gebruikt is `plugin:filesystem.plugin@filesystem`.

### De connector voor de database configureren
Met de databaseconnector kunt u een database crawlen door het uitvoeren van een aangepaste SQL-opdracht en het maken van één document per rij (record) en één contentelement per kolom (veld). U kunt een kolom aangeven die wordt gebruikt als een unieke sleutel en een kolom die een tijdsaanduiding bevat die de datum van de laatste wijziging van elk record vertegenwoordigt. De connector haalt alle records uit de opgegeven database op en kan ook via de SQL-instructie worden beperkt tot bepaalde tabellen, joins, enzovoorts.

Met de databaseconnector kunt u de volgende databases crawlen:

*  IBM DB2
*  MySQL
*  Oracle
*  PostgreSQL
*  Microsoft SQL Server
*  Sybase
*  Overige SQL-compatibele databases via een JDBC 3.0-compatibel stuurprogramma

De connector haalt alle records uit de opgegeven database en tabel op.

**JDBC-stuurprogramma's** De databaseconnector wordt geleverd met het Oracle JDBC (Java Database Connectivity) stuurprogramma, versie 1.5. Alle JDBC-stuurprogramma's van derden die bij de Data Crawler worden geleverd, bevinden zich in de directory `/lib/java/database` van uw installatie van de Data Crawler; u kunt hier desgewenst items toevoegen, verwijderen en wijzigen. U kunt ook de instelling `extra_jars_dir` in het bestand `crawler.conf` gebruiken om een andere locatie op te geven.

***DB2 JDBC-stuurprogramma's***
Data Crawler wordt niet geleverd met de JDBC-stuurprogramma's voor DB2 vanwege problemen met de licentiëring. Alle DB2-installaties waarin u JDBC-ondersteuning hebt geïnstalleerd bevatten echter wel de JAR-bestanden die vereist zijn om een DB2-installatie te crawlen. Om een DB2-instance te crawlen, moet u deze bestanden kopiëren naar de toepasselijke directory in de installatie van uw Data Crawler zodat de databaseconnector ze kan gebruiken.

Om ervoor te zorgen dat een gegevenscrawler een DB2-installatie kan doorzoeken, zoekt u de JAR-bestanden `db2jcc.jar` en de licentie ervan (meestal `db2jcc_license_cu.jar`) in uw DB2-installatie op en kopieert u deze bestanden naar de subdirectory `lib/java` van uw installatiedirectory van de gegevenscrawler; u kunt ook de instelling `extra_jars_dir` in het bestand `crawler.conf` gebruiken om een andere locatie op te geven.

***MySQL JDBC-stuurprogramma's***
De Data Crawler wordt niet geleverd met de JDBC-stuurprogramma's voor MySQL vanwege mogelijke problemen met de licentiëring als ze als onderdeel van het product zouden worden geleverd. Het downloaden van het JAR-bestand met de MySQL JDBC-stuurprogramma's en het integreren van dat JAR-bestand in uw installatie van de datacrawler is echter heel eenvoudig uit te voeren:

1.	Gebruik een webbrowser om naar de MySQL-downloadsite te gaan en zoek de downloadlink voor bronbestanden en binaire bestanden in de archiefindeling die u wilt gebruiken (meestal zip voor Microsoft Windows-systemen of een gzipped tarball voor Linux-systemen). Klik op die link om het downloaden te starten. Het kan zijn dat u zich moet registreren.

2.	Gebruik de daarvoor bestemde opdracht `unzip ZIP-archief-bestandsnaam` of `tar-zxf archief-bestandsnaam` voor het extraheren van de inhoud van het archief, afhankelijk van het type en de naam van het archiefbestand dat u downloadt.

3.	Ga naar de directory die is opgehaald uit het archiefbestand en kopieer het JAR-bestand uit deze directory naar de subdirectory `lib/java` van de installatiedirectory van uw datacrawler; u kunt ook de instelling `extra_jars_dir` in het bestand `crawler.conf` gebruiken om een andere locatie op te geven.

Hieronder vindt u de opties voor de basisconfiguratie die vereist zijn voor het gebruik van de connector voor de database. Om deze waarden in te stellen, opent u het bestand `config/connectors/database.conf` en wijzigt u de volgende waarden voor uw gebruiksvoorbeelden:

*  **protocol** - De naam van het connectorprotocol dat voor het crawlproces wordt gebruikt. De waarde voor deze aansluiting is gebaseerd op het databasesysteem dat u opent.
*  **collection** - Dit kenmerk wordt gebruikt voor het uitpakken van tijdelijke bestanden.
*  **classname** - De java-klassennaam voor de connector. De waarde die voor deze connector moet worden gebruikt is `plugin:database.plugin@database`.
*  **logging-config** - Hiermee geeft u het bestand aan dat wordt gebruikt voor het configureren van opties voor logboekregistratie; het moet worden opgemaakt als een `log4j` XML-tekenreeks.

### De connector voor CMIS configureren
Met de CMIS-connector (Content Management Interoperability Services) kunt u crawlen in CMIS-geschikte CMS-repository's  (Content Management System), zoals Alfresco, Documentum of IBM Content Manager en de gegevens daarin indexeren.

Hieronder vindt u de opties voor de basisconfiguratie die vereist zijn voor het gebruik van de CMIS-connector. Om deze waarden in te stellen, opent u het bestand `config/connectors/cmis.conf` en wijzigt u de volgende waarden voor uw gebruiksvoorbeelden:

*  **protocol** - De naam van het connectorprotocol dat voor het crawlproces wordt gebruikt. Gebruik `cmis` voor deze connector.
*  **collection** - Dit kenmerk wordt gebruikt voor het uitpakken van tijdelijke bestanden.
*  **dns** - Ongebruikte optie.
*  **classname** - De java-klassennaam voor de connector. De waarde die voor deze connector moet worden gebruikt is `plugin:cmis-v1.1.plugin@connector`.
*  **logging-config** - Hiermee geeft u het bestand aan dat wordt gebruikt voor het configureren van opties voor logboekregistratie; het moet worden opgemaakt als een `log4j` XML-tekenreeks.
*  **endpoint** - De URL van het service-eindpunt van een CMIS-compatibele repository. De URL-structuren voor SharePoint zijn bijvoorbeeld:
   *  Voor een AtomPub-binding:   
      http://<server>:<poort>/_vti_bin/cmis/rest?getRepositories
   *  Voor een WebServices-binding:   
      http://<server>:<poort>/_vti_bin/cmissoapwsdl.aspx

*  **username** - De gebruikersnaam van de gebruiker van de CMIS-repository die wordt gebruikt voor toegang tot de content. Deze gebruiker moet toegang hebben tot alle doelmappen en -documenten die moeten worden gecrawld en geïndexeerd.
*  **password** - Het wachtwoord van de CMIS-repository die wordt gebruikt voor toegang tot de content. Het wachtwoord mag NIET worden versleuteld; het moet in platte tekst opgegeven worden.
*  **repositoryid** - Het ID van de CMIS-repository die wordt gebruikt voor toegang tot de content van die specifieke repository.
*  **bindingtype** - Geeft aan welk bindingstype moet worden gebruikt om verbinding te maken met een CMIS-repository. De waarde is `AtomPub` of `WebServices`.
*  **authentication** - Geeft aan welk type verificatiemechanisme moet worden gebruikt bij het aanroepen van een CMIS-compatibele repository: `HTTP-standaardverificatie`, `NTLM` of `WS-Security (token voor gebruikersnaam)`.
*  **enable-acl** - Hiermee schakelt u het ophalen van toegangslijsten voor gecrawlde gegevens in. Als u zich geen zorgen maakt over beveiliging van de documenten in deze collectie, schakelt u de optie uit; dit verhoogt de performance omdat er geen informatie bij het document wordt aangevraagd en deze informatie niet hoeft te worden opgehaald en versleuteld. De waarde is `true` of `false`.
*  **user-agent** - Een header die naar de server verzonden wordt bij het crawlen van documenten.
*  **method** - De methode (`GET` of `POST`) waarmee parameters worden doorgegeven.
*  **url-logging** - De mate waarin gecrawlde URL's in het logboek worden vastgelegd. Mogelijke waarden zijn:

   *  ***full-logging*** - Alle informatie over de URL vastleggen.
   *  ***refined-logging*** - Alleen de gegevens vastleggen die nodig zijn om door het crawlerlogboek te bladeren en om de connector correct te laten functioneren; dit is de standaardwaarde.
   *  ***minimal-logging*** - Alleen de minimale gegevens vastleggen die nodig zijn om de connector correct te laten functioneren.

   Als u deze optie op minimal-logging instelt, wordt de grootte van de logboeken verkleind en wint u wat snelheid door de kleinere hoeveelheid I/O die samenhangt met het minimaliseren van de hoeveelheid vastgelegde informatie. 
*  **ssl-version** - Geeft een versie van SSL voor HTTPS-verbindingen aan. Standaard wordt het beste protocol gebruikt dat beschikbaar is.

### De connector voor SMB/CIFS/Samba configureren
Met de Samba-connector kunt u door SMB- (Server Message Block) en CIFS-fileshares (Common Internet Filesystem) crawlen. Dit type fileshare wordt veel gebruikt op Windows-netwerken en wordt ook geleverd via het open source-project [Samba](https://www.samba.org/).

Hieronder vindt u de opties voor de basisconfiguratie die vereist zijn voor het gebruik van de Samba-connector. Om deze waarden in te stellen, opent u het bestand `config/connectors/samba.conf` en wijzigt u de volgende waarden voor uw gebruiksvoorbeelden:

*  **protocol** - De naam van het connectorprotocol dat voor het crawlproces wordt gebruikt. De waarde die voor deze connector moet worden gebruikt is `smb`.
*  **collection** - Dit kenmerk wordt gebruikt voor het uitpakken van tijdelijke bestanden.
*  **classname** - De java-klassennaam voor de connector. De waarde die voor deze connector moet worden gebruikt is `plugin:smb.plugin@connector`.
*  **logging-config** - Hiermee geeft u het bestand aan dat wordt gebruikt voor het configureren van opties voor logboekregistratie; het moet worden opgemaakt als een `log4j` XML-tekenreeks.
*  **username** - De Samba-gebruikersnaam voor verificatie. Als u dit opgeeft, moet u ook een domein en wachtwoord opgeven. Als dit niet wordt opgegeven, wordt het gastaccount gebruikt.
*  **password** - Het Samba-wachtwoord voor verificatie. Als de gebruikersnaam opgegeven wordt, is dit verplicht. Het wachtwoord moet worden versleuteld met de VCrypt-bibliotheek die bij de datacrawler geleverd is.
*  **archive** - Hiermee zorgt u ervoor dat de Samba-connector bestanden gaat crawlen en indexeren die zijn gecomprimeerd in archiefbestanden. De waarde is `true` of `false`; de standaardwaarde is `false`.
*  **max-policies-per-handle** - Geeft het maximumaantal LSA-beleidsdefinities (Local Security Authority) aan dat kan worden geopend voor een enkele RPC-handle. Deze beleidsdefinities definiëren de toegangsmachtigingen die onder verschillende omstandigheden nodig zijn voor het doorzoeken of wijzigen van een bepaald systeem. De standaardwaarde voor deze optie is `255`.
*  **crawl-fs-metadata** - Als u deze optie inschakelt, zorgt dit ervoor dat de datacrawler een VXML-document toevoegt dat de beschikbare metagegevens over het bestand van het bestandssysteem bevat (aanmaakdatum, laatste wijzigingsdatum, bestandskenmerken, enz.)
*  **enable-arc-connector** - Ongebruikte optie.
*  **disable-indexes** - Door terugloop-met-nieuwe-regel gescheiden lijst van indexen die uitgeschakeld moeten worden; dit kan leiden tot een snellere crawl. Bijvoorbeeld:

   *  disable-url-index
   *  disable-error-state-index
   *  disable-crawl-time-index
*  **exact-duplicates-hash-size** - Hiermee kunt u de grootte van de hashtabel instellen die wordt gebruikt voor het omzetten van exacte duplicaten. Wees zeer voorzichtig bij het wijzigen van dit getal. De waarde die u selecteert moet goed doordacht zijn: een grotere omvang kan leiden tot snellere zoekopdrachten maar vereist meer geheugen, bij kleinere omvang wordt de crawl trager maar het geheugengebruik substantieel gereduceerd.
*  **user-agent** - Ongebruikte optie.
*  **timeout** - Ongebruikte optie.
*  **n-concurrent-requests** - Het aantal aanvragen dat parallel naar een enkel IP-adres wordt verzonden. De standaardwaarde is `1`.
*  **enqueue-persistence** - Ongebruikte optie.

### De connector voor SharePoint configureren
Met de SharePoint-connector kunt u objecten van SharePoint Server en SharePoint Online crawlen en de gegevens indexeren die ze bevatten. Objecten zoals een document, gebruikersprofiel, websitecollectie, blog, listitem, lidmaatschapslijst, adresboekpagina en meer kunnen worden geïndexeerd, samen met de bijbehorende metagegevens. Bij lijst-items en documenten kunnen indexen bijlagen bevatten. 

**Opmerking**: De SharePoint-connector houdt rekening met het kenmerk `noindex` op alle SharePoint-objecten, ongeacht hun specifieke type (blogs, documenten, gebruikersprofielen enz). Voor elk resultaat wordt een enkel document weergegeven.

**Belangrijk**: Het SharePoint-account dat u gebruikt voor het crawlen van uw SharePoint-sites moet ten minste volledige leestoegang hebben.

Hieronder vindt u de opties voor de basisconfiguratie die vereist zijn voor het gebruik van de SharePoint-connector. Om deze waarden in te stellen, opent u het bestand `config/connectors/sharepoint.conf` en wijzigt u de volgende waarden voor uw gebruiksvoorbeelden:

*  **protocol** - De naam van het connectorprotocol dat voor het crawlproces wordt gebruikt. Gebruik `io-sp` voor deze connector.
*  **collection** - Dit kenmerk wordt gebruikt voor het uitpakken van tijdelijke bestanden.
*  **classname** - De java-klassennaam voor de connector. De waarde die voor deze connector moet worden gebruikt is `plugin:io-sharepoint.plugin@connector`.
*  **logging-config** - Hiermee geeft u het bestand aan dat wordt gebruikt voor het configureren van opties voor logboekregistratie; het moet worden opgemaakt als een `log4j` XML-tekenreeks.
*  **seed-url-type** - Geeft aan naar welke type SharePoint-object de verstrekte seed-URL's verwijzen: siteverzamelingen of webapplicaties (ook wel virtuele servers genoemd).

   *  ***Site Collections*** - Als het type seed-URL ingesteld is op `Site Collections`, worden alleen de onderliggende items van de websitecollectie gecrawld waarnaar door de URL wordt verwezen.

   *  ***Web Applications*** - Als het type seed-URL is ingesteld op `Web Applications`, worden alle sitecollecties (en de bijbehorende onderliggende objecten) van de webtoepassingen waarnaar door elke URL wordt verwezen, gecrawld.
*  **auth-type** - Het verificatiemechanisme dat moet worden gebruikt bij het maken van contact met de SharePoint-server: `BASIC`, `NTLM2`, `KERBEROS`, of `CBA`. Het standaard verificatietype is `NTLM2`.
*  **spUser** - De gebruikersnaam van de gebruiker van SharePoint die wordt gebruikt voor toegang tot de content. Deze gebruiker moet toegang hebben tot alle doelsites en -lijsten die moeten worden gecrawld en geïndexeerd, en moet in staat zijn de bijbehorende machtigingen op te halen en om te zetten. Het is beter om er binnen te gaan met de domeinnaam, zoals: `MYDOMAIN\\beheerder`.
*  **spPassword** - Het wachtwoord van de gebruiker van SharePoint die wordt gebruikt voor toegang tot de content. Het wachtwoord moet worden versleuteld met het programma VCrypt dat bij de datacrawler geleverd is.
*  **cba-sts** - De URL voor het STS-eindpunt (Security Token Service) waarmee wordt geprobeerd de gebruiker te verifiëren. Bij SharePoint ter plaatse met ADFS, moet dit uw ADFS-eindpunt zijn. Als het verificatietype is ingesteld op `CBA` (Claims Based Authentication), dan is dit een verplicht veld.
*  **cba-realm** - Het trust-ID van de doorzendende partij dat gebruikt wordt bij het aanvragen van een beveiligingstoken vanuit de STS. Dit staat ook wel bekend als de waarde voor "AppliesTo", of de "Realm". Bij SharePoint Online moet dit de URL zijn naar de hoofdmap van de SharePoint Online-instance (bijvoorbeeld `https://mycompany.sharepoint.com`). Voor ADFS is dit de ID-waarde voor de Relying Party Trust tussen SharePoint en ADFS (bijvoorbeeld, `"urn:SHAREPOINT:adfs"`).
*  **everyone-group** - Als u deze optie opgeeft, wordt deze groepsnaam in de toegangslijsten gebruikt voor het opgeven van toegang voor iedereen. Dit veld is verplicht als het crawlen van gebruikersprofielen ingeschakeld is. **Opmerking** - bij de service Retrieve and Rank wordt beveiliging nog niet gebruikt.
*  **user-profile-master-url** - De basis-URL die de connector gebruikt voor het bouwen van links naar gebruikersprofielen. Deze moet zo worden geconfigureerd dat hij verwijst naar het weergaveformulier voor gebruikersprofielen. Als het token `%FIRST_SEED%` wordt aangetroffen, wordt dit vervangen door de eerste seed-URL. Verplicht als het crawlen van gebruikersprofielen ingeschakeld is.
*  **urls** - Een door terugloop-met-nieuwe-regel gescheiden lijst met HTTP-URL's van SharePoint-webtoepassingen of siteverzamelingen die gecrawld worden. 
*  **ehcache-config** - Ongebruikte optie.
*  **method** - De methode (`GET` of `POST`) waarmee parameters worden doorgegeven.
*  **cache-types** - Ongebruikte optie.
*  **cache-size** - Ongebruikte optie.
*  **enable-acl** - Hiermee schakelt u het crawlen van SharePoint-gebruikersprofielen in; waarden zijn `true` of `false`. De standaardwaarde is `false`.

### De connector voor Box configureren
Met de Box-connector kunt u uw instance van Enterprise Box crawlen en de informatie erin indexeren. Hieronder vindt u de opties voor de basisconfiguratie die vereist zijn voor het gebruik van de Box-connector. Om deze waarden in te stellen, opent u het bestand `config/connectors/box.conf` en wijzigt u de volgende waarden voor uw gebruiksvoorbeelden:

*  **protocol** - De naam van het connectorprotocol dat voor het crawlproces wordt gebruikt. Gebruik `box` voor deze connector.
*  **classname** - De java-klassennaam voor de connector. De waarde die voor deze connector moet worden gebruikt is `plugin:box.plugin@connector`.
*  **logging-config** - Hiermee geeft u het bestand aan dat wordt gebruikt voor het configureren van opties voor logboekregistratie; het moet worden opgemaakt als een `log4j` XML-tekenreeks.
*  **box-crawl-seed-url** - De basis-URL voor Box. De waarde voor deze connector is `box://app.box.com/`. U kunt verschillende typen URL's crawlen, bijvoorbeeld:

   *  ***Een gehele onderneming crawlen***: `box://app.box.com/`
   *  ***Een specifieke map crawlen***: `box://app.box.com/user/USER_ID/folder/FOLDER_ID/FolderName`
   *  ***Een specifieke gebruiker crawlen***: `box://app.box.com/user/USER_ID`
*  **client-id** - Geef het client-ID op dat door Box is verstrekt op het moment dat u de Box-toepassing maakte. 
*  **client-secret** - Geef het clientgeheim op dat door Box is verstrekt op het moment dat u de Box-toepassing maakte.
*  **path-to-private-key** - Dit is de locatie, op uw lokale bestandssysteem, van de persoonlijke sleutel die deel uitmaakt van het persoonlijke-openbare sleutelpaar dat is gegenereerd voor communicatie met Box.
*  **kid** - Geef het ID van de openbare sleutel op. Dit is de andere helft van het persoonlijke-openbare sleutelpaar dat is gegenereerd voor communicatie met Box.
*  **enterprise-id** - De onderneming waarin uw toepassing geautoriseerd is. Het ondernemings-ID wordt vermeld op de hoofdpagina van de beheerdersconsole van Box. 
*  **enable-acl** - Alleen voor intern gebruik. Hiermee schakelt u het ophalen van toegangslijsten voor gecrawlde gegevens in.
*  **user-agent** - Een header die naar de server verzonden wordt bij het crawlen van documenten.
*  **method** - De methode (`GET` of `POST`) waarmee parameters worden doorgegeven.
*  **url-logging** - De mate waarin gecrawlde URL's in het logboek worden vastgelegd. Mogelijke waarden zijn:

   *  ***full-logging*** - Alle informatie over de URL vastleggen.
   *  ***refined-logging*** - Alleen de gegevens vastleggen die nodig zijn om door het crawlerlogboek te bladeren en om de connector correct te laten functioneren; dit is de standaardwaarde.
   *  ***minimal-logging*** - Alleen de minimale gegevens vastleggen die nodig zijn om de connector correct te laten functioneren.

   Als u deze optie op minimal-logging instelt, wordt de grootte van de logboeken verkleind en wint u wat snelheid door de kleinere hoeveelheid I/O die samenhangt met het minimaliseren van de hoeveelheid vastgelegde informatie.
*  **ssl-version** - Geeft een versie van SSL voor HTTPS-verbindingen aan. Standaard wordt het beste protocol gebruikt dat beschikbaar is.

De Box-connector heeft een aantal beperkingen:

* Commentaar of taken voor bestanden worden niet opgehaald.
* De lopende tekst van opmerkingen wordt opgehaald in de vorm van JSON. Aanvullende conversie van opmerkingsgegevens kan vereist zijn.
* Afzonderlijke documenten kunnen niet via TestIt worden opgehaald. Alleen seed-URL's, map-URL's en  gebruikers-URL's kunnen via TestIt opgehaald worden.


## ZIE OOK

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
