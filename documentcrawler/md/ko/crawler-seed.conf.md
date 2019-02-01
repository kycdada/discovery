# 크롤링 시드 구성

시드는 크롤링의 시작점이며, 해당 시드로 식별된 자원에서 데이터를 검색하기 위해 데이터 크롤러에 의해 사용됩니다. 일반적으로, 시드는 다양한 웹 프로토콜에 의해 액세스 가능한 프로토콜 기반 자원(예: 파일 공유, SMB 공유, 데이터베이스 및 기타 데이터 저장소)에 액세스하기 위한 URL을 구성합니다. 게다가 서로 다른 시드 URL에는 서로 다른 기능이 있습니다. 

또한 시드는 CRM(Customer Relationship Management) 시스템, PLC(Product Life Cycle) 시스템, CMS(Content Management Systems), 클라우드 기반 애플리케이션 및 웹 데이터베이스 애플리케이션 등의 특정 써드파티 애플리케이션의 크롤링을 사용할 수 있도록 저장소에 특정할 수도 있습니다. 

현재 데이터 크롤러는 다음 저장소 유형에 대해 파일 커넥터를 지원하는 크롤링 시드를 제공합니다. 

*	파일 시스템
*	JDBC를 통한 데이터베이스
*	CMIS(Content Management Interoperability Services)
*	SMB(Server Message Block), CIFS(Common Internet Filesystem) 또는 Samba 파일 공유
*	SharePoint 및 SharePoint Online
*	Box

사용자 정의 커넥터에 대한 크롤링 시드의 사용자 정의를 허용하는 크롤링 시드 구성 템플리트도 제공됩니다. 

## 시작하기:

데이터 저장소를 크롤링하는 경우, 크롤러는 사용자 지정된 시드 URL에서 시작하며 정보 페이지의 다운로드를 시작합니다. 또한 크롤러는 다운로드된 페이지의 링크를 찾고 추가 크롤링을 위해 새로 검색된 페이지를 스케줄링합니다. 

구성 정보는 크롤링이 필요한 페이지와 이를 크롤링하는 방법을 판별하는 데 사용됩니다. 이 파일에서는 각 커넥터의 크롤링 시드 파일에 대해 구성할 수 있는 옵션을 설명합니다. 

**참고**: 각각의 크롤링 시드 구성 파일은 대응되는 파일 커넥터 구성 파일과 함께 작동됩니다. 파일 커넥터 옵션은 별도로 설명되어 있습니다. 

### 파일 시스템 크롤링 시드 구성

다음 값을 파일 시스템 크롤링 시드 파일에 대해 구성할 수 있습니다. 이러한 값을 설정하려면 `config/seeds/filesystem-seed.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 지정하십시오. 

*  **url** - 크롤링할 파일과 폴더의 줄 바꾸기로 분리된 목록입니다. UNIX 사용자는 `/usr/local/` 등의 경로를 사용할 수 있습니다.
URL은 `sdk-fs://`로 시작해야 합니다. 따라서 예를 들어 `/home/watson/mydocs`를 크롤링하기 위한 이 URL의 값은 `sdk-fs:///home/watson/mydocs`일 수 있습니다. 세 번째 `/`는 반드시 필요합니다!
**참고**: 파일 시스템 커넥터는 사용자 정의 프로토콜 `sdk-fs://`를 사용하여 유효한 URL을 작성합니다. 나열된 경로의 맨 앞에 `file://`을 추가하지 마십시오. URL은 `sdk-fs://`로 시작해야 합니다. 
*  **hops** - 내부 전용입니다. 
*  **default-allow** - 내부 전용입니다. 

### 데이터베이스 크롤링 시드 구성

다음 값을 데이터베이스 크롤링 시드 파일에 대해 구성할 수 있습니다. 이러한 값을 설정하려면 `config/seeds/database-seed.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 지정하십시오. 

*  **url** - 검색할 테이블 또는 뷰의 URL입니다. 사용자 정의 SQL 데이터베이스 시드 URL을 정의합니다. 구조는 다음과 같습니다.

   	`database-system://host:port/database?[per=num]&[sql=SQL]`

   시드 URL을 테스트하면 인큐된 모든 URL이 표시됩니다. 예를 들어, 200개의 레코드가 포함된 데이터베이스에 대해 다음 URL을 테스트합니다. 

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=100&sql=select%20*%20from%20vessel&`

   그러면 인큐된 다음 URL이 표시됩니다.

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=0&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=100&`

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?key-val=200&`

   테스트 중에 다음 URL은 행 43에서 검색된 데이터를 표시합니다. 

   	`sqlserver://test.mycompany.com:1433/WWII_Navy/?per=1&key-val=43`
*  **hops** - 내부 전용입니다. 
*  **default-allow** - 내부 전용입니다. 
*  **user-password** - 데이터베이스 시스템의 신임 정보입니다. 사용자 이름과 비밀번호는 `:`으로 분리되어야 하며, 비밀번호는 Data Crawler와 함께 제공되는 vcrypt 프로그램으로 암호화되어야 합니다. 예: `username:[[vcrypt/3]]passwordstring`.
*  **max-data-size** - 문서에 대한 데이터의 최대 크기입니다. 이는 한 번에 로드되는 가장 큰 메모리 블록입니다. 컴퓨터에 충분한 메모리가 있는 경우에만 이 한계를 늘리십시오. 
*  **filter-exact-duplicates** - 내부 전용입니다. 
*  **jdbc-class**(익스텐더 옵션) - 이를 지정하는 경우, 이 문자열은 `(other)`가 데이터베이스 시스템으로 선택될 때 커넥터에 의해 사용되는 JDBC 클래스를 대체합니다. 
*  **connection-string**(익스텐더 옵션) - 이를 지정하는 경우, 이 문자열은 자동 생성된 JDBC 연결 문자열을 대체합니다. 이를 사용하면 데이터베이스 연결에 대한 보다 자세한 구성을 제공할 수 있습니다(예: 로드 밸런싱 또는 SSL 연결). 예: `jdbc:netezza://127.0.0.1:5480/databasename`.
*  **save-frequency-for-resume**(익스텐더 옵션) - 크롤링의 재개나 부분 새로 고치기를 수행할 수 있도록 열 또는 연관된 레이블의 이름을 지정합니다. 시드는 크롤링을 진행하면서 일정한 간격으로 이 열의 이름을 저장하며, 일단 데이터베이스의 마지막 행이 크롤링되면 이를 다시 저장합니다. 크롤링을 재개하거나 이를 새로 고치는 경우, 크롤링은 이 필드에 대해 저장된 값에서 식별된 행에서 시작합니다. 

### CMIS 크롤링 시드 구성

다음 값을 CMIS 크롤링 시드 파일에 대해 구성할 수 있습니다. 이러한 값을 설정하려면 `config/seeds/cmis-seed.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하십시오. 

*  **url** - 크롤링의 시작점으로 사용되는 CMIS 저장소의 폴더 또는 URL입니다. 예를 들면, 다음과 같습니다. 

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=workspace://SpacesStore/guid`
   루트 폴더에서 크롤링하려면 다음과 같이 URL을 제공해야 합니다. 

   *  `cmis://alfresco.test.com:8080/alfresco/cmisatom?folderToProcess=`
*  **at** - 사용하지 않는 옵션입니다. 
*  **default-allow** - 내부 전용입니다. 

### Samba 크롤링 시드 구성

다음 값을 Samba 크롤링 시드 파일에 대해 구성할 수 있습니다. 이러한 값을 설정하려면 `config/seeds/samba-seed.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하십시오. 

*  **url** - 크롤링할 공유의 줄 바꾸기로 분리된 목록입니다. 예를 들면, 다음과 같습니다. 

   *  `smb://share.test.com/office`
   *  `smb://share.test.com/cash/money/change`
   *  `smb://share.test.com/C$/Program Files`

*  **hops** - 내부 전용입니다. 
*  **default-allow** - 내부 전용입니다. 

### SharePoint 크롤링 시드 구성

다음의 추가적인 값을 SharePoint 크롤링 시드 파일에 대해 구성할 수 있습니다. 이러한 값을 설정하려면 `config/seeds/sharepoint-seed.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 수정하십시오. 

*  **url** - 크롤링할 SharePoint 웹 애플리케이션 또는 사이트 콜렉션의 줄 바꾸기로 분리된 목록입니다. 예를 들면, 다음과 같습니다. 

   *  `io-sp://a.com`
   *  `io-sp://b.com:83/site`
   *  `io-sp://c.com/site2`

   이 사이트의 하위 사이트도 크롤링됩니다(다른 크롤링 규칙에서 이를 제외한 경우가 아니면). 
*  **filter-url** - 크롤링할 SharePoint 웹 애플리케이션 또는 사이트 콜렉션의 줄 바꾸기로 분리된 목록입니다. 예를 들면, 다음과 같습니다. 

   *  `http://a.com`
   *  `http://b.com:83/site`
   *  `http://c.com/site2`

*  **hops** - 내부 전용입니다. 
*  **n-concurrent-requests** - 내부 전용입니다. 
*  **delay** - 내부 전용입니다. 
*  **default-allow** - 내부 전용입니다. 
*  **seed-protocol** - 사이트 콜렉션의 하위에 대한 시드 프로토콜을 설정합니다. 사이트 콜렉션의 프로토콜이 SSL, HTTP 또는 HTTPS일 때 필요합니다. 이 값은 사이트 콜렉션의 프로토콜과 동일하게 설정되어야 합니다. 

### Box 시드 구성

다음 값을 Box 크롤링 시드 파일에 대해 구성할 수 있습니다. 이러한 값을 설정하려면 `config/seeds/box-seed.conf` 파일을 열고 사용자의 유스 케이스에 특정한 다음 값을 지정하십시오. 

*  **url** - 크롤링의 시작점으로 사용될 URL입니다. 기본값은 `box://app.box.com/`입니다. 
*  **default-allow** - 내부 전용입니다. 

## 관련 항목

crawler(1)

vcrypt(1)

crawler.conf(5)

crawler-options.conf(5)

orchestration_service.conf(5)
