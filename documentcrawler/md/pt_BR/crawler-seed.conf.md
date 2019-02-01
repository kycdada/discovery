# Configurando valores iniciais de crawl

Valores iniciais são os pontos de início de um crawl, e são usados pelo data crawler para
recuperar dados do recurso, identificados por esse valor inicial. Geralmente, os valores iniciais configuram
URLs para acessar recursos baseados em protocolo, como compartilhamentos de arquivos, compartilhamentos de
SMB, bancos de dados e outros repositórios de dados que são acessíveis por vários protocolos da web. Além
disso, as URLs iniciais diferentes possuem diferentes recursos.

Os valores iniciais podem ser também específicos do repositório, para ativar a execução de crawl de
aplicativos de terceiros específicos, como sistemas Customer Relationship Management (CRM), sistemas Product
Life Cycle (PLC), Content Management Systems (CMS), aplicativos baseados em nuvem e aplicativos baseados na
web.

O data crawler fornece atualmente os valores iniciais de crawl que suportam conectores de
arquivos para os tipos de repositórios a seguir:

*	Sistema de arquivo
*	Bancos de dados, por meio de JDBC
*	CMIS (Content Management Interoperability Services)
*	Compartilhamentos de arquivos SMB (Server Message Block), CIFS (Common Internet Filesystem) ou Samba
*	SharePoint e SharePoint Online
*	Postal

Um modelo de configuração inicial de crawl também é fornecido, o que permite
customizar um valor inicial de crawl para um conector customizado.

## Introdução:

Ao efetuar crawl de repositórios de dados, o crawler é iniciado em uma URL inicial especificada pelo
usuário, e inicia o download das páginas de informações. O crawler também localiza links nas páginas
transferidas por download e planeja as páginas descobertas recentemente para execução de crawl adicional.

As informações de configuração são usadas para determinar quais páginas precisam ser passadas por
crawl, e como efetuar crawl nelas. Esse arquivo explica as opções que é possível configurar para cada arquivo
inicial de crawl do conector.

**Nota**: cada arquivo de configuração inicial de crawl funciona com um
arquivo de configuração de conector de arquivo correspondente; as opções de conector de arquivo são
descritas separadamente.

### Configurando o valor inicial de crawl de sistema de arquivos

Os valores a seguir podem ser configurados para o arquivo inicial de crawl do sistema de
arquivos. Para configurar esses valores, abra o arquivo `config/seeds/filesystem-seed.conf`
e especifique os valores a seguir, específicos para os casos de uso:

*  **url** - Lista separada por quebras de linha de arquivos e
pasta para efetuar crawl. Os usuários do UNIX podem usar um caminho, como `/usr/local/`.
As URLs devem iniciar com `sdk-fs://`. Portanto, para efetuar crawl, por exemplo,
`/home/watson/mydocs`, o valor dessa URL seria
`sdk-fs:///home/watson/mydocs` - o terceiro `/` é necessário!
**Nota**: o conector Filesystem usa um protocolo customizado,
`sdk-fs://`, para criar uma URL válida. Não pré-anexe `file://` nos
caminhos listados; as URLs devem iniciar com `sdk-fs://`.
*  **hops** - Somente uso interno.
*  **default-allow** - Somente uso interno.

### Configurando o valor inicial de crawl de banco de dados

Os valores a seguir podem ser configurados para o arquivo inicial de crawl do banco de dados. Para
configurar esses valores, abra o arquivo `config/seeds/database-seed.conf` e
especifique os valores a seguir, específicos para os casos de uso:

*  **url** - A URL da tabela ou da visualização a ser recuperada. Define a URL
inicial do banco de dados SQL customizado. A estrutura é:

   	`database-system://host:port/database?[per=num]&[sql=SQL]`

   Testar uma URL inicial mostrará todas as URLs enfileiradas. Por exemplo, testando a URL a
seguir para um banco de dados que contém 200 registros:

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=100&sql=select%20*%20from%20vessel&`

   mostra as URLs enfileiradas a seguir:

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=0&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=100&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=200&`

   Ao testar a URL a seguir, os dados recuperados da linha 43 serão mostrados:

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=1&key-val=43`
*  **hops** - Somente uso interno.
*  **default-allow** - Somente uso interno.
*  **user-password** - Credenciais para o sistema de banco de dados. O nome do
usuário e senha precisam ser separados por um `:`, e a senha deve ser criptografada com
o programa vcrypt enviado com o Data Crawler. Por exemplo, `username:[[vcrypt/3]]passwordstring`.
*  **max-data-size** - Tamanho máximo dos dados para um documento. Este é o
maior bloco de memória que será carregado de uma vez. Aumente esse limite somente se tiver memória
suficiente em seu computador.
*  **filter-exact-duplicates** - Somente uso interno.
*  **jdbc-class** (Opção do extensor) - Quando especificada, essa sequência
substituirá a classe JDBC usada pelo conector quando `(outra)` for escolhida como o sistema
de banco de dados.
*  **connection-string** (Opção do extensor) - Quando especificada, essa sequência
substituirá a sequência de conexões JDBC gerada automaticamente. Isso permite fornecer configuração
mais detalhada sobre a conexão com o banco de dados, como por exemplo, balanceamento de carga ou
conexões SSL. Por exemplo: `jdbc:netezza://127.0.0.1:5480/databasename`.
*  **save-frequency-for-resume** (Opção do extensor) - Especifica o nome de
uma coluna ou rótulo associado para poder continuar um crawl ou executar uma atualização parcial. O valor
inicial salva o nome dessa coluna em intervalos regulares conforme ele continua com o crawl, e o salva
novamente quando a última linha do banco de dados tiver sido passada por crawl. Ao continuar o crawl ou
atualizá-lo, o crawl é iniciado com a linha identificada no valor salvo para esse campo.

### Configurando o valor inicial de crawl do CMIS

Os valores a seguir podem ser configurados para o arquivo inicial de crawl do CMIS. Para configurar
esses valores, abra o arquivo `config/seeds/cmis-seed.conf` e modifique os valores a seguir,
específicos para os casos de uso:

*  **url** -A URL de uma pasta do repositório CMIS a ser usado como um ponto de
início do crawl, por exemplo:

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=workspace://SpacesStore/guid`
 Para efetuar crawl a partir da pasta raiz, é necessário fornecer a URL como:

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=`
*  **at** - Opção não usada.
*  **default-allow** - Somente uso interno.

### Configurando o valor inicial de crawl do Samba

Os valores a seguir podem ser configurados para o arquivo inicial de crawl do Samba. Para configurar
esses valores, abra o arquivo `config/seeds/samba-seed.conf` e modifique os valores a
seguir, específicos para os casos de uso:

*  **url** - Uma lista separada por quebras de linha de compartilhamentos com
crawl, por exemplo:

   *  `smb://share.test.com/office`
   *  `smb://share.test.com/cash/money/change`
   *  `smb://share.test.com/C$/Program Files`

*  **hops** - Somente uso interno.
*  **default-allow** - Somente uso interno.

### Configurando o valor inicial de crawl do SharePoint

Os valores adicionais a seguir podem ser configurados para o arquivo inicial de crawl do
SharePoint. Para configurar esses valores, abra o arquivo
`config/seeds/sharepoint-seed.conf` e modifique os valores a seguir, específicos para os
casos de uso:

*  **url** - Uma lista separada por quebras de linha de aplicativos da web
SharePoint ou coleções de sites para efetuar crawl, por exemplo:

   *  `io-sp://a.com`
   *  `io-sp://b.com:83/site`
   *  `io-sp://c.com/site2`

   Os subsites desses sites também serão passados por crawl (a menos que sejam excluídos por
outras regras de crawling).
*  **filter-url** - Uma lista separada por quebras de linha de aplicativos da web
SharePoint ou coleções de sites para efetuar crawl, por exemplo:

   *  `http://a.com
`
   *  `http://b.com:83/site
`
   *  `http://c.com/site2`

*  **hops** - Somente uso interno.
*  **n-concurrent-requests** - Somente uso interno.
*  **delay** - Somente uso interno.
*  **default-allow** - Somente uso interno.
*  **seed-protocol** - Configura o protocolo inicial para filhos da
coleção de sites. Necessário quando o protocolo de coleção de sites for SSL, HTTP ou HTTPS. Esse valor deve
ser configurado de maneira igual ao protocolo de coleção de sites.

### Configurando o valor inicial do Box

Os valores a seguir podem ser configurados para o arquivo inicial de crawl do Box. Para configurar
esses valores, abra o arquivo `config/seeds/box-seed.conf` e especifique os valores a
seguir, específicos para os casos de uso:

*  **URL** -A URL a ser usada como o ponto de início do crawl. O valor padrão é
`box://app.box.com/`.
*  **default-allow** - Somente uso interno.

## CONSULTE TAMBÉM

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

orchestration_service.conf(5)
