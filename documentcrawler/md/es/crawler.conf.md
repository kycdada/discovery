# Configuración de Data Crawler

`crawler` requiere un archivo de configuración para sus opciones. En el directorio `share` se proporcionan ejemplos de configuración, dentro del directorio de instalación
de `crawler`. Copie estos ejemplos y modifíquelos. *No modifique los ejemplos originales.*

El archivo `crawler.conf` contiene información que indica al rastreador qué archivos usar en el rastreo (adaptador de entrada), dónde enviar la recopilación de archivos rastreados una vez finalizado el rastreo (adaptador de salida) y otras opciones de gestión de rastreo.

**Nota**: Todas las rutas son relativas al directorio `config` salvo que se indique lo contrario.

Las opciones que se pueden configurar en este archivo son:

## Adaptador de entrada
*  **class** - Para uso interno exclusivamente; define la clase del adaptador de entrada de Data Crawler. El valor predeterminado es: `com.ibm.watson.crawler.connectorframeworkinputadapter.Crawl`.
*  **config** - Para uso interno exclusivamente; define la configuración de la infraestructura de conectores. La clave de configuración predeterminada dentro de este bloque que se pasa al adaptador de entrada elegido es: `connector_framework`. **Nota** – La infraestructura de conectores es lo que permite hablar con los datos. Estos pueden ser datos internos dentro de la empresa o datos externos en la web o en la nube. Los siguientes conectores permiten acceder a diversas fuentes de datos, mientras la conexión propiamente dicha está controlada por el proceso de rastreo.
  -  **IMPORTANTE** - Los datos recuperados por el adaptador de entrada de la infraestructura de conectores se guardan localmente en caché. No se guardan cifrados. De forma predeterminada, los datos se guardan en caché en un directorio temporal que debe limpiarse al reiniciar y que solo pueda ser leído por el usuario que ejecuta el comando crawler. Existe una probabilidad de que este directorio sobreviva al rastreador si la infraestructura de conectores se cae antes de poder realizar la limpieza. Tenga cuidado al elegir la ubicación de los datos guardados en caché; puede colocarlos en un sistema de archivos cifrado, pero tenga presente el impacto que ello tiene en el rendimiento. Solo a usted corresponde decidir el equilibrio entre velocidad y seguridad de los rastreos. 
*  **crawl_config_file** - Archivo de configuración que se usa en el rastreo. El valor predeterminado es: `connectors/filesystem.conf`.
*  **crawl_seed_file** - Archivo de semilla de rastreo que se usa en el rastreo. El valor predeterminado es: `seeds/filesystem-seed.conf`.
*  **id_vcrypt_file** - Archivo de claves que usa el rastreador para el cifrado de datos; la clave predeterminada incluida en el rastreador es `id_vcrypt`.
Utilice el script vcrypt en la carpeta `bin` si necesita generar un id_vcrypt_file nuevo.
*  **crawler_temp_dir** - Carpeta temporal del rastreador para guardar los registros de conector. Se proporciona el valor predeterminado, `tmp`. En caso de no existir, la carpeta `tmp` se creará en el directorio de trabajo actual. 
*  **extra_jars_dir** - Para uso interno exclusivamente; añade archivos JAR al classpath de la infraestructura de conectores.
Este valor tiene que ser `oakland` cuando se utiliza el conector de SharePoint y `database` cuando se utiliza el conector de base de datos. Se puede dejar vacía (es decir, la cadena vacía "") cuando se usen otros conectores.
**Nota**: Es relativa al directorio `lib/java` de la infraestructura de conectores.
*  **urls_to_filter** - Lista blanca separada por saltos de línea de los URL que hay que rastrear, en formato de expresión regular. Data Crawler solo rastrea los URL que coinciden con una de las expresiones regulares proporcionadas. La lista de dominios contiene los dominios de nivel superior más habituales; añada los que considere oportunos. La lista de tipos de extensión de archivo contiene las extensiones de archivo que soporta el servicio Orchestration en este release de Data Crawler. Asegúrese de que el filtro permite su domino de URL de semilla. Por ejemplo, si el URL de semilla es del estilo `http://testdomain.test.in`, añada "`in`" al filtro de dominios. Asegúrese de que no haya ningún filtro que excluya el URL de semilla, pues, de lo contrario, el rastreador podría colgarse.
*  **max_text_size** - Tamaño máximo, en bytes, que puede tener un documento antes de que la infraestructura de conectores lo escriba en disco. Si se sube este valor, bajará la cantidad de documentos escritos en disco, pero aumentará el requisito de memoria. 
*  **extra_vm_params** - Permite añadir parámetros Java al comando utilizado para lanzar la infraestructura de conectores.
*  **bootstrap_logging** - Registra el arranque de la infraestructura de conectores; solo es útil en depuraciones avanzadas. Los valores son `true` o `false`. El archivo de registro se escribe en `crawler_temp_dir`.

## Adaptador de almacenamiento

Permite almacenar el estado interno del rastreador en una base de datos. Este valor es necesario para que las opciones de rastreo `restart` y `resume` funcionen correctamente.

```javascript
storage_adapter {
 config = "storage_in_db"
  storage_in_db {
    include "storage/database_storage.conf"
  } 
}
```
El archivo referenciado, `storage/database_storage.conf`, usa de forma predeterminada una base de datos H2. Se puede utilizar cualquier base de datos que disponga de un controlador JDBC en lugar de los valores predeterminados proporcionados. Consulte la documentación del controlador JDBC para encontrar información específica sobre algunos de estos valores. Las opciones predeterminadas pueden cambiarse directamente abriendo el archivo `config/storage/database_storage.conf` y modificando los siguientes valores en cada caso de uso concreto:
*  **class** - Esta clase apunta a la clase del adaptador de base de datos que se usa. El valor predeterminado es `com.ibm.watson.crawler.storageadapters.DatabasePersistAdapter`
*  **driver** - La clase del controlador JDBC. El valor predeterminado es `org.h2.Driver` para usar H2.
*  **url** - Consulte las opciones de su controlador JDBC. Este es el prefijo del URL de la cadena de conexión JDBC. El valor predeterminado es `jdbc:h2:file:`
*  **database_location** - La ubicación de la base de datos. Esto solo se aplica a las bases de datos basadas en archivo como sqlite y H2. El valor predeterminado es `./storage/database`
*  **database_name** - Nombre de la base de datos. El valor predeterminado es `ActivityDB`
*  **table_name** - Nombre de la tabla que se usa. El valor predeterminado es `Ledger`
*  **username** - Nombre de usuario con el que se conecta a la base de datos.
*  **password** - Contraseña con la que se conecta a la base de datos.

La configuración predeterminada es suficiente para la mayor parte de la actividad.

## Adaptador de salida

Se puede escoger entre un par de *adaptadores de salida*. Defina el adaptador de salida configurando `output_adapter.class`
en `crawler.conf`. Las opciones son:

*  **class** - Define la clase del adaptador de salida de Data Crawler. El valor predeterminado es `com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter`
*  **config** - Define qué clave de configuración se pasa al adaptador de salida. La cadena debe corresponderse con una clave dentro de este objeto de configuración. En el ejemplo de código siguiente:
```javascript
  orchestration_service {
    include "orchestration_service.conf"
  },
  test {
    output_directory = "/tmp/crawler-test-output"
  }
}
```
la clave de configuración es `orchestration_service`. El valor predeterminado es `discovery_service`

Hay que seleccionar un adaptador de salida especificando el parámetro `class` y la clave `config`.

* **Adaptador de salida del servicio Orchestration**: Sube los documentos rastreados al servicio Orchestration de Watson Developer Cloud. Este adaptador se selecciona definiendo el parámetro `class` y la clave `config` de la manera siguiente: 
```javascript
  class = "com.ibm.watson.crawler.orchestrationserviceoutputadapter.oneatatime.OrchestrationServiceOutputAdapter"
  config = "orchestration_service"
  orchestration_service {
    include "orchestration/orchestration_service.conf"
  }
```
* **Adaptador de salida del servicio Discovery**: Sube los documentos rastreados al servicio Discovery de Watson Developer Cloud. Este adaptador se selecciona definiendo el parámetro `class` y la clave `config` de la manera siguiente:
```javascript
  class = "com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter"
  config = "discovery_service"
  discovery_service {
    include "discovery/discovery_service.conf"
  }
```
* **Adaptador de salida de Watson Test**: Escribe una representación de los archivos rastreados en una ubicación especificada del disco. Este adaptador se selecciona definiendo el parámetro `class` y la clave `config` de la manera siguiente:

**Nota** – Un parámetro adicional, `output_directory`, selecciona el directorio en el que debe escribirse la representación de los datos rastreados.
```javascript
  class = "com.ibm.watson.crawler.testoutputadapter.TestOutputAdapter"
  config = "test"
  output_directory = "/tmp/crawler-test-output"
```
* **retry** - Especifica las opciones de reintento en caso de intentos fallidos de inyectar en el adaptador de salida.
  * max_attempts - Número máximo de reintentos. El valor predeterminado es `10`
  * delay - Retardo mínimo entre intentos, en segundos. El valor predeterminado es `2`
  * exponent_base - Factor que determina el crecimiento del tiempo de retardo con cada intento fallido. El valor predeterminado es `2`

 La fórmula es:
```
 r(nsimo-reintento) = retardo * (exponent_base ^ nsimo-reintento)
```

 Por ejemplo, una configuración de un retardo de 1 segundo y una base exponencial de 2 provoca que el segundo reintento (el tercer intento) se retarde 2 segundos en lugar de 1, y que el siguiente se retarde 4 segundos.

 ```
 r(0) = 1 * (2 ^ 0) = 1 segundo
 r(1) = 1 * (2 ^ 1) = 2 segundos
 r(2) = 1 * (2 ^ 2) = 4 segundos
```
 Así pues, con la configuración predeterminada, un envío se reintenta un máximo de 10 veces, llegando a esperar hasta unos 1022 segundos (algo más de 17 minutos). Este tiempo es aproximado porque se añade tiempo para evitar la ejecución simultánea de varios reenvíos. Este tiempo "borroso" llega a ser hasta del 10%, de modo que el último reintento del ejemplo anterior podría llegar a retrasarse hasta 4,4 segundos. El tiempo de espera no incluye el tiempo invertido en conectar con el servicio, en subir los datos o en esperar una respuesta.

 *Advertencia:* La reducción del tiempo de espera bajando cualquiera de estos valores predeterminados puede dar lugar a que los documentos no se suban correctamente a través del adaptador de salida configurado. Cuando se usan los servicios de Watson Developer Cloud, esto se pone de manifiesto en los mensajes RetryFailure que aparecen en el registro y en los que se hace mención a una limitación de velocidad "429 Demasiadas peticiones". 
 
## Opciones de depuración
*  **full_node_debugging** - Activa el modo de depuración; los valores posibles son `true` y `false`. **Advertencia**: Esto incluirá en los registros todos los datos de todos los documentos rastreados.
*  **heartbeat_wait_time** – Intervalo de tiempo, en milisegundos, que transcurre entre generaciones de informes de estadísticas de ingestión de documentos (solo en modo de depuración). El valor predeterminado es de 1000 milisegundos.

## Opciones de registro cronológico
*  **configuration_file** - El archivo de configuración que se usa para el registro. En el archivo de ejemplo `crawler.conf`, esta opción está definida en `logging.log4j` y su valor predeterminado es `log4j_custom.properties`.
Esta opción debe definirse de manera similar cuando se usen archivos `.properties` o `.conf`.

## Opciones de gestión de rastreo adicionales
*  **shutdown_timeout** – Especifica el valor del tiempo de espera, en minutos, antes de que se concluya la aplicación. El valor predeterminado es `10`.
*  **output_limit** - Número máximo de elementos indexables que el rastreador intenta enviar de forma simultánea al adaptador de salida. Pude limitarse adicionalmente con el número de núcleos disponibles para realizar el trabajo. Indica que, en cualquier momento dado, no habrá más de "x" elementos indexables enviados al adaptador en espera de devolución. El valor predeterminado es `10`.
*  **input_limit** – Limita el número de URL que el conector puede solicitar a la vez. El valor predeterminado es
`3`.
*  **output_timeout** - Cantidad de tiempo, en segundos, que transcurre antes de que Data Crawler desista ante una solicitud al adaptador de salida y elimine el elemento de la cola del adaptador de salida para permitir más procesamiento. El valor predeterminado es
`1200`. **Nota** - Deben tenerse en cuenta las restricciones impuestas por el adaptador de salida, ya que dichas restricciones pueden estar relacionadas con los límites definidos aquí. El `output_limit` definido anteriormente solo se refiere a cuántos objetos indexables pueden enviarse al adaptador de salida a la vez. Una vez que un objeto indexable se envía al adaptador de salida, empieza a "contar el reloj" definido en la variable `output_timeout`. Puede que el propio adaptador de salida tenga un regulador que impida que pueda procesar todas las entradas que reciba. Por ejemplo, puede que el adaptador de salida de Orchestration tenga una agrupación de conexiones configurable para las conexiones HTTP del servicio. Si, por ejemplo, su valor predeterminado es 8 y se configura `output_limit` a un número mayor que 8, habrá procesos que estén esperando su turno para ejecutar y para los que esté contando el reloj. Puede que en tal caso se produzcan agotamientos del tiempo de espera.
*  **num_threads** - Número de hilos paralelos que se pueden ejecutar a la vez. Este valor puede ser un entero, que especifica directamente el número de hilos paralelos, o puede ser una cadena con el formato "xNUM" que especifica el factor de multiplicación del número de procesadores disponibles. El valor predeterminado es `"30"`.

## VÉASE TAMBIÉN

crawler(1)

vcrypt(1)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
