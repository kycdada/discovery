# Configuration des valeurs de départ d'exploration

Les valeurs de départ représentent les points de départ d'une exploration et sont utilisées par Data Crawler pour extraire les données de la ressource identifiées par ces valeurs de départ. Généralement, les valeurs de départ configurent des adresses URL pour accéder à des ressources basées sur des protocoles, telles que des partages de fichiers, des partages SMB, des bases de données et d'autres référentiels de données accessibles par divers protocoles Web. Les différentes adresses URL de départ ont également des fonctionnalités différentes. 

Les valeurs de départ peuvent également être spécifiques au référentiel, pour
permettre l'exploration d'applications tiers spécifiques, telles que des systèmes CRM
(Customer Relationship Management), des systèmes PLC (Product Life Cycle), des systèmes
CMS (Content Management System), des applications cloud et des applications de base de
données Web. 

Data Crawler fournit actuellement des valeurs de départ d'exploration qui prennent en charge les connecteurs de fichier des types de référentiel suivant :

*	Système de fichiers
*	Bases de données, via JDBC
*	CMIS (Content Management Interoperability Services)
*	Partages de fichiers SMB (Server Message Block), CIFS (Common Internet Filesystem) ou Samba
*	SharePoint et SharePoint Online
*	Box

Un modèle de configuration des valeurs de départ d'exploration est également fourni, pour vous permettre de personnaliser une valeur de départ d'exploration pour un connecteur personnalisé. 

## Initiation

Lorsqu'il explore des référentiels de données, le moteur d'exploration commence à une adresse URL de départ spécifiée par l'utilisateur et commence à télécharger des pages d'informations. Il repère également les liens dans les pages téléchargées et planifie les pages nouvellement découvertes pour une exploration plus approfondie. 

Les informations de configuration permettent de déterminer les pages à explorer et la manière de les explorer. Ce fichier explique les options que vous pouvez configurer pour le fichier de départ d'exploration de chaque connecteur. 

**Remarque** : le fichier de configuration de départ de chaque exploration fonctionne avec un fichier de configuration de connecteur de fichier correspondant ; les options du connecteur de fichier sont décrites séparément. 

### Configuration de la valeur de départ d'exploration du système de fichiers

Les valeurs suivantes peuvent être configurées pour le fichier de départ d'exploration du système de fichiers. Pour définir ces valeurs, ouvrez le fichier `config/seeds/filesystem-seed.conf` et spécifiez les valeurs suivantes spécifiques à vos cas d'utilisation :

*  **url** - Liste de fichiers et dossiers à explorer, séparés par des retours à la ligne. Les utilisateurs UNIX peuvent utiliser un chemin d'accès tel que le suivant : `/usr/local/`.
Les adresses URL doivent commencer par `sdk-fs://`. Par conséquent, pour explorer, par exemple, `/home/watson/mydocs`, la valeur de cette adresse URL doit être `sdk-fs:///home/watson/mydocs` (le troisième `/` est nécessaire !)
**Remarque** : le connecteur de système de fichiers utilise un protocole personnalisé, `sdk-fs://`, pour créer une adresse URL valide. Ne précédez pas de `file://` les chemins d'accès répertoriés ; les adresses URL doivent commencer par `sdk-fs://`.
*  **hops** - Usage interne uniquement. 
*  **default-allow** - Usage interne uniquement. 

### Configuration de la valeur de départ d'exploration de la base de données

Les valeurs suivantes peuvent être configurées pour le fichier de départ d'exploration de la base de données. Pour définir ces valeurs, ouvrez le fichier `config/seeds/database-seed.conf` et spécifiez les valeurs suivantes spécifiques à vos cas d'utilisation :

*  **url** - Adresse URL de la table ou vue à extraire. Définit l'adresse URL de départ personnalisée de votre base de données SQL. Sa structure est la suivante : 

   	`database-system://host:port/database?[per=num]&[sql=SQL]`

   Le test d'une adresse URL de départ permet d'afficher toutes les adresses URL placées en file d'attente. Par exemple, le test de l'adresse URL suivante d'une base de données contenant 200 enregistrements :

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=100&sql=select%20*%20from%20vessel&`

   affiche les adresses URL en file d'attente suivantes : 

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=0&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=100&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=200&`

   Lors des tests, l'adresse URL suivante affichera les données extraites de la ligne 43 :

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=1&key-val=43`
*  **hops** - Usage interne uniquement. 
*  **default-allow** - Usage interne uniquement. 
*  **user-password** - Données d'identification du système de base de données. Le nom d'utilisateur et le mot de passe doivent être séparés par un signe `:` et le mot de passe doit être chiffré à l'aide du programme vcrypt fourni avec Data Crawler. Par exemple `username:[[vcrypt/3]]passwordstring`.
*  **max-data-size** - Taille maximale des données d'un document. Il s'agit du bloc de mémoire le plus volumineux qui sera chargé en une fois. N'augmentez cette limite que si vous disposez d'une quantité de mémoire suffisante sur votre ordinateur. 
*  **filter-exact-duplicates** - Usage interne uniquement. 
*  **jdbc-class** (option Extender) - Si cette chaîne est spécifiée, elle remplace la classe JDBC utilisée par le connecteur lorsque l'option `(other)` est sélectionnée comme système de base de données.
*  **connection-string** (option Extender) - Si cette chaîne est spécifiée, elle remplace la chaîne de connexion JDBC générée automatiquement. Cela vous permet de fournir une configuration plus détaillée sur la connexion de base de données, comme l'équilibrage de charge ou les connexions SSL. Par exemple : `jdbc:netezza://127.0.0.1:5480/databasename`.
*  **save-frequency-for-resume** (option Extender) - Spécifie le nom d'une colonne ou d'un libellé associé, pour pouvoir reprendre une exploration ou effectuer une actualisation partielle. La valeur de départ sauvegarde le nom de cette colonne à intervalles réguliers au cours de l'exploration et la sauvegarde de nouveau une fois que la dernière ligne de votre base de données a été explorée. Lors de la reprise de l'exploration ou de son actualisation, l'exploration commence par la ligne identifiée dans la valeur sauvegardée pour cette zone. 

### Configuration de la valeur de départ d'exploration CMIS

Les valeurs suivantes peuvent être configurées pour le fichier de départ d'exploration CMIS. Pour définir ces valeurs, ouvrez le fichier `config/seeds/cmis-seed.conf` et modifiez les valeurs suivantes spécifiques à vos cas d'utilisation :

*  **url** - Adresse URL d'un dossier du référentiel CMIS à utiliser comme point de départ de l'exploration. Par exemple : 

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=workspace://SpacesStore/guid`
   Pour une exploration à partir du dossier racine, vous devez spécifier l'adresse URL comme suit : 

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=`
*  **at** - Option inutilisée.
*  **default-allow** - Usage interne uniquement. 

### Configuration de la valeur de départ d'exploration Samba

Les valeurs suivantes peuvent être configurées pour le fichier de départ d'exploration Samba. Pour définir ces valeurs, ouvrez le fichier `config/seeds/samba-seed.conf` et modifiez les valeurs suivantes spécifiques à vos cas d'utilisation :

*  **url** - Liste de partages à explorer, séparés par des retours à la ligne. Par exemple : 

   *  `smb://share.test.com/office`
   *  `smb://share.test.com/cash/money/change`
   *  `smb://share.test.com/C$/Program Files`

*  **hops** - Usage interne uniquement. 
*  **default-allow** - Usage interne uniquement. 

### Configuration de la valeur de départ d'exploration SharePoint

Les valeurs supplémentaires ci-après peuvent être configurées pour le fichier de départ d'exploration SharePoint. Pour définir ces valeurs, ouvrez le fichier `config/seeds/sharepoint-seed.conf` et modifiez les valeurs suivantes spécifiques à vos cas d'utilisation :

*  **url** - Liste de collections de site ou d'applications Web SharePoint à explorer, séparées par des retours à la ligne. Par exemple : 

   *  `io-sp://a.com`
   *  `io-sp://b.com:83/site`
   *  `io-sp://c.com/site2`

   Les sites secondaires de ces sites seront également explorés (à moins qu'ils ne soient exclus par d'autres règles d'exploration).
*  **filter-url** - Liste de collections de site ou d'applications Web SharePoint à explorer, séparées par des retours à la ligne. Par exemple : 

   *  `http://a.com`
   *  `http://b.com:83/site`
   *  `http://c.com/site2`

*  **hops** - Usage interne uniquement. 
*  **n-concurrent-requests** - Usage interne uniquement. 
*  **delay** - Usage interne uniquement. 
*  **default-allow** - Usage interne uniquement. 
*  **seed-protocol** - Définit le protocole des valeurs de départ des enfants de la collecte du site. Nécessaire si le protocole de la collecte du site est SSL, HTTP ou HTTPS. Cette valeur doit correspondre à celle du protocole de la collecte du site. 

### Configuration de la valeur de départ Box

Les valeurs suivantes peuvent être configurées pour le fichier de départ d'exploration Box. Pour définir ces valeurs, ouvrez le fichier `config/seeds/box-seed.conf` et spécifiez les valeurs suivantes spécifiques à vos cas d'utilisation :

*  **url** - Adresse URL à utiliser comme point de départ de l'exploration. La valeur par défaut est `box://app.box.com/`.
*  **default-allow** - Usage interne uniquement. 

## VOIR AUSSI

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

orchestration_service.conf(5)
