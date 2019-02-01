# Configuration du service de reconnaissance
Le service de reconnaissance indique au moteur d'exploration comment gérer les fichiers explorés lors de l'utilisation du service de reconnaissance d'IBM Watson. 
Les options par défaut peuvent être modifiées directement en ouvrant le fichier
`config/discovery/discovery_service.conf` et en modifiant les valeurs suivantes spécifiques à votre
cas d'utilisation :

*  **http_timeout** - Délai, en secondes, de l'opération de lecture/d'indexation des documents ; la valeur par défaut est de `125`.
*  **concurrent_upload_connection_limit** - Nombre de connexions simultanées autorisées pour le téléchargement des documents ; la valeur par défaut est de `2`. Si l'adaptateur de sortie du service d'orchestration est utilisé, ce nombre doit être égal ou supérieur à la valeur `output_limit` définie lors de la configuration des options d'exploration. 
*  **base_url** - Adresse URL à laquelle vos documents explorés seront envoyés. Pour la version actuelle du service de reconnaissance, la valeur est `https://gateway.watsonplatform.net/discovery/api`.
*  **environment_id** - Emplacement de votre collection de documents explorés à l'adresse `base-url`.
*  **collection_id** - Nom de la collection de documents que vous configurez dans le service de reconnaissance.
*  **configuration_id** - Nom du fichier de configuration utilisé par le service de reconnaissance.
*  **check_for_completion** - Vérifie si le document a été correctement traité sur le noeud final. Cette opération réduit les performances perçues du moteur d'exploration, mais génère une notification fiable d'un téléchargement et d'une conversion de document réussis. La valeur admise est `true` ou `false`.  
**IMPORTANT** : lors de l'activation de ce paramètre, il est recommandé d'augmenter la valeur `concurrent_upload_connection_limit` de sorte qu'elle soit supérieure ou égale à la valeur `output_limit` définie lors de la configuration des options d'exploration, pour pouvoir utiliser intégralement les ressources mises à votre disposition. 

Spécifiez vos données d'identification pour le service de reconnaissance : 
*  **username** - Nom d'utilisateur permettant de s'authentifier avec l'emplacement de votre collection de documents explorés. 
*  **password** - Mot de passe permettant de s'authentifier avec l'emplacement de votre collection de documents explorés. 

L'adaptateur de sortie du service de reconnaissance peut envoyer des statistiques pour qu'IBM puisse mieux comprendre et servir ses utilisateurs. Les options suivantes peuvent être définies pour la variable `send_stats` :
*  **jvm** - Les statistiques de la machine virtuelle Java (JVM) envoyées incluent le fournisseur Java et sa version, tels qu'indiqués par la machine virtuelle Java utilisée pour exécuter Data Crawler. La valeur admise est `true` ou `false`.
*  **os** - Les statistiques du système d'exploitation envoyées incluent le nom du système d'exploitation, sa version et son architecture, tels qu'indiqués par la machine virtuelle Java utilisée pour exécuter Data Crawler. La valeur admise est `true` ou `false`.

*  **api_version** - Usage interne uniquement. Date de la dernière modification apportée à la version d'API.

# Configuration du stockage du suivi des adresses URL
Le dossier `config/discovery` contient également un fichier de configuration qui peut être utilisé pour le mappage interne des adresses URL du moteur d'exploration et des ID document. 
Les options par défaut peuvent être modifiées directement en ouvrant le fichier
`config/discovery/uri_tracking_storage.conf` et en modifiant les valeurs suivantes spécifiques à votre
cas d'utilisation :

*  **driver** - Classe de pilote JDBC H2 de votre base de données. La valeur par défaut est `org.h2.Driver`
*  **url** - Préfixe d'URL de la chaîne de connexion JDBC. Son format est `jdbc:h2:[file:]`. **Remarque** Le préfixe `file:` est facultatif. Si aucun chemin ou seulement un chemin relatif est utilisé pour `database_location`, le répertoire de travail en cours est utilisé comme point de départ. La valeur par défaut est `jdbc:h2:file:`
*  **database_location** - Emplacement de stockage sur disque de la base de données. Par exemple, `./storage/database` ou `~/storage/database`. La valeur par défaut est `./storage/database`
*  **database_name** - Nom de la base de données. La valeur par défaut est `ActivityDB`
*  **table_name** - Nom de table à utiliser. La valeur par défaut est `UriTracker`
*  **username** - Nom d'utilisateur permettant de se connecter à la base de données
*  **password** - Mot de passe permettant de se connecter à la base de données

## VOIR AUSSI

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
