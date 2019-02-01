# Configuración del servicio de orquestación
El servicio de orquestación inndica al rastreador cómo gestionar los archivos rastreados. Las opciones predeterminadas pueden cambiarse directamente abriendo el archivo `config/orchestration/orchestration-service.conf` y modificando los siguientes valores en cada caso de uso concreto:

*  **http_timeout** – Tiempo de espera, en segundos, de la operación de lectura/indexación de documentos; el valor predeterminado es `585`.
*  **concurrent_upload_connection_limit** – Número de conexiones simultáneas permitidas para subir documentos; el valor predeterminado es `10`. En general, este número debe ser mayor o igual que el `output_limit` definido al configurar las opciones de rastreo.
*  **base_url** - URL al que se envían los documentos rastreados.
*  **endpoint** - Ubicación de la recopilación de documentos rastreados en `base-url`.
*  **username** - Nombre de usuario con el que autenticarse en la ubicación `endpoint`.
*  **password** - Contraseña con la que autenticarse en la ubicación `endpoint`. **Importante** - **NO** use el programa vcrypt que se suministra con Data Crawler para cifrar esta contraseña.
*  **config_file** - Archivo de configuración que usa el servicio de orquestación. 

El adaptador de salida del servicio Orchestration (orquestación) puede enviar estadísticas para que IBM comprenda mejor a sus usuarios y pueda ofrecerles un mejor servicio. Pue den configurarse las opciones siguientes para la variable `send_stats`:
*  **jvm** – Las estadísticas de la máquina virtual Java (JVM) enviadas incluyen el proveedor y la versión Java tal cual los notifica la propia JVM que se usa para ejecutar el rastreador de datos. El valor es `true` o `false`.
*  **os** - Las estadísticas de sistema operativo (SO) enviadas incluyen el nombre, la versión y la arquitectura del SO tal y como los notifica la JVM usada para ejecutar el rastreador de datos. El valor es `true` o `false`.

## VÉASE TAMBIÉN

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
