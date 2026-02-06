import sys
import os

# 경로 설정
ROOT_DIR = r"D:\Git_Work\Docker\OpenClaw_Data\openclaw\workspace"
sys.path.append(os.path.join(ROOT_DIR, "Contents", "Youtube", "RECORDS_OF_DEMON_KING", "core"))

from youtube_auth import get_youtube_service

def finalize_global_links():
    youtube = get_youtube_service()
    
    target_link = "https://github.com/taemingames/Demon-Engine"
    
    videos = [
        {"id": "a1onzD8zmFY", "title": "자비스 게임 출시? | AI Jarvis Game Release #Shorts"},
        {"id": "PCx5ECnRbhc", "title": "[유출] 자비스 신작 게임 | Leaked: AI Jarvis New Game"},
        {"id": "9363z-roLhU", "title": "상위 1%의 비밀: 에이전트 자동화 | The Secret of Top 1% #Shorts"}
    ]
    
    for v in videos:
        try:
            v_get = youtube.videos().list(part="snippet", id=v['id']).execute()
            snippet = v_get['items'][0]['snippet']
            
            # 기존 설명에 링크가 없으면 추가
            if target_link not in snippet['description']:
                snippet['description'] += f"\n\n🔥 [SYSTEM] Access Demon-Engine:\n🔗 {target_link}"
                youtube.videos().update(part="snippet", body={"id": v['id'], "snippet": snippet}).execute()
                print(f"SUCCESS: Link added to {v['id']}")
            else:
                print(f"SKIP: Link already exists in {v['id']}")
        except Exception as e:
            print(f"FAIL: {v['id']} - {e}")

if __name__ == "__main__":
    finalize_global_links()
