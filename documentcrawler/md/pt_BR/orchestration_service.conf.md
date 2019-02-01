# Configurando o serviço de orquestração
O serviço de orquestração informa ao crawler como gerenciar arquivos passados por crawl. As opções
padrão podem ser mudadas abrindo diretamente o arquivo
`config/orchestration/orchestration-service.conf`, e modificando os valores a seguir,
específicos para o caso de uso:

*  **http_timeout** - O tempo limite, em segundos, para a operação de
leitura/indexação do documento; o padrão é `585`.
*  **concurrent_upload_connection_limit** - O número de conexões simultâneas
permitidas para fazer upload de documentos; o padrão é `10`. Geralmente, esse
número deve ser maior ou igual ao `output_limit` definido ao configurar as opções de crawl.
*  **base_url** - A URL para a qual dos documentos passados por crawl serão
enviados. 
*  **endpoint** - O local da coleção de documentos passados por crawl na
`base-url`.
*  **username** - Nome do usuário a ser autenticado para o local do
`endpoint`.
*  **password** - Senha a ser autenticada para o local do `endpoint`. **Importante** - **NÃO** use o programa vcrypt enviado com o Data Crawler para criptografar essa senha.
*  **config_file** - O arquivo de configuração que o serviço de orquestração usa.

O Orchestration Service Output Adapter pode enviar estatísticas para que a IBM entenda e atenda
melhor seus usuários. As opções a seguir podem ser configuradas para a variável `send_stats`:
*  **jvm** - As estatísticas enviadas da Java Virtual Machine (JVM) incluem o
fornecedor e a versão Java, conforme relatado pela JVM usada para executar o data crawler. O valor é `true` ou `false`.
*  **os** - As estatísticas enviadas do Sistema operacional (S.O.) incluem o nome,
versão e arquitetura do S.O., conforme relatado pela JVM usada para executar o data crawler. O valor é `true` ou `false`.

## CONSULTE TAMBÉM

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
