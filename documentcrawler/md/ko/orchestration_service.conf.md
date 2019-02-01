# 오케스트레이션 서비스 구성
오케스트레이션 서비스는 크롤링된 파일을 관리하는 방법을 크롤러에게 알려줍니다. 기본 옵션은 `config/orchestration/orchestration-service.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하여 직접 변경될 수 있습니다. 

*  **http_timeout** - 문서 읽기/색인화 조작에 대한 제한시간(초 단위)이며, 기본값은 `585`입니다. 
*  **concurrent_upload_connection_limit** - 문서의 업로드에 허용된 동시 연결의 수입니다. 기본값은 `10`입니다. 일반적으로, 이 숫자는 크롤링 옵션을 구성할 때 설정된 `output_limit`보다 크거나 같아야 합니다. 
*  **base_url** - 크롤링된 문서가 전송될 대상 URL입니다. 
*  **endpoint** - `base-url`에서 크롤링된 문서 콜렉션의 위치입니다. 
*  **username** - `endpoint` 위치를 인증하기 위한 사용자 이름입니다. 
*  **password** - `endpoint` 위치를 인증하기 위한 비밀번호입니다. **중요사항** - Data Crawler와 함께 제공된 vcrypt 프로그램을 사용하여 이 비밀번호를 암호화하지 **마십시오**. 
*  **config_file** - 오케스트레이션 서비스가 사용하는 구성 파일입니다. 

오케스트레이션 서비스 출력 어댑터는 IBM이 자체 사용자를 보다 잘 파악하고 서비스를 제공할 수 있도록 통계를 전송할 수 있습니다. 다음 옵션을 `send_stats` 변수에 대해 설정할 수 있습니다. 
*  **jvm** - 전송된 JVM(Java Virtual Machine) 통계에는 데이터 크롤러의 실행에 사용된 JVM에서 보고하는 대로 Java 벤더 및 버전이 포함됩니다. 값은 `true` 또는 `false`입니다.
*  **os** - 전송된 운영 체제(OS) 통계에는 데이터 크롤러의 실행에 사용된 JVM에서 보고하는 대로 OS 이름, 버전 및 아키텍처가 포함됩니다. 값은 `true` 또는 `false`입니다.

## 관련 항목

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

crawler-seed.conf(5)
