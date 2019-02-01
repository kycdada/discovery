Vcrypt (1) - Uma ferramenta para criptografar e decriptografar pequenas quantias de dados
===============================================================

## SINOPSE

Uso: vcrypt --decrypt|-d  --encrypt|-e  --genkey|-g [ OPTIONS ]

## DESCRIÇÃO

`vcrypt` é usado principalmente para criptografar senhas para uso pelo Connector
Framework.

### Uma nota especial sobre o comprimento da chave

Por padrão, uma implementação da Java Virtual Machine deve suportar chaves AES de 128 bits/16 bytes. Se o
o Java Cryptographic Extensions estiver instalado no sistema, ele poderá ser capaz de usar chaves
AES de 256 bits/32 bytes. Um erro mostrará se uma chave de 32 bytes é fornecida, mas não suportada pela JVM
usada para ativar `vcrypt`.

## COMMANDS

### --encrypt | -e OPTIONS INPUT
Criptografe dados fornecidos em um arquivo ou em uma entrada padrão.

### --decrypt | -d OPTIONS INPUT
Decriptografe dados fornecidos em um arquivo ou em uma entrada padrão.

### --genkey | -g
Gera uma chave de criptografia adequada para uso com `vcrypt` para saída padrão.

## OPTIONS

### --keyfile|-k PATH/TO/ID_VCRYPT
Especifique o caminho para o arquivo que contém uma chave apropriada codificada como Base64,
provavelmente gerada com o uso do comando `--genkey|-g`.

## DADO

### Modo de criptografia

    $FILE_CONTAINING_CLEARTEXT | -- $CLEARTEXT

### Modo de decriptografia

    $FILE_CONTAINING_CRYPTED_TEXT | -- $CRYPTED_TEXT

## EXEMPLOS

Gere uma chave e coloque-a no arquivo `id_vcrypt`:

    vcrypt --genkey > id_vcrypt

Criptografe uma senha da entrada padrão para a saída padrão, gravada aqui por meio do redirecionamento
de saída para `my_secret_data.txt`:

    ./vcrypt --encrypt --keyfile id_vcrypt -- "my secret password" > my_secret_data.txt

Também é possível canalizar a saída para `xclip`,
`pbcopy` ou semelhante para colocar a saída na área de transferência do sistema
operacional.

Decriptografe uma senha a partir de um arquivo:

    vcrypt --decrypt --keyfile id_vcrypt my_secret_data.txt

## PROPRIEDADES E VARIÁVEIS DE AMBIENTE

### Variável de ambiente `VCRYPT_OPTS`
Essa variável de ambiente pode ser usada para passar opções para o comando `java`
usado para iniciar `vcrypt`.

### Propriedade `vcrypt.key`
Passe isso como uma propriedade `-D` em `VCRYPT_OPTS` com uma
sequência de 16 ou 32 bytes para usar uma chave na linha de comandos, em vez de passar a opção
`--keyfile | -k keyfile`.

Exemplo de uso:

    VCRYPT_OPTIONS="-Dvcrypt.key='1234qwerasdfzxcv'" vcrypt --encrypt file_to_encrypt

### Variável de ambiente `VIV_VCRYPT_KEY`
`vcrypt` permite o uso dessa variável de ambiente para configurar a chave. Ela deve
ter 16 ou 32 bytes.

## CONSULTE TAMBÉM

crawler(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
