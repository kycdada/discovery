# Data Crawler 구성

`crawler`에서는 해당 옵션에 대한 구성 파일이 필요합니다. 구성의 예제는
`crawler` 설치 디렉토리 내의 `share` 디렉토리에서 제공됩니다. 
이러한 예제를 복사하고 이를 수정하십시오. *해당 위치에서는 예제를 수정하지 마십시오. *

`crawler.conf` 파일에는 크롤링에 사용할 파일(입력 어댑터), 크롤링 완료 시에 크롤링된 파일의
콜렉션이 전송될 위치(출력 어댑터), 그리고 기타 크롤링 관리 옵션을 크롤러에게 알리는 정보가 포함되어 있습니다. 

**참고**: 모든 파일 경로는 별도로 언급한 경우가 아니면 `config` 디렉토리에 상대적입니다. 

이 파일에서 설정될 수 있는 옵션은 다음과 같습니다. 

## 입력 어댑터
*  **class** - 내부 전용이며, Data Crawler 입력 어댑터 클래스를 정의합니다. 기본값은 `com.ibm.watson.crawler.connectorframeworkinputadapter.Crawl`입니다. 
*  **config** - 내부 전용이며, 커넥터 프레임워크 구성을 정의합니다. 선택된 입력 어댑터에 전달할 이 블록 내의 기본 구성 키는 `connector_framework`입니다. **참고** - 커넥터 프레임워크는 사용자가 데이터에 전달할 수 있도록 허용하는 프레임워크입니다. 이는 엔터프라이즈 내의 내부 데이터이거나 웹 또는 클라우드의 외부 데이터일 수 있습니다. 커넥터를 사용하면 다수의 서로 다른 데이터 소스에 액세스할 수 있지만, 연결은 실제로 크롤링 프로세스에 의해 제어됩니다. 
  -  **중요사항** - 커넥터 프레임워크 입력 어댑터에 의해 검색된 데이터는 로컬로 캐시됩니다. 이는 암호화되어 저장되지 않습니다. 기본적으로, 데이터는 재부팅 시에 지워져야 하고 크롤러 명령을 실행한 사용자만 읽기가 가능해야 하는 임시 디렉토리에 캐시됩니다. 자체 이후 정리가 가능하기 전에 커넥터 프레임워크가 사라지는 경우, 이 디렉토리의 수명이 크롤러보다 길 수가 있습니다. 캐시된 데이터의 위치를 신중히 고려하십시오. 이를 암호화된 파일 시스템에 둘 수 있지만, 이를 수행함으로써 성능에 미치는 영향을 고려하십시오. 오직 사용자만 크롤링에 대한 속도와 보안 간의 적절한 밸런스를 결정할 수 있습니다. 
*  **crawl_config_file** - 크롤링에 사용할 구성 파일입니다. 기본값은 `connectors/filesystem.conf`입니다. 
*  **crawl_seed_file** - 크롤링에 사용할 크롤링 시드 파일입니다. 기본값은 `seeds/filesystem-seed.conf`입니다. 
*  **id_vcrypt_file** - 크롤러에 의해 데이터 암호화에 사용되는 키 파일입니다. 크롤러와 함께 포함된 기본 키는 `id_vcrypt`입니다.
새 id_vcrypt_file을 생성해야 하는 경우에는 `bin` 폴더의 vcrypt 스크립트를 사용하십시오. 
*  **crawler_temp_dir** - 커넥터 로그의 크롤러 임시 폴더입니다. 기본값 `tmp`가 제공됩니다. 아직 존재하지 않으면 `tmp` 폴더가 현재 작업 디렉토리에서 작성됩니다. 
*  **extra_jars_dir** - 내부 전용이며, 추가 JAR을 커넥터 프레임워크 클래스 경로에 추가합니다.
SharePoint 커넥터를 사용할 때 이 값은 `oakland`여야 하며, 데이터베이스 커넥터를 사용할 때
이 값은 `database`여야 합니다. 기타 커넥터를 사용할 때는 이를 비워둘 수 있습니다(즉, 빈 문자열 "").
  **참고**: 커넥터 프레임워크 `lib/java` 디렉토리에 상대적입니다. 
*  **urls_to_filter** - 정규식 양식으로 크롤링할 URL의 줄 바꾸기로 분리된 화이트리스트입니다. Data Crawler는 제공된 정규식 중 하나와 일치하는 URL만 크롤링합니다. 도메인 목록에는 가장 일반적인 최상위 레벨 도메인이 포함됩니다. 필요하면 이에 추가하십시오. 파일 extension-type 목록에는 Data Crawler의 이 릴리스 현재로 오케스트레이션 서비스가 지원하는 파일 확장자가 포함되어 있습니다. 시드 URL 도메인이 필터에 의해 허용되는지 확인하십시오. 예를 들어, 시드 URL이 `http://testdomain.test.in`처럼 보이면 도메인 필터에 "`in`"을 추가하십시오. 시드 URL이 필터에 의해 제외되지 않음을 확인하십시오. 그렇지 않으면, 크롤러가 정지될 수 있습니다. 
*  **max_text_size** - 커넥터 프레임워크에 의해 디스크에 쓰여지기 전에 문서의 가능한 최대 크기(바이트 단위)입니다. 이를 보다 높게 조정하면 디스크에 쓰여지는 문서의 양은 감소되지만 메모리 요구사항은 증가됩니다. 
*  **extra_vm_params** - 커넥터 프레임워크를 실행하는 데 사용된 명령에 Java 매개변수를 더 추가할 수 있도록 허용합니다. 
*  **bootstrap_logging** - 커넥터 프레임워크 구동 로그를 씁니다. 고급 디버깅에만 유용합니다. 값은 `true` 또는 `false`입니다. 로그 파일은 `crawler_temp_dir`에 쓰여집니다. 

## 스토리지 어댑터

데이터베이스에 대한 크롤러의 내부 상태의 스토리지를 허용합니다. 크롤링 `restart` 및 `resume` 옵션이 올바르게 작동하려면 이 설정은 필수입니다. 

```javascript
storage_adapter {
 config = "storage_in_db"
  storage_in_db {
    include "storage/database_storage.conf"
  } 
}
```
참조된 파일 `storage/database_storage.conf`는 기본적으로 H2 데이터베이스를 사용합니다. 제공된 기본값 대신에 JDBC 드라이버로 데이터베이스를 사용할 수 있습니다. 이러한 설정 중 일부에 대한 특정 정보를 찾으려면 JDBC 드라이버에 대한 문서를 참조하십시오. 기본 옵션은 `config/storage/database_storage.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하여 직접 변경될 수 있습니다.

*  **class** - 이 클래스는 사용할 데이터베이스 어댑터 클래스를 지시합니다. 기본값은 `com.ibm.watson.crawler.storageadapters.DatabasePersistAdapter`입니다. 
*  **driver** - JDBC 드라이버의 클래스입니다. H2를 사용하려면 기본값은 `org.h2.Driver`입니다. 
*  **url** - 드라이버의 JDBC 옵션을 참조합니다. 이는 JDBC 연결 문자열의 URL 접두부입니다. 기본값은 `jdbc:h2:file:`입니다. 
*  **database_location** - 데이터베이스에 대해 원하는 위치입니다. 이는 sqlite 및 H2 등의 파일 기반 데이터베이스에만 적용됩니다. 기본값은 `./storage/database`입니다. 
*  **database_name** - 데이터베이스의 이름입니다. 기본값은 `ActivityDB`입니다. 
*  **table_name** - 사용할 테이블의 이름입니다. 기본값은 `Ledger`입니다. 
*  **username** - 데이터베이스에 연결하기 위한 사용자 이름입니다. 
*  **password** - 데이터베이스에 연결하기 위한 비밀번호입니다. 

대부분의 활동에는 기본 구성으로도 충분합니다. 

## 출력 어댑터

선택할 수 있는 몇 가지 *출력 어댑터*가 있습니다. `crawler.conf`에서
`output_adapter.class`를 설정하여 출력 어댑터를 설정하십시오. 옵션은 다음과 같습니다.  

*  **class** - Data Crawler 출력 어댑터 클래스를 정의합니다. 기본값은 `com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter`입니다. 
*  **config** - 출력 어댑터에 전달할 구성 키를 정의합니다. 문자열은 이 구성 오브젝트 내의 키와 대응되어야 합니다. 다음 코드 예제를 참조하십시오. 
```javascript
  orchestration_service {
    include "orchestration_service.conf"
  },
  test {
    output_directory = "/tmp/crawler-test-output"
  }
}
```
여기서 구성 키는 `orchestration_service`입니다. 기본값은 `discovery_service`입니다.

해당 `class` 매개변수 및 `config` 키를 지정하여 출력 어댑터를 선택해야 합니다. 

* **오케스트레이션 서비스 출력 어댑터**: 크롤링된 문서를 Watson Developer Cloud의 오케스트레이션 서비스로 업로드합니다. 
`class` 매개변수 및 `config` 키를 다음과 같이 설정하여 이 어댑터를 선택하십시오.  
```javascript
  class = "com.ibm.watson.crawler.orchestrationserviceoutputadapter.oneatatime.OrchestrationServiceOutputAdapter"
  config = "orchestration_service"
  orchestration_service {
    include "orchestration/orchestration_service.conf"
  }
```
* **Discovery Service 출력 어댑터**: 크롤링된 문서를 Watson Developer Cloud의 Discovery Service로 업로드합니다. 
`class` 매개변수 및 `config` 키를 다음과 같이 설정하여 이 어댑터를 선택하십시오. 
```javascript
  class = "com.ibm.watson.crawler.discoveryserviceoutputadapter.DiscoveryServiceOutputAdapter"
  config = "discovery_service"
  discovery_service {
    include "discovery/discovery_service.conf"
  }
```
* **Watson 테스트 출력 어댑터**: 크롤링된 파일의 표현을 디스크의 지정된 위치에 씁니다. 
`class` 매개변수 및 `config` 키를 다음과 같이 설정하여 이 어댑터를 선택하십시오. 

**참고** - 추가 매개변수 `output_directory`는 크롤링된 데이터의 표현이 쓰여져야 하는 디렉토리를 선택합니다. 
```javascript
  class = "com.ibm.watson.crawler.testoutputadapter.TestOutputAdapter"
  config = "test"
  output_directory = "/tmp/crawler-test-output"
```
* **retry** - 출력 어댑터에 푸시하는 시도가 실패한 경우에 재시도를 위한 옵션을 지정합니다. 
  * max_attempts - 최대 재시도 횟수입니다. 기본값은 `10`입니다. 
  * delay - 각각의 시도 간의 최소 지연 시간(초 단위)입니다. 기본값은 `2`입니다. 
  * exponent_base - 실패한 각 시도에서 지연 시간 증가를 판별하는 계수입니다. 기본값은 `2`입니다. 

 공식: 
```
 d(nth_retry) = delay * (exponent_base ^ nth_retry)
```

 예를 들어, 1초의 지연과 지수 베이스 2의 설정은 두 번째 재시도(세 번째 시도)가 1초 대신 2초가 지연되도록 하며 그 다음엔 4초가 지연되도록 합니다. 
 ```
 d(0) = 1 * (2 ^ 0) = 1 second
 d(1) = 1 * (2 ^ 1) = 2 seconds
 d(2) = 1 * (2 ^ 2) = 4 seconds
```
따라서 기본 설정에서 제출은 최대 10회까지 시도되며 약 1,022초(17분을 약간 초과함)까지 대기합니다. 다수의 재제출이 동시에 실행되지 않도록 시간이 더 추가되므로 이 시간은 단지 추정치에 불과합니다. 이 "불특정" 시간이 최대 10% 이므로, 이전 예제에서 마지막 재시도는 최대 4.4초까지 지연될 수 있습니다. 대기 시간에는 서비스에 연결, 데이터 업로드 또는 응답 대기에 소요된 시간은 포함되지 않습니다.

 *경고:* 이러한 기본값을 낮추어 대기 시간을 줄이면 구성된 출력 어댑터를 통해 문서가 정상적으로 업로드되지 못할 수 있습니다. Watson Developer Cloud 서비스의 사용 시에 이에 대한 근거는 "429 너무 많은 요청" 등급 한계를 기술하는 로그의 RetryFailure 메시지입니다. 
 
## 디버깅 옵션
*  **full_node_debugging** - 디버깅 모드를 활성화합니다. 가능한 값은 `true` 또는 `false`입니다. **경고**: 이는 크롤링된 모든 문서의 전체 데이터를 로그에 둡니다. 
*  **heartbeat_wait_time** - 문서 수집 통계를 보고하는 중의 시간 간격(밀리초 단위)입니다(디버깅 모드에만 해당). 기본값은 1000밀리초입니다. 

## 로깅 옵션
*  **configuration_file** - 로깅에 사용할 구성 파일입니다. 샘플 `crawler.conf` 파일에서 이 옵션은 `logging.log4j`에 정의되어 있으며, 이의 기본값은 `log4j_custom.properties`입니다.
이 옵션은 `.properties` 또는 `.conf` 파일을 사용하는지 여부와는 무관하게 유사하게 정의되어야 합니다. 

## 추가 크롤링 관리 옵션
*  **shutdown_timeout** - 애플리케이션을 종료하기 전의 제한시간 값(분 단위)을 지정합니다. 기본값은 `10`입니다. 
*  **output_limit** - 크롤러가 출력 어댑터에 동시 전송을 시도할 색인화 가능 항목의 최대 수입니다. 이는 작업 수행에 사용 가능한 코어의 수에 의해 추가로 제한될 수 있습니다. 이는 주어진 시점에 리턴을 대기 중인 출력 어댑터에 전송된 색인화 가능 항목이 최대 "x"개에 불과함을 의미합니다. 기본값은 `10`입니다. 
*  **input_limit** - 동시에 커넥터에서 요청 가능한 URL의 수를 제한합니다. 기본값은 `3`입니다. 
*  **output_timeout** - Data Crawler가 출력 어댑터에 대한 요청을 포기한 후에 출력 어댑터 큐에서 해당 항목을 제거하여 추가 처리를 허용하기 전의 시간의 양(초 단위)입니다. 기본값은 `1200`입니다. 
**참고** - 해당 제한조건이 여기에 정의된 한계와 관련될 수 있으므로, 출력 어댑터에 의해 적용되는 제한조건에 대해서는 고려가 필요합니다. 
위에서 정의된 `output_limit`는 오직 동시에 출력 어댑터에 전송될 수 있는 색인화 가능 오브젝트의 수에만 관련됩니다. 
일단 출력 어댑터로 전송된 경우, 색인화 가능 오브젝트는 `output_timeout` 변수에서 정의한 대로 "클럭 상"에 놓입니다. 
출력 어댑터 자체에 제한이 있어서 수신하는 수 만큼의 입력을 처리하지 못할 수 있습니다. 
예를 들어, 오케스트레이션 출력 어댑터에는 서비스에 대한 HTTP 연결을 위해 구성 가능한 연결 풀이 있을 수 있습니다. 예를 들어, 해당 기본값이 8이며 `output_limit`를 8보다 큰 수로 설정하면 실행할 차례를 대기하는 클럭 상의 프로세스를 보유하게 됩니다. 그러면 제한시간 초과가 발생할 수 있습니다. 
*  **num_threads** - 동시에 실행 가능한 병렬 스레드의 수입니다. 이 값은 직접 병렬 스레드의 수를 지정하는 정수이거나, 사용 가능한 프로세서의 수의 증배율을 지정하는 "xNUM" 형식의 문자열일 수 있습니다(예: "x1.5"). 기본값은 `"30"`입니다. 

## 관련 항목

crawler(1)

vcrypt(1)

crawler-options.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
