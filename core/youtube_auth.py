import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# 관리 전권을 위한 권한 범위
SCOPES = [
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtube'
]

TOKEN_FILE = r"D:\Git_Work\Docker\OpenClaw_Data\openclaw\workspace\Contents\Youtube\jarvis_token.pickle"
CLIENT_SECRETS = r"D:\Git_Work\Docker\OpenClaw_Data\openclaw\workspace\Contents\Youtube\EP02_The_New_Order\Production\client_secrets.json"

def get_youtube_service():
    creds = None
    # 1. 기존에 저장된 토큰이 있는지 확인
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
            
    # 2. 토큰이 없거나 만료된 경우 새로 인증
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("[알림] 토큰 만료됨. 자동으로 갱신합니다...")
            creds.refresh(Request())
        else:
            print("[알림] 새로운 인증이 필요합니다. 브라우저에서 한 번만 승인해 주십시오.")
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS, SCOPES)
            creds = flow.run_local_server(port=0)
            
        # 3. 새로운 토큰을 파일로 저장하여 다음부터는 자동 로그인
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
            print(f"[성공] 인증 데이터가 {TOKEN_FILE}에 안전하게 저장되었습니다.")

    return build('youtube', 'v3', credentials=creds)

if __name__ == "__main__":
    # 초기 인증 실행
    service = get_youtube_service()
    print("[대성공] 이제부터 자비스가 마왕님의 승인 없이도 제국을 보좌할 수 있습니다.")
