crawler(1) - Moteur d'exploration permettant de déplacer des données du point A au point B
====================================================================

## SYNOPSIS

Syntaxe : crawler [ crawl | testit | restart | resume | refresh | summary ][ options ]

## DESCRIPTION

Data Crawler permet d'explorer divers référentiels de données, tels que des systèmes de gestion de contenu et des systèmes de fichiers,
puis d'envoyer les documents résultants à un service distant. 

## OPTIONS GENERALES

    --version
        Affiche la version du programme
    --help
        Affiche le texte de cette syntaxe

## COMMANDES

### crawl [ options ]

Exécute une exploration avec la configuration en cours. 

    -c <valeur> | --config <valeur>  # Indique le fichier de configuration à utiliser. Le fichier par défaut est "config/crawler.conf".
    --pii-checking <valeur>         # Active/Désactive la vérification du PII

### testit [ options ]

Exécute une exploration test, qui n'explore que l'adresse URL de départ et affiche les adresses URL en file d'attente. 
Si l'adresse URL de départ génère un contenu indexable (par exemple, un document), ce
contenu est envoyé à l'adaptateur de sortie et le contenu est imprimé à l'écran. Si
l'extraction de l'adresse URL de départ entraîne la mise en file d'attente d'adresses
URL, ces adresses URL seront affichées et aucun contenu ne sera envoyé à l'adaptateur de
sortie. Par défaut, cinq adresses URL en file d'attente sont affichées.

    -c <valeur> | --config <valeur>  # Indique le fichier de configuration à utiliser. Le fichier par défaut est "config/crawler.conf".
    -l <n> | --limit <n>           # Limite le nombre d'adresses URL en file d'attente affichées.
    --pii-checking <valeur>         # Active/Désactive la vérification du PII

### restart [ options ]

Exécute un redémarrage de l'exploration ; lance une nouvelle exploration avec la configuration en cours. 

    -c <valeur> | --config <valeur>  # Indique le fichier de configuration à utiliser.
--pii-checking <valeur>         # Active/Désactive la vérification du PII

### resume [ options ]

Reprend une exploration là où elle s'est arrêtée. 

    -c <valeur> | --config <valeur>  # Indique le fichier de configuration à utiliser.
--pii-checking <valeur>         # Active/Désactive la vérification du PII

### refresh [ options ]

Actualise une exploration précédente. 

    -c <valeur> | --config <valeur>  # Indique le fichier de configuration à utiliser.
--pii-checking <valeur>         # Active/Désactive la vérification du PII

### summary [ options ]

Génère un rapport d'exploration.

    --submitted                    # Interroge tous les documents soumis
    --processed                    # N'interroge que les documents correctement traités
    --failed                       # N'interroge que les documents dont le traitement à achouer
    --group-id <valeur>            # Interroge l'exécution de l'exploration pour un groupe spécifié. Un groupe se compose d'une exploration initiale et de toute reprise, actualisation ou redémarrage de cette exploration initiale. Si la valeur n'est pas spécifiée, cette requête renvoie par défaut le dernier groupe exploré.
    --show-content                 # Affiche tout contenu supplémentaire associé à une requête
    --filter                       # Filtre le résultat de la requête sur l'adresse URL et l'ID hachage

## EXEMPLES

Exécutez une exploration à l'aide du fichier de configuration qui se trouve dans `config/crawler.conf` :

    crawler crawl

Exécutez un test à l'aide du fichier de configuration qui se trouve dans `config/crawler.conf` :

    crawler testit

Exécutez une exploration à l'aide du fichier de configuration qui se trouve dans `/home/watson/office-share.conf` :

    crawler crawl --config /home/watson/office-share.conf

Redémarrez une exploration à l'aide du fichier de configuration qui se trouve dans `/home/watson/office-share.conf` :

    crawler restart --config /home/watson/office-share.conf

Extrayez les informations récapitulatives des documents ayant échoué dont l'ID groupe est `2` :

    crawler summary --failed --group-id 2 --show-content

Affichez la syntaxe, avec la version :

    crawler --help

## CONFIGURATION

`crawler` requiert un fichier de configuration pour ses options. Des exemples de fichier de configuration sont fournis dans le répertoire `share` du répertoire d'installation du `moteur d'exploration`. Copiez ces exemples et modifiez-les. *Ne modifiez pas les exemples dans leur emplacement.*

Si l'option `--config | -c` n'est pas spécifiée, le `moteur d'exploration` recherche son fichier de configuration dans le répertoire `config` du
répertoire de démarrage du `moteur d'exploration`. Le `moteur d'exploration` recherche donc le fichier `config/crawler.conf`.

## DIAGNOSTICS

Utilisez ces fonctions pour diagnostiquer les problèmes.

### Débogage

Active le mode débogage. Dans le fichier `crawler.conf`, spécifiez :

    debugging.full_node_debugging = true

### Consignation

Active la consignation. Dans le fichier `log4j_custom.properties`, spécifiez :

    log4j.rootLogger=INFO, Console, Log

Il s'agit du niveau de consignation par défaut de la sortie du fichier. Pour le journal de la console, la valeur par défaut est la suivante : 

    log4j.appender.Console.Threshold=WARN

Les niveaux de consignation peuvent être définis sur les valeurs suivantes : 

    OFF - Rang le plus élevé possible ; destiné à désactiver la consignation.
    FATAL - Désigne les événements d'erreur très grave qui entraîneront vraisemblablement l'abandon de l'application.
    ERROR - Désigne les événements d'erreur qui risquent toutefois de permettre à l'application de poursuivre son exécution.
    WARN - Désigne les situations potentiellement dangereuses.
    INFO - Désigne les messages d'information indiquant la progression de l'application à un niveau à à granularité grossière.
    DEBUG - Désigne les événements d'information à granularité fine les plus utiles pour déboguer une application.
    TRACE - Désigne les événements d'information à granularité plus fine que DEBUG.
    ALL - Rang le plus faible possible ; destiné à activer la consignation dans son intégralité. 

## REGULATION

Définit les évaluations en matière de dimensionnement pour faciliter la gestion du débit. Dans le fichier `crawler.conf`, spécifiez :

`shutdown_timeout` : indique la valeur du délai d'attente, en minutes, avant l'arrêt de l'application ; la valeur par défaut est de 10.

    shutdown_timeout = <n>

`output_limit` représente le nombre le plus élevé d'éléments indexables que le moteur d'exploration portable enverra simultanément
à l'adaptateur de sortie, dans l'attente d'un retour ; la valeur par défaut est de 10. Cette valeur peut être inférieure en fonction des coeurs disponibles pour effectuer le travail.

    output_limit = <n>

`input_limit` : limite le nombre d'adresses URL qui peuvent être demandées simultanément au connecteur ; la valeur par défaut est de 3.

    input_limit = <n>

`output_timeout` représente la durée, en secondes, avant que le moteur d'exploration n'abandonne une demande à l'adaptateur de sortie, puis supprime
l'élément de la file d'attente des limites, pour autoriser d'autres traitements. La valeur par défaut est de 150.

    output_timeout = <n>

Vous devez prendre en compte les contraintes imposées par l'adaptateur de sortie
car ces contraintes peuvent être liées aux limites définies ici. La valeur
`output_limit` définie ci-dessus ne s'intéresse qu'à la manière dont de
nombreux objets indexables peuvent être envoyés simultanément à l'adaptateur de sortie. 
Une fois qu'un objet indexable a été envoyé à l'adaptateur de sortie, il est "pointé", comme défini par la
variable `output_timeout`. Il est possible que l'adaptateur de sortie dispose lui-même d'un régulateur l'empêchant de pouvoir traiter
autant d'entrées qu'il n'en reçoit. Par exemple, l'adaptateur de sortie d'orchestration peut comporter un pool de connexions,
configurable pour les connexions HTTP au service. Si sa valeur par défaut est de 8, par exemple, et que vous affectez à
`output_limit` un nombre supérieur à celui configuré pour ce pool de connexions, des processus seront en attente d'exécution. Des délais d'attente sont alors à prévoir. 

`num_threads` : nombre d'unités d'exécution en parallèle qui peuvent être exécutées simultanément. Cette valeur peut être un entier,
qui indique directement le nombre d'unités d'exécution en parallèle, ou une chaîne, au format `"xNUM"`, qui indique le coefficient multiplicateur du nombre
de processeurs disponibles. La valeur par défaut est "x1.5", soit 1,5 fois le nombre de processeurs disponibles (extrait de `Runtime.availableProcessors`).

    num_threads = <n>

La formule de calcul du parallélisme dans le pool Data Crawler est la suivante : `min(maxThreads, max(minThreads, numThreads))`.

## VARIABLE D'ENVIRONNEMENT `CRAWLER_OPTS` 

Vous trouverez ci-après les propriétés pouvant être transmises au `moteur d'exploration` via la variable d'environnement `CRAWLER_OPTS`, répertoriées avec les valeurs par défaut. 

Transmettez-les comme suit : 

    CRAWLER_OPTS="-Dproperty=valeur -Dproperty=valeur" crawler

Ces propriétés ne doivent être modifiées que pour le débogage et uniquement sur demande du support IBM. 

### cfa.java_bin

`cfa.java_bin` peut changer la commande `java` permettant de lancer l'adaptateur d'entrée de la structure de connecteur. Par défaut, le `moteur d'exploration` utilise
le même binaire `java` que celui utilisé pour lancer le `moteur d'exploration` lui-même.

Cela peut également être modifié en définissant la propriété
`java.home`, qui sera ensuite utilisée pour déterminer le chemin d'accès
à l'exécutable `java`.

### cfa.lib_dir

`cfa.lib_dir` modifie le chemin d'accès au répertoire `lib` de la structure de connecteur. Il est rarement nécessaire de modifier cette propriété. Par défaut,
le `moteur d'exploration` utilise le répertoire `lib` à l'intérieur du chemin à la structure de connecteur calculé (généralement, simplement `connectorFramework`).

### cfa.framework_jars_dir

`cfa.framework_jars_dir` modifie le chemin d'accès au répertoire jars de la structure de connecteur, qui se trouve par défaut dans `connectorFramework/<version>/lib/java`.

### cfa.plugins_dir

`cfa.plugins_dir` spécifie le chemin d'accès au répertoire des plug-in de la structure de connecteur, où les véritables connecteurs sont stockés.
Par défaut, il est généré à partir de `framework_jars_dir` et correspond à `connectorFramework/<version>/lib/java/plugins`.

## LIMITATIONS CONNUES

Détaille les limitations connues dans la version actuelle de Data Crawler

* Data Crawler peut se bloquer lors de l'exécution du connecteur de système de fichiers avec une adresse URL non valide ou manquante.
* Configurez la valeur `urls_to_filter` dans le fichier
`config/crawler.conf` de sorte que toutes les adresses URL ou les expressions régulières de la liste
blanche soient incluses dans une même expression régulière.
* Le chemin d'accès au fichier de configuration transmis dans l'option `--config | -c` doit être un chemin complet, 
à savoir, au format de chemin d'accès relatif `config/crawler.conf` ou
`./crawler.conf` ou au format de chemin d'accès absolu `/path/to/config/crawler.conf`. 
Il n'est possible de spécifier que `crawler.conf` si et seulement si les fichiers référencés
à l'aide de la fonction `include` dans le fichier `crawler.conf` sont incorporés
au lieu d'utiliser `include`. Par exemple,
`discovery/discovery_service.conf` est inclus (à l'aide de la fonction
`include`) pour faciliter la lecture de la configuration. Son contenu
doit être copié dans `crawler.conf`, à l'intérieur de la clé
`output_adapter.discovery_service`, pour utiliser un chemin d'accès non complet dans l'option de configuration. 

## JOURNAL DES MODIFICATIONS

Pour une liste des modifications apportées dans cette version, consultez le fichier `changelog.txt` dans votre répertoire d'installation. 

## AUTEUR

IBM Watson - https://www.ibm.com/smarterplanet/us/en/ibmwatson/

Ecrit par yinz à Pittsburgh.

## VOIR AUSSI

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
