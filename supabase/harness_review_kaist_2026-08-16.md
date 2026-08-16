# KAIST 장학금 하네스 수집 리뷰 — 2026-08-16

## 목록 수집 결과 (원칙 1 — "다 봤는지"를 코드가 대조한 결과)
- 신소재공학과 공지사항(장학 공고 포함): 수집 109건 / 게시판 표시 파싱 안 됨건 — OK

이름+기관 유사도로 스킵된 기존 중복: 0건 · 신규 처리: 33건

## 신규 장학금 33건 (플래그된 필드 총 26개)

### 2026 삼성전자 MX사업부 Tech & Career 세미나
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=389264
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 플렉셀스페이스(주) 채용(~9/31)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=389250
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### [동원그룹] 2026 동원그룹 Open House로 여러분을 초대합니다! (08.25~26)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=389260
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 신세계그룹 '리테일 All-in-One 교육 과정 2기' 교육생 모집
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=389245
- ⚠️ 확인 필요 필드 5개:
  - `amount` = `500000` — dual_extract_mismatch(2차 추출값=None) (인용: '교육비 전액(중식 포함), 교육지원금(50만원/월) 등 학습에 집중할 수 있는 환경 제공')
  - `min_age` = `15` — quote_not_found (인용: '만 15세 ~ 34세 이하 미취업 청년')
  - `max_age` = `34` — quote_not_found (인용: '만 15세 ~ 34세 이하 미취업 청년')
  - `application_deadline` = `'2026-08-18'` — quote_not_found (인용: '모집기간 : [2기] 2026.06.18(목) ~ 2026.08.18.(화), 17시까지')
  - `application_period` = `'[2기] 2026.06.18(목) ~ 2026.08.18.(화), 17시까지'` — quote_not_found (인용: '모집기간 : [2기] 2026.06.18(목) ~ 2026.08.18.(화), 17시까지')
- 확인된 근거 (원문 인용):
  - `name` = `"신세계그룹 '리테일 All-in-One 교육 과정 2기' 교육생 모집"` ← "신세계그룹 '리테일 All-in-One 교육 과정 2기' 교육생 모집 안내 (~8/18)"
  - `provider` = `'신세계그룹'` ← "[신세계그룹] 리테일 All-in-One 교육 과정 2기 모집"
  - `description` = `'교육부터 취업까지, 상위 5% 채용. 신세계그룹과 함께하는 리테일 All-in-One 교육 과정 모집. 오프라인 리테일, F&B, 호텔·서비스, 리테일테크까지 다양한 산업 영역을 한 과정에서 경험할 수 있음. 교육혜택: 1. 우수 교육생 채용 연계 - 상위 5% 채용, 차상위 10% 서류전형 면제(이마트, 조선호텔앤리조트, 신세계푸드, 신세계아이앤씨) 2. 교육비 전액 지원 및 교육지원금 지급 - 교육비 전액(중식 포함), 교육지원금(50만원/월) 3. 체계적인 취업 지원 프로그램 운영 - 합숙 취업캠프, 진로 멘토링, 기업 설명회 등. 교육기간: [2기] 2026.09.09(수) ~ 2026.12.02.(수). 교육장소: 천안(서북구), 대전(서구), 대구(동구), 부산(금정구, 해운대구), 광주(남구)'` ← "교육부터 취업까지, 상위 5% 채용 신세계그룹과 함께하는 리테일 All-in-One 교육 과정 모집"
  - `application_url` = `'https://futurendreamacademy.com/'` ← "모집 홈페이지 : https://futurendreamacademy.com/"
  - `category_l1` = `'support_fund'` ← "교육비 전액 지원 및 교육지원금 지급"
  - `category_l2` = `'activity_participation_support'` ← "체계적인 취업 지원 프로그램 운영"

### 박사학위 청구논문 심사 (Guide to the evaluation of Ph. D. Dissertation.)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=389060
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 박사졸업논문 최소요건(Minimum requirements for doctoral thesis)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=389062
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)
- 확인된 근거 (원문 인용):
  - `affiliated_institution` = `'신소재공학과 박사과정'` ← "박사 졸업논문 요건"
  - `eligible_university` = `'KAIST'` ← "Korea Advanced Institute of Science and Technology (KAIST) 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea, KAIST"
  - `eligible_college` = `'신소재공학과'` ← "Department of Materials Science and Engineering"
  - `required_enrollment_status` = `'post_undergrad'` ← "박사 졸업논문 요건"
  - `required_degree_level` = `'doctoral'` ← "박사 졸업논문 요건"

### 박사과정 자격시험 세부규정(Detailed Regulations for the Ph.D. Qualifying Examination)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=389061
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)
- 확인된 근거 (원문 인용):
  - `affiliated_institution` = `'신소재공학과 박사과정'` ← "2020년이후 박사과정 입학생은 입학 후 1년이내 최초 응시해야 함."
  - `eligible_university` = `'KAIST'` ← "Korea Advanced Institute of Science and Technology (KAIST)"
  - `eligible_college` = `'신소재공학과'` ← "박사과정 자격시험 세부규정"
  - `required_enrollment_status` = `'post_undergrad'` ← "2020년이후 박사과정 입학생은 입학 후 1년이내 최초 응시해야 함."
  - `required_degree_level` = `'doctoral'` ← "2020년이후 박사과정 입학생은 입학 후 1년이내 최초 응시해야 함."

### 박사학위 예비심사 (프로포잘) 신청(Apply for a doctoral degree proposal)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=389059
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)
- 확인된 근거 (원문 인용):
  - `eligible_university` = `'KAIST'` ← "Korea Advanced Institute of Science and Technology (KAIST)"
  - `required_enrollment_status` = `'post_undergrad'` ← "박사학위 예비심사 (프로포잘) 신청(Apply for a doctoral degree proposal)"
  - `required_degree_level` = `'doctoral'` ← "ㅇ 박사 Proposal 절차 ( 입학후 2 년이내 , 심사경과시 심사지연경위서 제출 )"

### 대학원과정 이수요건 Course Requirements of Graduate
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=389058
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### Merck International Graduate Fellowship - 2027년 장학생 모집
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=388949
- ⚠️ 확인 필요 필드 4개:
  - `description` = `'분야는 총 두가지로 Next Generation Biology와 Sustainability이며, 각 분야별 2명을 모집하여 정원이 작년에 비해 2배로 확대되었습니다. 저년차 대상으로 모집하여 성과중심이 아닌 잠재력 위주로 평가하여 장학생을 선발할 예정이라고 합니다. 선정된 연구자는 최대 3년간 매년 €16,000(최대 한화 8,300만원 상당)의 장학금을 받을 수 있습니다.'` — quote_not_found (인용: '분야는 총 두가지로 Next Generation Biology와 Sustainability이며, 각 분야별 2명을 모집하여 정원이 작년에 비해 2배로 확대되었습니다. 저년차 대상으로 모집하여 성과중심이 아닌 잠재력 위주로 평가하여 장학생을 선발할 예정이라고 합니다. 선정된 연구자는 최대 3년간 매년 €16,000 (최대 한화 8,300만원 상당)의 장학금을 받을 수 있습니다.')
  - `amount` = `None` — dual_extract_mismatch(2차 추출값=8300) (인용: '')
  - `application_deadline` = `None` — dual_extract_mismatch(2차 추출값='2027-07-20') (인용: '')
  - `major` = `None` — value_missing_but_quoted (인용: '학과제한은 따로 없으며')
- 확인된 근거 (원문 인용):
  - `name` = `'Merck International Graduate Fellowship - 2027년 장학생 모집'` ← "Merck International Graduate Fellowship - 2027년 장학생 모집"
  - `provider` = `'Merck'` ← "카이스트 대학원생 장학금 모집을 오픈하여 신소재공학과 구성원분들께 홍보를 부탁드리고자 합니다"
  - `grade_level` = `'저년차 대상으로 모집'` ← "저년차 대상으로 모집하여 성과중심이 아닌 잠재력 위주로 평가하여 장학생을 선발할 예정이라고 합니다."
  - `headcount` = `'각 분야별 2명 (총 4명)'` ← "각 분야별 2명을 모집하여 정원이 작년에 비해 2배로 확대되었습니다."
  - `application_period` = `'지원 기한은 7월 20일까지'` ← "지원 기한은 7월 20일까지 이며, 자세한 일정은 첨부 드리는 포스터를 참고 부탁드립니다."
  - `required_enrollment_status` = `'post_undergrad'` ← "카이스트 대학원생 장학금 모집을 오픈하여 신소재공학과 구성원분들께 홍보를 부탁드리고자 합니다"
  - `category_l1` = `'school_external'` ← "카이스트 대학원생 장학금 모집을 오픈하여 신소재공학과 구성원분들께 홍보를 부탁드리고자 합니다"
  - `category_l2` = `'private_foundation'` ← "Merck International Graduate Fellowship - 2027년 장학생 모집"

### 신소재공학과 학부 교과목 이수체계 (MSE Curriculum Structure for Undergraduates)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=386090
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 신소재공학과 시설안전및화재예방 등을 위한 CCTV 설치 안내
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=385374
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 2026년 미원상사 두명장학생(추가) 선발
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=389230
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)
- 확인된 근거 (원문 인용):
  - `name` = `'2026년 미원상사 두명장학생(추가) 선발'` ← "2026년 미원상사 두명장학생(추가) 선발 공고문"
  - `provider` = `'미원상사'` ← "2026년 미원상사 두명장학생(추가) 선발 공고문"
  - `affiliated_institution` = `'신소재공학과'` ← "(신소재공학과) 붙임1. 2026년 미원상사 두명장학생 선발 공고문_추가"
  - `eligible_university` = `'KAIST'` ← "Department of Materials Science and Engineering Korea Advanced Institute of Science and Technology (KAIST)"
  - `category_l1` = `'school_external'` ← "2026년 미원상사 두명장학생(추가) 선발 공고문"
  - `category_l2` = `'private_foundation'` ← "2026년 미원상사 두명장학생(추가) 선발 공고문"

### KAIST-EPSD 장학생 (삼성디스플레이)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=389009
- ⚠️ 확인 필요 필드 1개:
  - `admission_track` = `'general'` — no_quote (인용: '')
- 확인된 근거 (원문 인용):
  - `name` = `'KAIST-EPSD 장학생 (삼성디스플레이)'` ← "[삼성디스플레이] KAIST-EPSD 장학생 모집 안내 (지원마감: 7/8(수) 17:30)"
  - `provider` = `'삼성디스플레이'` ← "삼성디스플레이는 세계 최고 수준의 디스플레이 기술을 선도하고, 차세대 디스플레이 원천기술 확보에 기여할 우수 인재를 양성하기 위해 국내 우수 대학인 KAIST와 협력하여 산학교육 프로그램을 운영하고 있습니다"
  - `description` = `'삼성디스플레이 인재양성 프로그램(EPSD)으로, KAIST와 협력하여 산학교육 프로그램을 운영하며 학부 기졸업자 및 졸업예정자를 대상으로 장학생을 모집함'` ← "* EPSD (Educational Program for Samsung Display) : 삼성디스플레이 인재양성 프로그램"
  - `application_url` = `'https://epsd.kaist.ac.kr/'` ← "- 지원서 접수 바로가기 : https://epsd.kaist.ac.kr/"
  - `application_deadline` = `'2026-07-08'` ← "- 2026. 6. 29(금) 10:00 ~ 7.8(수) 17:30"
  - `grade_level` = `'학부 기졸업자, 2027년 2월 졸업 예정자'` ← "- 학부 기졸업자
- 2027년 2월 졸업 예정자"
  - `application_period` = `'2026. 6. 29(금) 10:00 ~ 7.8(수) 17:30'` ← "- 2026. 6. 29(금) 10:00 ~ 7.8(수) 17:30"
  - `eligible_university` = `'KAIST'` ← "국내 우수 대학인 KAIST와 협력하여 산학교육 프로그램을 운영하고 있습니다"
  - `required_enrollment_status` = `'post_undergrad'` ← "- 학부 기졸업자
- 2027년 2월 졸업 예정자"
  - `category_l1` = `'school_external'` ← "삼성디스플레이는 세계 최고 수준의 디스플레이 기술을 선도하고, 차세대 디스플레이 원천기술 확보에 기여할 우수 인재를 양성하기 위해 국내 우수 대학인 KAIST와 협력하여 산학교육 프로그램을 운영하고 있습니다"
  - `category_l2` = `'private_foundation'` ← "삼성디스플레이는 세계 최고 수준의 디스플레이 기술을 선도하고, 차세대 디스플레이 원천기술 확보에 기여할 우수 인재를 양성하기 위해 국내 우수 대학인 KAIST와 협력하여 산학교육 프로그램을 운영하고 있습니다"

### 삼성디스플레이 KAIST-EPSD 장학생 구분변경 신청
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=389006
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)
- 확인된 근거 (원문 인용):
  - `name` = `'삼성디스플레이 KAIST-EPSD 장학생 구분변경 신청'` ← "2026년 하반기 삼성디스플레이 KAIST-EPSD 장학생 구분변경 신청을 아래와 같이 안내드립니다"
  - `provider` = `'삼성디스플레이'` ← "삼성디스플레이는 세계 최고 수준의 디스플레이 기술을 선도하고 차세대 디스플레이 원천기술 확보에 기여할 수 있는 우수 인재를 양성하기 위해 국내 우수 대학과와 협력하여 산학교육 프로그램을 운영하고 있습니다"
  - `description` = `"삼성디스플레이 KAIST-EPSD(Educational Program for Samsung Display, 삼성디스플레이 인재양성 프로그램) 장학생의 구분변경 신청 안내. 학교 산학프로그램 사무국에서 발송한 'KAIST 장학생 구분변경 신청' 안내 메일을 확인한 후, 신청서를 작성하여 EPSD 사무국으로 제출."` ← "학교 산학프로그램 사무국에서 발송한 'KAIST 장학생 구분변경 신청' 안내 메일을 확인한 후, 신청서를 작성하여  EPSD 사무국으로 제출"
  - `application_deadline` = `'2026-07-08'` ← "접수기간 - 2026. 7.1(수) ~ 7.8(수)"
  - `application_period` = `'2026. 7.1(수) ~ 7.8(수)'` ← "접수기간 - 2026. 7.1(수) ~ 7.8(수)"
  - `eligible_university` = `'KAIST'` ← "지원 대상 - KAIST 대학원 석·박사 재학생"
  - `required_enrollment_status` = `'post_undergrad'` ← "지원 대상 - KAIST 대학원 석·박사 재학생"
  - `category_l1` = `'school_external'` ← "삼성디스플레이는 세계 최고 수준의 디스플레이 기술을 선도하고 차세대 디스플레이 원천기술 확보에 기여할 수 있는 우수 인재를 양성하기 위해 국내 우수 대학과와 협력하여 산학교육 프로그램을 운영하고 있습니다"
  - `category_l2` = `'private_foundation'` ← "삼성디스플레이는 세계 최고 수준의 디스플레이 기술을 선도하고 차세대 디스플레이 원천기술 확보에 기여할 수 있는 우수 인재를 양성하기 위해 국내 우수 대학과와 협력하여 산학교육 프로그램을 운영하고 있습니다"

### KAIST 신소재공학과 대학원 OPEN HOUSE 2026
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=388935
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 삼성디스플레이-KAIST EPSD 구분변경 장학생 모집
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=388760
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)
- 확인된 근거 (원문 인용):
  - `name` = `'삼성디스플레이-KAIST EPSD 구분변경 장학생 모집'` ← "삼성디스플레이-KAIST EPSD 구분변경 장학생 모집(~4/10)"
  - `provider` = `'삼성디스플레이'` ← "삼성디스플레이-KAIST EPSD 구분변경 장학생 모집(~4/10)"
  - `description` = `'삼성디스플레이-KAIST EPSD 구분변경 장학생 모집 관련 공고. 첨부파일(삼성디스플레이 EPSD 구분변경 장학생 모집.png)에 세부 내용이 있으나 본문 텍스트에는 상세 자격조건이 제시되어 있지 않음.'` ← "삼성디스플레이 EPSD 구분변경 장학생 모집.png"
  - `application_deadline` = `'2026-04-10'` ← "삼성디스플레이-KAIST EPSD 구분변경 장학생 모집(~4/10)"
  - `major` = `'신소재공학과'` ← "DMSE"
  - `application_period` = `'~4/10'` ← "삼성디스플레이-KAIST EPSD 구분변경 장학생 모집(~4/10)"
  - `eligible_university` = `'KAIST'` ← "삼성디스플레이-KAIST EPSD 구분변경 장학생 모집(~4/10)"
  - `category_l1` = `'school_external'` ← "삼성디스플레이-KAIST EPSD 구분변경 장학생 모집(~4/10)"
  - `category_l2` = `'private_foundation'` ← "삼성디스플레이-KAIST EPSD 구분변경 장학생 모집(~4/10)"

### 신세계그룹과 함께하는 리테일 All-in-One 교육 과정
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=388998
- ⚠️ 확인 필요 필드 1개:
  - `required_enrollment_status` = `None` — value_missing_but_quoted (인용: '※\n학교 재학 및 회사 재직 중일 경우 지원 불가\n※\n장기 휴학생 가능\n(\n연속\n1\n년 이상 또는 통산\n2\n년이상 휴학\n)\n※\n졸업예정자 가능\n(\n마지막 학기 재학 시\n)')
- 확인된 근거 (원문 인용):
  - `name` = `'신세계그룹과 함께하는 리테일 All-in-One 교육 과정'` ← "신세계그룹과 함께하는 리테일 All-in-One 교육 과정 모집"
  - `provider` = `'신세계그룹'` ← "신세계그룹과 함께하는 리테일 All-in-One 교육 과정 모집"
  - `description` = `'미취업 청년 대상 리테일 분야 교육 과정으로, 우수 교육생 채용 연계(상위 5% 채용, 차상위 10% 서류전형 면제), 교육비 전액 지원 및 교육지원금(50만원/월) 지급, 취업 지원 프로그램(합숙 취업캠프, 진로 멘토링, 기업 설명회 등)을 제공함. 교육장소는 천안(서북구), 대전(동구), 대구(동구), 부산(금정구, 해운대구, 연제구), 광주(남구).'` ← "교육혜택
1.
우수 교육생 채용 연계
-
상위
5%
채용
-
차상위
10%
서류전형 면제
(
이마트
,
조선호텔앤리조트
,
신세계푸드
,
신세계아이앤씨
)
2.
교육비 전액 지원 및 교육지원금 지급
-
교육비 전액
(
중식 포함
),
교육지원금
(50
만원
/
월
)
등 학습에 집중할 수 있는 환경 제공
3.
체계적인 취업 지원 프로그램 운영
-
합숙 취업캠프
,
진로 멘토링
,
기업 설명회 등 체계적인 취업 프로그램 지원"
  - `application_url` = `'https://futurendreamacademy.com/'` ← "모집 홈페이지
:
https://futurendreamacademy.com/"
  - `min_age` = `15` ← "만
15
세
~
만
34
세 이하 미취업 청년"
  - `max_age` = `34` ← "만
15
세
~
만
34
세 이하 미취업 청년"
  - `application_period` = `'[1기] 2026.06.18(목) ~ 2026.07.13(월), 17시까지 / [2기] 2026.06.18(목) ~ 2026.08.18(화), 17시까지'` ← "모집기간
:
[1
기
] 2026.06.18(
목
) ~ 2026.07.13(
월
), 17
시까지
[2
기
] 2026.06.18(
목
) ~ 2026.08.18(
화
), 17
시까지"
  - `category_l1` = `'support_fund'` ← "교육비 전액 지원 및 교육지원금 지급"
  - `category_l2` = `'activity_participation_support'` ← "교육비 전액 지원 및 교육지원금 지급
-
교육비 전액
(
중식 포함
),
교육지원금
(50
만원
/
월
)
등 학습에 집중할 수 있는 환경 제공"

### [고용노동부x(주)메이크인 대전지사] 국민취업지원제도
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=388721
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 삼성디스플레이 EPSD 장학생
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=1&document_srl=388717
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)
- 확인된 근거 (원문 인용):
  - `name` = `'삼성디스플레이 EPSD 장학생'` ← "[삼성디스플레이] '26년 상반기 EPSD 장학생 모집 관련 안내드립니다 (접수기간 : 3.27(금)~4.7(화))"
  - `provider` = `'삼성디스플레이'` ← "[삼성디스플레이] '26년 상반기 EPSD 장학생 모집 관련 안내드립니다 (접수기간 : 3.27(금)~4.7(화))"
  - `application_period` = `'3.27(금)~4.7(화)'` ← "[삼성디스플레이] '26년 상반기 EPSD 장학생 모집 관련 안내드립니다 (접수기간 : 3.27(금)~4.7(화))"
  - `eligible_university` = `'KAIST'` ← "[삼성디스플레이] '26년 상반기 EPSD 장학생 모집 관련 안내드립니다 (접수기간 : 3.27(금)~4.7(화))"
  - `category_l1` = `'school_external'` ← "[삼성디스플레이] '26년 상반기 EPSD 장학생 모집 관련 안내드립니다 (접수기간 : 3.27(금)~4.7(화))"
  - `category_l2` = `'private_foundation'` ← "[삼성디스플레이] '26년 상반기 EPSD 장학생 모집 관련 안내드립니다 (접수기간 : 3.27(금)~4.7(화))"

### 2026 삼성전자 MX사업부 Tech & Career 세미나
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=389264
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### [동원그룹] 2026 동원그룹 Open House로 여러분을 초대합니다! (08.25~26)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=389260
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 플렉셀스페이스(주) 채용(~9/31)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=389250
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 박사졸업논문 최소요건(Minimum requirements for doctoral thesis)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=389062
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 박사과정 자격시험 세부규정(Detailed Regulations for the Ph.D. Qualifying Examination)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=389061
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 박사학위 청구논문 심사 (Guide to the evaluation of Ph. D. Dissertation.)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=389060
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 신세계그룹 '리테일 All-in-One 교육 과정 2기' 교육생 모집
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=389245
- ⚠️ 확인 필요 필드 5개:
  - `min_age` = `15` — quote_not_found (인용: '만 15세 ~ 34세 이하 미취업 청년')
  - `max_age` = `34` — quote_not_found (인용: '만 15세 ~ 34세 이하 미취업 청년')
  - `application_deadline` = `'2026-08-18'` — quote_not_found (인용: '모집기간 : [2기] 2026.06.18(목) ~ 2026.08.18.(화), 17시까지')
  - `application_period` = `'2026.06.18(목) ~ 2026.08.18.(화), 17시까지'` — quote_not_found (인용: '모집기간 : [2기] 2026.06.18(목) ~ 2026.08.18.(화), 17시까지')
  - `category_l2` = `'activity_participation_support'` — quote_not_found (인용: '교육비 전액(중식 포함), 교육지원금(50만원/월) 등 학습에 집중할 수 있는 환경 제공')
- 확인된 근거 (원문 인용):
  - `name` = `"신세계그룹 '리테일 All-in-One 교육 과정 2기' 교육생 모집"` ← "신세계그룹 '리테일 All-in-One 교육 과정 2기' 교육생 모집 안내 (~8/18)"
  - `provider` = `'신세계그룹'` ← "[신세계그룹] 리테일 All-in-One 교육 과정 2기 모집"
  - `description` = `'교육부터 취업까지, 상위 5% 채용. 오프라인 리테일, F&B, 호텔·서비스, 리테일테크까지 다양한 산업 영역을 한 과정에서 경험. 우수 교육생 채용 연계(상위 5% 채용, 차상위 10% 서류전형 면제 - 이마트, 조선호텔앤리조트, 신세계푸드, 신세계아이앤씨), 교육비 전액 지원 및 교육지원금 지급(교육비 전액(중식 포함), 교육지원금 50만원/월), 체계적인 취업 지원 프로그램(합숙 취업캠프, 진로 멘토링, 기업 설명회 등). 교육장소: 천안(서북구), 대전(서구), 대구(동구), 부산(금정구, 해운대구), 광주(남구). 교육기간: 2026.09.09(수) ~ 2026.12.02(수)'` ← "교육부터 취업까지, 상위 5% 채용 신세계그룹과 함께하는 리테일 All-in-One 교육 과정 모집 오프라인 리테일, F&B, 호텔·서비스, 리테일테크까지 다양한 산업 영역을 한 과정에서 경험할 수 있습니다."
  - `application_url` = `'https://futurendreamacademy.com/'` ← "모집 홈페이지 : https://futurendreamacademy.com/"
  - `category_l1` = `'support_fund'` ← "교육비 전액 지원 및 교육지원금 지급"

### 박사학위 예비심사 (프로포잘) 신청(Apply for a doctoral degree proposal)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=389059
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 대학원과정 이수요건 Course Requirements of Graduate
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=389058
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 리테일 All-in-One 교육 과정 2기
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=389050
- ⚠️ 확인 필요 필드 7개:
  - `amount` = `500000` — dual_extract_mismatch(2차 추출값=None) (인용: '교육비 전액(중식 포함), 교육지원금(50만원/월) 등 학습에 집중할 수 있는 환경 제공')
  - `min_age` = `15` — quote_not_found (인용: '만 15세 ~ 34세 이하 미취업 청년')
  - `max_age` = `34` — quote_not_found (인용: '만 15세 ~ 34세 이하 미취업 청년')
  - `required_military_status` = `None` — value_missing_but_quoted (인용: '군필자의 경우, 의무복무 기간만큼 연령 상한 연장(최대 만 39세)')
  - `application_deadline` = `'2026-08-18'` — dual_extract_mismatch(2차 추출값=None) (인용: '모집기간: [2기] 2026.06.18(목) ~ 2026.08.18.(화), 17시까지')
  - `application_period` = `'[2기] 2026.06.18(목) ~ 2026.08.18.(화), 17시까지'` — quote_not_found (인용: '모집기간: [2기] 2026.06.18(목) ~ 2026.08.18.(화), 17시까지')
  - `required_enrollment_status` = `None` — value_missing_but_quoted (인용: '※ 학교 재학 및 회사 재직 중인 경우 지원 불가\n※ 휴학생, 졸업예정자 가능(교육 시작일 기준 휴학상태인 경우 참여 가능)')
- 확인된 근거 (원문 인용):
  - `name` = `'리테일 All-in-One 교육 과정 2기'` ← "신세계그룹과 함께하는 리테일 All-in-One 교육 과정 모집"
  - `provider` = `'신세계그룹'` ← "[신세계그룹] 리테일 All-in-One 교육 과정 2기 모집"
  - `description` = `'오프라인 리테일, F&B, 호텔·서비스, 리테일테크까지 다양한 산업 영역을 한 과정에서 경험할 수 있는 교육 과정. 우수 교육생은 상위 5% 채용, 차상위 10% 서류전형 면제(이마트, 조선호텔앤리조트, 신세계푸드, 신세계아이앤씨) 혜택 제공. 교육비 전액(중식 포함) 및 교육지원금(50만원/월) 지급, 합숙 취업캠프·진로 멘토링·기업 설명회 등 취업 지원 프로그램 운영.'` ← "오프라인 리테일, F&B, 호텔·서비스, 리테일테크까지 다양한 산업 영역을 한 과정에서 경험할 수 있습니다."
  - `application_url` = `'https://futurendreamacademy.com/'` ← "모집 홈페이지 : https://futurendreamacademy.com/"
  - `category_l1` = `'support_fund'` ← "교육비 전액 지원 및 교육지원금 지급"
  - `category_l2` = `'activity_participation_support'` ← "교육비 전액 지원 및 교육지원금 지급"

### 신소재공학과 학부 교과목 이수체계 (MSE Curriculum Structure for Undergraduates)
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=386090
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### 신소재공학과 시설안전및화재예방 등을 위한 CCTV 설치 안내
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=385374
- 플래그된 필드 없음(값이 채워진 모든 필드의 인용이 원문과 일치, 원칙 2 통과)

### Merck International Graduate Fellowship
- 출처: https://mse.kaist.ac.kr/index.php?mid=mse_notice&page=2&document_srl=388949
- ⚠️ 확인 필요 필드 3개:
  - `amount` = `None` — dual_extract_mismatch(2차 추출값=8300) (인용: '')
  - `application_deadline` = `None` — dual_extract_mismatch(2차 추출값='2027-07-20') (인용: '')
  - `admission_track` = `'general'` — no_quote (인용: '')
- 확인된 근거 (원문 인용):
  - `name` = `'Merck International Graduate Fellowship'` ← "Merck International Graduate Fellowship - 2027년 장학생 모집"
  - `provider` = `'Merck'` ← "Merck International Graduate Fellowship - 2027년 장학생 모집"
  - `description` = `'카이스트 대학원생 장학금 모집으로, 분야는 Next Generation Biology와 Sustainability 두 가지이며 각 분야별 2명을 모집(작년 대비 정원 2배 확대). 저년차 대상으로 성과중심이 아닌 잠재력 위주로 평가하여 장학생을 선발할 예정.'` ← "분야는 총 두가지로 Next Generation Biology 와 Sustainability 이며 , 각 분야별 2 명을 모집하여 정원이 작년에 비해 2 배로 확대되었습니다 . 저년차 대상으로 모집하여 성과중심이 아닌 잠재력 위주로 평가하여 장학생을 선발할 예정이라고 합니다 ."
  - `grade_level` = `'저년차 대상'` ← "저년차 대상으로 모집하여 성과중심이 아닌 잠재력 위주로 평가하여 장학생을 선발할 예정이라고 합니다 ."
  - `headcount` = `'분야별 2명, 총 4명'` ← "각 분야별 2 명을 모집하여 정원이 작년에 비해 2 배로 확대되었습니다 ."
  - `application_period` = `'지원 기한은 7월 20일까지'` ← "지원 기한은 7 월 20 일까지 이며 , 자세한 일정은 첨부 드리는 포스터를 참고 부탁드립니다 ."
  - `required_enrollment_status` = `'post_undergrad'` ← "카이스트 대학원생 장학금 모집을 오픈하여 신소재공학과 구성원분들께 홍보를 부탁드리고자 합니다 ."
  - `category_l1` = `'school_external'` ← "카이스트 대학원생 장학금 모집을 오픈하여 신소재공학과 구성원분들께 홍보를 부탁드리고자 합니다 ."
  - `category_l2` = `'private_foundation'` ← "Merck International Graduate Fellowship - 2027년 장학생 모집"
