# Configuration des options d'exploration
Data Crawler collecte les données brutes qui seront utilisées pour constituer les résultats de recherche du service IBM Watson Retrieve and Rank.

Data Crawler fournit actuellement des connecteurs pour prendre en charge la collecte de données à partir des référentiels suivants :

*	Système de fichiers
*	Bases de données, via JDBC
*	CMIS (Content Management Interoperability Services)
*	Partages de fichiers SMB (Server Message Block), CIFS (Common Internet Filesystem) ou Samba
*	SharePoint et SharePoint Online
*	Box

Un modèle de configuration de connecteur est également fourni, pour vous permettre de personnaliser un connecteur. 

## Initiation
Lorsqu'il explore des référentiels de données, le moteur d'exploration commence à une adresse URL de départ spécifiée par l'utilisateur et commence à télécharger des pages d'informations. Il repère également les liens dans les pages téléchargées et planifie les pages nouvellement découvertes pour une exploration plus approfondie. 

Les informations de configuration permettent de déterminer les pages à explorer et la manière de les explorer. Ce fichier explique les options que vous pouvez configurer pour chaque connecteur. 

**Remarque** : chaque connecteur possède également un fichier de configuration de départ correspondant ; les options de configuration de départ sont décrites séparément. 

### Configuration du connecteur de système de fichiers
Le connecteur de système de fichiers vous permet d'explorer les fichiers locaux de l'installation de Data Crawler. Vous trouverez ci-après les options de configuration de base requises pour utiliser le connecteur de système de fichiers. Pour définir ces valeurs, ouvrez le fichier `config/connectors/filesystem.conf` et modifiez les valeurs suivantes spécifiques à vos cas d'utilisation :

*  **protocol** - Nom du protocole de connecteur utilisé pour l'exploration. Utilisez `sdk-fs` pour ce connecteur. 
*  **collection** - Cet attribut permet de décompresser les fichiers temporaires. 
*  **logging-config** - Spécifie le fichier utilisé pour configurer les options de consignation ; il doit être formaté sous forme de chaîne XML `log4j`.
*  **classname** - Nom de classe Java du connecteur. Pour utiliser ce connecteur, la valeur doit être `plugin:filesystem.plugin@filesystem`.

### Configuration du connecteur de base de données
Le connecteur de base de données vous permet d'explorer une base de données en exécutant une commande SQL personnalisée et en créant un document par ligne (enregistrement) et un élément de contenu par colonne (zone). Vous pouvez spécifier une colonne à utiliser comme clé unique, ainsi qu'une colonne contenant un horodatage représentant la date de la dernière modification de chaque enregistrement. Le connecteur extrait tous les enregistrements de la base de données spécifiée et peut être également restreint à des tables ou jointures spécifiques dans l'instruction SQL.

Le connecteur de base de données vous permet d'explorer les bases de données suivantes : 

*  IBM DB2
*  MySQL
*  Oracle
*  PostgreSQL
*  Microsoft SQL Server
*  Sybase
*  Autres bases de données compatibles SQL via un pilote compatible JDBC 3.0

Le connecteur extrait tous les enregistrements de la base de données et de la table spécifiées. 

**Pilotes JDBC**
Le connecteur de base de données est fourni avec le pilote Oracle JDBC (Java Database Connectivity) version 1.5. Tous les pilotes JDBC tiers fournis avec Data Crawler se trouvent dans le répertoire `/lib/java/database` de votre installation Data Crawler, dans lequel vous pouvez en ajouter, en supprimer et en modifier, si nécessaire. Vous pouvez également utiliser le paramètre `extra_jars_dir` du fichier `crawler.conf` pour spécifier un autre emplacement.

***Pilotes JDBC DB2***
Data crawler n'est pas fourni avec les pilotes JDBC pour DB2 en raison de problèmes de licence. Toutefois, toutes les installations DB2 dans lesquelles vous avez installé le support JDBC incluent les fichiers JAR requis par Data Crawler, pour pouvoir explorer une installation DB2. Pour explorer une instance DB2, vous devez copier ces fichiers dans le répertoire approprié de votre installation Data Crawler pour que le connecteur de base de données puisse les utiliser. 

Pour permettre à Data Crawler d'explorer une installation DB2, recherchez le fichier `db2jcc.jar` et les fichiers JAR de licence (généralement, `db2jcc_license_cu.jar`) dans votre installation DB2 et copiez-les dans le sous-répertoire `lib/java` de votre répertoire d'installation Data Crawler ; vous pouvez également utiliser le paramètre `extra_jars_dir` du fichier `crawler.conf` pour spécifier un autre emplacement.

***Pilotes JDBC MySQL***
Data Crawler n'est pas fourni avec les pilotes JDBC pour MySQL en raison d'éventuels problèmes de licence si les pilotes ont été distribués comme partie intégrante du produit. Toutefois, il est facile de télécharger le fichier JAR contenant les pilotes JDBC MySQL et de l'intégrer dans votre installation Data Crawler :

1.	Utilisez un navigateur Web pour visiter le site de téléchargement de MySQL et rechercher le lien de téléchargement de la source et du binaire pour le format d'archive à utiliser (généralement zip pour les systèmes Microsoft Windows et fichier compressé gzipped pour les systèmes Linux). Cliquez sur ce lien pour lancer le processus de téléchargement. L'inscription peut être requise. 

2.	Utilisez la commande `unzip archive-file-name` ou `tar zxf archive-file-name` appropriée pour extraire le contenu de cette archive, en fonction du type et du nom du fichier archive que vous téléchargez.

3.	Accédez au répertoire extrait du fichier archive et copiez le fichier JAR de ce répertoire dans le sous-répertoire `lib/java` de votre répertoire d'installation Data Crawler ; vous pouvez également utiliser le paramètre `extra_jars_dir` du fichier `crawler.conf` pour spécifier un autre emplacement.

Vous trouverez ci-après les options de configuration de base requises pour utiliser le connecteur de base de données. Pour définir ces valeurs, ouvrez le fichier `config/connectors/database.conf` et modifiez les valeurs suivantes spécifiques à vos cas d'utilisation :

*  **protocol** - Nom du protocole de connecteur utilisé pour l'exploration. La valeur de ce connecteur est basée sur le système de base de données à atteindre. 
*  **collection** - Cet attribut permet de décompresser les fichiers temporaires. 
*  **classname** - Nom de classe Java du connecteur. Pour utiliser ce connecteur, la valeur doit être `plugin:database.plugin@database`.
*  **logging-config** - Spécifie le fichier utilisé pour configurer les options de consignation ; il doit être formaté sous forme de chaîne XML `log4j`.

### Configuration du connecteur CMIS
Le connecteur CMIS (Content Management Interoperability Services) vous permet d'explorer des référentiels CMS (Content Management System) compatibles CMIS, tels que Alfresco, Documentum ou IBM Content Manager, et d'indexer les données qu'ils contiennent. 

Vous trouverez ci-après les options de configuration de base requises pour utiliser le connecteur CMIS. Pour définir ces valeurs, ouvrez le fichier `config/connectors/cmis.conf` et modifiez les valeurs suivantes spécifiques à vos cas d'utilisation :

*  **protocol** - Nom du protocole de connecteur utilisé pour l'exploration. Utilisez `cmis` pour ce connecteur. 
*  **collection** - Cet attribut permet de décompresser les fichiers temporaires. 
*  **dns** - Option inutilisée.
*  **classname** - Nom de classe Java du connecteur. Pour utiliser ce connecteur, la valeur doit être `plugin:cmis-v1.1.plugin@connector`.
*  **logging-config** - Spécifie le fichier utilisé pour configurer les options de consignation ; il doit être formaté sous forme de chaîne XML `log4j`.
*  **endpoint** - Adresse URL du noeud final de service d'un référentiel compatible CMIS. Par exemple, les structures d'adresse URL pour SharePoint sont les suivantes : 
   *  Pour une liaison AtomPub :   
      http://<serveur>:<port>/_vti_bin/cmis/rest?getRepositories
   *  Pour une liaison WebServices :   
      http://<serveur>:<port>/_vti_bin/cmissoapwsdl.aspx

*  **username** - Nom d'utilisateur de l'utilisateur de référentiel CMIS utilisé pour accéder au contenu. Cet utilisateur doit avoir accès à tous les dossiers cible et documents à explorer et indexer.
*  **password** - Mot de passe du référentiel CMIS utilisé pour accéder au contenu. Le mot de passe ne doit PAS être chiffré ; il doit être spécifié en texte en clair. 
*  **repositoryid** - ID du référentiel CMIS permettant d'accéder au contenu de ce répertoire spécifique. 
*  **bindingtype** - Identifie le type de liaison permettant de se connecter à un référentiel CMIS. La valeur admise est `AtomPub` ou `WebServices`.
*  **authentication** - Identifie le type de mécanisme d'authentification à utiliser pour contacter un référentiel compatible CMIS : `Basic HTTP Authentication`, `NTLM` ou `WS-Security(Username token)`.
*  **enable-acl** - Permet d'extraire les listes de contrôle d'accès des données explorées. Si vous n'êtes pas préoccupé par la sécurité pour les documents de cette collection, la désactivation de cette option améliore les performances car ces informations ne sont pas demandées avec le document et elles ne sont donc ni extraites, ni codées. La valeur admise est `true` ou `false`.
*  **user-agent** - En-tête envoyé au serveur lors de l'exploration de documents.
*  **method** - Méthode (`GET` ou `POST`) par laquelle les paramètres seront transmis. 
*  **url-logging** - Mesure dans laquelle les adresses URL explorées sont consignées. Les valeurs possibles sont :

   *  ***full-logging*** - Consigne toutes les informations sur l'adresse URL.
   *  ***refined-logging*** - Ne consigne que les informations nécessaires pour parcourir le journal du moteur d'exploration et pour que le connecteur fonctionne correctement ; il s'agit de la valeur par défaut. 
   *  ***minimal-logging*** - Ne consigne que la quantité minimale d'informations nécessaire pour que le connecteur fonctionne correctement.

   Si vous choisissez la valeur minimal-logging pour cette option, la taille des journaux est réduite et les performances sont légèrement améliorées en raison de la moindre quantité d'E/S associée à la minimisation de la quantité de données consignées.
*  **ssl-version** - Spécifie une version de SSL à utiliser pour les connexions HTTPS. Par défaut le protocole le plus fort disponible est utilisé. 

### Configuration du connecteur SMB/CIFS/Samba
Le connecteur Samba vous permet d'explorer les partages de fichiers SMB (Server Message Block) et CIFS (Common Internet Filesystem). Ce type de partage est courant sur les réseaux Windows et est également fourni par l'intermédiaire du projet open source [Samba](https://www.samba.org/).

Vous trouverez ci-après les options de configuration de base requises pour utiliser le connecteur Samba. Pour définir ces valeurs, ouvrez le fichier `config/connectors/samba.conf` et modifiez les valeurs suivantes spécifiques à vos cas d'utilisation :

*  **protocol** - Nom du protocole de connecteur utilisé pour l'exploration. La valeur à utiliser pour ce connecteur est `smb`.
*  **collection** - Cet attribut permet de décompresser les fichiers temporaires. 
*  **classname** - Nom de classe Java du connecteur. Pour utiliser ce connecteur, la valeur doit être `plugin:smb.plugin@connector`.
*  **logging-config** - Spécifie le fichier utilisé pour configurer les options de consignation ; il doit être formaté sous forme de chaîne XML `log4j`.
*  **username** - Nom d'utilisateur Samba permettant de s'authentifier. S'il est spécifié, le domaine et le mot de passe doivent l'être également. S'il ne l'est pas, le compte invité est utilisé. 
*  **password** - Mot de passe Samba permettant de s'authentifier. Si le nom d'utilisateur est spécifié, ce mot de passe est requis. Le mot de passe doit être chiffré à l'aide de la bibliothèque VCrypt fournie avec Data Crawler.
*  **archive** - Permet au connecteur Samba d'explorer et d'indexer les fichiers compressés dans les fichiers archive. Les valeurs possibles sont `true` et `false` ; la valeur par défaut est `false`.
*  **max-policies-per-handle** - Indique le nombre maximal de règles LSA (Local Security Authority) pouvant être ouvertes pour un même descripteur RPC. Ces règles définissent les droits d'accès requis pour interroger ou modifier un système particulier dans diverses conditions. La valeur par défaut de cette option est `255`. 
*  **crawl-fs-metadata** - Si cette option est désactivée, Data Crawler ajoute un document VXML contenant les métadonnées de système de fichiers disponibles sur le fichier (date de création, date de la dernière modification, attributs de fichier, etc.)
*  **enable-arc-connector** - Option inutilisée.
*  **disable-indexes** - Liste d'index à désactiver, séparés par des retours à la ligne, qui peut accélérer l'exploration. Par exemple :

   *  disable-url-index
   *  disable-error-state-index
   *  disable-crawl-time-index
*  **exact-duplicates-hash-size** - Définit la taille de la table de hachage utilisée pour résoudre les doublons exacts. Soyez très prudent lorsque vous modifiez ce nombre. La valeur que vous sélectionnez doit être primordiale ; des tailles plus grandes peuvent fournir des recherches plus rapides, mais nécessiteront davantage de mémoire, tandis que des tailles plus petites pourront ralentir les explorations, mais réduiront considérablement la quantité de mémoire requise. 
*  **user-agent** - Option inutilisée.
*  **timeout** - Option inutilisée.
*  **n-concurrent-requests** - Nombre de demandes qui seront envoyées en parallèle à une même adresse IP. La valeur par défaut est `1`.
*  **enqueue-persistence** - Option inutilisée.

### Configuration du connecteur SharePoint
Le connecteur SharePoint vous permet d'explorer des objets SharePoint Server et SharePoint Online et d'indexer les informations qu'ils contiennent. Un objet tel qu'un document, un profil utilisateur, une collecte de site, un blogue, un élément de liste, une liste d'appartenance ou encore une page d'annuaire, peut être indexé avec ses métadonnées associées. Pour les éléments de liste et les documents, les index peuvent inclure des pièces jointes. 

**Remarque** : le connecteur SharePoint respecte l'attribut `noindex` sur tous les objets SharePoint, quel que soit leur type (blogue, document, profil utilisateur, etc.). Un seul document est renvoyé pour chaque résultat.

**Important** : le compte SharePoint que vous utilisez pour explorer vos sites SharePoint doit disposer au minimum des droits d'accès en lecture complets. 

Vous trouverez ci-après les options de configuration de base requises pour utiliser le connecteur SharePoint. Pour définir ces valeurs, ouvrez le fichier `config/connectors/sharepoint.conf` et modifiez les valeurs suivantes spécifiques à vos cas d'utilisation :

*  **protocol** - Nom du protocole de connecteur utilisé pour l'exploration. Utilisez `io-sp` pour ce connecteur. 
*  **collection** - Cet attribut permet de décompresser les fichiers temporaires. 
*  **classname** - Nom de classe Java du connecteur. Pour utiliser ce connecteur, la valeur doit être `plugin:io-sharepoint.plugin@connector`.
*  **logging-config** - Spécifie le fichier utilisé pour configurer les options de consignation ; il doit être formaté sous forme de chaîne XML `log4j`.
*  **seed-url-type** - Identifie le type d'objet SharePoint vers lequel pointent les adresses URL de départ : collections de site ou applications Web (également appelées serveurs virtuels).

   *  ***Site Collections*** - Si le type d'adresse URL de départ est défini sur `Site Collections`, seuls les enfants de la collecte de site sont référencés par l'adresse URL explorée. 
   *  ***Web Applications*** - Si le type d'adresse URL de départ est défini sur `Web Applications`, toutes les collections de site (et leurs enfants) appartenant aux applications Web référencées par chaque adresse URL sont explorées.
*  **auth-type** - Mécanisme d'authentification à utiliser lorsque vous contactez le serveur SharePoint : `BASIC`, `NTLM2`, `KERBEROS` ou `CBA`. Le type d'authentification par défaut est `NTLM2`.
*  **spUser** - Nom d'utilisateur de l'utilisateur SharePoint utilisé pour accéder au contenu. Cet utilisateur doit avoir accès à tous les sites cible, ainsi qu'à toutes les listes à explorer et indexer et doit pouvoir extraire et résoudre les droits associés. Il est préférable de l'entrer avec le nom de domaine. Par exemple : `MYDOMAIN\\Administrator`.
*  **spPassword** - Mot de passe de l'utilisateur SharePoint utilisé pour accéder au contenu. Le mot de passe doit être chiffré à l'aide du programme vcrypt fourni avec Data Crawler. 
*  **cba-sts** - Adresse URL du noeud final STS (Security Token Service) pour tenter d'authentifier l'utilisateur de l'exploration. Pour SharePoint sur site avec ADFS, il doit s'agir de votre noeud final ADFS. Si le type d'authentification est défini sur `CBA` (Claims Based Authentication), cette zone est requise.
*  **cba-realm** - Identificateur de l'approbation de partie de confiance à utiliser lors d'une demande de jeton de sécurité au service STS. Cette option est parfois appelée valeur "AppliesTo" ou "Domaine". Pour SharePoint Online, elle doit correspondre à l'adresse URL de la racine de l'instance SharePoint Online (par exemple, `https://mycompany.sharepoint.com`). Pour ADFS, il s'agit de la valeur de l'ID de l'approbation de partie de confiance entre SharePoint et ADFS (par exemple, `"urn:SHAREPOINT:adfs"`).
*  **everyone-group** - Si ce nom de groupe est spécifié, il est utilisé dans les listes de contrôle d'accès lorsque l'accès doit être octroyé à tous les utilisateurs. Cette zone est requise si l'exploration des profils utilisateur est activée. **Remarque** : la sécurité n'est pas encore respectée par le service Retrieve and Rank.
*  **user-profile-master-url** - Adresse URL de base utilisée par le connecteur pour générer les liens aux profils utilisateur. Elle doit être configurée pour pointer vers le formulaire d'affichage des profils utilisateur. Si le jeton `%FIRST_SEED%` est rencontré, il est remplacé par la première adresse URL de départ. Cette zone est requise si l'exploration des profils utilisateur est activée. 
*  **urls** - Liste d'adresses URL HTTP de collections de site ou d'applications Web SharePoint à explorer, séparées par des retours à la ligne. 
*  **ehcache-config** - Option inutilisée.
*  **method** - Méthode (`GET` ou `POST`) par laquelle les paramètres seront transmis. 
*  **cache-types** - Option inutilisée.
*  **cache-size** - Option inutilisée.
*  **enable-acl** - Active l'exploration des profils utilisateur SharePoint ; les valeurs possibles sont `true` et `false`. La valeur par défaut est `false`.

### Configuration du connecteur Box
Le connecteur Box vous permet d'explorer l'instance Box de votre entreprise et d'indexer les informations qu'elle contient. Vous trouverez ci-après les options de configuration de base requises pour utiliser le connecteur Box. Pour définir ces valeurs, ouvrez le fichier `config/connectors/box.conf` et modifiez les valeurs suivantes spécifiques à vos cas d'utilisation :

*  **protocol** - Nom du protocole de connecteur utilisé pour l'exploration. Utilisez `box` pour ce connecteur. 
*  **classname** - Nom de classe Java du connecteur. Pour utiliser ce connecteur, la valeur doit être `plugin:box.plugin@connector`.
*  **logging-config** - Spécifie le fichier utilisé pour configurer les options de consignation ; il doit être formaté sous forme de chaîne XML `log4j`.
*  **box-crawl-seed-url** - Adresse URL de base pour Box. La valeur de ce connecteur est `box://app.box.com/`. Vous pouvez explorer différents types d'adresse URL. Par exemple : 

   *  ***Pour explorer toute une entreprise*** : `box://app.box.com/`
   *  ***Pour explorer un dossier spécifique*** : `box://app.box.com/user/USER_ID/folder/FOLDER_ID/FolderName`
   *  ***Pour explorer un utilisateur spécifique*** : `box://app.box.com/user/USER_ID/`
*  **client-id** - Entrez l'ID client fourni par Box lorsque vous avez créé votre application Box.
*  **client-secret** - Entrez le secret client fourni par Box lorsque vous avez créé votre application Box.
*  **path-to-private-key** - Emplacement sur votre système de fichiers local de la clé privée qui fait partie de la paire de clés privée/publique générée pour les communications avec Box.
*  **kid** - Spécifie l'ID clé publique. Il s'agit de l'autre moitié de la paire de clés privée/publique générée pour les communications avec Box.
*  **enterprise-id** - Entreprise dans laquelle votre application a été autorisée. L'ID entreprise est indiqué dans la page principale de la console d'administrateur Box.
*  **enable-acl** - Usage interne uniquement. Permet d'extraire les listes de contrôle d'accès des données explorées. 
*  **user-agent** - En-tête envoyé au serveur lors de l'exploration de documents.
*  **method** - Méthode (`GET` ou `POST`) par laquelle les paramètres seront transmis. 
*  **url-logging** - Mesure dans laquelle les adresses URL explorées sont consignées. Les valeurs possibles sont :

   *  ***full-logging*** - Consigne toutes les informations sur l'adresse URL.
   *  ***refined-logging*** - Ne consigne que les informations nécessaires pour parcourir le journal du moteur d'exploration et pour que le connecteur fonctionne correctement ; il s'agit de la valeur par défaut. 
   *  ***minimal-logging*** - Ne consigne que la quantité minimale d'informations nécessaire pour que le connecteur fonctionne correctement.

   Si vous choisissez la valeur minimal-logging pour cette option, la taille des journaux est réduite et les performances sont légèrement améliorées en raison de la moindre quantité d'E/S associée à la minimisation de la quantité de données consignées.
*  **ssl-version** - Spécifie une verion de SSL à utiliser pour les connexions HTTPS. Par défaut le protocole le plus fort disponible est utilisé. 

Le connecteur Box possède certaines limitations :

* Les commentaires et les tâches sur les fichiers ne sont pas extraits. 
* Le corps du contenu des notes est extrait au format JSON. Une conversion supplémentaire des données de note peut être requise. 
* Les documents individuels ne peuvent pas être extraits via TestIt. Seules les adresses URL de départ, de dossier et d'utilisateur peuvent être extraites via TestIt.


## VOIR AUSSI

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
