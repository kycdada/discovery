crawler(1) - Um crawler para mover dados do ponto A para o ponto B
====================================================================

## SINOPSE

Uso: crawler [ crawl | testit | restart | resume | refresh | summary ][ options ]

## DESCRIÇÃO

O Data Crawler é usado para efetuar crawl em vários repositórios de dados, como sistemas de
gerenciamento de conteúdo e sistemas de arquivos e, em seguida, enviar por push os documentos
resultantes para um serviço remoto.

## OPÇÕES GLOBAIS

    --versão
        Exibe a versão do programa
    --ajuda
        Exibe este texto de uso

## COMANDOS

### crawl [ opções ]

Executa um crawl com a configuração atual.

    -c <value> | --config <value>  # Especifica o arquivo de configuração a ser
usado. O padrão é "config/crawler.conf".
    --pii-checking <value>         # Alterna a verificação de PII

### testit [ opções ]

Executa um crawl de teste, que executa crawl somente na URL inicial e exibe as URLs
enfileiradas. Se a URL inicial resultar em conteúdo indexável (por exemplo, é um documento), em seguida,
esse conteúdo será enviado ao adaptador de saída e o conteúdo será impresso na tela. Se a recuperação da URL
inicial fizer com que as URLs sejam enfileiradas, essas URLs serão exibidas, e nenhum conteúdo será enviado
ao adaptador de saída. Por padrão, cinco URLs enfileiradas são exibidas.

    -c <value> | --config <value>  # Especifica o arquivo de configuração a ser
usado. O padrão é "config/crawler.conf".
    -l <n> | --limit <n>           # Limita o número de URLs enfileiradas que são exibidas.
    --pii-checking <value>         # Alterna a verificação de PII

### Reiniciar [ opções ]

Executa uma Reinicialização de crawl; inicia um novo crawl com a configuração atual.

    -c <value> | --config <value>  # Especifica o arquivo de configuração a ser usado. 
--pii-checking <value>         # Alterna a verificação de PII

### Continuar [ opções ]

Continua um crawl de onde ele foi interrompido.

    -c <value> | --config <value>  # Especifica o arquivo de configuração a ser usado. 
--pii-checking <value>         # Alterna a verificação de PII

### Atualizar [ opções ]

Atualiza um crawl anterior.

    -c <value> | --config <value>  # Especifica o arquivo de configuração a ser usado. 
--pii-checking <value>         # Alterna a verificação de PII

### Resumo [ opções ]

Gera um relatório de crawl.

    --submitted                    # Consulta todos os documentos enviados
    --processed                    # Consulta somente documentos que foram processados com sucesso
    --failed                       # Consulta somente documentos que falharam ao serem processados com
                                     sucesso
    --group-id <value>             # Consulta a execução de crawl para um grupo especificado. Um grupo
consiste em um crawl inicial, e qualquer continuação, atualização ou reinicialização desse crawl inicial. Se
o valor não for especificado, essa consulta será padronizada para o grupo mais recente passado por crawl.
    --show-content                 # Exibe qualquer conteúdo adicional associado a uma consulta
    --filter                       # Filtra o resultado da consulta na URL e ID de hash

## EXEMPLOS

Execute um crawl usando o arquivo de configuração em `config/crawler.conf`:

    crawler crawl

Execute um teste usando o arquivo de configuração em `config/crawler.conf`:

    crawler testit

Execute um crawl usando o arquivo de configuração em `/home/watson/office-share.conf`:

    crawler crawl --config /home/watson/office-share.conf

Reinicie um crawl usando o arquivo de configuração em `/home/watson/office-share.conf`:

    crawler restart --config /home/watson/office-share.conf

Obtenha informações de resumo para documentos com falha com um ID do grupo de
`2`:

    crawler summary --failed --group-id 2 --show-content

Exiba o uso, incluindo a versão:

    crawler --help

## CONFIGURAÇÃO

O `crawler` requer um arquivo de configuração para suas opções. Exemplos de arquivos
de configuração são fornecidos no diretório `share` dentro do diretório
de instalação `crawler`. Copie esses exemplos e modifique-os. *Não modifique os
exemplos no local.*

Sem especificar a opção `-- config | -c`, o `crawler` procurará
sua configuração no diretório `config` do diretório no qual o
`crawler` é iniciado. Ou seja, o `crawler` procurará `config/crawler.conf`.

## DIAGNÓSTICOS

Use estes recursos para diagnosticar problemas.

### Depuração

Ativa o modo de depuração. No arquivo `crawler.conf`, configure: 

    debugging.full_node_debugging = true

### Criação de log

Aliva o registro. No arquivo `log4j_custom.properties`, configure: 

    log4j.rootLogger=INFO, Console, Log

Este é o nível de criação de log padrão para a saída do arquivo. Para o log do console, o padrão é: 

    log4j.appender.Console.Threshold=WARN

Os níveis de criação de log podem ser configurados para os valores a seguir:

    OFF - A classificação mais alta possível, ela se destina a desativar a criação de log.
    FATAL - Designa muitos eventos de erros severos que provavelmente farão com que o aplicativo seja
            interrompido.
    ERROR - Designa eventos de erros que ainda podem permitir que o aplicativo continue em execução.
    WARN - Designa situações potencialmente prejudiciais.
    INFO - Designa mensagens informativas que destacam o progresso do aplicativo em um nível de
           alta granularidade.
    DEBUG - Designa eventos informativos de baixa granularidade que são os mais úteis para depurar um
            aplicativo.
    TRACE - Designa eventos informativos de granularidade mais baixa do que DEPURAÇÃO.
    ALL - A classificação mais baixa possível, que se destina a ativar todas as criações de log.

## REGULAGEM

Define as limitações de dimensionamento, para ajudar a gerenciar o rendimento. No arquivo
`crawler.conf`, configure: 

`shutdown_timeout` Especifica o valor de tempo limite, em minutos, antes de encerrar o
aplicativo; o valor padrão é 10.

    shutdown_timeout = <n>

`output_limit` é o número mais alto de itens indexáveis que o crawler portátil
enviará simultaneamente ao adaptador de saída, aguardando um retorno; o valor padrão é 10. Isso pode ser mais
limitado por núcleos disponíveis para fazer o trabalho.

    output_limit = <n>

`input_limit` Limita o número de URLs que podem ser solicitadas a partir do conector
de uma vez; o valor padrão é 3.

    input_limit = <n>

`output_timeout` é a quantidade de tempo, em segundos, antes que o crawler portátil
desista de uma solicitação para o adaptador de saída e, em seguida, remove o item da fila limite, para
permitir mais processamento. O
valor padrão é 150.

    output_timeout = <n>

A consideração deve ser fornecida às restrições impostas pelo adaptador de saída, pois essas restrições
podem se relacionar aos limites definidos aqui. O `output_limit` definido acima
se relaciona somente à quantidade de objetos indexáveis que podem ser enviados ao adaptador de saída de uma
vez. Quando um objeto indexável é enviado ao adaptador de saída, ele estará "on the clock", conforme definido
pela variável `output_timeout`. É possível que o próprio adaptador de saída tenha regulador
que o impeça de poder processar tantas entradas quantas recebe. Por exemplo, o adaptador de saída de
orquestração pode ter um conjunto de conexões, configuráveis para conexões HTTP com o serviço. Se ele for
padronizado como 8, por exemplo, e se você configurar o `output_limit` para um número
maior do que está configurado como esse conjunto de conexões, em seguida, você terá processos on the clock
que aguardam que uma alternância seja executada. Em seguida, você pode experimentar os tempos limites.

`num_threads` O número de encadeamentos paralelos que podem ser executados de uma vez. 
Esse valor pode ser um número inteiro, que especifica o número de encadeamentos paralelos diretamente, ou
pode ser uma sequência, com o formato `"xNUM"`, especificando o fator de
multiplicação do número de processadores disponíveis. O valor padrão é "x1.5", ou 1,5 vez o número de
processadores disponíveis (conforme obtido com `Runtime.availableProcessors`).

    num_threads = <n>

A fórmula para calcular o paralelismo no conjunto Data Crawler é: `min
(maxThreads, max(minThreads, numThreads))`.

## VARIÁVEL DE AMBIENTE `CRAWLER_OPTS` 

A seguir estão as propriedades que podem ser passadas para o `crawler` por meio
da variável de ambiente `CRAWLER_OPTS`, listadas com valores padrão.

Passe-as da seguinte forma:

    CRAWLER_OPTS="-Dproperty=value -Dproperty=value" crawler

Elas devem ser mudadas somente para depuração, e somente sob a direção do Suporte IBM.

### cfa.java_bin

`cfa.java_bin` pode mudar o comando `java` usado para iniciar o
Adaptador de Entrada Connector Framework. Por padrão, o `crawler` usa o mesmo
`java` binário que é usado para ativar o próprio `crawler`.

Isso também pode ser mudado configurando a propriedade `java.home` que, em seguida,
será usada para calcular o caminho para o executável `Java`.

### cfa.lib_dir

`cfa.lib_dir` muda o caminho para o diretório `lib` do Connector Framework. Isso precisa ser mudado raramente. Por padrão, o `crawler` usa o
diretório `lib` dentro do caminho calculado para o Connector Framework, em geral,
simplesmente `connectorFramework`.

### cfa.framework_jars_dir

`cfa.framework_jars_dir` muda o caminho para o diretório jars do Connector Framework,
que está, por padrão, em `connectorFramework/<version>/lib/java`.

### cfa.plugins_dir

`cfa.plugins_dir` especifica o caminho para o diretório de plug-ins do Connector Framework, onde os Conectores reais são armazenados. Por padrão, isso é construído a partir do
`framework_jars_dir` e será `connectorFramework/<version>/lib/java/plugins`.

## LIMITAÇÕES CONHECIDAS

Detalha as limitações conhecidas na liberação atual do Data Crawler

* O Data Crawler pode ser interrompido quando estiver executando o conector Filesystem com uma URL
inválida ou ausente.
* Configure o valor `urls_to_filter` no arquivo
`config/crawler.conf`, de modo que todas as URLs da lista de desbloqueio ou RegExes sejam
incluídas em uma única expressão RegEx.
* O caminho para o arquivo de configuração passado na opção `-- config |
-c` deve ser um caminho qualificado. Ou seja, ele deve estar nos formatos relativos
`config/crawler.conf` ou `./crawler.conf` ou no caminho absoluto
`/path/to/config/crawler.conf`. Especificar somente `crawler.conf`,
será possível se, e somente se, os arquivos referenciados que usam `include` no arquivo
`crawler.conf` estiverem em sequência, em vez de usarem `include`. Por
exemplo, `discovery/discovery_service.conf` é `include` para tornar a
configuração mais fácil de ler. Seu conteúdo deve ser copiado no `crawler.conf` dentro da
chave `output_adapter.discovery_service` para usar um caminho não qualificado na opção de
configuração.

## CHANGE LOG

Consulte o arquivo `changelog.txt` no diretório de instalação para obter uma lista de
mudanças nessa liberação.

## AUTHOR

IBM Watson - https://www.ibm.com/smarterplanet/us/en/ibmwatson/

Feito por yinz em Pittsburgh.

## CONSULTE TAMBÉM

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
