# Configuration du service d'orchestration
Le service d'orchestration indique au moteur d'exploration comment gérer les fichiers explorés. 
Les options par défaut peuvent être modifiées directement en ouvrant le fichier
`config/orchestration/orchestration-service.conf` et en modifiant les valeurs suivantes spécifiques à votre
cas d'utilisation :

*  **http_timeout** - Délai, en secondes, de l'opération de lecture/d'indexation des documents ; la valeur par défaut est de `585`.
*  **concurrent_upload_connection_limit** - Nombre de connexions simultanées autorisées pour le téléchargement des documents ; la valeur par défaut est de `10`. En général, ce nombre doit être supérieur ou égal à la valeur `output_limit` définie lors de la configuration des options d'exploration. 
*  **base_url** - Adresse URL à laquelle vos documents explorés seront envoyés.
*  **endpoint** - Emplacement de votre collection de documents explorés à l'adresse `base-url`.
*  **username** - Nom d'utilisateur permettant de s'authentifier à l'emplacement `endpoint`.
*  **password** - Mot de passe permettant de s'authentifier à l'emplacement `endpoint`. **Important** : n'utilisez **PAS** le programme vcrypt fourni avec Data Crawler pour chiffrer ce mot de passe.
*  **config_file** - Fichier de configuration utilisé par le service d'orchestration. 

L'adaptateur de sortie du service d'orchestration peut envoyer des statistiques pour qu'IBM puisse mieux comprendre et servir ses utilisateurs. Les options suivantes peuvent être définies pour la variable `send_stats` :
*  **jvm** - Les statistiques de la machine virtuelle Java (JVM) envoyées incluent le fournisseur Java et sa version, tels qu'indiqués par la machine virtuelle Java utilisée pour exécuter Data Crawler. La valeur admise est `true` ou `false`.
*  **os** - Les statistiques du système d'exploitation envoyées incluent le nom du système d'exploitation, sa version et son architecture, tels qu'indiqués par la machine virtuelle Java utilisée pour exécuter Data Crawler. La valeur admise est `true` ou `false`.

## VOIR AUSSI

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
