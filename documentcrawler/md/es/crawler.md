crawler(1) - Rastreador para mover datos desde el punto A al punto B
====================================================================

## SINOPSIS

Uso: crawler [ crawl | testit | restart | resume | refresh | summary ][ options ]

## DESCRIPCIÓN

Data Crawler se usa para rastrear diversos repositorios de datos como, por ejemplo, sistemas de gestión de contenidos y sistemas de archivos y, a continuación, inyectar los documentos resultantes a un servicio remoto.

## OPCIONES GLOBALES

    --version
        Muestra la versión del programa
    --help
        Muestra este texto de uso

## COMANDOS

### crawl [ opciones ]

Ejecuta un rastreo con la configuración actual.

    -c <valor> | --config <valor>  # Especifica el archivo de configuración por usar. El valor predeterminado es "config/crawler.conf".
    --pii-checking <valor>         # Conmuta la comprobación PII

### testit [ opciones ]

Ejecuta un rastreo de prueba, que solo rastrea el URL de semilla y muestra los URL que haya encolados. Si el URL de semilla da lugar a un contenido indexable (p.ej., un documento), dicho contenido se envía al adaptador de salida y el contenido se saca por pantalla. Si la recuperación del URL de semilla provoca un encolamiento de URL, dichos URL se mostrarán y no se enviará ningún contenido al adaptador de salida. De forma predeterminada, se muestran cinco URL encolados.

    -c <valor> | --config <valor>  # Especifica el archivo de configuración por usar. El valor predeterminado es "config/crawler.conf".
    -l <n> | --limit <n>           # Limita el número de URL encolados que se muestran.
--pii-checking <valor>         # Conmuta la comprobación PII

### restart [ opciones ]

Ejecuta un reinicio de rastreo; inicia un rastreo nuevo con la configuración actual.

    -c <valor> | --config <valor>  # Especifica el archivo de configuración por usar.
    --pii-checking <valor>         # Conmuta la comprobación PII

### resume [ opciones ]

Reanuda un rastreo en el punto en que se detuvo.

    -c <valor> | --config <valor>  # Especifica el archivo de configuración por usar.
    --pii-checking <valor>         # Conmuta la comprobación PII

### refresh [ opciones ]

Renueva un rastreo anterior.

    -c <valor> | --config <valor>  # Especifica el archivo de configuración por usar.
    --pii-checking <valor>         # Conmuta la comprobación PII

### summary [ opciones ]

Genera un informe de rastreo.

    --submitted                    # Consulta todos los documentos enviados
    --processed                    # Consulta solo los documentos procesados satisfactoriamente
    --failed                       # Consulta solo los documentos cuyo procesamiento no ha sido satisfactorio
    --group-id <value>             # Consulta la ejecución de rastreo de un grupo especificado. Un grupo consta de un rastreo inicial y de cualquier reanudación, renovación o reinicio de dicho rastreo inicial. Si no se especifica el valor, de forma predeterminada la consulta se hace al grupo rastreado más recientemente.
--show-content                 # Muestra contenido adicional asociado a una consulta
    --filter                       # Filtra el resultado de la consulta por URL y hashID

## EJEMPLOS

Ejecución de un rastreo usando el archivo de configuración `config/crawler.conf`:

    crawler crawl

Ejecución de una prueba usando el archivo de configuración `config/crawler.conf`:

    crawler testit

Ejecución de un rastreo usando el archivo de configuración `/home/watson/office-share.conf`:

    crawler crawl --config /home/watson/office-share.conf

Reinicio de un rastreo usando el archivo de configuración `/home/watson/office-share.conf`:

    crawler restart --config /home/watson/office-share.conf

Obtención de información de resumen de los documentos fallidos con el ID de grupo `2`:

    crawler summary --failed --group-id 2 --show-content

Mostrar ayuda de uso, incluida la versión:

    crawler --help

## CONFIGURACIÓN

`crawler` requiere un archivo de configuración para sus opciones. En el directorio `share` se proporcionan ejemplos de archivo de configuración, dentro del directorio de instalación
de `crawler`. Copie estos ejemplos y modifíquelos. *No modifique los ejemplos originales.*

Si no se especifica la opción `--config | -c`, `crawler` buscará su configuración en el directorio `config` del directorio en el que se haya iniciado
`crawler`. Es decir, `crawler` buscará `config/crawler.conf`.

## DIAGNÓSTICO

Utilice estas funciones para diagnosticar problemas.

### Depuración

Activa el modo de depuración. En el archivo `crawler.conf`, configure:

    debugging.full_node_debugging = true

### Registro cronológico

Habilita el registro cronológico de anotaciones. En el archivo `log4j_custom.properties`, configure:

    log4j.rootLogger=INFO, Console, Log

Este es el nivel de registro predeterminado para la salida de archivos. En el registro de consola, el valor predeterminado es:

    log4j.appender.Console.Threshold=WARN

Los niveles de registro se pueden configurar con los valores siguientes:

    OFF - La clasificación más alta posible, su finalidad es desactivar el registro.
FATAL - Indica errores muy graves suelen dar lugar a una terminación anómala de la aplicación.
    ERROR - Indica errores que no impiden que la aplicación siga ejecutando.
WARN - Indica situaciones potencialmente dañinas.
    INFO - Indica mensajes informativos que destacan el progreso de la aplicación a nivel de grano grueso.
DEBUG - Indica eventos informativos de grano fino que son de utilidad en la depuración de una aplicación.
TRACE - Indica eventos informativos de grano más fino que DEBUG.
    ALL - La clasificación más baja posible, su finalidad es activar todo el registro.

## REGULACIÓN

Define las limitaciones de tamaño establecidas para ayudar a gestionar el rendimiento. En el archivo `crawler.conf`, configure:

`shutdown_timeout` Especifica el valor del tiempo que se espera, en minutos, antes de concluir la aplicación; el valor predeterminado es 10.

    shutdown_timeout = <n>

`output_limit` es el máximo número de elementos indexables que el rastreador portátil envía de forma simultánea al adaptador de salida en espera de una devolución; el valor predeterminado es 10. Esto puede quedar limitado adicionalmente por los núcleos disponibles para hacer el trabajo.

    output_limit = <n>

`input_limit` Limita el número de URL que pueden solicitarse desde el conector a la vez; el valor predeterminado es 3.

    input_limit = <n>

`output_timeout` es la cantidad de tiempo, en segundos, que transcurre antes de que el rastreador portátil desista ante una solicitud al adaptador de salida y elimine el elemento de la cola límite para permitir más procesamiento. El valor predeterminado es 150.

    output_timeout = <n>

Deben tenerse presentes las restricciones impuestas por el adaptador de salida, ya que dichas restricciones pueden estar relacionadas con los límites definidos aquí.
El `output_limit` definido anteriormente solo se refiere a cuántos objetos indexables pueden enviarse al adaptador de salida a la vez. Una vez que un objeto indexable se envía al adaptador de salida, empieza a "contar el reloj" definido en la variable `output_timeout`. Puede que el propio adaptador de salida tenga un regulador que impida que pueda procesar todas las entradas que reciba. Por ejemplo, puede que el adaptador de salida de Orchestration tenga una agrupación de conexiones configurable para las conexiones HTTP del servicio. Si, por ejemplo, su valor predeterminado es 8 y se configura `output_limit` a un número mayor que el configurado en dicha agrupación de conexiones, habrá procesos que estén esperando su turno para ejecutar y para los que esté contando el reloj.
Puede que en tal caso se produzcan agotamientos del tiempo de espera.

`num_threads` Número de hilos paralelos que se pueden ejecutar a la vez. Este valor puede ser un entero, que especifica directamente el número de hilos paralelos, o puede ser una cadena con el formato `"xNUM"` que especifica el factor de multiplicación del número de procesadores disponibles. El valor predeterminado es "x1.5", o 1,5 veces el número de procesadores disponibles (según conste en `Runtime.availableProcessors`).

    num_threads = <n>

La fórmula para calcular el paralelismo en la agrupación de Data Crawler es: `min(maxThreads, max(minThreads, numThreads))`.

## VARIABLE DE ENTORNO `CRAWLER_OPTS` 

A continuación se indican las propiedades que se pueden pasar a `crawler` a través de la variable de entorno `CRAWLER_OPTS`, listadas con los valores predeterminados.

Se pasan de esta manera:

    CRAWLER_OPTS="-Dproperty=valor -Dproperty=valor" crawler

Solo deben cambiarse a efectos de depuración y con las indicaciones del soporte de IBM.

### cfa.java_bin

`cfa.java_bin` puede cambiar el comando `java` que se utiliza para iniciar el conector de entrada de la infraestructura de conectores. De forma predeterminada, `crawler` usa el mismo binario `java` que se usa para lanzar el propio `crawler`. 

Esto también puede cambiarse configurando la propiedad `java.home`, que luego se usa para calcular la ruta del ejecutable `java`.

### cfa.lib_dir

`cfa.lib_dir` cambia la ruta del directorio `lib` de la infraestructura de conectores. No suele ser necesario cambiarla. De forma predeterminada,
`crawler` usa el directorio `lib` dentro de la ruta calculada de la infraestructura de conectores, que suele ser `connectorFramework`.

### cfa.framework_jars_dir

`cfa.framework_jars_dir` cambia la ruta del directorio de jars de la infraestructura de conectores, que de forma predeterminada está en `connectorFramework/<versión>/lib/java`.

### cfa.plugins_dir

`cfa.plugins_dir` especifica la ruta del directorio de plugins de la infraestructura de conectores, donde se almacenan los propios conectores.
De forma predeterminada, se construye a partir de `framework_jars_dir` y es `connectorFramework/<versión>/lib/java/plugins`.

## LIMITACIONES CONOCIDAS

Se detallan las limitaciones conocidas en el release actual de Data Crawler

* Data Crawler puede colgarse al ejecutar el conector de sistema de archivos con un URL no válido o ausente.
* Configure el valor de `urls_to_filter` en el archivo `config/crawler.conf` de forma que todos los URL o expresiones regulares de lista blanca estén incluidos en una única expresión regular.
* La ruta del archivo de configuración que se pasa en la opción `--config | -c` tiene que ser una ruta cualificada. Es decir, tiene que estar en los formatos relativos `config/crawler.conf` o `./crawler.conf`, o ser una ruta absoluta `/ruta/a/config/crawler.conf`. La mera especificación de `crawler.conf` solo es posible si los archivos referenciados con `include` en el archivo `crawler.conf` están incorporados directamente en lugar de usarse `include`. Por ejemplo, `discovery/discovery_service.conf` se incluye mediante `include` para que la configuración sea más legible. Hay que copiar su contenido en `crawler.conf` dentro de la clave `output_adapter.discovery_service` para usar una ruta no cualificada en la opción config. 

## REGISTRO DE CAMBIOS

Consulte el archivo `changelog.txt` en el directorio de instalación para obtener la lista de cambios de este release.

## AUTOR

IBM Watson - https://www.ibm.com/smarterplanet/us/en/ibmwatson/

Hecho por yinz in Pittsburgh.

## VÉASE TAMBIÉN

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
