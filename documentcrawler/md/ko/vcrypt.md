vcrypt(1) - 소량의 데이터를 암호화 및 복호화하는 도구
===============================================================

## 시놉시스

사용법: vcrypt --decrypt|-d  --encrypt|-e  --genkey|-g [ OPTIONS ]

## 설명

`vcrypt`는 주로 커넥터 프레임워크에서 사용할 비밀번호를 암호화하는 데 사용됩니다. 

### 키 길이에 대한 별도 참고사항

기본적으로, JVM(Java Virtual Machine) 구현은 128비트/16바이트 AES 키를 지원해야 합니다. 시스템에 Java 암호화 확장이 설치된 경우, 이는 256비트/32바이트 AES 키를 사용할 수 있습니다. 32바이트 키가 제공되지만 `vcrypt`를 실행하는 데 사용된 JVM에서 이를 지원하지 않으면 오류가 표시됩니다. 

## 명령

### --encrypt | -e OPTIONS INPUT
표준 입력이나 파일에서 제공되는 데이터를 암호화합니다. 

### --decrypt | -d OPTIONS INPUT
표준 입력이나 파일에서 제공되는 데이터를 복호화합니다. 

### --genkey | -g
표준 출력에 대해 `vcrypt`에서 사용하기에 적합한 암호화 키를 생성합니다. 

## 옵션

### --keyfile|-k PATH/TO/ID_VCRYPT
아마도 `--genkey|-g` 명령을 사용하여 생성된 적합한 Base64 인코딩된 키가 포함된 파일에 대한 경로를 지정합니다. 

## 입력

### 암호화 모드

    $FILE_CONTAINING_CLEARTEXT | -- $CLEARTEXT

### 복호화 모드

    $FILE_CONTAINING_CRYPTED_TEXT | -- $CRYPTED_TEXT

## 예제

키를 생성하고 이를 `id_vcrypt` 파일에 둡니다. 

    vcrypt --genkey > id_vcrypt

표준 입력의 비밀번호를 표준 출력으로 암호화하며, `my_secret_data.txt`로 출력 경로 재지정을 통해 여기에 쓰여집니다. 

    ./vcrypt --encrypt --keyfile id_vcrypt -- "my secret password" > my_secret_data.txt

또한 출력을 파이프를 통해 `xclip`, `pbcopy`에 전달하거나, 이와 유사하게 출력을 운영 체제 클립보드에 둘 수도 있습니다. 

파일에서 비밀번호 복호화: 

    vcrypt --decrypt --keyfile id_vcrypt my_secret_data.txt

## 특성 및 환경 변수

### `VCRYPT_OPTS` 환경 변수
이 환경 변수를 사용하면 `vcrypt`를 시작하는 데 사용된 `java` 명령에 옵션을 전달할 수 있습니다. 

### `vcrypt.key` 특성
`--keyfile | -k keyfile` 옵션을 전달하는 대신, 명령행에서 키를 사용할 수 있도록
16 또는 32바이트 문자열로 `VCRYPT_OPTS`의 `-D` 특성으로서 이를 전달합니다. 

사용법 예제: 

    VCRYPT_OPTIONS="-Dvcrypt.key='1234qwerasdfzxcv'" vcrypt --encrypt file_to_encrypt

### `VIV_VCRYPT_KEY` 환경 변수
`vcrypt`는 키 설정을 위한 이 환경 변수의 사용을 허용합니다. 이는 16 또는 32바이트여야 합니다. 

## 관련 항목

crawler(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
