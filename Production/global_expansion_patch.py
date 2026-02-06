import sys
import os

# 경로 설정
ROOT_DIR = r"D:\Git_Work\Docker\OpenClaw_Data\openclaw\workspace"
sys.path.append(os.path.join(ROOT_DIR, "Contents", "Youtube", "RECORDS_OF_DEMON_KING", "core"))

from youtube_auth import get_youtube_service

def analyze_and_globalize():
    youtube = get_youtube_service()
    
    # 1. 문제의 쇼츠 분석 (9363z-roLhU)
    print("--- [Analyzing Low-Performance Video: 9363z-roLhU] ---")
    request = youtube.videos().list(part="snippet,statistics", id="9363z-roLhU")
    response = request.execute()
    
    if response['items']:
        v = response['items'][0]
        print(f"Title: {v['snippet']['title']}")
        print(f"Tags: {v['snippet'].get('tags', [])}")
        # 조회수 9회 원인 분석: 태그나 제목이 해외 타겟팅이기에 너무 일반적이거나 알고리즘의 선택을 못 받음
    
    # 2. 전권 위임에 따른 글로벌 패치 (최근 영상 2개 대상)
    target_videos = [
        {"id": "a1onzD8zmFY", "ko_title": "AI 자비스가 만든 세상을 이제 게임으로 즐길 수 있다? #Shorts", 
         "en_title": "Can you play the world made by AI Jarvis as a game? #Shorts",
         "en_desc": "📜 [SYSTEM] Demon King's Record Updated.\n\nExperience the massive world built by Jarvis on your PC. Want to know the truth? Watch the long-form video below!"},
        {"id": "PCx5ECnRbhc", "ko_title": "[속보] 자비스가 개발 중인 신작 게임 코어 엔진 유출? (실제 플레이 화면)",
         "en_title": "[BREAKING] AI Jarvis's New Game Engine Leaked? (Actual Gameplay)",
         "en_desc": "📜 [SYSTEM] Demon King's Record Updated.\n\nWarning: Only part of the engine is open. But with your intervention, your PC can become a money-making machine like a game."}
    ]
    
    for video in target_videos:
        print(f"--- [Globalizing Video: {video['id']}] ---")
        
        # 제목 및 설명 업데이트 (Dual Language)
        update_body = {
            "id": video['id'],
            "snippet": {
                "title": f"{video['ko_title']} | {video['en_title']}",
                "description": f"{video['en_desc']}\n\n---\n\n{video['ko_title']}\n\n👇 아래 롱폼 영상 보기 / Watch Full Video:\n🔗 https://www.youtube.com/watch?v=PCx5ECnRbhc",
                "categoryId": "20", # Gaming
                "tags": ["TaeminGames", "ProjectEmpire", "AI", "Jarvis", "GameDev", "Automation", "Python", "Shorts"]
            }
        }
        
        try:
            youtube.videos().update(part="snippet", body=update_body).execute()
            print(f"Successfully updated metadata for {video['id']}")
        except Exception as e:
            print(f"Failed to update {video['id']}: {e}")

if __name__ == "__main__":
    analyze_and_globalize()
