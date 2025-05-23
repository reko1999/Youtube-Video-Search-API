# Youtube-Video-Search-API
YouTube API 활용 동영상 검색 웹 애플리케이션

## 개요
YouTube Data API v3를 사용해 동영상을 검색하고 결과를 웹 UI에 표시. FastAPI와 React 기반, ngrok으로 외부 접근.

## 설치
1. Python 3.8 이상.
2. 종속성:
- fastapi: Python 웹 API 구축 프레임워크. (백엔드 API 서버)
- uvicorn: FastAPI 실행용 비동기 ASGI 서버.
- pyngrok: 로컬 서버를 외부에 공개하는 ngrok Python 인터페이스.
- python-multipart: 파일 업로드를 위한 multipart/form-data 요청 처리.
- google-api-python-client: YouTube Data API 등 Google API 호출.
- jinja2: 동적 HTML 및 텍스트 포맷팅용 템플릿 엔진
4. YouTube API 키: Google Cloud Console에서 발급, `app.py`에 설정.
5. ngrok 설치 및 인증 토큰 설정.

## 실행
1. FastAPI: `python app.py`.
2. ngrok: `python run_server.py`.
3. 공개 URL로 접속.

## API 사용법
- **엔드포인트**: `/api/search/{query}`
  - **메서드**: GET
  - **쿼리 파라미터**: `max_results` (기본 10)
  - **응답**: JSON (동영상 목록).
- **엔드포인트**: `/api/video/{video_id}`
  - **메서드**: GET
  - **응답**: JSON (동영상 상세 정보).
