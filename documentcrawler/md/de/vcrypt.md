vcrypt(1) - Ein Tool zum Verschlüsseln und Entschlüsseln kleiner Datenmengen
===============================================================

## Übersicht

Verwendung: vcrypt --decrypt|-d  --encrypt|-e  --genkey|-g [ OPTIONS ]

## Beschreibung

`vcrypt` wird primär zum Verschlüsseln von Kennwörtern für Connector-Framework verwendet. 

### Besonderer Hinweis zur Schlüssellänge

Standardmäßig muss eine Implementierung von Java Virtual Machine 128-Bit/16-Byte-AES-Schlüssel unterstützen. Falls auf dem System
Java Cryptographic Extensions installiert ist, kann es 256-Bit/32-Byte-AES-Schlüssel verwenden. Ein Fehler wird angezeigt, wenn ein 32-Byte-Schlüssel zur Verfügung gestellt wird, jedoch nicht  von der zum Starten von `vcrypt` verwendeten JVM unterstützt wird.

## Befehle

### --encrypt | -e OPTIONS INPUT
Verschlüsselt Daten, die in einer Datei oder in der Standardeingabe bereitgestellt werden. 

### --decrypt | -d OPTIONS INPUT
Entschlüsselt Daten, die in einer Datei oder einer Standardeingabe bereitgestellt werden. 

### --genkey | -g
Generiert einen Verschlüsselungsschlüssel, der für die Verwendung mit `vcrypt` für die Standardausgabe geeignet ist. 

## Optionen

### --keyfile|-k PATH/TO/ID_VCRYPT
Geben Sie den Pfad für die Datei an, die einen entsprechenden Base64-codierten Schlüssel enthält. Dieser wurde wahrscheinlich mit dem Befehl `--genkey|-g` erstellt.

## Eingabe

### Verschlüsselungsmodus

    $FILE_CONTAINING_CLEARTEXT | -- $CLEARTEXT

### Entschlüsselungsmodus

    $FILE_CONTAINING_CRYPTED_TEXT | -- $CRYPTED_TEXT

## Beispiele

Generiert einen Schlüssel und stellt diesen in die Datei `id_vcrypt`:

    vcrypt --genkey > id_vcrypt

Verschlüsselt ein Kennwort von der Standardeingabe zur Standardausgabe. Dies wird hier über die Ausgabeumleitung zu `my_secret_data.txt` geschrieben:

    ./vcrypt --encrypt --keyfile id_vcrypt -- "my secret password" > my_secret_data.txt

Sie können die Ausgabe auch zu `xclip`, `pbcopy` oder ähnlich wie beim Kopieren der Ausgabe in die Zwischenablage des Betriebssystems über eine Pipe leiten.

Entschlüsselt ein Kennwort aus einer Datei: 

    vcrypt --decrypt --keyfile id_vcrypt my_secret_data.txt

## Eigenschaften und Umgebungsvariablen

### Umgebungsvariable `VCRYPT_OPTS`
Diese Umgebungsvariable kann verwendet werden, um Optionen an den Befehl `java` zu übergeben, der für das Starten von `vcrypt` verwendet wird.

### Eigenschaft `vcrypt.key`
Übergeben Sie diese als Eigenschaft `-D` in `VCRYPT_OPTS` mit einer 16- oder 32-Byte-Zeichenfolge, um einen Schlüssel in der Befehlszeile zu verwenden, anstatt die Option `--keyfile | -k keyfile` zu übergeben.

Beispiel für die Verwendung:

    VCRYPT_OPTIONS="-Dvcrypt.key='1234qwerasdfzxcv'" vcrypt --encrypt file_to_encrypt

### Umgebungsvariable `VIV_VCRYPT_KEY`
`vcrypt` ermöglicht die Verwendung dieser Umgebungsvariable zum Festlegen des Schlüssels. Er muss 16 oder 32 Byte umfassen. 

## Weitere Informationen

crawler(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
