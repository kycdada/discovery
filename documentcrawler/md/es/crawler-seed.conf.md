# Configuración de las semillas de rastreo

Las semillas son el puntos de partida de un rastreo y las usa el rastreador de datos para recuperar datos de los recursos identificados por ellas. Las semillas suelen configurar los URL de acceso a recursos basados en protocolo como, por ejemplo, comparticiones de archivos, comparticiones SMB, bases de datos y otros repositorios de datos que sean accesibles a través de diversos protocolos web. Además, distintos URL de semilla tienen prestaciones distintas.

Una semilla también puede ser específica de repositorio a fin de habilitar el rastreo de aplicaciones de terceros concretas como, por ejemplo, sistemas de gestión de relaciones con los clientes (CRM), sistemas de ciclo de vida de producto (PLC), sistemas de gestión de contenidos (CMS), aplicaciones basadas en la nube y aplicaciones de base de datos web. 

El rastreado de datos proporciona en la actualidad semillas de rastreo que soportan conectores de archivo para los tipos de repositorio siguientes:

*	Sistema de archivos.
*	Bases de datos vía JDBC.
*	CMIS (Content Management Interoperability Services).
*	Comparticiones de archivos SMB (Server Message Block), CIFS (Common Internet Filesystem) o Samba.
*	SharePoint y SharePoint Online.
*	Box.

También se proporciona una plantilla de configuración de semilla de rastreo que permite personalizar una semilla de rastreo para un conector personalizado.

## Primeros pasos:

Al rastrear repositorios de datos, el rastreador comienza en un URL de semilla especificado por el usuario y empieza a descargar páginas de información. El rastreador también localiza los enlaces de las páginas descargadas y planifica las páginas recién descubiertas para su rastreo adicional.

La información de configuración se utiliza para determinar qué páginas hay que rastrear y cómo rastrearlas. En este archivo se explican las opciones que se pueden configurar en cada archivo de semilla de rastreo del conector.

**Nota**: Cada archivo de configuración de semilla de rastreo funciona con su correspondiente archivo de configuración de conector de archivo; las opciones de conector de archivo se describen aparte.

### Configuración de la semilla de rastreo de sistema de archivos

Pueden configurarse los valores siguientes para el archivo semilla de rastreo de sistema de archivos. Para configurar estos valores, abra el archivo `config/seeds/filesystem-seed.conf` y especifique los siguientes valores conforme a cada caso de uso concreto:

*  **url** - Lista separada por saltos de línea de los archivos y carpetas por rastrear. Los usuarios de UNIX pueden usar una ruta como, por ejemplo, `/usr/local/`.
Los URL tienen que empezar por `sdk-fs://`. Por ejemplo, para rastrear `/home/watson/mydocs`, el valor de este URL sería `sdk-fs:///home/watson/mydocs` - la tercera `/` es necesaria.
**Nota**: El conector de sistema de archivos utiliza un protocolo personalizado, `sdk-fs://`, para crear un URL válido. No prefije `file://` a las rutas listadas; los URL tienen que empezar por `sdk-fs://`.
*  **hops** - Para uso interno exclusivamente.
*  **default-allow** - Para uso interno exclusivamente.

### Configuración de la semilla de rastreo de base de datos

Pueden configurarse los valores siguientes para el archivo semilla de rastreo de base de datos. Para configurar estos valores, abra el archivo `config/seeds/database-seed.conf` y especifique los siguientes valores conforme a cada caso de uso concreto:

*  **url** - El URL de la tabla o vista que hay que recuperar. Define el URL de semilla de base de datos SQL personalizado. La estructura es:

   	`sistema-basedatos://host:puerto/basedatos?[per=num]&[sql=SQL]`

   Al probar un URL de semilla se mostrarán todos los URL encolados. Por ejemplo, si se prueba el siguiente URL de una base de datos que contiene 200 registros:

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=100&sql=select%20*%20from%20vessel&`

   se mostrarán los siguientes URL encolados:

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=0&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=100&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=200&`

   Mientras que si se prueba el URL siguiente se mostrarán los datos recuperados de la fila 43:

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=1&key-val=43`
*  **hops** - Para uso interno exclusivamente.
*  **default-allow** - Para uso interno exclusivamente.
*  **user-password** - Credenciales del sistema de base de datos. El nombre de usuario y la contraseña tienen que estar separados por `:` y la contraseña tiene que estar cifrada con el programa vcrypt que se suministra con el rastreador de datos. Por ejemplo, `nombreusuario:[[vcrypt/3]]cadenacontraseña`.
*  **max-data-size** - Tamaño máximo de los datos de un documento. Es el mayor bloque de memoria que se carga a la vez. Suba este límite solo si dispone de suficiente memoria en el sistema.
*  **filter-exact-duplicates** - Para uso interno exclusivamente.
*  **jdbc-class** (opción de ampliación) - Cuando se especifica, esta cadena sustituye la clase JDBC usada por el conector cuando se seleccione `(other)` (otro) como sistema de base de datos. 
*  **connection-string** (opción de ampliación) - Cuando se especifica, esta cadena sustituye la cadena de conexión JDBC generada de forma automática. Esto permite proporcionar una configuración más detallada de la conexión de base de datos como, por ejemplo, el equilibrio de carga o las conexiones SSL. Por ejemplo, `jdbc:netezza://127.0.0.1:5480/nombrebasedatos`.
*  **save-frequency-for-resume** (opción de ampliación) - Especifica el nombre de una etiqueta asociada o columna para poder reanudar un rastreo o realizar una renovación parcial. La semilla guarda el nombre de esta columna a intervalos regulares a medida que progresa el rastreo y lo guarda de nuevo una vez rastreada que la última fila de la base de datos. Cuando se reanuda o renueva el refresco, este comienza por la fila identificada en el valor guardado de este campo. 

### Configuración de la semilla de rastreo de CMIS

Pueden configurarse los valores siguientes para el archivo semilla de rastreo de CMIS. Para configurar estos valores, abra el archivo `config/seeds/cmis-seed.conf` y modifique los siguientes valores conforme a cada caso de uso concreto:

*  **url** - URL de una carpeta del repositorio CMIS que se usa como punto de partida del rastreo, por ejemplo:

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=workspace://SpacesStore/guid`
   Para rastrear desde la carpeta raíz, hay que especificar el URL así:

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=`
*  **at** - Opción no usada.
*  **default-allow** - Para uso interno exclusivamente.

### Configuración de la semilla de rastreo de Samba

Pueden configurarse los valores siguientes para el archivo semilla de rastreo de Samba. Para configurar estos valores, abra el archivo `config/seeds/samba-seed.conf` y modifique los siguientes valores conforme a cada caso de uso concreto:

*  **url** - Lista de separada por saltos de línea de las comparticiones que hay que rastrear, por ejemplo:

   *  `smb://share.test.com/office`
   *  `smb://share.test.com/cash/money/change`
   *  `smb://share.test.com/C$/Program Files`

*  **hops** - Para uso interno exclusivamente.
*  **default-allow** - Para uso interno exclusivamente.

### Configuración de la semilla de rastreo de SharePoint

Pueden configurarse los valores adicionales siguientes para el archivo semilla de rastreo de SharePoint. Para configurar estos valores, abra el archivo `config/seeds/sharepoint-seed.conf` y modifique los siguientes valores conforme a cada caso de uso concreto:

*  **url** - Lista de separada por saltos de línea de las aplicaciones web o recopilaciones de sitio de SharePoint que hay que rastrear, por ejemplo:

   *  `io-sp://a.com`
   *  `io-sp://b.com:83/site`
   *  `io-sp://c.com/site2`

   Los subsitios de estos sitios también se rastrearán (a menos que sean excluidos por otras reglas de rastreo).
*  **filter-url** - Lista de separada por saltos de línea de las aplicaciones web o recopilaciones de sitio de SharePoint que hay que rastrear, por ejemplo:

   *  `http://a.com`
   *  `http://b.com:83/site`
   *  `http://c.com/site2`

*  **hops** - Para uso interno exclusivamente.
*  **n-concurrent-requests** - Para uso interno exclusivamente.
*  **delay** - Para uso interno exclusivamente.
*  **default-allow** - Para uso interno exclusivamente.
*  **seed-protocol** - Define el protocolo de semilla de los hijos de la recopilación de sitios. Es obligatorio cuando el protocolo de la recopilación de sitios es SSL, HTTP o HTTPS. Este valor tiene que coincidir con el protocolo de la recopilación de sitios.

### Configuración de la semilla de Box

Pueden configurarse los valores siguientes para el archivo semilla de rastreo de Box. Para configurar estos valores, abra el archivo `config/seeds/box-seed.conf` y especifique los siguientes valores conforme a cada caso de uso concreto:

*  **url** - URL que se usa como punto de partida del rastreo. El valor predeterminado es `box://app.box.com/`.
*  **default-allow** - Para uso interno exclusivamente.

## VÉASE TAMBIÉN

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

orchestration_service.conf(5)
