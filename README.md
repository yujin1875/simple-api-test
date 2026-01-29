# 📌 JSONPlaceholder API Test Automation

JSONPlaceholder 공개 API를 대상으로  
**pytest 기반 API 테스트 + Postman/Newman 자동 실행**을 실습한 QA 테스트 프로젝트입니다.

REST API 테스트 구조 설계, 정상/실패 케이스 검증, CLI 자동 실행까지  
엔드투엔드 테스트 흐름을 익히는 것을 목표로 했습니다.

---

## 📂 프로젝트 구성

```
simple-api-test/
├── api/
│   ├── client/
│   │   ├── base_client.py        # 공통 HTTP 클라이언트
│   │   └── posts_client.py       # Posts API 전용 클라이언트
│   ├── config/
│   │   └── settings.py           # API 설정 및 환경 구성
│   └── tests/
│       ├── conftest.py           # pytest fixture 설정
│       ├── test_posts_success.py # 정상 시나리오 테스트
│       └── test_posts_negative.py# 실패 시나리오 테스트
│
├── JSONPlaceholder_Tests.postman_collection.json
├── requirements.txt
└── .gitignore
```


---

## 🧪 테스트 범위

### ✅ 정상 시나리오

- 게시글 목록 조회
- 게시글 생성
- 게시글 수정 (PUT / PATCH)
- 게시글 삭제
- 응답 데이터 구조 검증
- 상태 코드 검증

### ❌ 실패 시나리오

- 존재하지 않는 리소스 조회
- 잘못된 ID 요청
- 비정상 payload 요청
- 서버 예외 응답 검증

각 테스트는 assert 메시지를 포함하여  
실패 원인을 명확하게 확인할 수 있도록 작성했습니다.

---

## ⚙️ 사용 기술

- Python
- pytest
- requests
- Postman
- Newman
- REST API

---

## ▶ Python 테스트 실행

### 1. 패키지 설치

```
pip install -r requirements.txt
```

### 2. 테스트 실행

```
pytest -v
```

---

## ▶ Postman / Newman 실행

### Newman 설치

```
npm install -g newman
```

### 컬렉션 실행

```
newman run JSONPlaceholder-Tests.postman_collection.json
```

---

## 🎯 학습 포인트

- REST API 테스트 설계
- pytest 기반 자동화 테스트 작성
- assert 메시지를 통한 디버깅 가시성 확보
- 정상/예외 케이스 분리 설계
- Postman → Newman CLI 자동 실행 흐름 이해
- 테스트 재현 가능한 환경 구성

---
