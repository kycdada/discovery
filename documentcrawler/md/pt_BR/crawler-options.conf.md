# Configurando opções de crawl
O Data Crawler coleta os dados brutos eventualmente usados para formar resultados da procura para o
serviço do IBM Watson Retrieve and Rank.

O Data Crawler fornece atualmente os conectores para suportar a coleção de dados a partir dos
repositórios a seguir:

*	Sistema de arquivos
*	Bancos de dados, por meio de JDBC
*	CMIS (Content Management Interoperability Services)
*	Compartilhamentos de arquivos SMB (Server message Block), CIFS (Common Internet Filesystem) ou Samba
*	SharePoint e SharePoint Online
*	Postal

Um modelo de configuração do conector também é fornecido, o que permite customizar um conector.

## Introdução:
Ao efetuar crawl dos repositórios de dados, o crawler é iniciado em uma URL de valor inicial especificada
pelo usuário, e inicia o download das páginas de informações. O crawler também localiza links nas páginas
transferidas por download e planeja as páginas descobertas recentemente para execução de crawl adicional.

As informações de configuração são usadas para determinar quais páginas precisam ser
passadas por crawl, e como efetuar crawl nelas. Esse arquivo explica as opções que são possíveis de configurar para
cada conector.

**Nota**: cada conector também possui um arquivo de configuração inicial
correspondente; as opções de configuração inicial são descritas separadamente.

### Configurando o Filesystem Connector
O Filesystem Connector permite efetuar crawl do local dos arquivos
para a instalação do Data Crawler. A seguir estão as opções de configuração básica necessárias para usar o
Filesystem Connector. Para configurar esses valores, abra o arquivo
`config/connectors/filesystem.conf` e modifique os valores a seguir, específicos para os
casos de uso:

*  **protocol** - O nome do protocolo do conector usado para o crawl. Use
`sdk-fs` para esse conector.
*  **collection** - Este atributo é usado para descompactar arquivos temporários.
*  **logging-config** - Especifica o arquivo usado para configurar opções de
criação de log; ele deve ser formatado como uma sequência XML `log4j`.
*  **classname** - Nome de classe Java para o conector. O valor para usar esse
conector deve ser `plugin:filesystem.plugin@filesystem`.

### Configurando o conector de banco de dados
O conector de banco de dados permite efetuar crawl de um banco de dados executando um comando SQL
customizado e criando um documento por linha (registro) e um elemento de conteúdo por coluna (campo). É
possível especificar uma coluna a ser usada como uma chave exclusiva, bem como uma coluna que contém um
registro de data e hora que representa a data da última modificação de cada registro. O conector recupera
todos os registros do banco de dados especificado, e também pode ser restrito às tabelas específicas,
junções, etc., na instrução SQL.

O conector de banco de dados permite efetuar crawl dos bancos de dados a seguir:

*  IBM DB2
*  MySQL
*  Oracle
*  PostgreSQL
*  Microsoft SQL Server
*  Sybase
*  Outros bancos de dados compatíveis com SQL por meio de um driver compatível com JDBC 3.0

O conector recupera todos os registros da tabela e do banco de dados especificados.

**Drivers JDBC**
O conector de banco de dados é enviado com o driver Oracle JDBC (Java Database
Connectivity) versão 1.5. Todos os drivers JDBC de terceiros enviados com o data crawler estão
localizados no diretório `/lib/java/database` de instalação do data crawler, em que é
possível incluí-los, removê-los e modificá-los, conforme necessário. Também é possível usar a configuração
`extra_jars_dir` no arquivo `crawler.conf` para especificar outro local.

**Drivers JDBC *DB2***
O data crawler não é enviado com os drivers JDBC para DB2 devido a problemas de
licensa. No entanto, todas as instalações do DB2 nas quais o suporte do JDBC foi instalado, incluem os arquivos JAR que
o data crawler requer, para poder efetuar crawl de uma instalação do DB2. Para executar crawl em uma instância do
DB2, deve-se copiar esses arquivos no diretório apropriado na instalação do data crawler, para que o
conector de banco de dados possa usá-los.

Para ativar o data crawler para efetuar crawl de uma instalação do DB2, localize os arquivos JAR
`db2jcc.jar` e a licença (geralmente, `db2jcc_license_cu.jar`)
na instalação do DB2, e copie esses arquivos no subdiretório `lib/java` do diretório de
instalação do data crawler, ou é possível usar a configuração de `extra_jars_dir`
no arquivo `crawler.conf` para especificar outro local.

**Drivers JDBC *MySQL***
O data crawler não é enviado com os drivers JDBC para MySQL por causa de possíveis problemas de
licença, se eles foram entregues como parte do produto. No entanto, fazer download do
arquivo JAR que contém os drivers JDBC MySQL e integrar esse arquivo JAR na instalação do data crawler é
muito fácil: 

1.	Use um navegador da web para visitar o site de download do MySQL, e localize a origem e o link de
download binário para o formato de archive que deseja usar (geralmente zip para sistemas Microsoft Windows
ou um gzipped tarball para sistemas Linux). Clique nesse link para iniciar o processo de download. O registro
pode ser necessário.

2.	Use o comando `unzip archive-file-name` ou `tar zxf
archive-file-name` apropriado para extrair o conteúdo desse archive, com base no tipo e no nome do
archive do qual é feito download.

3.	Mude para o diretório que foi extraído do archive, e copie o arquivo JAR desse
diretório para o subdiretório `lib/java` do diretório de instalação do
data crawler, ou é possível usar a configuração `extra_jars_dir` no arquivo
`crawler.conf` para especificar outro local.

A seguir estão as opções de configuração básica necessárias para usar o conector de banco de dados. Para
configurar esses valores, abra o arquivo `config/connectors/database.conf` e modifique
os valores a seguir, específicos para os casos de uso: 

*  **protocol** - O nome do protocolo do conector usado para o crawl. O valor para
esse conector é baseado no sistema de banco de dados a ser acessado.
*  **collection** - Este atributo é usado para descompactar arquivos temporários.
*  **classname** - Nome de classe Java para o conector. O valor para usar esse
conector deve ser `plugin:database.plugin@database`.
*  **logging-config** - Especifica o arquivo usado para configurar opções de
criação de log; ele deve ser formatado como uma sequência XML `log4j`.

### Configurando o conector CMIS
O conector CMIS (Content Management Interoperability Services) permite efetuar crawl dos repositórios
do CMS (Content Management System) ativados pelo CMIS, como Alfresco, Documentum ou IBM Content
Manager, e indexar os dados que eles contêm.

A seguir estão as opções de configuração básica necessárias para usar o conector CMIS. Para configurar
esses valores, abra o arquivo `config/connectors/cmis.conf` e modifique os valores a seguir,
específicos para os casos de uso:

*  **protocol** - O nome do protocolo do conector usado para o crawl. Use
`cmis` para esse conector.
*  **collection** - Este atributo é usado para descompactar arquivos temporários.
*  **dns** - Opção não usada.
*  **classname** - Nome de classe Java para o conector. O valor para usar esse
conector deve ser `plugin:cmis-v1.1.plugin@connector`.
*  **logging-config** - Especifica o arquivo usado para configurar opções de
criação de log; ele deve ser formatado como uma sequência XML `log4j`.
*  **endpoint** - A URL do terminal em serviço de um repositório compatível com CMIS. 
Por exemplo, as estruturas da URL para SharePoint são:
   *  Para ligação de AtomPub:   
      http://<server>:<port>/_vti_bin/cmis/rest?getRepositories
   *  Para ligação de WebServices:   
      http://<server>:<port>/_vti_bin/cmissoapwsdl.aspx

*  **username** - O nome do usuário do repositório CMIS usado para
acessar o conteúdo. Esse usuário deve ter acesso a todas as pastas e documentos de destino a serem passados
por crawl e indexados.
*  **password** - A senha do repositório CMIS, usada para acessar o conteúdo. A
senha NÃO deve ser criptografada; ela deve fornecida em texto simples.
*  **repositoryid** - O ID do repositório CMIS usado para acessar o conteúdo para
esse repositório específico.
*  **bindingtype** - Identifica o tipo de ligação que deve ser usado para
se conectar a um repositório CMIS. O valor é `AtomPub` ou `WebServices`.
*  **authentication** - Identifica qual tipo de mecanismo de autenticação usar ao
entrar em contato com um repositório compatível com CMIS: `Basic HTTP Authentication`,
`NTLM` ou `WS-Security(Username token)`.
*  **enable-acl** - Permite a recuperação de ACLs para dados passados por crawl. Se
você não estiver preocupado com a segurança dos documentos nessa coleção, a desativação dessa
opção aumentará o desempenho por não solicitar essas informações com o documento e não
recuperar e codificar essas informações. O valor é `true` ou `false`.
*  **user-agent** - Um cabeçalho enviado ao servidor ao efetuar crawl de documentos.
*  **method** - O método (`GET` ou `POST`) pelo
qual os parâmetros serão passados.
*  **url-logging** - A extensão para a qual as URLs passadas por crawl são
registradas. Os valores
possíveis são:

   *  ***full-logging*** - Registre todas as informações sobre a URL.
   *  ***refined-logging*** - Registre somente as informações necessárias para
procurar o log do crawler e para que o conector funcione corretamente; este é o valor padrão.
   *  ***minimal-logging*** -Registre somente a quantia mínima de informações
necessárias para que o conector funcione corretamente.

   Configurar esta opção para criação de log mínima reduzirá o tamanho dos logs e ganhará um
ligeiro aumento de desempenho devido à E/S menor associada à minimização da quantia de dados que está sendo
registrada.
*  **ssl-version** - Especifica uma versão de SSL a ser usada para conexões HTTPS. Por
padrão, o protocolo mais sólido disponível é usado.

### Configurando o Conector SMB/CIFS/Samba
O conector Samba permite efetuar crawl de compartilhamentos de arquivos de Server Message Block (SMB) e
Common Internet Filesystem (CIFS). Esse tipo de compartilhamento de arquivos é comum em redes Windows, e
também é fornecido por meio do projeto de software livre [Samba](https://www.samba.org/).

A seguir estão as opções de configuração básica necessárias para usar o conector Samba. Para configurar
esses valores, abra o arquivo `config/connectors/samba.conf` e modifique os valores a
seguir, específicos para os casos de uso:

*  **protocol** - O nome do protocolo do conector usado para o crawl. O valor para
usar esse conector é `smb`.
*  **collection** - Este atributo é usado para descompactar arquivos temporários.
*  **classname** - Nome de classe Java para o conector. O valor para usar esse
conector deve ser `plugin:smb.plugin@connector`.
*  **logging-config** - Especifica o arquivo usado para configurar opções de
criação de log; ele deve ser formatado como uma sequência XML `log4j`.
*  **username** - O nome do usuário do Samba com o qual se autenticar. Se
fornecido, o domínio e a senha deverão ser fornecidos também. Se não for fornecido, a conta guest será
usada.
*  **password** - A senha do Samba com a qual se autenticar. Se o nome do usuário
for fornecido, ela será necessária. A senha deve ser criptografada usando a biblioteca VCrypt enviada
com o data crawler.
*  **archive** - Permite que o conector Samba efetue crawl e indexe arquivos
compactados dentro de archives. O valor é `true` ou `false`; o valor padrão
é `false`.
*  **max-policies-per-handle** - Especifica o número máximo de políticas Local
Security Authority (LSA) que podem ser abertas para uma única manipulação de RPC. Essas políticas definem
as permissões de acesso necessárias para consultar ou modificar um sistema específico sob várias
condições. O valor padrão para essa opção é `255`.
*  **crawl-fs-metadata** - A ativação dessa opção fará com que o data crawler inclua um documento VXML que contém os metadados do sistema de arquivos disponíveis sobre o arquivo
(data de criação, data da última modificação, atributos de arquivos, etc.)
*  **enable-arc-connector** - Opção não usada.
*  **disable-indexes** - Nova lista separada por quebras de linha de índices a serem
desativados, o que pode resultar em um crawl mais rápido, por exemplo:

   *  disable-url-index
   *  disable-error-state-index
   *  disable-crawl-time-index
*  **exact-duplicates-hash-size** - Configura o tamanho da hashtable usada para
resolver duplicatas exatas. Tenha muito cuidado ao modificar esse número. O valor selecionado deve ser o
principal, e os tamanhos maiores podem fornecer consultas mais rápidas, mas requererão mais memória, enquanto
que os tamanhos menores podem desacelerar crawls, mas reduzirão substancialmente o uso de memória.
*  **user-agent** - Opção não usada.
*  **timeout** - Opção não usada.
*  **n-concurrent-requests** - O número de solicitações que serão enviadas em
paralelo para um único endereço IP. O padrão é `1`.
*  **enqueue-persistence** - Opção não usada.

### Configurando o conector SharePoint
O conector SharePoint permite efetuar crawl dos objetos SharePoint Server e SharePoint Online e
indexar as informações que eles contêm. Um objeto, como um documento, perfil do usuário, coleção de sites,
blog, item da lista, lista da associação, página de diretório, e mais, pode ser indexado com seus metadados
associados. Para itens da lista e documentos, os índices podem incluir anexos.

**Nota**: o conector SharePoint respeita o atributo `noindex` em
todos os objetos SharePoint, independentemente de seu tipo específico (blogs, documentos, perfis do usuário e muito mais). Um único documento é retornado para cada resultado.

**Importante**: a conta do SharePoint usada para efetuar crawl dos sites do
SharePoint deve ter pelo menos privilégios totais de acesso de leitura.

A seguir estão as opções de configuração básica necessárias para usar o conector SharePoint. Para
configurar esses valores, abra o arquivo `config/connectors/sharepoint.conf` e modifique os
valores a seguir, específicos para os casos de uso:

*  **protocol** - O nome do protocolo do conector usado para o crawl. Use
`io-sp` para esse conector.
*  **collection** - Este atributo é usado para descompactar arquivos temporários.
*  **classname** - Nome de classe Java para o conector. O valor para usar esse
conector deve ser `plugin:io-sharepoint.plugin@connector`.
*  **logging-config** - Especifica o arquivo usado para configurar opções de
criação de log; ele deve ser formatado como uma sequência XML `log4j`.
*  **seed-url-type** - Identifica para qual tipo de objeto SharePoint as URLs
iniciais fornecidas apontam: coleções de sites ou aplicativos da web (também conhecidos como servidores
virtuais).

   *  ***Site Collections*** - Se o Tipo de URL Inicial for configurado como
`Site Collections`, em seguida, somente os filhos da coleção de sites referenciados pela
URL passarão por crawl.
   *  ***Web Applications*** - Se o Tipo de URL Inicial for configurado como `Web
Applications`, em seguida, todas as coleções de sites (e seus filhos) pertencentes aos
aplicativos da web referenciados por cada URL passarão por crawl.
*  **auth-type** - O mecanismo de autenticação a ser usado ao entrar em contato com
o servidor SharePoint: `BASIC`, `NTLM2`, `KERBEROS` ou
`CBA`. O tipo de autenticação padrão é `NTLM2`.
*  **spUser** - O nome do usuário do SharePoint usado para acessar o
conteúdo. Esse usuário deve ter acesso a todos os sites e listas de destino a serem
passados por crawl e indexados, e deve poder recuperar e resolver as permissões associadas. É melhor
inseri-lo com o nome de domínio, como: `MYDOMAIN \\Administrator`.
*  **spPassword** - A senha do usuário do SharePoint usada para acessar o
conteúdo. A senha deve ser criptografada usando o programa vcrypt enviado com o Data Crawler.
*  **cba-sts** - A URL para o terminal Security Token Service (STS) para tentar
se autenticar com relação ao usuário do crawl. Para locais do SharePoint com ADFS, esse deve ser o
terminal ADFS. Se o Tipo de Autenticação for configurado como `CBA` (Claims Based
Authentication), em seguida, esse campo será obrigatório.
*  **cba-realm** - O identificador de confiança de parte de retransmissão a ser
usado ao solicitar um token de segurança a partir do STS. Às vezes isso é conhecido como o valor "AppliesTo"
ou "Realm". Para o SharePoint Online, essa deve ser a URL para a raiz da instância do SharePoint Online
(por exemplo, `https://mycompany.sharepoint.com`). Para ADFS, esse é o valor do ID para a
Confiança de Parte Confiável entre SharePoint e ADFS (por exemplo,
`"urn:SHAREPOINT:adfs"`).
*  **everyone-group** - Quando especificado, o nome desse grupo é usado nas ACLs
quando o acesso precisar ser fornecido a todos. Esse campo será obrigatório quando os perfis do usuário do
crawl forem ativados. **Nota** - A segurança ainda não é respeitada pelo serviço
Recuperar e Classificar.
*  **user-profile-master-url** - A URL base que o conector usa para construir links
para perfis do usuário. Isso deve ser configurado como apontar para o formato de exibição para perfis do usuário. Se
o token `%FIRST_SEED%` for encontrado, ele será substituído pela primeira URL inicial. Necessário quando o crawl em perfis do usuário está ativado.
*  **urls** - Lista separada por quebras de linha de URLs de HTTP de aplicativos da
web SharePoint ou coleções de sites a efetuar crawl.
*  **ehcache-config** - Opção não usada.
*  **method** - O método (`GET` ou `POST`) pelo
qual os parâmetros serão passados.
*  **cache-types** - Opção não usada.
*  **cache-size** - Opção não usada.
*  **enable-acl** - Permite a execução de crawl dos perfis do usuário do
SharePoint; os valores são `true` ou `false`. O valor padrão é `false`.

### Configurando o Conector Box
O Conector Box permite efetuar crawl da instância do Enterprise Box, e indexar as informações
que ela contém. A seguir estão as opções de configuração básica necessárias para usar o conector Box. Para
configurar esses valores, abra o arquivo `config/connectors/box.conf` e modifique os
valores a seguir, específicos para os casos de uso:

*  **protocol** - O nome do protocolo do conector usado para o crawl. Use
`box` para esse conector.
*  **classname** - Nome de classe Java para o conector. O valor para usar esse
conector deve ser `plugin:box.plugin@connector`.
*  **logging-config** - Especifica o arquivo usado para configurar opções de
criação de log; ele deve ser formatado como uma sequência XML `log4j`.
*  **box-crawl-seed-url** - A URL base para o Box. O valor para esse conector é
`box://app.box.com/`. É possível efetuar crawl de diferentes tipos de
URLs, por exemplo:

   *  ***Para efetuar crawl de uma empresa inteira***:
`box://app.box.com/`
   *  ***Para efetuar crawl de uma Pasta específica***:
`box://app.box.com/user/USER_ID/folder/FOLDER_ID/FolderName`
   *  ***Para efetuar crawl de um Usuário específico***:
`box://app.box.com/user/USER_ID/`
*  **client-id** - Insira o ID do Cliente fornecido pelo Box quando você criou o
aplicativo Box.
*  **client-secret** - Insira o Segredo do cliente fornecido pelo Box quando você
criou o aplicativo Box.
*  **path-to-private-key** - Este é o local, no sistema de arquivos local, da Chave
Privada que faz parte do par de chaves privada-pública gerado para comunicação com o Box.
*  **kid** - Especifique o ID da Chave Pública. Essa é a outra metade do par de
chaves privada-pública gerado para comunicação com o Box.
*  **enterprise-id** - A Empresa na qual o aplicativo foi autorizado. O ID da
Empresa é listado na página principal do Console do administrador do Box.
*  **enable-acl** - Somente uso interno. Permite recuperar as ACLs para dados
passados por crawl.
*  **user-agent** - Um cabeçalho enviado para o servidor ao efetuar crawl dos
documentos.
*  **method** - O método (`GET` ou `POST`) pelo
qual os parâmetros serão passados.
*  **url-logging** - A extensão para a qual as URLs passadas por crawl são registradas. Os valores
possíveis são:

   *  ***full-logging*** - Registre todas as informações sobre a URL.
   *  ***refined-logging*** - Registre somente as informações necessárias para
procurar o log do crawler e para que o conector funcione corretamente; este é o valor padrão.
   *  ***minimal-logging*** -Registre somente a quantia mínima de informações
necessárias para que o conector funcione corretamente.

   Configurar esta opção para criação de log mínima reduzirá o tamanho dos logs e ganhará um ligeiro
aumento de desempenho devido à E/S menor associada à minimização da quantia de dados que está sendo
registrada.
*  **ssl-version** - Especifica a versão de SSL a ser usada para conexões HTTPS. 
Por padrão, o protocolo mais sólido disponível é usado.

O Conector Box possui algumas limitações:

* Comentários ou Tarefas sobre arquivos não são recuperados.
* O corpo do conteúdo do Notes é recuperado como JSON. A conversão adicional de dados do
Notes pode ser necessária.
* Documentos individuais não podem ser recuperados por meio de TestIt. Somente as URLs iniciais, URLs
da Pasta e URLs do Usuário podem ser recuperadas por meio de TestIt.


## CONSULTE TAMBÉM

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
