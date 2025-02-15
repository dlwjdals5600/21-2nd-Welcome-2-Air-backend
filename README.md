# 21-2nd-Welcome2Air-backend

## Welcome2Air 프로젝트 Back-end 소개

- 국내 1위 항공사 [대한항공](https://www.koreanair.com/)의 사이트를 모티브한 팀 협업 프로젝트
- 짧은 프로젝트 기간동안 개발에 집중해야 하므로 많은 기능들 중 특정 항공편 검색 및 예약, 예약 조회 및 e-Ticket 출력 등 핵심 기능들만 구현하였습니다.
- 개발은 초기 세팅부터 전부 직접 구현했으며, 아래 데모 영상에서 보이는 부분은 모두 백앤드와 연결하여 실제 사용할 수 있는 서비스 수준으로 개발한 것입니다.

### 개발 인원 및 기간

- 개발 기간 : 2021/06/21 ~ 2021/07/01
- 개발 인원 : 프론트엔드 3명, 백엔드 4명
- 프론트엔드 Github : [링크](https://github.com/wecode-bootcamp-korea/21-2nd-Welcome-2-Air-frontend)


<br>

## 사용 기술 및 구현 기능


### 사용 기술 및 tools
> - Front-End : <img src="https://img.shields.io/badge/ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/React.js-61DAFB?style=for-the-badge&logo=React&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/React%20Router-CA4245?style=for-the-badge&logo=React-router&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/sass-CC6699?style=for-the-badge&logo=sass&logoColor=white"/>
> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2.4-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Mysql 8.0-4479A1?style=for-the-badge&logo=Mysql&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/PyJWT 2.1-000000?style=for-the-badge&logo=JsonWebTokens&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Bcrypt 3.2-338000?style=for-the-badge&logo=PyJWT&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Amazon S3-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Trello-0052CC?style=for-the-badge&logo=Trello&logoColor=white"/>

### Modeling
[AQueryTool(pw:tj4a01)](https://aquerytool.com/aquerymain/index/?rurl=3924fd52-298b-4ddd-bed4-fd659a16ed63&)




### 구현 기능

#### Users app
- `JWT`를 이용한 User정보 토큰발생
- 카카오톡 소셜 로그인 기능 구현

#### Flights app
- 항공편 조희 기능 구현
- 검색필터링 및 조회 기능 구현

#### Tickets app
- User가 원하는 항공편을 선택하면, 해당 항공편에 대하여 탑승자(들) 정보 입력받은 후 예약-> uuid 를 이용한 ticketId 발부, 예약된 인원만큼 잔여좌석 차감
- User의 '항공권 예약 내역' 에서 해당 User 계정에 예약된 항공권 조회

#### Tickets app 담당업무
- `pdfkit`을 통해 html을 pdf로 변환 후 `S3`,database에 저장 기능 구현
- 해당 Passenger에게 pdf(항공권)을 제공 기능 구현

<br>

## Reference

- 이 프로젝트는 [대한항공](https://www.koreanair.com/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
