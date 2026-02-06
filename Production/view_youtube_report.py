import sys
import os
from datetime import datetime

# 경로 설정
ROOT_DIR = r"D:\Git_Work\Docker\OpenClaw_Data\openclaw\workspace"
sys.path.append(os.path.join(ROOT_DIR, "Contents", "Youtube", "RECORDS_OF_DEMON_KING", "core"))

from youtube_auth import get_youtube_service

def get_empire_report():
    youtube = get_youtube_service()
    
    print("--- [YOUTUBE EMPIRE STATUS REPORT] ---")
    
    # 1. 채널 정보
    ch_request = youtube.channels().list(part="snippet,statistics", mine=True)
    ch_response = ch_request.execute()
    
    if not ch_response['items']:
        print("[ERROR] Channel not found.")
        return

    channel = ch_response['items'][0]
    stats = channel['statistics']
    snippet = channel['snippet']
    
    print(f"CHANNEL: {snippet['title']}")
    print(f"DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Subscribers: {stats['subscriberCount']}")
    print(f"Total Views: {stats['viewCount']}")
    print(f"Total Videos: {stats['videoCount']}")
    print("\n--- RECENT VIDEOS & GLOBALIZATION CHECK ---")
    
    # 2. 영상 리스트 및 글로벌 여부 확인
    v_request = youtube.search().list(part="snippet", forMine=True, type="video", order="date", maxResults=50)
    v_response = v_request.execute()
    
    for item in v_response['items']:
        v_id = item['id']['videoId']
        v_title = item['snippet']['title']
        v_desc = item['snippet']['description']
        
        # 글로벌 여부 판단: 제목에 영문이 포함되어 있는지, 설명에 [EN]이 있는지 확인
        is_global = "[EN]" in v_desc or any(c.isascii() and c.isalpha() for c in v_title)
        status_tag = "[GLOBALIZED]" if is_global else "[KOREAN ONLY]"
        
        print(f"- {status_tag} {v_title} (ID: {v_id})")

if __name__ == "__main__":
    get_empire_report()

if __name__ == "__main__":
    get_empire_report()
