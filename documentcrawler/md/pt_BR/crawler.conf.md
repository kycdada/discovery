# Configurando o Data Crawler

O `crawler` requer um arquivo de configuração para suas opções. Exemplos de
configuração são fornecidos no diretório `share` dentro do diretório de instalação do `crawler`. Copie esses exemplos e modifique-os. *Não modifique os exemplos no local.*

O arquivo `crawler.conf` contém informações que dizem ao crawler quais arquivos usar
para seu crawl (adaptador de entrada), onde enviar a coleção de arquivos passados por crawl depois do crawl ter sido concluído (adaptador de saída), e outras opções de gerenciamento de crawl.

**Nota**: todos os caminhos de arquivo são relativos ao diretório `config`, exceto onde indicado.

As opções que podem ser configuradas neste arquivo são:

## Adaptador de entrada
*  **class** - Somente uso interno; define a classe do adaptador de entrada do Data Crawler. O valor padrão é: `com.ibm.watson.crawler.connectorframeworkinputadapter.Crawl`.
*  **config** - Somente uso interno; define a configuração do Connector Framework. A chave de configuração padrão dentro desse bloco para passar para o adaptador de entrada escolhido é: `connector_framework`.**Nota** - O Connector Framework é o que permite falar com os dados. Podem ser dados internos dentro da empresa, ou pode ser dados externos na web ou na nuvem. Os conectores permitem acesso a várias origens de dados diferentes, enquanto a conexão é realmente controlada pelo processo de crawl.
  -  **IMPORTANTE** - Os dados recuperados pelo Adaptador de Entrada Connector Framework são armazenados em cache localmente. Eles não são armazenados criptografados. Por padrão, os dados são armazenados em cache em um diretório temporário que deve ser limpo na reinicialização, e devem ser legíveis somente pelo usuário que executou o comando do crawler. Há uma chance de que esse diretório possa sobreviver ao crawler, se a estrutura do conector desaparecesse antes que pudesse se limpar. Considere cuidadosamente o local para os dados em cache - você pode colocá-los em um sistema de arquivos criptografados, mas esteja ciente das implicações de desempenho ao fazer isso. É possível decidir somente o equilíbrio apropriado entre a velocidade e a segurança para os crawls.
*  **crawl_config_file** - O arquivo de configuração a ser usado para o crawl. O valor padrão é: `connectors/filesystem.conf`.
*  **crawl_seed_file** - O arquivo inicial de crawl a ser usado para o crawl. O valor padrão é: `seeds/filesystem-seed.conf`.
*  **id_vcrypt_file** - O arquivo-chave usado para criptografia de dados pelo crawler; a chave padrão incluída com o crawler é `id_vcrypt`.
Use o script vcrypt na pasta `bin`, se precisar gerar um novo id_vcrypt_file
*  **crawler_temp_dir** - A pasta temporária do Crawler para logs do conector. O valor padrão, `tmp`, é fornecido. Se ele ainda não existir, a pasta `tmp` será criada no diretório atualmente em funcionamento.
*  **extra_jars_dir** - Somente uso interno; inclui JARs extras no caminho de classe do Connector Framework.
Esse valor deve ser `oakland` ao usar o conector SharePoint, e `database` ao usar o conector de banco de dados. É possível deixá-lo vazio (ou seja, sequência vazia "") ao usar outros conectores.
  **Nota**: relativo ao diretório `lib/java` de estrutura do conector.
*  **urls_to_filter** - Lista de desbloqueio separada por quebras de linha de URLs para efetuar crawl, na forma de expressão regular. O Data Crawler somente efetua crawl das URLs que correspondem a uma das expressões regulares fornecidas. A lista de domínio contém os domínios mais comuns de nível superior; inclua nela, se necessário.  lista de tipos de extensão do arquivo contém as extensões dos arquivos que o Orchestration Service suporta, a partir dessa liberação do Data Crawler. Assegure-se de que o domínio da URL inicial seja permitido pelo filtro. Por exemplo, se a URL inicial se parecer com `http://testdomain.test.in`, inclua "`in`" no filtro de domínio. Assegure-se de que a URL inicial não seja excluída por um filtro ou o Crawler poderá ser interrompido.
*  **max_text_size** - O tamanho máximo, em bytes, que um documento pode ter antes que ele seja gravado no disco pelo Connector Framework. Ajustando isso para mais alto, diminuirá a quantia de documentos gravados no disco, mas aumentará os requisitos de memória.
*  **extra_vm_params** - Permite incluir parâmetros Java extras no comando usado para ativar o Connector Framework.
*  **bootstrap_logging** - Grava o log de inicialização da estrutura do conector; útil somente para depuração avançada. Os valores são `true` ou `false`. O arquivo de log será gravado no `crawler_temp_dir`.

## Adaptador de armazenamento

Permite o armazenamento do estado interno do crawler em um banco de dados. Essa configuração é necessária para que as opções `restart` e `resume` do crawl funcionem corretamente.

```javascript
storage_adapter {
 config = "storage_in_db"
  storage_in_db {
    include "storage/database_storage.conf"
  } 
}
```
O arquivo referenciado, `storage/database_storage.conf`, usa um banco de dados H2, por padrão. É possível usar qualquer banco de dados com um driver JDBC, em vez dos padrões fornecidos. Consulte a documentação para o driver JDBC para localizar informações específicas sobre algumas dessas configurações. As opções padrão podem ser mudadas abrindo diretamente o arquivo `config/storage/database_storage.conf` e modificando os valores a seguir, específicos para o caso de uso:

*  **class** - Esta classe aponta para a classe do adaptador de banco de dados a ser usada. O valor padrão é `com.ibm.watson.crawler.storageadapters.DatabasePersistAdapter`
*  **driver** - A classe para o driver JDBC. O valor padrão é `org.h2.Driver` para usar H2
*  **url** - Consulte as opções de JDBC para o driver. Esse é o prefixo da URL para a sequência de conexões JDBC. O padrão é `jdbc:h2:file:`
*  **database_location** - O local onde você deseja seu banco de dados. Isso se aplica somente aos bancos de dados baseados em arquivos como sqlite e H2. O valor padrão é `./storage/database`
*  **database_name** - Nome do banco de dados. O valor padrão é `ActivityDB`
*  **table_name** - Nome da tabela a ser usada. O valor padrão é `Ledger`
*  **username** - Nome do usuário a conectar-se ao banco de dados
*  **password** - Senha para conectar-se ao banco de dados

A configuração padrão é suficiente para a maioria das atividades.

## Adaptador de saída

Existem dois *adaptadores de saída* dos quais escolher. Defina o adaptador de saída
configurando `output_adapter.class` em `crawler.conf`. As opções são:

*  **class** - Define a classe do adaptador de saída Data Crawler. O valor padrão é `com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter`
*  **config** - Define qual chave de configuração passar para o adaptador de saída. A sequência deve corresponder a uma chave dentro desse objeto de configuração. No exemplo de código a seguir:
```javascript
  orchestration_service {
    include "orchestration_service.conf"
  },
  test {
    output_directory = "/tmp/crawler-test-output"
  }
}
```
a chave de configuração é `orchestration_service`. O valor padrão é `discovery_service`
Deve-se selecionar um adaptador de saída especificando seu parâmetro `class` e a chave `config`.

* **Orchestration Service Output Adapter**: Faz upload de documentos passados por crawl para o Orchestration Service do Watson Developer Cloud. Selecione esse adaptador configurando o parâmetro `class` e a chave `config` da maneira a seguir: 
```javascript
  class = "com.ibm.watson.crawler.orchestrationserviceoutputadapter.oneatatime.OrchestrationServiceOutputAdapter"
  config = "orchestration_service"
  orchestration_service {
    include "orchestration/orchestration_service.conf"
  }
```
* **Discovery Service Output Adapter**: faz upload de documentos passados por crawl para o Discovery Service do Watson Developer Cloud. Selecione esse adaptador configurando o parâmetro `class` e a chave `config` da maneira a seguir:
```javascript
  class = "com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter"
  config = "discovery_service"
  discovery_service {
    include "discovery/discovery_service.conf"
  }
```
* **Adaptador de saída do Watson Test**: grava uma representação dos arquivos passados por crawl no disco em um local especificado. Selecione esse adaptador configurando o parâmetro `class` e a chave `config` da maneira a seguir:

**Nota** - Um parâmetro adicional, `output_directory`, seleciona o diretório no qual a representação dos dados passados por crawl deve ser gravada.
```javascript
  class = "com.ibm.watson.crawler.testoutputadapter.TestOutputAdapter"
  config = "test"
  output_directory = "/tmp/crawler-test-output"
```
* **retry** - Especifica as opções para tentar novamente em caso de tentativas com falha de envio por push para o adaptador de saída.
  * max_attempts - número máximo de novas tentativas. O valor padrão é `10`
  * delay - Quantia mínima de atraso entre tentativas, em segundos. O valor padrão é `2`
  * exponent_base - Fator que determina o crescimento do tempo de atraso sobre cada tentativa com falha. O valor padrão é `2`

 A fórmula é:
```
 d(nth_retry) = delay * (exponent_base ^ nth_retry)
```

 Por exemplo, as configurações com um atraso de 1 segundo e uma base de expoente de 2, fará com
que a segunda tentativa e a terceira tentativa atrasem 2 segundos, em vez de 1, e a próxima atrase 4
segundos.
 ```
 d(0) = 1 * (2 ^ 0) = 1 second
 d(1) = 1 * (2 ^ 1) = 2 seconds
 d(2) = 1 * (2 ^ 2) = 4 seconds
```
Portanto, com as configurações padrão, haverá a tentativa de um envio até 10 vezes,
aguardando até aproximadamente 1.022 segundos (um pouco mais de 17 minutos). Esse tempo é aproximado porque há tempo
adicional incluído para evitar ter múltiplas execuções de reenvio simultaneamente. Esse tempo "difuso" é até 10%, portanto, a última nova tentativa no exemplo anterior pode atrasar até 4.4 segundos. 
O tempo de espera não inclui o tempo gasto conectando-se ao serviço, fazendo upload de dados ou aguardando
uma resposta. *Aviso:* reduzir o tempo de espera diminuindo qualquer um desses
padrões pode resultar em documentos que não estão sendo transferidos por upload com sucesso por meio do
adaptador de saída configurado. A evidência disso ao usar serviços do Watson
Developer Cloud serão mensagens de RetryFailure no log que cita a limitação de taxa de "429 Muitas
Solicitações".
 
## Opções de depuração
*  **full_node_debugging** - Ativa o modo de depuração; os valores possíveis são
`true` ou `false`. **Aviso**: isso colocará os dados
integrais de cada documento passado por crawl para os logs.
*  **heartbeat_wait_time** - Intervalo de tempo, em milissegundos, entre
estatísticas de ingestão de documento de relatório (somente modo de depuração). O valor padrão é 1000 milissegundos.

## Opções de Criação de Log
*  **configuration_file** - O arquivo de configuração a ser usado para criação de
log. No arquivo de amostra `crawler.conf`, essa opção é definida em
`logging.log4j` e seu valor padrão é `log4j_custom.properties`.
Essa opção deve ser definida de maneira semelhante se usar um arquivo `.properties` ou
`.conf`.

## Opções adicionais de gerenciamento de crawl
*  **shutdown_timeout** - Especifica o valor de tempo limite, em minutos, antes de
encerrar o aplicativo. O valor padrão é `10`.
*  **output_limit** - O número mais alto de itens indexáveis que o Crawler tentará
enviar simultaneamente ao adaptador de saída. Isso pode ser limitado ainda mais pelo número de núcleos
disponíveis para executar o trabalho. Ele diz que em qualquer ponto fornecido haverá não mais que "x" itens
indexáveis enviados ao adaptador de saída aguardando o retorno. O valor padrão é `10`.
*  **input_limit** - Limita o número de URLs que podem ser solicitadas a partir do
conector de uma vez. O valor padrão é `3`.
*  **output_timeout** - A quantia de tempo, em segundos, antes que o Data Crawler
desista de uma solicitação para o adaptador de saída e, em seguida, remova o item da fila do adaptador de
saída, para permitir mais processamento. O valor padrão é `1200`. **Nota** - A consideração deve ser fornecida às restrições impostas pelo adaptador de saída, pois essas restrições podem se relacionar aos limites definidos aqui. O `output_limit` definido acima se relaciona somente à quantidade de objetos indexáveis que podem ser enviados ao adaptador de saída de uma vez. Quando um objeto indexável é enviado ao adaptador de saída, ele estará "on the clock", conforme definido pela variável `output_timeout`. É possível que o próprio adaptador de saída tenha regulador que o impeça de poder processar tantas entradas quantas recebe. Por exemplo, o adaptador de saída de orquestração pode ter um conjunto de conexões, configuráveis para conexões HTTP com o serviço. Se ele for padronizado como 8, por exemplo, e se você configurar o `output_limit` para um número maior que 8, em seguida, você terá processos on the clock que aguardam que uma alternância seja executada. Em seguida, você pode experimentar os tempos limites.
*  **num_threads** - O número de encadeamentos paralelos que podem ser executados de uma vez. Esse valor pode ser um número inteiro, que especifica o número de encadeamentos paralelos
diretamente, ou pode ser uma sequência, com o formato "xNUM", especificando o fator de multiplicação do
número de processadores disponíveis, por exemplo, "x1.5". O valor padrão é `"30"`.

## CONSULTE TAMBÉM

crawler(1)

vcrypt(1)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
