# 크롤링 구성 옵션
데이터 크롤러는 최종적으로 IBM Watson 검색 및 순위 지정 서비스에 대한 검색 결과를 작성하는 데 사용되는 원시 데이터를 수집합니다. 

데이터 크롤러는 현재 다음 저장소에서 데이터 콜렉션을 지원하기 위한 커넥터를 제공합니다. 

*	파일 시스템
*	JDBC를 통한 데이터베이스
*	CMIS(Content Management Interoperability Services)
*	SMB(Server Message Block), CIFS(Common Internet Filesystem) 또는 Samba 파일 공유
*	SharePoint 및 SharePoint Online
*	Box

커넥터의 사용자 정의를 허용하는 커넥터 구성 템플리트도 함께 제공됩니다. 

## 시작하기:
데이터 저장소를 크롤링하는 경우, 크롤러는 사용자 지정된 시작 시드 URL에서 시작하며 정보 페이지의 다운로드를 시작합니다. 또한 크롤러는 다운로드된 페이지의 링크를 찾고 추가 크롤링을 위해 새로 검색된 페이지를 스케줄링합니다. 

구성 정보는 크롤링이 필요한 페이지와 이를 크롤링하는 방법을 판별하는 데 사용됩니다. 이 파일에서는 각 커넥터에 대해 구성할 수 있는 옵션을 설명합니다. 

**참고**: 각 커넥터에는 대응되는 시드 구성 파일도 있으며, 시드 구성 옵션은 별도로 설명됩니다. 

### 파일 시스템 커넥터 구성
파일 시스템 커넥터를 사용하면 데이터 크롤러 설치에 로컬인 파일을 크롤링할 수 있습니다. 다음은 파일 시스템 커넥터를 사용하는 데 필요한 기본 구성 옵션입니다. 이러한 값을 설정하려면 `config/connectors/filesystem.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하십시오. 

*  **protocol** - 크롤링에 사용되는 커넥터 프로토콜의 이름입니다. 이 커넥터에는 `sdk-fs`를 사용하십시오. 
*  **collection** - 이 속성은 임시 파일의 압축을 푸는 데 사용됩니다. 
*  **logging-config** - 로깅 옵션을 구성하는 데 사용된 파일을 지정하며, 이는 `log4j` XML 문자열로서 형식화되어야 합니다. 
*  **classname** - 커넥터의 Java 클래스 이름입니다. 이 커넥터를 사용하기 위한 값은 `plugin:filesystem.plugin@filesystem`이어야 합니다. 

### 데이터베이스 커넥터 구성
데이터베이스 커넥터를 사용하면 사용자 정의 SQL 명령을 실행하고 행(레코드)당 하나의 문서와 열(필드)당 하나의 컨텐츠 요소를 작성하여 데이터베이스를 크롤링할 수 있습니다. 각 레코드의 마지막 수정 날짜를 표시하는 시간소인이 포함된 열은 물론 고유 키로서 사용될 열을 지정할 수 있습니다. 커넥터는 지정된 데이터베이스의 모든 레코드를 검색하며 SQL문에서 특정 테이블, 결합 등으로 제한될 수도 있습니다. 

데이터베이스 커넥터를 사용하면 다음 데이터베이스를 크롤링할 수 있습니다. 

*  IBM DB2
*  MySQL
*  Oracle 
*  PostgreSQL
*  Microsoft SQL Server
*  Sybase
*  JDBC 3.0 준수 드라이버를 통한 기타 SQL 준수 데이터베이스

커넥터는 지정된 데이터베이스 및 테이블의 모든 레코드를 검색합니다. 

**JDBC 드라이버**
데이터베이스 커넥터는 Oracle JDBC(Java Database Connectivity) 드라이버 버전 1.5와 함께 제공됩니다. 데이터 크롤러와 함께 제공되는 모든 써드파티 JDBC 드라이버는 데이터 크롤러 설치의 `/lib/java/database` 디렉토리에 있으며, 여기서 사용자는 필요에 따라 이를 추가, 제거하고 수정할 수 있습니다. `crawler.conf` 파일의 `extra_jars_dir` 설정을 사용하여 다른 위치를 지정할 수도 있습니다. 

***DB2 JDBC 드라이버*** 데이터 크롤러는 라이센싱 문제 때문에 DB2용 JDBC와 함께 제공되지 않습니다. 그러나 JDBC 지원이 설치된 모든 DB2 설치에는 DB2 설치를 크롤링할 수 있도록 데이터 크롤러가 요구하는 JAR 파일이 포함되어 있습니다. DB2 인스턴스를 크롤링하려면, 데이터베이스 커넥터가 이를 사용할 수 있도록 데이터 크롤러 설치의 적합한 디렉토리로 이러한 파일을 복사해야 합니다. 

데이터 크롤러를 사용하여 DB2 설치를 크롤링하려면, DB2 설치에서 `db2jcc.jar` 및 라이센스(일반적으로 `db2jcc_license_cu.jar`) JAR 파일을 찾고 해당 파일을 데이터 크롤러 설치 디렉토리의 `lib/java` 서브디렉토리에 복사하십시오. 또는 `crawler.conf` 파일의 `extra_jars_dir` 설정을 사용하여 다른 위치를 지정할 수도 있습니다. 

***MySQL JDBC Drivers***
데이터 크롤러는 제품의 일부로서 제공될 경우에 발생 가능한 라이센싱 문제 때문에 MySQL용 JDBC와 함께 제공되지 않습니다. 그러나 MySQL JDBC 드라이버가 포함된 JAR 파일을 다운로드하고 해당 JAR 파일을 데이터 크롤러 설치에 통합하는 일은 수행하기가 매우 쉽습니다. 

1.	웹 브라우저를 사용하여 MySQL 다운로드 사이트를 방문하고 사용할 아카이브 형식에 대한 소스와 2진 다운로드 링크를 찾으십시오(일반적으로 Microsoft Windows 시스템의 경우는 zip이며, Linux 시스템의 경우는 gzip 처리된 tarball임). 해당 링크를 클릭하여 다운로드 프로세스를 시작하십시오. 등록이 필요할 수도 있습니다.

2.	해당되는 `unzip archive-file-name` 또는 `tar zxf archive-file-name` 명령을 사용하여 다운로드한 아카이브 파일의 유형과 이름을 기반으로 해당 아카이브의 컨텐츠를 추출하십시오. 

3.	아카이브 파일에서 추출된 디렉토리로 변경하고 이 디렉토리의 JAR 파일을 데이터 크롤러 설치 디렉토리의 `lib/java` 서브디렉토리로 복사하십시오. 또는 `crawler.conf` 파일의 `extra_jars_dir` 설정을 사용하여 다른 위치를 지정할 수도 있습니다. 

다음은 데이터베이스 커넥터를 사용하는 데 필요한 기본 구성 옵션입니다. 이러한 값을 설정하려면 `config/connectors/database.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하십시오. 

*  **protocol** - 크롤링에 사용되는 커넥터 프로토콜의 이름입니다. 이 커넥터의 값은 액세스되는 데이터베이스 시스템을 기반으로 합니다. 
*  **collection** - 이 속성은 임시 파일의 압축을 푸는 데 사용됩니다. 
*  **classname** - 커넥터의 Java 클래스 이름입니다. 이 커넥터를 사용하기 위한 값은 `plugin:database.plugin@database`여야 합니다. 
*  **logging-config** - 로깅 옵션을 구성하는 데 사용된 파일을 지정하며, 이는 `log4j` XML 문자열로서 형식화되어야 합니다. 

### CMIS 커넥터 구성
CMIS(Content Management Interoperability Services) 커넥터를 사용하면 Alfresco, Documentum 또는 IBM Content Manager 등의 CMIS 사용 CMS(Content Management System) 저장소를 크롤링할 수 있으며, 이에 포함된 데이터를 색인화할 수 있습니다. 

다음은 CMIS 커넥터를 사용하는 데 필요한 기본 구성 옵션입니다. 이러한 값을 설정하려면 `config/connectors/cmis.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하십시오. 

*  **protocol** - 크롤링에 사용되는 커넥터 프로토콜의 이름입니다. 이 커넥터에는 `cmis`를 사용하십시오. 
*  **collection** - 이 속성은 임시 파일의 압축을 푸는 데 사용됩니다. 
*  **dns** - 사용하지 않는 옵션입니다. 
*  **classname** - 커넥터의 Java 클래스 이름입니다. 이 커넥터를 사용하기 위한 값은 `plugin:cmis-v1.1.plugin@connector`여야 합니다. 
*  **logging-config** - 로깅 옵션을 구성하는 데 사용된 파일을 지정하며, 이는 `log4j` XML 문자열로서 형식화되어야 합니다. 
*  **endpoint** - CMIS 준수 저장소의 서비스 엔드포인트 URL입니다. 예를 들어, SharePoint의 URL 구조는 다음과 같습니다. 
   *  AtomPub 바인딩의 경우:    
      http://<server>:<port>/_vti_bin/cmis/rest?getRepositories
   *  WebServices 바인딩의 경우:    
      http://<server>:<port>/_vti_bin/cmissoapwsdl.aspx

*  **username** - 컨텐츠에 액세스하는 데 사용되는 CMIS 저장소 사용자의 사용자 이름입니다. 이 사용자에게는 크롤링되고 색인화되는 모든 대상 폴더와 문서에 대한 액세스 권한이 있어야 합니다. 
*  **password** - 컨텐츠에 액세스하는 데 사용되는 CMIS 저장소의 비밀번호입니다. 비밀번호는 암호화되지 않아야 하며 평문으로 제공되어야 합니다. 
*  **repositoryid** - 해당 특정 저장소에 대한 컨텐츠에 액세스하는 데 사용되는 CMIS 저장소의 ID입니다. 
*  **bindingtype** - CMIS 저장소에 연결하는 데 사용되는 바인딩의 유형을 식별합니다. 값은 `AtomPub` 또는 `WebServices`입니다. 
*  **authentication** - CMIS 호환 가능 저장소에 접속 중인 동안에 사용할 인증 메커니즘의 유형을 식별합니다(`기본 HTTP 인증`, `NTLM` 또는 `WS-Security(사용자 이름 토큰)`).
*  **enable-acl** - 크롤링된 데이터에 대한 ACL 검색을 사용합니다. 이 콜렉션의 문서에 대한 보안이 염려되지 않는 경우, 이 옵션을 사용하지 않으면 문서와 함께 이 정보를 요청하지 않고 이 정보를 검색 및 인코딩하지 않음으로써 성능이 향상됩니다. 값은 `true` 또는 `false`입니다.
*  **user-agent** - 문서를 크롤링할 때 서버에 전송된 헤더입니다. 
*  **method** - 매개변수가 전달될 메소드(`GET` 또는 `POST`)입니다. 
*  **url-logging** - 크롤링된 URL이 로깅되는 범위입니다. 가능한 값은 다음과 같습니다. 

   *  ***full-logging*** - URL에 대한 모든 정보를 로깅합니다. 
   *  ***refined-logging*** - 크롤러 로그를 찾아보고 커넥터가 올바르게 작동하는 데 필요한 정보만 로깅합니다. 이는 기본값입니다. 
   *  ***minimal-logging*** - 커넥터가 올바르게 작동하는 데 필요한 최소 정보량만 로깅합니다. 

   이 옵션을 최소 로깅으로 설정하면 로그의 크기가 감소되며, 로깅되는 데이터 양의 최소화와 연관되어 I/O가 감소되므로 약간의 성능 향상이 예상됩니다. 
*  **ssl-version** - HTTPS 연결에 사용할 SSL의 버전을 지정합니다. 기본적으로, 사용 가능한 가장 강력한 프로토콜이 사용됩니다. 

### SMB/CIFS/Samba 커넥터 구성
Samba 커넥터를 사용하면 SMB(Server Message Block) 및 CIFS(Common Internet Filesystem) 파일 공유를 크롤링할 수 있습니다. 이러한 유형의 파일 공유는 Windows 네트워크에서 일반적이며, 오픈 소스 프로젝트 [Samba](https://www.samba.org/)를 통해서도 제공됩니다. 

다음은 Samba 커넥터를 사용하는 데 필요한 기본 구성 옵션입니다. 이러한 값을 설정하려면 `config/connectors/samba.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하십시오. 

*  **protocol** - 크롤링에 사용되는 커넥터 프로토콜의 이름입니다. 이 커넥터를 사용하기 위한 값은 `smb`입니다. 
*  **collection** - 이 속성은 임시 파일의 압축을 푸는 데 사용됩니다. 
*  **classname** - 커넥터의 Java 클래스 이름입니다. 이 커넥터를 사용하기 위한 값은 `plugin:smb.plugin@connector`여야 합니다. 
*  **logging-config** - 로깅 옵션을 구성하는 데 사용된 파일을 지정하며, 이는 `log4j` XML 문자열로서 형식화되어야 합니다. 
*  **username** - 인증할 Samba 사용자 이름입니다. 이를 제공하는 경우, 도메인 및 비밀번호도 제공해야 합니다. 이를 제공하지 않는 경우, 게스트 계정이 사용됩니다. 
*  **password** - 인증할 Samba 비밀번호입니다. 사용자 이름이 제공되는 경우, 이는 필수입니다. 비밀번호는 데이터 크롤러와 함께 제공되는 VCrypt 라이브러리를 사용하여 암호화되어야 합니다. 
*  **archive** - Samba 커넥터를 사용하여 아카이브 파일 내에 압축된 파일을 크롤링하고 색인화합니다. 값은 `true` 또는 `false`이며, 기본값은 `false`입니다. 
*  **max-policies-per-handle** - 단일 RPC 핸들에 대해 열릴 수 있는 LSA(Local Security Authority) 정책의 최대 수를 지정합니다. 이러한 정책은 다양한 조건 하에서 특정 시스템을 조회하거나 수정하는 데 필요한 액세스 권한을 정의합니다. 이 옵션의 기본값은 `255`입니다. 
*  **crawl-fs-metadata** - 이 옵션을 켜는 경우에는 데이터 크롤러가 파일에 대한 사용 가능한 파일 시스템 메타데이터(작성 날짜, 마지막 수정 날짜, 파일 속성 등)가 포함된 VXML 문서를 추가하게 됩니다. 
*  **enable-arc-connector** - 사용하지 않는 옵션입니다. 
*  **disable-indexes** - 사용하지 않을 색인의 줄 바꾸기로 분리된 목록이며, 이에 따라 크롤링이 보다 빨라질 수 있습니다. 예를 들면, 다음과 같습니다. 

   *  disable-url-index
   *  disable-error-state-index
   *  disable-crawl-time-index
*  **exact-duplicates-hash-size** - 완전 중복을 분석하는 데 사용되는 해시 테이블의 크기를 설정합니다. 이 숫자를 수정할 때는 매우 신중해야 합니다. 선택하는 값은 소수여야 합니다. 크기가 더 크면 보다 빠른 검색을 제공할 수 있지만 추가 메모리가 요구되는 한편, 크기가 더 작으면 크롤링을 늦출 수 있지만 메모리 사용량이 현저히 감소됩니다. 
*  **user-agent** - 사용하지 않는 옵션입니다. 
*  **timeout** - 사용하지 않는 옵션입니다. 
*  **n-concurrent-requests** - 단일 IP 주소에 병렬로 전송될 요청의 수입니다. 기본값은 `1`입니다. 
*  **enqueue-persistence** - 사용하지 않는 옵션입니다. 

### SharePoint 커넥터 구성
SharePoint 커넥터를 사용하면 SharePoint 서버 및 SharePoint Online 오브젝트를 크롤링하고 이에 포함된 정보를 색인화할 수 있습니다. 문서, 사용자 프로파일, 사이트 콜렉션, 블로그, 목록 항목, 멤버십 목록, 디렉토리 페이지 등의 오브젝트는 이와 연관된 메타데이터로 색인화될 수 있습니다. 목록 항목 및 문서의 경우, 색인에는 첨부 파일이 포함될 수 있습니다. 

**참고**: 특정 유형(블로그, 문서, 사용자 프로파일 등)과는 무관하게, SharePoint 커넥터는 모든 SharePoint 오브젝트의 `noindex` 속성을 준수합니다. 단일 문서가 각각의 결과에 대해 리턴됩니다. 

**중요사항**: SharePoint 사이트를 크롤링하는 데 사용되는 SharePoint 계정에는 최소한 전체 읽기 액세스 권한이 있어야 합니다. 

다음은 SharePoint 커넥터를 사용하는 데 필요한 기본 구성 옵션입니다. 이러한 값을 설정하려면 `config/connectors/sharepoint.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하십시오. 

*  **protocol** - 크롤링에 사용되는 커넥터 프로토콜의 이름입니다. 이 커넥터에는 `io-sp`를 사용하십시오. 
*  **collection** - 이 속성은 임시 파일의 압축을 푸는 데 사용됩니다. 
*  **classname** - 커넥터의 Java 클래스 이름입니다. 이 커넥터를 사용하기 위한 값은 `plugin:io-sharepoint.plugin@connector`여야 합니다. 
*  **logging-config** - 로깅 옵션을 구성하는 데 사용된 파일을 지정하며, 이는 `log4j` XML 문자열로서 형식화되어야 합니다. 
*  **seed-url-type** - 제공된 시드 URL이 지시하는 SharePoint 오브젝트의 유형(사이트 콜렉션 또는 웹 애플리케이션(가상 서버라도고 함))을 식별합니다. 

   *  ***사이트 콜렉션*** - 시드 URL 유형이 `Site Collections`로 설정된 경우에는 URL에서 참조하는 사이트 콜렉션의 하위만 크롤링됩니다. 
   *  ***웹 애플리케이션*** - 시드 URL 유형이 `Web Applications`로 설정된 경우에는 각 URL에서 참조하는 웹 애플리케이션에 속하는 모든 사이트 콜렉션(및 해당 하위)이 크롤링됩니다. 
*  **auth-type** - SharePoint 서버에 접속 중일 때 사용할 인증 메커니즘: `BASIC`, `NTLM2`, `KERBEROS` 또는 `CBA`. 기본 인증 유형은 `NTLM2`입니다. 
*  **spUser** - 컨텐츠에 액세스하는 데 사용되는 SharePoint 사용자의 사용자 이름입니다. 이 사용자는 크롤링되고 색인화되는 모든 대상 사이트와 목록에 대한 액세스 권한을 보유해야 하며, 연관된 권한을 검색하고 분석할 수 있어야 합니다. `MYDOMAIN\\Administrator`와 같이 도메인 이름으로 이를 입력하도록 권장합니다. 
*  **spPassword** - 컨텐츠에 액세스하는 데 사용되는 SharePoint 사용자의 비밀번호입니다. 비밀번호는 Data Crawler와 함께 제공되는 vcrypt 프로그램을 사용하여 암호화되어야 합니다. 
*  **cba-sts** - 크롤링 사용자의 인증을 시도하기 위한 STS(Security Token Service) 엔드포인트에 대한 URL입니다. ADFS의 SharePoint 사내 구축형의 경우, 이는 사용자의 ADFS 엔드포인트여야 합니다. 인증 유형이 `CBA`(Claims Based Authentication)로 설정된 경우, 이 필드는 필수입니다. 
*  **cba-realm** - STS에서 보안 토큰을 요청할 때 사용할 Relying Party Trust ID입니다. 이는 종종 "AppliesTo" 값 또는 "Realm"으로 알려져 있습니다. SharePoint Online의 경우, 이는 SharePoint Online 인스턴스의 루트에 대한 URL이어야 합니다(예: `https://mycompany.sharepoint.com`). ADFS의 경우, 이는 SharePoint 및 ADFS 간의 Relying Party Trust에 대한 ID 값입니다(예: `"urn:SHAREPOINT:adfs"`).
*  **everyone-group** - 이를 지정한 경우, 이 그룹 이름은 모든 사용자에게 액세스 권한이 부여되어야 할 때 ACL에서 사용됩니다. 이 필드는 사용자 프로파일의 크롤링이 사용될 때 필요합니다. **참고** - 보안은 아직 검색 및 순위 지정 서비스에 의해 준수되지 않습니다. 
*  **user-profile-master-url** - 커넥터가 사용자 프로파일에 대한 링크를 빌드하는 데 사용하는 기본 URL입니다. 이는 사용자 프로파일에 대한 표시 양식을 지시하도록 구성되어야 합니다. `%FIRST_SEED%` 토큰이 발견된 경우, 이는 첫 번째 시드 URL로 대체됩니다. 사용자 프로파일의 크롤링을 사용할 때 필요합니다. 
*  **urls** - 크롤링할 사이트 콜렉션 또는 SharePoint 웹 애플리케이션의 HTTP URL의 줄 바꾸기로 분리된 목록입니다. 
*  **ehcache-config** - 사용하지 않는 옵션입니다. 
*  **method** - 매개변수가 전달될 메소드(`GET` 또는 `POST`)입니다. 
*  **cache-types** - 사용하지 않는 옵션입니다. 
*  **cache-size** - 사용하지 않는 옵션입니다. 
*  **enable-acl** - SharePoint 사용자 프로파일의 크롤링을 사용하며, 값은 `true` 또는 `false`입니다. 기본값은 `false`입니다.

### Box 커넥터 구성
Box 커넥터를 사용하면 엔터프라이즈 Box 인스턴스를 크롤링하고 이에 포함된 정보를 색인화할 수 있습니다. 다음은 Box 커넥터를 사용하는 데 필요한 기본 구성 옵션입니다. 이러한 값을 설정하려면 `config/connectors/box.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하십시오. 

*  **protocol** - 크롤링에 사용되는 커넥터 프로토콜의 이름입니다. 이 커넥터에는 `box`를 사용하십시오. 
*  **classname** - 커넥터의 Java 클래스 이름입니다. 이 커넥터를 사용하기 위한 값은 `plugin:box.plugin@connector`여야 합니다. 
*  **logging-config** - 로깅 옵션을 구성하는 데 사용된 파일을 지정하며, 이는 `log4j` XML 문자열로서 형식화되어야 합니다. 
*  **box-crawl-seed-url** - Box의 기본 URL입니다. 이 커넥터의 값은 `box://app.box.com/`입니다. 다양한 유형의 URL을 크롤링할 수 있습니다. 예를 들면, 다음과 같습니다. 

   *  ***전체 엔터프라이즈의 크롤링***: `box://app.box.com/`
   *  ***특정 폴더의 크롤링***: `box://app.box.com/user/USER_ID/folder/FOLDER_ID/FolderName`
   *  ***특정 사용자의 크롤링***: `box://app.box.com/user/USER_ID/`
*  **client-id** - Box 애플리케이션 작성 시에 Box에 의해 제공된 클라이언트 ID를 입력하십시오. 
*  **client-secret** - Box 애플리케이션 작성 시에 Box에 의해 제공된 클라이언트 시크릿을 입력하십시오. 
*  **path-to-private-key** - 이는 로컬 파일 시스템에서 Box와의 통신을 위해 생성된 개인-공개 키 쌍의 일부인 개인 키의 위치입니다. 
*  **kid** - 공개 키 ID를 지정합니다. 이는 Box와의 통신을 위해 생성된 개인-공개 키 쌍의 다른 반쪽입니다. 
*  **enterprise-id** - 애플리케이션이 권한 부여된 엔터프라이즈입니다. 엔터프라이즈 ID는 Box 관리자 콘솔의 기본 페이지에 나열되어 있습니다. 
*  **enable-acl** - 내부 전용입니다. 크롤링된 데이터에 대한 ACL 검색을 사용합니다. 
*  **user-agent** - 문서를 크롤링할 때 서버에 전송된 헤더입니다. 
*  **method** - 매개변수가 전달될 메소드(`GET` 또는 `POST`)입니다. 
*  **url-logging** - 크롤링된 URL이 로깅되는 범위입니다. 가능한 값은 다음과 같습니다. 

   *  ***full-logging*** - URL에 대한 모든 정보를 로깅합니다. 
   *  ***refined-logging*** - 크롤러 로그를 찾아보고 커넥터가 올바르게 작동하는 데 필요한 정보만 로깅합니다. 이는 기본값입니다. 
   *  ***minimal-logging*** - 커넥터가 올바르게 작동하는 데 필요한 최소 정보량만 로깅합니다. 

   이 옵션을 최소 로깅으로 설정하면 로그의 크기가 감소되며, 로깅되는 데이터 양의 최소화와 연관되어 I/O가 감소되므로 약간의 성능 향상이 예상됩니다. 
*  **ssl-version** - HTTPS 연결에 사용할 SSL의 버전을 지정합니다. 기본적으로, 사용 가능한 가장 강력한 프로토콜이 사용됩니다. 

Box 커넥터에는 일부 제한사항이 있습니다. 

* 파일의 태스크 또는 주석은 검색되지 않습니다. 
* 참고 컨텐츠 본문은 JSON으로 검색됩니다. 참고 데이터의 추가 변환이 필요할 수 있습니다. 
* 개별 문서는 TestIt을 통해 검색될 수 없습니다. 시드 URL, 폴더 URL 및 사용자 URL만 TestIt을 통해 검색이 가능합니다. 


## 관련 항목

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-seed.conf(5)

orchestration_service.conf(5)
