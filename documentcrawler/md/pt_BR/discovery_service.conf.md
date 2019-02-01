# Configurando o serviço do Discovery
O serviço do Discovery informa ao crawler como gerenciar arquivos passados por crawl ao
usar o serviço do IBM Watson Discovery. As opções padrão podem ser mudadas, abrindo diretamente o arquivo
`config/discovery/discovery_service.conf`, e modificando os valores a seguir, específicos
para o caso de uso:

*  **http_timeout** - O tempo limite, em segundos, para a operação de
leitura/indexação do documento; o padrão é `125`.
*  **concurrent_upload_connection_limit** - O número de conexões simultâneas
permitidas para fazer upload de documentos; o padrão é `2`. Ao usar o Orchestration Service
Output Adapter, esse número deve ser maior ou igual ao `output_limit` definido ao configurar as
opções de crawl.
*  **base_url** - A URL para a qual dos documentos passados por crawl serão
enviados. Para a liberação atual do serviço do Discovery, o valor é
`https://gateway.watsonplatform.net/discovery/api`.
*  **environment_id** - O local da coleção de documentos passados por crawl na
`base-url`.
*  **collection_id** - Nome da coleção de documentos configurada no
serviço do Discovery.
*  **configuration_id** - O nome do arquivo de configuração que o serviço do
Discovery usa.
*  **check_for_completion** - Verifica se o documento foi processado com êxito no
terminal. Isso reduz o desempenho percebido do crawler, mas produzirá notificação confiável de uma conversão
e upload bem-sucedidos do documento. O valor é `true` ou `false`.  
**IMPORTANTE** - Ao ativar este parâmetro, é aconselhável aumentar o
`concurrent_upload_connection_limit` para maior ou igual ao `output_limit`
definido ao configurar as opções de crawl, para utilizar integralmente os recursos disponíveis.

Forneça suas credenciais de serviço do Discovery:
*  **username** - Nome do usuário a ser autenticado com o local da coleção de
documentos passados por crawl.
*  **password** - A senha a ser autenticada com o local da coleção de documentos
passados por crawl.

O Discovery Service Output Adapter pode enviar estatísticas para que a IBM entenda e atenda
melhor seus usuários. As opções a seguir podem ser configuradas para a variável `send_stats`:
*  **jvm** - As estatísticas enviadas da Java Virtual Machine (JVM) incluem o
fornecedor e a versão Java, conforme relatado pela JVM usada para executar o data crawler. O valor é `true` ou `false`.
*  **os** - As estatísticas enviadas do Sistema operacional (S.O.) incluem o nome,
versão e arquitetura do S.O., conforme relatado pela JVM usada para executar o data crawler. O valor é `true` ou `false`.

*  **api_version** - Somente uso interno. A data da última mudança de versão
da API.

# Configurando o armazenamento de rastreamento da URL
A pasta `config/discovery` também contém um arquivo de configuração que pode ser
usado para mapeamento interno de URLs do crawler e IDs do documento. As opções padrão podem ser mudadas,
abrindo diretamente o arquivo `config/discovery/uri_tracking_storage.conf`, e modificando os
valores a seguir, específicos para o caso de uso:

*  **driver** - Classe do driver H2 JDBC do banco de dados. O valor padrão é `org.h2.Driver`
*  **url** -Este é o prefixo da URL para a sequência de conexões JDBC. O
formato é `jdbc:h2:[file:]`. **NOTA** O prefixo `file:`
é opcional. Se não for, ou se somente um caminho relativo para `database_location` for usado,
em seguida, o diretório atualmente em funcionamento será usado como um ponto de início. O padrão é
`jdbc:h2:file:`
*  **database_location** - O local no disco em que o banco de dados está
armazenado, por exemplo, `./storage/database` ou `~/storage/database`. O
valor padrão é `./storage/database`
*  **database_name** - Nome do banco de dados. O valor padrão é
`ActivityDB`
*  **table_name** - Nome da tabela a ser usada. O valor padrão é `UriTracker`
*  **username** - Nome do usuário a conectar-se ao banco de dados
*  **password** - Senha para conectar-se ao banco de dados

## CONSULTE TAMBÉM

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
