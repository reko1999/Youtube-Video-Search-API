import subprocess
import time
from pyngrok import ngrok
import threading
import webbrowser

def run_fastapi():
    subprocess.run(["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"])

def setup_ngrok(auth_token, port=8000):
    try:
        ngrok.set_auth_token(auth_token)

        # ngrok 터널 생성
        public_url = ngrok.connect(port).public_url
        print(f"\n✨ ngrok 터널이 생성되었습니다!")
        print(f"🌐 Public URL: {public_url}")
        print(f"\n브라우저에서 위 URL로 접속하세요.")
        
        return public_url
    except exception.PyngrokNgrokError as e:
        print(f"ngrok 에러: {e}")
        raise

def setup_youtube_api_key(api_key):
    try:
        # app/app.py 파일에서 YOUR_YOUTUBE_API_KEY_HERE를 실제 API 키로 교체
        app_file = "app/app.py"

        with open(app_file, 'r') as file:
            content = file.read()

        content = content.replace('YOUR_YOUTUBE_API_KEY_HERE', api_key)

        with open(app_file, 'w') as file:
            file.write(content)
            print(f"{app_file} 파일의 YouTube API 키가 성공적으로 업데이트되었습니다.")
    except Exception as e:
        print(f"에러: {app_file} 파일 수정 중 오류 발생: {e}")
        exit(1)

if __name__ == "__main__":
    # YouTube API 키 입력 받기
    youtube_api_key = input("YouTube API 키를 입력하세요: ").strip()

    # YouTube API 키 설정
    setup_youtube_api_key(youtube_api_key)

    try:
        # FastAPI 서버를 별도 스레드에서 실행
        server_thread = threading.Thread(target=run_fastapi)
        server_thread.daemon = True
        server_thread.start()

        print("FastAPI 서버가 시작되었습니다...")
        time.sleep(3)  # 서버 시작 대기
    except Exception as e:
        print(f"에러: FastAPI 서버 시작 중 오류 발생: {e}")
        exit(1)
    
    try:

        # ngrok 인증 토큰 입력 받기
        auth_token = input("ngrok 인증 토큰을 입력하세요: ")

        # ngrok 설정
        public_url = setup_ngrok(auth_token)
        
        # 앱이 계속 실행되도록 대기
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # 종료 시 프로세스 정리
        ngrok.kill()
        time.sleep(3)
        print("ngrok 터널 및 FastAPI 서버가 종료되었습니다.")
    except Exception as e:
        print(f"에러 발생: {e}")
        ngrok.kill()
        time.sleep(3)
        print("ngrok 터널 및 FastAPI 서버가 종료되었습니다.")