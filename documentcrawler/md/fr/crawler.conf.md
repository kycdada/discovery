# Configuration de Data Crawler

`crawler` requiert un fichier de configuration pour ses options. Des exemples de configuration sont fournis dans le répertoire `share` du répertoire d'installation du `moteur d'exploration`. Copiez ces exemples et modifiez-les. *Ne modifiez pas les exemples dans leur emplacement.*

Le fichier `crawler.conf` contient des informations qui indiquent au moteur d'exploration les fichiers à utiliser pour son exploration (adaptateur d'entrée),
la destination de la collection des fichiers explorés une fois l'exploration terminée (adaptateur de sortie) et les autres options de gestion des explorations. 

**Remarque** : tous les chemins d'accès aux fichiers sont relatifs au répertoire `config`, sauf indication contraire.

Les options pouvant être définies dans ce fichier sont les suivantes : 

## Adaptateur d'entrée
*  **class** - Usage interne uniquement ; définit la classe de l'adaptateur d'entrée de Data Crawler. La valeur par défaut est : `com.ibm.watson.crawler.connectorframeworkinputadapter.Crawl`.
*  **config** - Usage interne uniquement ; définit la configuration de la structure de connecteur. La clé de configuration par défaut à l'intérieur de ce bloc à transmettre à l'adaptateur d'entrée choisi est : `connector_framework`. **Remarque** : la structure de connecteur vous permet de communiquer avec vos données. Il peut s'agir de données internes à l'entreprise ou de données externes sur le Web ou dans le cloud. Les connecteurs permettent d'accéder à un certain nombre de sources de données différentes, tandis que la connexion est en fait contrôlée par le processus d'exploration. 
  -  **IMPORTANT** - Les données extraites par l'adaptateur d'entrée de la structure de connecteur sont mises en cache en local. Elles ne sont pas stockées sous forme chiffrée. Par défaut, les données sont mises en cache dans un répertoire temporaire dont le contenu doit être effacé au réamorçage et elles ne doivent être lisibles que par l'utilisateur qui a exécuté la commande du moteur d'exploration. Il est possible que ce répertoire puisse survivre au moteur d'exploration si la structure de connecteur devait disparaître avant de pouvoir nettoyer les fichiers après lui. Etudiez soigneusement l'emplacement de vos données en cache ; vous pouvez les placer sur un système de fichiers chiffré, mais soyez conscient de l'impact que cela pourrait avoir sur les performances. Vous seul pouvez déterminer l'équilibre approprié entre vitesse et sécurité pour vos explorations. 
*  **crawl_config_file** - Fichier de configuration à utiliser pour l'exploration. La valeur par défaut est : `connectors/filesystem.conf`.
*  **crawl_seed_file** - Fichier de départ de l'exploration à utiliser pour l'exploration. La valeur par défaut est : `seeds/filesystem-seed.conf`.
*  **id_vcrypt_file** - Fichier de clés utilisé pour le chiffrement des données par le moteur d'exploration ; la clé par défaut incluse avec le moteur d'exploration est `id_vcrypt`.
Utilisez le script vcrypt du dossier `bin` si vous devez générer un nouveau fichier id_vcrypt_file
*  **crawler_temp_dir** - Dossier temporaire du moteur d'exploration pour les journaux du connecteur. La valeur par défaut, `tmp`, est fournie. S'il n'existe pas déjà, le dossier `tmp` est créé dans le répertoire de travail en cours. 
*  **extra_jars_dir** - Usage interne uniquement ; ajoute des fichiers JAR supplémentaires au chemin d'accès aux classes de la structure de connecteur.
Cette valeur doit être `oakland` si le connecteur SharePoint et utilisé et `database` si le connecteur de base de données est utilisé. Vous pouvez la laisser vide (chaine vide "") si vous utilisez d'autres connecteurs.
  **Remarque** : relatif au répertoire `lib/java` de la structure de connecteur. 
*  **urls_to_filter** - Liste blanche d'adresses URL à explorer, sous forme d'expression régulière, séparées par des retours à la ligne. Data Crawler n'explore que les adresses URL qui correspondent à l'une des expressions régulières fournies. La liste des domaines contient les domaines de niveau supérieur les plus courants ; ajoutez-en si nécessaire. La liste des types d'extension de fichier contient les extensions de fichier prises en charge par le service d'orchestration, pour cette version de Data Crawler. Vérifiez que le domaine de votre adresse URL de départ est autorisé par le filtre. Par exemple, si l'adresse URL de départ est semblable à `http://testdomain.test.in`, ajoutez"`in`" au filtre de domaines. Vérifiez que votre adresse URL de départ ne sera pas exclue par un filtre, faute de quoi, le moteur d'exploration pourrait se bloquer. 
*  **max_text_size** - Taille maximale, en octets, d'un document avant que ce dernier ne soit enregistré sur le disque par la structure de connecteur. Si vous spécifiez une taille supérieure, la quantité de documents enregistrés sur le disque diminuera, mais la quantité de mémoire requise augmentera. 
*  **extra_vm_params** - Permet d'ajouter des paramètres Java supplémentaires à la commande utilisée pour lancer la structure de connecteur.
*  **bootstrap_logging** - Enregistre le journal de démarrage de la structure de connecteur ; utile uniquement pour un débogage avancé. Les valeurs possibles sont `true` et `false`. Le fichier journal sera enregistré dans `crawler_temp_dir`.

## Adaptateur de stockage

Permet de stocker l'état interne du moteur d'exploration dans une base de données. Ce paramètre est nécessaire pour que les options `restart` et `resume` des explorations fonctionnent correctement.

```javascript
storage_adapter {
 config = "storage_in_db"
  storage_in_db {
    include "storage/database_storage.conf"
  } 
}
```
Le fichier référencé, `storage/database_storage.conf`, utilise par défaut une base de données H2. Vous pouvez utiliser n'importe quelle base de données avec un pilote JDBC, au lieu des valeurs par défaut fournies. Consultez la documentation de votre pilote JDBC pour rechercher des informations spécifiques sur certains de ces paramètres. 
Les options par défaut peuvent être modifiées directement en ouvrant le fichier
`config/storage/database_storage.conf` et en modifiant les valeurs suivantes spécifiques à votre
cas d'utilisation :
*  **class** - Cette classe pointe vers la classe d'adaptateur de base de données à utiliser. La valeur par défaut est `com.ibm.watson.crawler.storageadapters.DatabasePersistAdapter`
*  **driver** - Classe du pilote JDBC. La valeur par défaut est `org.h2.Driver` pour utiliser H2
*  **url** - Reportez-vous aux options JDBC de votre pilote. Il s'agit du préfixe d'URL de la chaîne de connexion JDBC. La valeur par défaut est `jdbc:h2:file:`
*  **database_location** - Emplacement de votre choix pour votre base de données. Ne s'applique qu'aux bases de données basées sur des fichiers, telles que sqlite et H2. La valeur par défaut est `./storage/database`
*  **database_name** - Nom de la base de données. La valeur par défaut est `ActivityDB`
*  **table_name** - Nom de table à utiliser. La valeur par défaut est `Ledger`
*  **username** - Nom d'utilisateur permettant de se connecter à la base de données
*  **password** - Mot de passe permettant de se connecter à la base de données

La configuration par défaut est suffisante pour la plupart des activités. 

## Adaptateur de sortie

Vous avez le choix entre deux *adaptateurs de sortie*. Définissez l'adaptateur de sortie en définissant `output_adapter.class` dans `crawler.conf`. Les options disponibles sont les suivantes :

*  **class** - Définit la classe de l'adaptateur de sortie de Data Crawler. La valeur par défaut est `com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter`
*  **config** - Définit la clé de configuration à transmettre à l'adaptateur de sortie. La chaîne doit correspondre à une clé de cet objet de configuration. Dans l'exemple de code suivant :
```javascript
  orchestration_service {
    include "orchestration_service.conf"
  },
  test {
    output_directory = "/tmp/crawler-test-output"
  }
}
```
La clé de configuration est `orchestration_service`. La valeur par défaut est `discovery_service`

Vous devez sélectionner un adaptateur de sortie en spécifiant son paramètre `class` et sa clé `config`.

* **Adaptateur de sortie du service d'orchestration** : télécharge les documents explorés dans le service d'orchestration de Watson Developer Cloud. Sélectionnez cet adaptateur en définissant le paramètre `class` et la clé `config` comme suit : 
```javascript
  class = "com.ibm.watson.crawler.orchestrationserviceoutputadapter.oneatatime.OrchestrationServiceOutputAdapter"
  config = "orchestration_service"
  orchestration_service {
    include "orchestration/orchestration_service.conf"
  }
```
* **Adaptateur de sortie du service de reconnaissance** : télécharge les documents explorés dans le service de reconnaissance de Watson Developer. Sélectionnez cet adaptateur en définissant le paramètre `class` et la clé `config` comme suit :
```javascript
  class = "com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter"
  config = "discovery_service"
  discovery_service {
    include "discovery/discovery_service.conf"
  }
```
* **Adaptateur de sortie de test Watson** : enregistre une représentation des fichiers explorés sur le disque, dans un emplacement spécifié. Sélectionnez cet adaptateur en définissant le paramètre `class` et la clé `config` comme suit :

**Remarque** : un paramètre supplémentaire, `output_directory`, sélectionne le répertoire dans lequel la représentation des données explorées doit être enregistrée.
```javascript
  class = "com.ibm.watson.crawler.testoutputadapter.TestOutputAdapter"
  config = "test"
  output_directory = "/tmp/crawler-test-output"
```
* **retry** - Spécifie les options des nouvelles tentatives en cas de tentatives infructueuses d'envoi à l'adaptateur de sortie. 
  * max_attempts - Nombre maximal de nouvelles tentatives. La valeur par défaut est de `10`
  * delay - Délai minimal entre les tentatives, en secondes. La valeur par défaut est de `2`
  * exponent_base - Facteur déterminant l'évolution du délai sur chaque tentative infructueuse. La valeur par défaut est de `2`

 La formule est la suivante :
```
 d(nième_tentative) = délai * (base_exponentielle ^ nième_tentative)
```

 Par exemple, pour les paramètres avec un délai d'une seconde et une base
exponentielle de 2, la deuxième nouvelle tentative (troisième tentative) est retardée de
deux secondes au lieu d'une et la suivante, de quatre secondes.
 ```
 d(0) = 1 * (2 ^ 0) = 1 seconde
 d(1) = 1 * (2 ^ 1) = 2 secondes
 d(2) = 1 * (2 ^ 2) = 4 secondes
```
Ainsi, avec les paramètres par défaut, une soumission est tentée jusqu'à 10 fois, sur une période d'attente d'environ 1 022 secondes (soit un peu plus de 17 minutes). 
Ce délai est approximatif car un délai supplémentaire est ajouté pour éviter l'exécution simultanée de plusieurs nouvelles soumissions. 
Ce délai "approximatif" pouvant atteindre 10 %, la dernière nouvelle tentative dans l'exemple précédent peut être retardée jusqu'à 4,4 secondes. Le délai d'attente n'inclut pas le temps passé à se connecter au service, à télécharger les données ou à attendre une réponse.
 *Avertissement :* si le délai d'attente est réduit en diminuant l'une de ces valeurs par défaut, certains documents risquent de ne pas être téléchargés
 correctement via l'adaptateur de sortie configuré. Si vous utilisez les services Watson Developer Cloud, vous en serez averti dans le journal par des messages RetryFailure indiquant "429 Trop de requêtes" (limitation de débit). 
 
## Options de débogage
*  **full_node_debugging** - Active le mode débogage ; les valeurs possibles sont `true` et `false`. **Avertissement** : l'intégralité des données de chacun des documents explorées est consignée dans les journaux. 
*  **heartbeat_wait_time** - Intervalle, en millisecondes, entre les générations des statistiques d'ingestion des documents (mode débogage uniquement). La valeur par défaut est de 1 000 millisecondes.

## Options de consignation
*  **configuration_file** - Fichier de configuration à utiliser pour la consignation. Dans l'exemple de fichier `crawler.conf`, cette option est définie dans `logging.log4j` et sa valeur par défaut est `log4j_custom.properties`.
Cette option doit être définie de la même manière qu'un fichier `.properties` ou `.conf` soit utilisé.

## Options supplémentaires de gestion des explorations
*  **shutdown_timeout** - Spécifie la valeur du délai d'attente, en minutes, avant l'arrêt de l'application. La valeur par défaut est de `10`.
*  **output_limit** - Nombre le plus élevé d'éléments indexables que le moteur d'exploration tentera d'envoyer simultanément à l'adaptateur de sortie. Cette valeur peut être inférieure en fonction du nombre de coeurs disponibles pour effectuer le travail. Elle indique qu'à tout moment, pas plus de "x" éléments indexables seront envoyés à l'adaptateur de sortie en attente de retour. La valeur par défaut est de `10`.
*  **input_limit** - Limite le nombre d'adresses URL qui peuvent être demandées simultanément au connecteur. La valeur par défaut est de `3`.
*  **output_timeout** - Durée, en secondes, avant que Data Crawler n'abandonne une demande à l'adaptateur de sortie, puis supprime l'élément de la file d'attente de l'adaptateur de sortie, pour autoriser d'autres traitements. La valeur par défaut est de `1200`. **Remarque** : vous devez prendre en compte les contraintes imposées par l'adaptateur de sortie, car ces contraintes peuvent être liées aux limites définies ici. La valeur
`output_limit` définie ci-dessus ne s'intéresse qu'à la manière dont de
nombreux objets indexables peuvent être envoyés simultanément à l'adaptateur de sortie. 
Une fois qu'un objet indexable a été envoyé à l'adaptateur de sortie, il est "pointé", comme défini par la
variable `output_timeout`. Il est possible que l'adaptateur de sortie dispose lui-même d'un régulateur l'empêchant de pouvoir traiter
autant d'entrées qu'il n'en reçoit. Par exemple, l'adaptateur de sortie d'orchestration peut comporter un pool de connexions,
configurable pour les connexions HTTP au service. Si sa valeur par défaut est de 8, par exemple, et que vous affectez à `output_limit` un nombre supérieur à 8, des processus seront en attente d'exécution. Des délais d'attente sont alors à prévoir. 
*  **num_threads** - Nombre d'unités d'exécution en parallèle qui peuvent être exécutées simultanément. Cette valeur peut être un entier, qui indique directement le nombre d'unités d'exécution en parallèle, ou une chaîne, au format "xNUM", qui indique le coefficient multiplicateur du nombre de processeurs disponibles. Par exemple, "x1.5". La valeur par défaut est de `"30"`.

## VOIR AUSSI

crawler(1)

vcrypt(1)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
