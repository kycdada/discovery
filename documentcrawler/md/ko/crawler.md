크롤러(1) - A 위치에서 B 위치로 데이터 이동을 위한 크롤러
====================================================================

## 시놉시스

사용법: crawler [ crawl | testit | restart | resume | refresh | summary ][ options ]

## 설명

Data Crawler는 컨텐츠 관리 시스템 및 파일 시스템 등과 같은 데이터의 다양한 저장소를 크롤링한 후에 결과 문서를 원격 서비스로 푸시하는 데 사용됩니다. 

## 글로벌 옵션

    --version
        프로그램 버전을 표시합니다.
    --help
        이 사용법 텍스트를 표시합니다. 

## 명령

### crawl [ options ]

현재 구성으로 크롤링을 실행합니다. 

    -c <value> | --config <value>  # 사용할 구성 파일을 지정합니다. 기본값은 "config/crawler.conf"입니다.
    --pii-checking <value>         # PII 확인을 토글합니다. 

### testit [ options ]

시드 URL만 크롤링하며 인큐된 URL을 표시하는 테스트 크롤링을 실행합니다. 시드 URL이 결과적으로
색인화 가능 컨텐츠(예: 문서)를 생성하는 경우, 해당 컨텐츠는 출력 어댑터로 전송되며 컨텐츠가 화면에 인쇄됩니다. 
시드 URL 검색으로 URL이 인큐되면 해당 URL이 표시되며, 어떤 컨텐츠도 출력 어댑터로 전송되지 않습니다. 기본적으로 5개의 인큐된 URL이 표시됩니다. 

    -c <value> | --config <value>  # 사용할 구성 파일을 지정합니다. 기본값은 "config/crawler.conf"입니다.
    -l <n> | --limit <n>           # 표시되는 인큐된 URL의 수를 제한합니다.
    --pii-checking <value>         # PII 확인을 토글합니다. 

### restart [ options ]

크롤링 재시작을 실행합니다. 현재 구성으로 새 크롤링을 실행합니다. 

    -c <value> | --config <value>  # 사용할 구성 파일을 지정합니다.
    --pii-checking <value>         # PII 확인을 토글합니다. 

### resume [ options ]

중지된 위치에서 크롤링을 재개합니다. 

    -c <value> | --config <value>  # 사용할 구성 파일을 지정합니다.
    --pii-checking <value>         # PII 확인을 토글합니다. 

### refresh [ options ]

이전 크롤링을 새로 고칩니다. 

    -c <value> | --config <value>  # 사용할 구성 파일을 지정합니다.
    --pii-checking <value>         # PII 확인을 토글합니다. 

### summary [ options ]

크롤링 보고서를 생성합니다. 

    --submitted                    # 제출된 모든 문서를 조회합니다.
    --processed                    # 정상적으로 처리된 문서만 조회합니다.
    --failed                       # 정상 처리에 실패한 문서만 조회합니다.
    --group-id <value>             # 지정된 그룹에 대한 크롤링 실행을 조회합니다. 그룹은 초기 크롤링 및 해당 초기 크롤링의 재개, 새로 고치기 또는 재시작으로 구성됩니다. 값이 지정되지 않은 경우, 이 조회의 기본값은 크롤링된 최신 그룹입니다.
    --show-content                 # 조회와 연관된 추가 컨텐츠를 표시합니다.
    --filter                       # URL 및 hashID의 조회 결과를 필터링합니다. 

## 예제

`config/crawler.conf`에서 구성 파일을 사용하여 크롤링을 실행합니다. 

    crawler crawl

`config/crawler.conf`에서 구성 파일을 사용하여 테스트를 실행합니다. 

    crawler testit

`/home/watson/office-share.conf`에서 구성 파일을 사용하여 크롤링을 실행합니다. 

    crawler crawl --config /home/watson/office-share.conf

`/home/watson/office-share.conf`에서 구성 파일을 사용하여 크롤링을 다시 시작합니다. 

    crawler restart --config /home/watson/office-share.conf

`2`의 그룹 ID로 실패한 문서에 대한 요약 정보를 가져옵니다. 

    crawler summary --failed --group-id 2 --show-content

버전을 포함하여 사용법을 표시합니다. 

    crawler --help

## 구성

`crawler`에서는 해당 옵션에 대한 구성 파일이 필요합니다. 구성 파일의 예제는
`crawler` 설치 디렉토리 내의 `share` 디렉토리에서 제공됩니다. 
이러한 예제를 복사하고 이를 수정하십시오. *해당 위치에서는 예제를 수정하지 마십시오. *

`--config | -c` 옵션을 지정하지 않은 경우, `crawler`는
`crawler`가 시작된 디렉토리의 `config` 디렉토리에서 해당 구성을 찾습니다. 
즉, `crawler`는 `config/crawler.conf`를 찾습니다. 

## 진단

이 기능을 사용하여 문제점을 진단할 수 있습니다. 

### 디버깅

디버깅 모드를 활성화합니다. `crawler.conf` 파일에서 다음을 설정하십시오. 

    debugging.full_node_debugging = true

### 로깅

로깅을 사용합니다. `log4j_custom.properties` 파일에서 다음을 설정하십시오. 

    log4j.rootLogger=INFO, Console, Log

이는 파일 출력에 대한 기본 로깅 레벨입니다. 콘솔 로그의 경우, 기본값은 다음과 같습니다. 

    log4j.appender.Console.Threshold=WARN

로깅 레벨은 다음 값으로 설정될 수 있습니다. 

    OFF - 최상위의 가능한 순위이며, 이는 로깅을 끄는 용도로 사용됩니다.
    FATAL - 애플리케이션 중단을 유발할 가능성이 큰 매우 심각한 오류 이벤트를 지정합니다.
    ERROR - 아직은 애플리케이션이 실행을 계속하도록 허용할 수 있는 오류 이벤트를 지정합니다.
    WARN - 잠재적으로 유해한 상황을 지정합니다.
    INFO - 상세하지 않은 레벨에서 애플리케이션의 진행 상태를 강조표시하는 정보 메시지를 지정합니다.
    DEBUG - 애플리케이션을 디버그하기에 최적인 상세한 정보 이벤트를 지정합니다.
    TRACE - DEBUG보다 상세한 정보 이벤트를 지정합니다.
    ALL - 최하위의 가능한 순위이며, 이는 모든 로깅을 켜는 용도로 사용됩니다. 

## 제한

처리량을 관리하는 데 도움이 되도록 크기 제한사항을 정의합니다. `crawler.conf` 파일에서 다음을 설정하십시오. 

`shutdown_timeout` 애플리케이션을 종료하기 전의 제한시간 값(분 단위)을 지정합니다. 기본값은 10입니다. 

    shutdown_timeout = <n>

`output_limit`는 휴대용 크롤러가 리턴을 대기하며 출력 어댑터에 동시에 전송할
색인화 가능 항목의 최대 수입니다. 기본값은 10입니다. 이는 작업 수행에 사용 가능한 코어에 의해 추가로 제한될 수 있습니다. 

    output_limit = <n>

`input_limit` 동시에 커넥터에서 요청 가능한 URL의 수를 제한합니다. 기본값은 3입니다. 

    input_limit = <n>

`output_timeout`은 휴대용 크롤러가 출력 어댑터에 대한 요청을 포기한 후에
한계 큐에서 해당 항목을 제거하여 추가 처리를 허용하기 전의 시간의 양(초 단위)입니다. 기본값은 150입니다.

    output_timeout = <n>

해당 제한조건이 여기에 정의된 한계와 관련될 수 있으므로, 출력 어댑터에 의해 적용되는 제한조건에 대해서는 고려가 필요합니다. 
위에서 정의된 `output_limit`는 오직 동시에 출력 어댑터에 전송될 수 있는 색인화 가능 오브젝트의 수에만 관련됩니다. 
일단 출력 어댑터로 전송된 경우, 색인화 가능 오브젝트는 `output_timeout` 변수에서 정의한 대로 "클럭 상"에 놓입니다. 
출력 어댑터 자체에 제한이 있어서 수신하는 수 만큼의 입력을 처리하지 못할 수 있습니다. 
예를 들어, 오케스트레이션 출력 어댑터에는 서비스에 대한 HTTP 연결을 위해 구성 가능한 연결 풀이 있을 수 있습니다. 
예를 들어, 해당 기본값이 8이며 해당 연결 풀에 대해 구성된 것보다 큰 수로 `output_limit`를 설정하면
실행할 차례를 대기하는 클럭 상의 프로세스를 보유하게 됩니다. 그러면 제한시간 초과가 발생할 수 있습니다. 

`num_threads` 동시에 실행 가능한 병렬 스레드의 수입니다. 
이 값은 직접 병렬 스레드의 수를 지정하는 정수이거나,
사용 가능한 프로세서의 수의 증배율을 지정하는 `"xNUM"` 형식의 문자열일 수 있습니다. 
기본값은 "x1.5" 또는 사용 가능한 프로세서의 수의 1.5배입니다(`Runtime.availableProcessors`에서 취한 대로). 

    num_threads = <n>

Data Crawler 풀에서 병렬성을 계산하는 공식은 `min(maxThreads, max(minThreads, numThreads))`입니다. 

## 환경 변수 `CRAWLER_OPTS` 

다음은 기본값으로 나열된 `CRAWLER_OPTS` 환경 변수를 통해 `crawler`에 전달될 수 있는 특성입니다. 

다음과 같이 이를 전달하십시오. 

    CRAWLER_OPTS="-Dproperty=value -Dproperty=value" crawler

이는 디버깅 용도로만, 그리고 IBM 지원 센터의 지시 하에서만 변경되어야 합니다. 

### cfa.java_bin

`cfa.java_bin`은 커넥터 프레임워크 입력 어댑터를 시작하는 데 사용되는
`java` 명령을 변경할 수 있습니다. 기본적으로, `crawler`는
`crawler` 자체를 실행하는 데 사용되는 것과 동일한 `java` 2진을 사용합니다. 

또한 이는 `java.home` 특성을 설정하여 변경이 가능하며, 이는 다시 `java` 실행 파일에 대한 경로를 계산하는 데 사용됩니다. 

### cfa.lib_dir

`cfa.lib_dir`은 커넥터 프레임워크의 `lib` 디렉토리에 대한 경로를 변경합니다. 가급적이면 이를 변경하지 마십시오. 
기본적으로, `crawler`는 커넥터 프레임워크(보통 단순히 `connectorFramework`)에 대한 계산된 경로 내의 `lib` 디렉토리를 사용합니다. 

### cfa.framework_jars_dir

`cfa.framework_jars_dir`은 기본적으로 `connectorFramework/<version>/lib/java`에 있는 커넥터 프레임워크의 jars 디렉토리로 경로를 변경합니다. 

### cfa.plugins_dir

`cfa.plugins_dir`은 실제 커넥터가 저장된 커넥터 프레임워크의 플러그인 디렉토리로 경로를 지정합니다.
기본적으로, 이는 `framework_jars_dir`에서 빌드되며 `connectorFramework/<version>/lib/java/plugins`가 됩니다. 

## 알려진 제한사항

Data Crawler의 현재 릴리스에서 알려진 제한사항을 자세히 설명합니다. 

* 올바르지 않거나 누락된 URL로 파일 시스템 커넥터를 실행하면 Data Crawler가 정지될 수 있습니다. 
* 모든 화이트리스트 URL 또는 RegExe가 단일 RegEx 표현식에 포함되도록 `config/crawler.conf` 파일에서 `urls_to_filter` 값을 구성하십시오. 
* `--config | -c` 옵션에서 전달된 구성 파일에 대한 경로는 규정된 경로여야 합니다. 즉, 이는 상대 형식 `config/crawler.conf` 또는 `./crawler.conf`이거나 절대 경로 `/path/to/config/crawler.conf`여야 합니다. 단순 `crawler.conf` 지정은 `crawler.conf` 파일에서 `include`를 사용하여 참조된 파일이 `include`를 사용하는 대신 인라인된 경우에만 가능합니다. 예를 들어, `discovery/discovery_service.conf`는 구성의 읽기가 쉬워지도록 `include`됩니다. 해당 컨텐츠는 config 옵션에서 규정되지 않은 경로를 사용할 수 있도록 `output_adapter.discovery_service` 키 내에서 `crawler.conf`로 복사되어야 합니다. 

## 변경 로그

이 릴리스에서 변경사항의 목록은 설치 디렉토리의 `changelog.txt` 파일을 참조하십시오. 

## 작성자

IBM Watson - https://www.ibm.com/smarterplanet/us/en/ibmwatson/

피츠버그에서 yinz에 의해 작성되었습니다. 

## 관련 항목

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
