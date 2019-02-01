vcrypt(1) - Herramienta para cifrar y descifrar pequeñas cantidades de datos
===============================================================

## SINOPSIS

Uso: vcrypt --decrypt|-d  --encrypt|-e  --genkey|-g [ OPCIONES ]

## DESCRIPCIÓN

`vcrypt` se utiliza principalmente para cifrar las contraseñas que usa la infraestructura de conectores.

### Nota sobre la longitud de las claves

De forma predeterminada, una implementación de máquina virtual Java tiene que soportar claves AES de 128 bits/16 bytes. Si el sistema tiene instalado Java Cryptographic Extensions, puede ser capaz de utilizar claves AES de 256 bits/32 bytes. Se producirá un error si se facilita una clave de 32 bytes no soportada por la JVM usada para ejecutar `vcrypt`.

## COMANDOS

### --encrypt | -e OPCIONES ENTRADA
Cifrar los datos proporcionados en un archivo o en la entrada estándar.

### --decrypt | -d OPCIONES ENTRADA
Descifrar los datos proporcionados en un archivo o en la entrada estándar.

### --genkey | -g
Genera una clave de cifrado adecuada para su uso con `vcrypt` en la salida estándar.

## OPCIONES

### --keyfile|-k RUTA/A/ID_VCRYPT
Especifica la ruta del archivo que contiene una clave codificada en Base64 generada normalmente con el comando `--genkey|-g`.

## ENTRADA

### Modo de cifrado

    $ARCHIVO_CON_TEXTO_EN_CLARO | -- $TEXTO_EN_CLARO

### Modo de descifrado

    $ARCHIVO_CON_TEXTO_CIFRADO | -- $TEXTO_CIFRADO

## EJEMPLOS

Generar una clave y ponerla en el archivo `id_vcrypt`:

    vcrypt --genkey > id_vcrypt

Cifrar una contraseña desde la entrada estándar a la salida estándar, escrita aquí a través de una redirección de salida a
`my_secret_data.txt`:

    ./vcrypt --encrypt --keyfile id_vcrypt -- "mi contraseña secreta" > my_secret_data.txt

También se puede canalizar la salida a `xclip`, `pbcopy` o similar para colocar la salida en el portapapeles del sistema.


Descifrar la contraseña de un archivo:

    vcrypt --decrypt --keyfile id_vcrypt my_secret_data.txt

## PROPIEDADES Y VARIABLES DE ENTORNO

### Variable de entorno `VCRYPT_OPTS`
Esta variable de entorno puede utilizarse para pasar opciones al comando `java` que se utiliza para iniciar `vcrypt`.

### Propiedad `vcrypt.key`
Pásela como una propiedad `-D` en `VCRYPT_OPTS` con una cadena de 16 o 32 bytes para usar una clave en la línea de comandos en lugar de pasar la opción `--keyfile | -k keyfile`.

Ejemplo de uso:

    VCRYPT_OPTIONS="-Dvcrypt.key='1234qwerasdfzxcv'" vcrypt --encrypt archivo_por_cifrar

### Variable de entorno `VIV_VCRYPT_KEY`
`vcrypt` permite usar esta variable de entorno para configurar la clave. Tiene que ser de 16 o 32 bytes.

## VÉASE TAMBIÉN

crawler(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
