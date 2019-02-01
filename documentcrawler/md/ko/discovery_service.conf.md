# Discovery Service 구성
Discovery Service는 IBM Watson Discovery Service를 사용할 때 크롤링된 파일을 관리하는 방법을 크롤러에게 알려줍니다. 기본 옵션은 `config/discovery/discovery_service.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하여 직접 변경될 수 있습니다. 

*  **http_timeout** - 문서 읽기/색인화 조작에 대한 제한시간(초 단위)이며, 기본값은 `125`입니다. 
*  **concurrent_upload_connection_limit** - 문서의 업로드에 허용된 동시 연결의 수입니다. 기본값은 `2`입니다. 오케스트레이션 서비스 출력 어댑터를 사용 중인 경우, 이 숫자는 크롤링 옵션을 구성할 때 설정된 `output_limit`보다 크거나 같아야 합니다. 
*  **base_url** - 크롤링된 문서가 전송될 대상 URL입니다. Discovery Service의 현재 릴리스의 경우, 값은 `https://gateway.watsonplatform.net/discovery/api`입니다. 
*  **environment_id** - `base-url`에서 크롤링된 문서 콜렉션의 위치입니다. 
*  **collection_id** - Discovery Service에서 설정한 문서 콜렉션의 이름입니다. 
*  **configuration_id** - Discovery Service가 사용하는 구성 파일의 파일 이름입니다. 
*  **check_for_completion** - 문서가 엔드포인트에서 정상적으로 처리되었는지 여부를 확인합니다. 이로 인해 크롤러의 감지된 성능이 저하되지만, 성공적인 문서 업로드와 변환에 대한 신뢰할 수 있는 알림이 생성됩니다. 값은 `true` 또는 `false`입니다.  
**IMPORTANT** - 이 매개변수를 사용하는 경우, 사용 가능한 자원을 충분히 활용할 수 있도록 크롤링 옵션을 구성할 때 설정된 `output_limit`보다 크거나 같게 `concurrent_upload_connection_limit`를 늘리도록 권장합니다. 

Discovery Service 신임 정보 제공: 
*  **username** - 크롤링된 문서 콜렉션의 위치를 인증하기 위한 사용자 이름입니다. 
*  **password** - 크롤링된 문서 콜렉션의 위치를 인증하기 위한 비밀번호입니다. 

Discovery Service 출력 어댑터는 IBM이 자체 사용자를 보다 잘 파악하고 서비스를 제공할 수 있도록 통계를 전송할 수 있습니다. 다음 옵션을 `send_stats` 변수에 대해 설정할 수 있습니다. 
*  **jvm** - 전송된 JVM(Java Virtual Machine) 통계에는 데이터 크롤러의 실행에 사용된 JVM에서 보고하는 대로 Java 벤더 및 버전이 포함됩니다. 값은 `true` 또는 `false`입니다.
*  **os** - 전송된 운영 체제(OS) 통계에는 데이터 크롤러의 실행에 사용된 JVM에서 보고하는 대로 OS 이름, 버전 및 아키텍처가 포함됩니다. 값은 `true` 또는 `false`입니다.

*  **api_version** - 내부 전용입니다. 마지막 API 버전 변경 날짜입니다. 

# URL 추적 스토리지 구성
`config/discovery` 폴더에는 크롤러 URL 및 문서 ID의 내부 맵핑에 사용될 수 있는 구성 파일도 포함됩니다. 기본 옵션은 `config/discovery/uri_tracking_storage.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하여 직접 변경될 수 있습니다. 

*  **driver** - 데이터베이스의 JDBC H2 드라이버 클래스입니다. 기본값은 `org.h2.Driver`입니다. 
*  **url** - 이는 JDBC 연결 문자열의 URL 접두부입니다. 형식은 `jdbc:h2:[file:]`입니다. **참고** 접두부 `file:`은 선택사항입니다. 사용되지 않거나 `database_location`에 대한 상대 경로만 사용되는 경우, 현재 작업 디렉토리가 시작점으로서 사용됩니다. 기본값은 `jdbc:h2:file:`입니다. 
*  **database_location** - 데이터베이스가 저장된 디스크의 위치입니다(예: `./storage/database` 또는 `~/storage/database`). 기본값은 `./storage/database`입니다. 
*  **database_name** - 데이터베이스의 이름입니다. 기본값은 `ActivityDB`입니다. 
*  **table_name** - 사용할 테이블의 이름입니다. 기본값은 `UriTracker`입니다. 
*  **username** - 데이터베이스에 연결하기 위한 사용자 이름입니다. 
*  **password** - 데이터베이스에 연결하기 위한 비밀번호입니다. 

## 관련 항목

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
