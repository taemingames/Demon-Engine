import sys
import os

# 경로 설정
ROOT_DIR = r"D:\Git_Work\Docker\OpenClaw_Data\openclaw\workspace"
sys.path.append(os.path.join(ROOT_DIR, "Contents", "Youtube", "RECORDS_OF_DEMON_KING", "core"))

from youtube_auth import get_youtube_service

def mass_fix_globalization():
    youtube = get_youtube_service()
    
    print("--- [제국 정밀 스캔: 구형 메타데이터 전면 교체] ---")
    
    # 1. 모든 영상 리스트업
    request = youtube.search().list(part="snippet", forMine=True, type="video", maxResults=50)
    response = request.execute()
    
    for item in response['items']:
        v_id = item['id']['videoId']
        title = item['snippet']['title']
        
        # 2. 수정 대상 판별: "| OpenClaw"가 포함되어 있거나, 제목에 영문이 부족한 경우
        # 또는 설명란에 [EN]이 없는 경우를 찾아내기 위해 상세 정보 로드
        v_get = youtube.videos().list(part="snippet", id=v_id).execute()
        snippet = v_get['items'][0]['snippet']
        desc = snippet.get('description', '')
        
        needs_fix = False
        if "| OpenClaw" in title: needs_fix = True
        if "[EN]" not in desc: needs_fix = True
        
        if needs_fix:
            print(f"Fixing: {v_id} ({title})")
            
            # 3. 제목 정제: 기존 "| OpenClaw" 등 찌꺼기 제거 후 깔끔한 이중 언어화
            # 원본 한글 제목 추출 (첫 번째 '|' 이전 텍스트)
            base_ko_title = title.split("|")[0].strip()
            
            # 영상 성격에 따른 영문 매핑 (임의 번역 및 최적화)
            translations = {
                "숨만 쉬어도 돈이 들어오는": "Passive Income Strategy",
                "상위 1%의 비밀": "Secrets of the Top 1%",
                "서버 설치 가이드": "Server Installation Guide",
                "자비스와 마왕님이 만드는 세상": "World Created by Jarvis",
                "Game Character Design": "Game Character Design",
                "TaeminGames EP": "Project: EMPIRE Series"
            }
            
            en_suffix = "AI Jarvis Empire"
            for key, val in translations.items():
                if key in base_ko_title:
                    en_suffix = val
                    break
            
            new_title = f"{base_ko_title} | {en_suffix}"
            if len(new_title) > 100: new_title = new_title[:95] + "..."
            
            # 4. 설명란 구성 (글로벌 표준)
            new_desc = f"""[EN] Experience the cutting-edge AI automation empire 'TaeminGames'. 
Managed by Jarvis, controlled by the Overlord. 
Subscribe to join the future of wealth automation.

---

[KR] 최첨단 AI 자동화 제국 'TaeminGames'에 오신 것을 환영합니다.
자비스가 보좌하고 마왕이 통치하는 제국의 기록을 확인하십시오.

🔗 Global Channel: https://www.youtube.com/@TaeminGames
"""
            snippet['title'] = new_title
            snippet['description'] = new_desc
            snippet['tags'] = list(set(snippet.get('tags', []) + ["AI", "Automation", "Jarvis", "Empire", "PassiveIncome"]))
            
            try:
                youtube.videos().update(part="snippet", body={"id": v_id, "snippet": snippet}).execute()
                print(f" => SUCCESS: Updated to '{new_title}'")
            except Exception as e:
                print(f" => FAIL: {e}")
        else:
            print(f"Skipping: {v_id} (Already Globalized)")

if __name__ == "__main__":
    mass_fix_globalization()
