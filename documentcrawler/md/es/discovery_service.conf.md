# Configuración del servicio Discovery
El servicio Discovery indica al rastreador cómo gestionar los archivos rastreados cuando se utiliza el servicio IBM Watson Discovery. Las opciones predeterminadas pueden cambiarse directamente abriendo el archivo `config/discovery/discovery_service.conf` y modificando los siguientes valores en cada caso de uso concreto:

*  **http_timeout** – Tiempo de espera, en segundos, de la operación de lectura/indexación de documentos; el valor predeterminado es `125`.
*  **concurrent_upload_connection_limit** - Número de conexiones simultáneas permitidas para subir documentos; el valor predeterminado es `2`. Cuando se utiliza el adaptador de salida de Orchestration, este número debe ser mayor o igual que el `output_limit` definido al configurar las opciones de rastreo.
*  **base_url** - URL al que se envían los documentos rastreados. Para el release actual del servicio Discovery, el valor es `https://gateway.watsonplatform.net/discovery/api`.
*  **environment_id** - Ubicación de la recopilación de documentos rastreados en `base-url`.
*  **collection_id** -Nombre de la recopilación de documentos configurada en el servicio Discovery.
*  **configuration_id** - Nombre de archivo del archivo de configuración que usa el servicio Discovery.
*  **check_for_completion** - Comprueba si el documento se ha procesado correctamente en el punto final. Así baja el rendimiento observado del rastreador, pero se generan notificaciones fiables de la subida y conversión satisfactorias de los documentos. El valor es `true` o `false`.  
**IMPORTANTE** - Cuando se habilita este parámetro, es recomendable incrementar el `concurrent_upload_connection_limit` a un valor mayor o igual que el `output_limit` definido al configurar las opciones de rastreo para usar plenamente los recursos disponibles.

Proporcione las credenciales del servicio Discovery:
*  **username** - Nombre de usuario con el que autenticarse en la ubicación de la recopilación de documentos rastreados.
*  **password** - Contraseña con la que autenticarse en la ubicación de la recopilación de documentos rastreados.

El adaptador de salida del servicio Discovery puede enviar estadísticas para que IBM comprenda mejor a sus usuarios y pueda ofrecerles un mejor servicio. Pue den configurarse las opciones siguientes para la variable `send_stats`:
*  **jvm** – Las estadísticas de la máquina virtual Java (JVM) enviadas incluyen el proveedor y la versión Java tal cual los notifica la propia JVM que se usa para ejecutar el rastreador de datos. El valor es `true` o `false`.
*  **os** - Las estadísticas de sistema operativo (SO) enviadas incluyen el nombre, la versión y la arquitectura del SO tal y como los notifica la JVM usada para ejecutar el rastreador de datos. El valor es `true` o `false`.

*  **api_version** - Para uso interno exclusivamente. Fecha del último cambio de versión del API.

# Configuración del almacenamiento de seguimiento de URL
La carpeta `config/discovery` también contiene un archivo de configuración que puede usarse para correlacionar internamente los URL del rastreador y los ID de documento. Las opciones predeterminadas pueden cambiarse directamente abriendo el archivo `config/discovery/uri_tracking_storage.conf` y modificando los siguientes valores en cada caso de uso concreto:

*  **driver** - Clase del controlador JDBC H2 de la base de datos. El valor predeterminado es `org.h2.Driver`
*  **url** - Prefijo de URL de la cadena de conexión JDBC. El formato es `jdbc:h2:[file:]`. **NOTA** El prefijo `file:` es opcional. Si no se usa, o solo se usa una ruta relativa en `database_location`, se usa el directorio de trabajo actual como punto de partida. El valor predeterminado es `jdbc:h2:file:`
*  **database_location** - Ubicación en disco donde se almacena la base de datos, por ejemplo, `./storage/database` o `~/storage/database`. El valor predeterminado es `./storage/database`
*  **database_name** - Nombre de la base de datos. El valor predeterminado es `ActivityDB`
*  **table_name** - Nombre de la tabla que se usa. El valor predeterminado es `UriTracker`
*  **username** - Nombre de usuario con el que se conecta a la base de datos.
*  **password** - Contraseña con la que se conecta a la base de datos.

## VÉASE TAMBIÉN

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
