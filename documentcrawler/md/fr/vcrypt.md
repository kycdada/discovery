vcrypt(1) - Outil permettant de chiffrer et déchiffrer de petites quantités de données
===============================================================

## SYNOPSIS

Syntaxe : vcrypt --decrypt|-d  --encrypt|-e  --genkey|-g [ OPTIONS ]

## DESCRIPTION

`vcrypt` est utilisé principalement pour chiffrer les mots de passe à utiliser par la structure de connecteur.

### Remarque spéciale sur la longueur des clés

Par défaut, une implémentation de machine virtuelle Java doit prendre en charge les clés AES de 128 bits/16 octets. 
Si les extensions cryptographiques Java sont installées sur le système, ce dernier doit pouvoir utiliser des clés AES de 256 bits/32 octets. Une erreur est affichée si
une clé de 32 octets est fournie alors qu'elle n'est pas prise en charge par la machine virtuelle Java utilisée pour lancer `vcrypt`.

## COMMANDES

### --encrypt | -e OPTIONS ENTREE
Chiffre les données fournies dans un fichier ou une entrée standard. 

### --decrypt | -d OPTIONS ENTREE
Déchiffre les données fournies dans un fichier ou une entrée standard. 

### --genkey | -g
Génère une clé de chiffrement pouvant être utilisée avec `vcrypt` dans la sortie standard. 

## OPTIONS

### --keyfile|-k PATH/TO/ID_VCRYPT
Spécifiez le chemin d'accès au fichier contenant une clé appropriée codée en base 64, probablement générée à l'aide de la commande `--genkey|-g`.

## ENTREE

### Mode chiffrement

    $FILE_CONTAINING_CLEARTEXT | -- $CLEARTEXT

### Mode déchiffrement

    $FILE_CONTAINING_CRYPTED_TEXT | -- $CRYPTED_TEXT

## EXEMPLES

Générez une clé et placez-la dans le fichier `id_vcrypt` :

    vcrypt --genkey > id_vcrypt

Chiffrez un mot de passe de l'entrée standard à la sortie standard, écrit ici via une redirection de sortie
vers `my_secret_data.txt`:

    ./vcrypt --encrypt --keyfile id_vcrypt -- "mon mot de passe secret" > my_secret_data.txt

Vous pouvez également diriger la sortie vers `xclip`, `pbcopy` ou une commande similaire pour placer la sortie dans le presse-papiers
de votre système d'exploitation.

Déchiffrez un mot de passe à partir d'un fichier :

    vcrypt --decrypt --keyfile id_vcrypt my_secret_data.txt

## PROPRIETES ET VARIABLES D'ENVIRONNEMENT

### Variable d'environnement `VCRYPT_OPTS`
Cette variable d'environnement permet de transmettre des options à la commande `java` utilisée pour lancer `vcrypt`.

### Propriété `vcrypt.key`
Transmettez cette propriété comme propriété `-D` dans `VCRYPT_OPTS` avec une chaîne de 16 ou 32 octets pour utiliser une clé sur la ligne de commande,
au lieu de transmettre l'option `--keyfile | -k keyfile`.

Exemple de syntaxe

    VCRYPT_OPTIONS="-Dvcrypt.key='1234qwerasdfzxcv'" vcrypt --encrypt file_to_encrypt

### Variable d'environnement `VIV_VCRYPT_KEY`
`vcrypt` permet d'utiliser cette variable d'environnement pour définir la clé. Elle doit être de 16 ou 32 octets.

## VOIR AUSSI

crawler(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
