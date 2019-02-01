# Configuratie van crawlseeds

Seeds vormen het uitgangspunt van een crawl en worden door de datacrawler gebruikt voor het ophalen van gegevens uit de resource die door die seed wordt aangegeven. De seeds configureren in het algemeen URL's om toegang te krijgen tot op protocol gebaseerde resources zoals fileshares, SMB-shares, databases en andere gegevens die toegankelijk zijn middels verschillende webprotocollen. Daarnaast hebben verschillende seed-URL's verschillende mogelijkheden.

Seeds kunnen ook specifiek voor een repository zijn om het crawlen van specifieke toepassingen van derden mogelijk te maken, bijvoorbeeld CRM-systemen (customer relationship management), PLC-systemen (product life cycle), CMS-systemen (content management systems), cloudtoepassingen en webdatabasetoepassingen.

De data crawler biedt op dit moment crawlseeds die ondersteuning bieden voor bestandsconnectors voor de volgende typen repository's:

*	Bestandssysteem
*	Databases, via JDBC
*	CMIS (Content Management Interoperability Services)
*	Bestandsshares van SMB (Server Message Block), CIFS (Common Internet Filesystem) of Samba
*	SharePoint en SharePoint Online
*	Box

Er is ook een configuratiesjabloon voor crawlseeds beschikbaar, waarmee u wijzigingen in een crawlseed kunt aanbrengen voor een aangepaste connector.

## Aan de slag:

Bij het crawlen van gegevensrepository's begint de crawler met een door de gebruiker opgegeven seed-URL en begint met het downloaden van pagina's met informatie. De crawler zoekt ook links in de gedownloade pagina's en plant de nieuw gevonden pagina's voor verdere crawls.

Er worden configuratiegegevens gebruikt om te bepalen welke pagina's moeten worden gecrawld en hoe u crawlt. In dit bestand vindt u een overzicht van de opties die u voor elk crawlseedbestand voor een connector kunt configureren.

**Opmerking**: Elk configuratiebestand voor een crawlseed werkt met een corresponderend configuratiebestand van de bestandsconnector; opties voor bestandsconnectors worden afzonderlijk beschreven.

### De crawlseed voor het bestandssysteem configureren

De volgende waarden kunnen worden geconfigureerd voor het crawlseedbestand voor het bestandssysteem. Om deze waarden in te stellen, opent u het bestand `config/seeds/filesystem-seed.conf` en geeft u de volgende waarden voor uw gebruiksvoorbeelden op:

*  **url** - Door terugloop-met-nieuwe-regel gescheiden lijst van bestanden en mappen die gecrawld worden. UNIX-gebruikers kunnen een pad zoals `/usr/local/` opgeven.
De URL's moet beginnen met `sdk-fs://`. Als u dus bijvoorbeeld `/home/watson/mydocs` wilt crawlen, is de waarde van deze URL `sdk-fs:///home/watson/mydocs` - de derde `/` is vereist!
**Opmerking**: De bestandssysteemconnector maakt gebruik van een aangepast protocol, `sdk-fs://`, voor het maken van een geldige URL. Voeg niet `file://` aan de afgebeelde paden toe; de URL's moet beginnen met `sdk-fs://`.
*  **hops** - Alleen voor intern gebruik.
*  **default-allow** - Alleen voor intern gebruik.

### De crawlseed voor de database configureren

De volgende waarden kunnen worden geconfigureerd voor het crawlseedbestand voor de database. Om deze waarden in te stellen, opent u het bestand `config/seeds/database-seed.conf` en geeft u de volgende waarden voor uw gebruiksvoorbeelden op:

*  **URL** - De URL van de tabel of de view om op te halen. Hiermee definieert u de seed-URL van uw aangepaste SQL-database. De structuur is:

   	`databasesysteem://host:poort/database?[per=num]&[sql=SQL]`

   Door het testen van een seed-URL ziet u alle URL's die in de wachtrij zijn geplaatst. Een voorbeeld is het testen van de volgende URL voor een database met 200 records:

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=100&sql=select%20*%20from%20vessel&`

   u ziet de volgende in de wachtrij geplaatste URL's:

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=0&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=100&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=200&`

   Bij het testen van de volgende URL ziet u de gegevens die zijn opgehaald uit rij 43:

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=1&key-val=43`
*  **hops** - Alleen voor intern gebruik.
*  **default-allow** - Alleen voor intern gebruik.
*  **user-password** - Legitimatiegegevens voor het databasesysteem. De gebruikersnaam en het wachtwoord moeten worden gescheiden door een `:` en het wachtwoord moet worden versleuteld met het programma vcrypt dat bij de Data Crawler wordt geleverd. Bijvoorbeeld `username:[[vcrypt/3]]passwordstring`.
*  **max-data-size** - Maximumgrootte van de gegevens van een document. Dit is het grootste geheugenblok dat op een bepaald moment wordt geladen. Verhoog deze limiet alleen als u beschikt over voldoende geheugen op uw computer.
*  **filter-exact-duplicates** - Alleen voor intern gebruik.
*  **jdbc-class** (Extender optie) - Als u deze optie opgeeft, vervangt deze reeks de JDBC-klasse die wordt gebruikt door de connector als `(other)` gekozen is voor het databasesysteem.
*  **connection-string** (Extender optie) - Als u deze optie opgeeft, vervangt deze reeks de automatisch gegenereerde JDBC-verbindingsreeks. Op deze manier kunt u een meer gedetailleerde configuratie van de databaseverbinding opgeven, bijvoorbeeld voor belastingsverdeling of SSL-verbindingen. Bijvoorbeeld: `jdbc:netezza://127.0.0.1:5480/databasenaam`.
*  **save-frequency-for-resume** (Extender optie) - De naam van een kolom of bijbehorend label, voor het hervatten van crawls of een gedeeltelijke vernieuwing. De seed slaat de naam van deze kolom met regelmatige intervallen op tijdens de crawl en slaat hem opnieuw op nadat de laatste rij van de database is gecrawld. Bij het hervatten of vernieuwen van de crawl begint de crawl met de rij die wordt aangegeven in de opgeslagen waarde voor dit veld.

### De crawlseed voor CMIS configureren

De volgende waarden kunnen worden geconfigureerd voor het CMIS-crawlseedbestand. Om deze waarden in te stellen, opent u het bestand `config/seeds/cmis-seed.conf` en wijzigt u de volgende waarden voor uw gebruiksvoorbeelden:

*  **URL** - De URL van een map in de CMIS-repository die wordt gebruikt als beginpunt van de crawl, bijvoorbeeld:

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=workspace://SpacesStore/guid`
   Voor het crawlen vanaf de hoofdmap moet u de URL als volgt opgeven:

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=`
*  **at** - Ongebruikte optie.
*  **default-allow** - Alleen voor intern gebruik.

### De crawlseed voor Samba configureren

De volgende waarden kunnen worden geconfigureerd voor het SAMBA-crawlseedbestand. Om deze waarden in te stellen, opent u het bestand `config/seeds/samba-seed.conf` en wijzigt u de volgende waarden voor uw gebruiksvoorbeelden:

*  **url** - Een door terugloop-met-nieuwe-regel gescheiden lijst van shares die gecrawld worden, bijvoorbeeld:

   *  `smb://share.test.com/office`
   *  `smb://share.test.com/cash/money/change`
   *  `smb://share.test.com/C$/Program Files`

*  **hops** - Alleen voor intern gebruik.
*  **default-allow** - Alleen voor intern gebruik.

### De crawlseed voor SharePoint configureren

De volgende extra waarden kunnen worden geconfigureerd voor het crawlseedbestand voor SharePoint. Om deze waarden in te stellen, opent u het bestand `config/seeds/sharepoint-seed.conf` en wijzigt u de volgende waarden voor uw gebruiksvoorbeelden:

*  **url** - Een door terugloop-met-nieuwe-regel gescheiden lijst van SharePoint-webtoepassingen of siteverzamelingen die gecrawld worden, bijvoorbeeld:

   *  `io-sp://a.com`
   *  `io-sp://b.com:83/site`
   *  `io-sp://c.com/site2`

   De subsites van deze sites worden ook gecrawld (tenzij ze zijn uitgesloten door andere regels voor crawlen). 
*  **filter-url** - Een door terugloop-met-nieuwe-regel gescheiden lijst van SharePoint-webtoepassingen of siteverzamelingen die gecrawld worden, bijvoorbeeld:

   *  `http://a.com`
   *  `http://b.com:83/site`
   *  `http://c.com/site2`

*  **hops** - Alleen voor intern gebruik.
*  **n-concurrent-requests** - Alleen voor intern gebruik.
*  **delay** - Alleen voor intern gebruik.
*  **default-allow** - Alleen voor intern gebruik.
*  **seed-protocol** - Hiermee stelt u het seedprotocol in voor onderliggende items van de websitecollectie. Dit is nodig als het protocol van de siteverzameling SSL, HTTP of HTTPS is. Voor deze waarde moet hetzelfde worden opgegeven als voor het protocol van de siteverzameling. 

### De seed voor Box configureren

De volgende waarden kunnen worden geconfigureerd voor het Box-crawlseedbestand. Om deze waarden in te stellen, opent u het bestand `config/seeds/box-seed.conf` en geeft u de volgende waarden voor uw gebruiksvoorbeelden op:

*  **url** - De URL die moet worden gebruikt als startpunt voor de crawl. De standaardwaarde is `box://app.box.com/`.
*  **default-allow** - Alleen voor intern gebruik.

## ZIE OOK

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

orchestration_service.conf(5)
