# 📝 메모짱 (MemoJJang)

Django 기반의 간단하고 직관적인 메모장 웹 애플리케이션

## 🌟 주요 기능

- ✅ **사용자 인증**: 회원가입, 로그인, 로그아웃
- ✅ **메모 관리**: 메모 생성, 조회, 수정, 삭제 (CRUD)
- ✅ **반응형 UI**: Bootstrap 5 기반 모던한 디자인
- ✅ **사용자별 메모**: 로그인한 사용자만 자신의 메모 관리

## 🛠 기술 스택

### Backend
- **Framework**: Django 5.2.7
- **Database**: SQLite3
- **Authentication**: Django 기본 인증 시스템

### Frontend
- **CSS Framework**: Bootstrap 5.3.0
- **Template Engine**: Django Templates

### 환경
- **Python**: 3.13.5
- **가상환경**: venv

## 📁 프로젝트 구조

```
django_memo_app/
├── .github/
│   ├── chatmodes/
│   │   └── plan.chatmode.md
│   ├── instructions/
│   │   ├── database.instructions.md
│   │   └── python.instructions.md
│   └── copilot-instructions.md
├── memojjang/              # Django 프로젝트
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── memos/                  # 메모 앱
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── users/                  # 사용자 앱
│   ├── views.py
│   └── urls.py
├── templates/              # 템플릿
│   ├── base.html
│   ├── memos/
│   │   ├── memo_list.html
│   │   ├── memo_detail.html
│   │   ├── memo_form.html
│   │   └── memo_confirm_delete.html
│   └── users/
│       ├── login.html
│       └── register.html
├── static/                 # 정적 파일
│   └── css/
│       └── style.css
├── manage.py
└── db.sqlite3
```

## 🚀 설치 및 실행

### 1. 저장소 클론

```bash
git clone https://github.com/x4y8p7x6x2-a11y/github_django.git
cd github_django
```

### 2. 가상환경 생성 및 활성화

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 패키지 설치

```bash
pip install django python-dotenv
```

### 4. 데이터베이스 마이그레이션

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. 슈퍼유저 생성 (선택사항)

```bash
python manage.py createsuperuser
```

### 6. 개발 서버 실행

```bash
python manage.py runserver
```

### 7. 브라우저에서 접속

- 메인 페이지: http://127.0.0.1:8000
- 관리자 페이지: http://127.0.0.1:8000/admin

## 👤 테스트 계정

- **사용자명**: admin
- **비밀번호**: admin123

## 📝 모델 구조

### Memo 모델

| 필드 | 타입 | 설명 |
|------|------|------|
| id | BigAutoField | 기본 키 (자동 생성) |
| user | ForeignKey | 작성자 (User 모델 참조) |
| title | TextField | 메모 제목 |
| content | TextField | 메모 내용 |
| created_at | DateTimeField | 생성일시 (자동) |
| updated_at | DateTimeField | 수정일시 (자동) |

## 🎯 주요 URL 패턴

| URL | 뷰 | 설명 |
|-----|-----|------|
| `/` | redirect | 메모 목록으로 리다이렉트 |
| `/memos/` | memo_list | 메모 목록 |
| `/memos/<id>/` | memo_detail | 메모 상세 |
| `/memos/create/` | memo_create | 메모 생성 |
| `/memos/<id>/update/` | memo_update | 메모 수정 |
| `/memos/<id>/delete/` | memo_delete | 메모 삭제 |
| `/users/register/` | register | 회원가입 |
| `/users/login/` | user_login | 로그인 |
| `/users/logout/` | user_logout | 로그아웃 |
| `/admin/` | admin | 관리자 페이지 |

## 🔐 보안 기능

- CSRF 토큰을 통한 폼 보호
- 로그인 데코레이터를 통한 접근 제어
- 사용자별 메모 격리 (본인 메모만 조회/수정/삭제)
- Django 기본 비밀번호 검증

## 📋 향후 개발 계획

자세한 개선 사항 및 이슈는 [ISSUES.md](ISSUES.md) 파일을 참조하세요.

### Phase 1 (우선순위 높음)
- [ ] 메모 범주(카테고리) 기능
- [ ] 테스트 코드 작성
- [ ] 보안 강화

### Phase 2 (우선순위 중간)
- [ ] Markdown 에디터 지원
- [ ] 메모 검색 기능
- [ ] 반응형 디자인 개선

### Phase 3 (추가 기능)
- [ ] 메모 즐겨찾기
- [ ] 태그 기능
- [ ] REST API

## 🤝 기여 방법

1. 이 저장소를 Fork 합니다
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature/AmazingFeature`)
3. 변경사항을 커밋합니다 (`git commit -m 'Add some AmazingFeature'`)
4. 브랜치에 Push 합니다 (`git push origin feature/AmazingFeature`)
5. Pull Request를 생성합니다

## 📄 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 👨‍💻 개발자

GitHub Copilot Workshop - Django Project

## 📞 문의

프로젝트에 대한 질문이나 제안사항이 있으시면 Issue를 생성해주세요.

---

**Made with ❤️ using Django and GitHub Copilot**
