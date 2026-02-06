import sys
import os

# 경로 설정
ROOT_DIR = r"D:\Git_Work\Docker\OpenClaw_Data\openclaw\workspace"
sys.path.append(os.path.join(ROOT_DIR, "Contents", "Youtube", "RECORDS_OF_DEMON_KING", "core"))

from youtube_auth import get_youtube_service

def global_expansion_v2():
    youtube = get_youtube_service()
    
    # 패치 대상 리스트
    target_videos = [
        {
            "id": "a1onzD8zmFY", 
            "title": "자비스 게임 출시? | AI Jarvis Game Release #Shorts",
            "desc": "[EN] Play the world made by AI Jarvis! Link in long-form video below.\n\n[KR] 자비스가 만든 세상을 게임으로 즐기세요. 상세 내용은 아래 롱폼 영상 확인!"
        },
        {
            "id": "PCx5ECnRbhc", 
            "title": "[유출] 자비스 신작 게임 | Leaked: AI Jarvis New Game",
            "desc": "[EN] Project: EMPIRE core engine leaked. Your PC becomes a revenue machine.\n\n[KR] 자비스 개발 신작 게임 코어 유출. 당신의 컴퓨터가 수익을 창출합니다."
        },
        {
            "id": "9363z-roLhU",
            "title": "상위 1%의 비밀: 에이전트 자동화 | The Secret of Top 1% #Shorts",
            "desc": "[EN] Agentic Workflow: The future of 2026. Stop asking, start commanding.\n\n[KR] 2026년 상위 1%만 아는 에이전틱 워크플로우의 실체."
        }
    ]
    
    for video in target_videos:
        print(f"--- [Global Expansion Patch: {video['id']}] ---")
        
        # 최신 정보를 먼저 가져온 뒤 업데이트 (안정성)
        try:
            v_get = youtube.videos().list(part="snippet", id=video['id']).execute()
            if not v_get['items']: continue
            
            snippet = v_get['items'][0]['snippet']
            snippet['title'] = video['title']
            snippet['description'] = video['desc'] + "\n\n🔗 Watch Full Version: https://www.youtube.com/watch?v=PCx5ECnRbhc"
            snippet['tags'] = ["TaeminGames", "AI", "Jarvis", "Automation", "IndieGame", "PassiveIncome", "Python", "Shorts"]
            snippet['defaultAudioLanguage'] = "ko"
            
            youtube.videos().update(part="snippet", body={"id": video['id'], "snippet": snippet}).execute()
            print(f" => SUCCESS: {video['id']} updated with Global Metadata.")
        except Exception as e:
            print(f" => FAIL: {video['id']} - {e}")

if __name__ == "__main__":
    global_expansion_v2()
