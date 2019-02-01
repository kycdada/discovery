# Configuración de las opciones de rastreo
El rastreador de datos recopila los datos en bruto que en un momento dado se usarán para construir los resultados de búsqueda del servicio IBM Watson Retrieve and  Rank. 

El rastreador de datos proporciona en la actualidad conectores que soportan la recopilación de datos de los repositorios siguientes:

*	Sistema de archivos.
*	Bases de datos vía JDBC.
*	CMIS (Content Management Interoperability Services).
*	Comparticiones de archivos SMB (Server message Block, CIFS (Common Internet Filesystem) o Samba.
*	SharePoint y SharePoint Online.
*	Box.

También se proporciona una plantilla de configuración de conector que permite personalizar un conector.

## Primeros pasos:
Al rastrear repositorios de datos, el rastreador comienza en un URL de semilla inicial especificado por el usuario y empieza a descargar páginas de información. El rastreador también localiza los enlaces de las páginas descargadas y planifica las páginas recién descubiertas para su rastreo adicional.

La información de configuración se utiliza para determinar qué páginas hay que rastrear y cómo rastrearlas. En este archivo se explican las opciones que se pueden configurar en cada conector.

**Nota**: Cada conector tiene también su correspondiente archivo de configuración de semilla; las opciones de configuración de semilla se describen aparte.

### Configuración del conector de sistema de archivos
El conector de sistema de archivos permite rastrear archivos locales a la instalación del rastreador de datos. A continuación se indican las opciones de configuración básicas necesarias para usar el conector de sistema de archivos. Para configurar estos valores, abra el archivo `config/connectors/filesystem.conf` y modifique los siguientes valores conforme a cada caso de uso concreto:

*  **protocol** - Nombre del protocolo de conector usado en el rastreo. Use `sdk-fs` para este conector.
*  **collection** – Este atributo se utiliza para desempaquetar los archivos temporales.
*  **logging-config** - Especifica el archivo usado para configurar las opciones de registro; tiene que formatearse como una cadena XML de `log4j`.
*  **classname** - Nombre de la clase Java del conector. El valor que tiene que usar este conector es `plugin:filesystem.plugin@filesystem`.

### Configuración del conector de base de datos
El conector de base de datos permite rastrear una base de datos ejecutando un comando SQL personalizado y creando un documento por fila (registro) y un elemento de contenido por columna (campo). Se puede especificar una columna para que se use como clave exclusiva, así como una columna que contenga una indicación de fecha y hora que represente la fecha de última modificación de cada registro. El conector recupera todos los registros de la base de datos especificada y también puede limitarse a determinadas tablas, uniones, etc. en la sentencia SQL.

El conector de base de datos permite rastrear las bases de datos siguientes:

*  IBM DB2
*  MySQL
*  Oracle
*  PostgreSQL
*  Microsoft SQL Server
*  Sybase
*  Otras bases de datos compatibles con SQL a través de un controlador compatible con JDBC 3.0

El conector recupera todos los registros de la base de datos y la tabla especificadas.

**Controladores JDBC**
El conector de base de datos se distribuye con un controlador JDBC de Oracle (conectividad de base de datos Java) versión 1.5. Todos los controladores JDBC de terceros que se distribuyen con el rastreador de datos se encuentran en el directorio `/lib/java/database` de la instalación del rastreador de datos, donde se pueden añadir, eliminar y modificar según sea necesario. También se puede utilizar el valor de `extra_jars_dir` en el archivo `crawler.conf` para especificar otra ubicación.

***Controladores JDBC DB2***
El rastreador de datos no incluye controladores JDBC de DB2 por motivos de licencia. No obstante, todas las instalaciones DB2 en las que se haya instalado un soporte de JDBC incluyen los archivos JAR que necesita el rastreador de datos a fin de poder rastrear una instalación DB2. Para rastrear una instancia de DB2, hay que copiar dichos archivos en el correspondiente directorio de la instalación del rastreador de datos para que el conector de base de datos pueda usarlos.

Para posibilitar que el rastreador de datos rastree una instalación de DB2, localice los archivos JAR `db2jcc.jar` y de licencia (normalmente `db2jcc_license_cu.jar`) en la instalación de DB2 y cópielos en el subdirectorio `lib/java` del directorio de instalación del rastreador de datos, o use el valor de configuración `extra_jars_dir` en el archivo `crawler.conf` para especificar otra ubicación.

***Controladores JDBC de MySQL***
El rastreador de datos no incluye controladores JDBC de MySQL por posibles problemas de licencia que surgirían si se incluyeran en el producto. No obstante, es muy fácil descargar el archivo JAR que contiene los controladores JDBC de MySQL e integrarlo en la instalación del rastreador de datos:

1.	Use un navegador web para visitar el sitio de descargas de MySQL y localice el enlace  de descarga de fuentes y binarios del formato de archivo que desee utilizar (normalmente zip en sistemas Microsoft Windows o un archivo tar comprimido con gzip en sistemas Linux). Pulse en ese enlace para iniciar el proceso de descarga. Es posible que se tenga que registrar.

2.	Use el correspondiente comando `unzip nombre-archivo-archivado` o `tar zxf nombre-archivo-archivado` para extraer el contenido del archivado en función del tipo y del nombre del archivo de archivado descargado.

3.	Vaya al directorio extraído del archivo de archivado y copie el archivo JAR de este directorio en el subdirectorio `lib/java` del directorio de instalación del rastreador de datos, o puede utilizar el valor de configuración `extra_jars_dir` en el archivo `crawler.conf` para especificar otra ubicación.

A continuación se indican las opciones de configuración básicas necesarias para usar el conector de base de datos. Para configurar estos valores, abra el archivo `config/connectors/database.conf` y modifique los siguientes valores conforme a cada caso de uso concreto:

*  **protocol** - Nombre del protocolo de conector usado en el rastreo. El valor de este conector se basa en el sistema de base de datos al que se accede.
*  **collection** – Este atributo se utiliza para desempaquetar los archivos temporales.
*  **classname** - Nombre de la clase Java del conector. El valor que tiene que usar este conector es `plugin:database.plugin@database`.
*  **logging-config** - Especifica el archivo usado para configurar las opciones de registro; tiene que formatearse como una cadena XML de `log4j`.

### Configuración del conector CMIS
El conector CMIS (Content Management Interoperability Services) permite rastrear repositorios CMS (Content Management System) habilitados para CMIS como, por ejemplo, Alfresco, Documentum o IBM Content Manager, e indexar los datos que contienen.

A continuación se indican las opciones de configuración básicas necesarias para usar el conector CMIS. Para configurar estos valores, abra el archivo `config/connectors/cmis.conf` y modifique los siguientes valores conforme a cada caso de uso concreto:

*  **protocol** - Nombre del protocolo de conector usado en el rastreo. Use `cmis` para este conector.
*  **collection** – Este atributo se utiliza para desempaquetar los archivos temporales.
*  **dns** - Opción no usada.
*  **classname** - Nombre de la clase Java del conector. El valor que tiene que usar este conector debe ser `plugin:cmis-v1.1.plugin@connector`.
*  **logging-config** - Especifica el archivo usado para configurar las opciones de registro; tiene que formatearse como una cadena XML de `log4j`.
*  **endpoint** - URL del punto final de servicio de un repositorio compatible con CMIS. Por ejemplo, las estructuras de URL de SharePoint son:
   *  Para un enlace AtomPub:   
      http://<servidor>:<puerto>/_vti_bin/cmis/rest?getRepositories
   *  Para un enlace WebServices:   
      http://<servidor>:<puerto>/_vti_bin/cmissoapwsdl.aspx

*  **username** - Nombre de usuario del repositorio CMIS que se usa para acceder al contenido. Este usuario debe tener acceso a todos los documentos y carpetas de destino que se van a rastrear e indexar.
*  **password** - Contraseña del repositorio CMIS que se va a usar para acceder al contenido. La contraseña NO puede estar cifrada; hay que proporcionarla en claro.
*  **repositoryid** – ID de repositorio CMIS que se utiliza para acceder al contenido de un repositorio concreto.
*  **bindingtype** -Identifica qué tipo de enlace hay que usar para conectarse a un repositorio CMIS. El valor puede ser `AtomPub` o `WebServices`.
*  **authentication** - Identifica qué tipo de mecanismo de autenticación se usa al  conectar con un repositorio compatible con CMIS: `Basic HTTP Authentication` (autenticación HTTP básica), `NTLM` o `WS-Security(Username token)` (token de nombre de usuario).
*  **enable-acl** - Habilita la recuperación de las ACL de los datos rastreados. Si no le importa la seguridad de los documentos de esta recopilación puede inhabilitar esta opción, ya que aumentará el rendimiento al no solicitar esta información en el documento y no tener que recuperarla ni decodificarla.El valor es `true` o `false`.
*  **user-agent** - Cabecera que se envía al servidor cuando se rastrean documentos.
*  **method** - Método (`GET` o `POST`) mediante el que se pasan los parámetros.
*  **url-logging** - Nivel de registro de los URL rastreados. Los
valores posibles son:

   *  ***full-logging*** - Registra toda la información del URL.
   *  ***refined-logging*** - Solo registra la información necesaria para examinar el registro del rastreador y para que el conector funcione correctamente; este es el valor predeterminado. 
   *  ***minimal-logging*** - Solo registra la mínima cantidad de información necesaria para que el conector funcione correctamente.

   Si se configura esta opción a minimal-logging se reducirá el tamaño de los registros y se obtendrá una ligera mejora de rendimiento gracias a la reducción de E/S que conlleva la minimización de la cantidad de datos registrados. 
*  **ssl-version** - Especifica la versión de SSL que se usa en las conexiones HTTPS. De forma predeterminada, se utiliza el protocolo más fuerte
disponible.

### Configuración del conector SMB/CIFS/Samba
El conector de Samba permite rastrear comparticiones de archivos Server Message Block (SMB) y Common Internet archivos (CIFS). Este tipo de compartición de archivos es común en las redes Windows y también se proporciona en el proyecto de código abierto [Samba](https://www.samba.org/).

A continuación se indican las opciones de configuración básicas necesarias para usar el conector Samba. Para configurar estos valores, abra el archivo `config/connectors/samba.conf` y modifique los siguientes valores conforme a cada caso de uso concreto:

*  **protocol** - Nombre del protocolo de conector usado en el rastreo. El valor para usar este conector es `smb`.
*  **collection** – Este atributo se utiliza para desempaquetar los archivos temporales.
*  **classname** - Nombre de la clase Java del conector. El valor que tiene que usar este conector es `plugin:smb.plugin@connector`.
*  **logging-config** - Especifica el archivo usado para configurar las opciones de registro; tiene que formatearse como una cadena XML de `log4j`.
*  **username** - Nombre de usuario Samba con el que autenticar. Si se proporciona, también hay que proporcionar el dominio y la contraseña. Si no se proporciona, se usa la cuenta de invitado. 
*  **password** - Contraseña Samba con la que autenticar. Si se proporciona el nombre de usuario, este valor es obligatorio. La contraseña tiene que cifrarse utilizando la biblioteca VCrypt que se distribuye con el rastreador de datos.
*  **archive** - Permite que el conector Samba rastree e indexe los archivos comprimidos dentro de los archivos de archivado. El valor puede ser `true` o `false`; el valor predeterminado es `false`.
*  **max-policies-per-handle** - Especifica el número máximo de políticas Local Security Authority (LSA) que pueden abrirse para un único manejador (handle) RPC. Estas políticas definen los permisos de acceso necesarios para consultar o modificar un determinado sistema en diversas condiciones. El valor predeterminado de esta opción es `255`.
*  **crawl-fs-metadata** - Si se activa esta opción, se provoca que el rastreador de datos añada un documento VXML que contiene los metadatos de sistema de archivos disponibles del archivo (fecha de creación, fecha de última modificación, atributos de archivo, etc.)
*  **enable-arc-connector** - Opción no usada.
*  **disable-indexes** - Lista separada por saltos de línea de los índices que hay que inhabilitar, lo que puede acelerar el rastreo; por ejemplo:

   *  disable-url-index
   *  disable-error-state-index
   *  disable-crawl-time-index
*  **exact-duplicates-hash-size** - Define el tamaño de la tabla hash usada para resolver duplicados exactos. Tenga cuidado al modificar este número. El valor que seleccione tiene que ser primo y cuanto mayor sea el tamaño más rápidas serán las búsquedas, aunque requerirán más memoria, mientras que tamaños más pequeños pueden ralentizar los rastreos aunque a la vez reducir considerablemente el consumo de memoria.
*  **user-agent** - Opción no usada.
*  **timeout** - Opción no usada.
*  **n-concurrent-requests** - Número de peticiones que se envían en paralelo a una única dirección IP. El valor predeterminado es `1`.
*  **enqueue-persistence** - Opción no usada.

### Configuración del conector de SharePoint
El conector de SharePoint permite rastrear objetos de SharePoint Server y SharePoint Online e indexar la información que contienen. Objetos como, por ejemplo, documento, perfil de usuario, recopilación de sitio, blog, listitem, lista de membresía, página de directorio, etc. pueden indexarse con sus metadatos asociados. En el caso de los elementos de lista y documentos, los índices pueden incluir anexos. 

**Nota**: El conector de SharePoint respeta el atributo `noindex` en todos los objetos de SharePoint independientemente de su tipo concreto (blogs, documentos, perfiles de usuario, etc.). En cada resultado se devuelve un único documento.

**Importante**: La cuenta de SharePoint que se utiliza para rastrear los sitios SharePoint ha de tener al menos privilegios completos de lectura. 

A continuación se indican las opciones de configuración básicas necesarias para usar el conector de SharePoint. Para configurar estos valores, abra el archivo `config/connectors/sharepoint.conf` y modifique los siguientes valores conforme a cada caso de uso concreto:

*  **protocol** - Nombre del protocolo de conector usado en el rastreo. Use `io-sp` para este conector.
*  **collection** – Este atributo se utiliza para desempaquetar los archivos temporales.
*  **classname** - Nombre de la clase Java del conector. El valor que tiene que usar este conector es `plugin:io-sharepoint.plugin@connector`.
*  **logging-config** - Especifica el archivo usado para configurar las opciones de registro; tiene que formatearse como una cadena XML de `log4j`.
*  **seed-url-type** - Identifica a qué tipo de objeto SharePoint apuntan los URL de semilla proporcionados: recopilaciones de sitio o aplicaciones web (también conocidas como servidores virtuales).

   *  ***Site Collections*** - Si el tipo de URL de semilla se establece a `Site Collections`, solo se rastrearán los hijos de la recopilación de sitio referenciada por el URL.

   *  ***Web Applications*** - Si el tipo de URL de semilla se establece a `Web Applications`, se rastrearán todas las recopilaciones de sitio (y sus hijos) que pertenezcan a las aplicaciones web referenciadas por cada URL. 
*  **auth-type** - Mecanismo de autenticación que se usa al contactar con el servidor de SharePoint: `BASIC`, `NTLM2`, `KERBEROS` o `CBA`. El tipo de autenticación predeterminado es `NTLM2`.
*  **spUser** – Nombre de usuario del usuario de SharePoint que se utiliza para acceder al contenido. Este usuario debe tener acceso a todos los sitios de destino y listas que hay que rastrear e indexar, y tiene que ser capaz de recuperar y resolver los permisos asociados. El mejor especificarlo con el nombre de dominio, por ejemplo: `MIDOMINIO\\Administrator`.
*  **spPassword** - Contraseña del usuario de SharePoint que se usa para acceder al contenido. La contraseña tiene que cifrarse utilizando el programa vcrypt que se distribuye con Data Crawler.
*  **cba-sts** - URL el punto final de Security Token Service (STS) contra el que se autentica el usuario de rastreo. En el caso de un SharePoint in situ con ADFS, tiene que ser el punto final de ADFS. Si ell tipo de autenticación se establece a `CBA` (Claims Based Authentication), este campo es obligatorio. 
*  **cba-realm** - Identificador de relación de confianza para usuario autenticado ("Relying Party Trust") que se usa al solicitar un token al STS. A veces se conoce como valor "AppliesTo" o el "Realm" (reino). En el caso de SharePoint Online, tiene que ser el URL de la raíz de la instancia de SharePoint Online (por ejemplo, `https://miempresa.sharepoint.com`). En el caso de ADFS, es el valor de ID de la relación de confianza para usuario autenticado entre SharePoint y ADFS (por ejemplo, `"urn:SHAREPOINT:adfs"`).
*  **everyone-group** - Cuando se especifica, se usa este nombre de grupo en las ACL cuando hay que dar acceso a todo el mundo. Este campo es obligatorio cuando están habilitados los perfiles de usuario de rastreo. **Nota** - El servicio de recuperación y clasificación aún no respeta la seguridad. 
*  **user-profile-master-url** - URL base que usa el conector para crear enlaces a perfiles de usuario. Debe configurarse para que apunte al formulario de pantalla de los perfiles de usuario. Si se encuentra el token `%FIRST_SEED%`, se sustituye por el primer URL de semilla. Es obligatorio cuando está habilitada la búsqueda de perfiles de usuario.
*  **urls** - Lista separada por saltos de línea de los URL HTTP de las aplicaciones web de SharePoint o recopilaciones de sitio que hay que rastrear.
*  **ehcache-config** - Opción no usada.
*  **method** - Método (`GET` o `POST`) mediante el que se pasan los parámetros.
*  **cache-types** - Opción no usada.
*  **cache-size** - Opción no usada.
*  **enable-acl** - Habilita el rastreo de perfiles de usuario de SharePoint; los valores son `true` o `false`. El valor predeterminado es `false`.

### Configuración del conector de Box
El conector de Box permite rastrear una instancia de Enterprise Box e indexar la información que contiene. A continuación se indican las opciones de configuración básicas necesarias para usar el conector de Box. Para configurar estos valores, abra el archivo `config/connectors/box.conf` y modifique los siguientes valores conforme a cada caso de uso concreto:

*  **protocol** - Nombre del protocolo de conector usado en el rastreo. Use `box` para este conector.
*  **classname** - Nombre de la clase Java del conector. El valor que tiene que usar este conector es `plugin:box.plugin@connector`.
*  **logging-config** - Especifica el archivo usado para configurar las opciones de registro; tiene que formatearse como una cadena XML de `log4j`.
*  **box-crawl-seed-url** - URL base de Box. El valor de este conector es `box://app.box.com/`. Se pueden rastrear diferentes tipos de URL, por ejemplo:

   *  ***Para rastrear una empresa entera***: `box://app.box.com/`
   *  ***Para rastrear una carpeta concreta***: `box://app.box.com/user/ID_USUARIO/folder/ID_CARPETA/NombreCarpeta`
   *  ***Para rastrear un usuario concreto***: `box://app.box.com/user/ID_USUARIO/`
*  **client-id** - Especifique el ID de cliente proporcionado por Box al crear la aplicación Box.
*  **client-secret** - Especifique el secreto de cliente proporcionado por Box al crear la aplicación Box.
*  **path-to-private-key** - Ubicación en el sistema de archivos local de la clave privada que forma parte del par de claves pública-privada generado para la comunicación con Box.
*  **kid** - Especifica el ID de la clave pública. Esta es la otra mitad del par de claves privada-pública generado para la comunicación con Box.
*  **enterprise-id** - Empresa en la que se ha autorizado la aplicación. El ID de empresa se lista en la página principal de la consola del administrador de Box.
*  **enable-acl** - Para uso interno exclusivamente. Habilita la recuperación de las ACL de los datos rastreados.
*  **user-agent** - Cabecera que se envía al servidor cuando se rastrean documentos.
*  **method** - Método (`GET` o `POST`) mediante el que se pasan los parámetros.
*  **url-logging** - Nivel de registro de los URL rastreados. Los
valores posibles son:

   *  ***full-logging*** - Registra toda la información del URL.
   *  ***refined-logging*** - Solo registra la información necesaria para examinar el registro del rastreador y para que el conector funcione correctamente; este es el valor predeterminado.
   *  ***minimal-logging*** - Solo registra la mínima cantidad de información necesaria para que el conector funcione correctamente.

   Si se configura esta opción a minimal-logging se reducirá el tamaño de los registros y se obtendrá una ligera mejora de rendimiento gracias a la reducción de E/S que conlleva la minimización de la cantidad de datos registrados.
*  **ssl-version** - Especifica la versión de SSL que se usa en las conexiones HTTPS. De forma predeterminada, se utiliza el protocolo más fuerte
disponible.

El conector de Box tiene algunas limitaciones:

* No se recuperan los comentarios ni las tareas en los archivos.
* El cuerpo del contenido de notas se recupera en formato JSON. Puede que sea necesaria una conversión adicional de los datos de nota. 
* Los documentos individuales no se pueden recuperar vía TestIt. Vía TestIt solo se pueden recuperar los URL, URL de carpeta y URL de usuario.


## VÉASE TAMBIÉN

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
