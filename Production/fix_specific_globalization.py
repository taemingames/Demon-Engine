import sys
import os

# 경로 설정
ROOT_DIR = r"D:\Git_Work\Docker\OpenClaw_Data\openclaw\workspace"
sys.path.append(os.path.join(ROOT_DIR, "Contents", "Youtube", "RECORDS_OF_DEMON_KING", "core"))

from youtube_auth import get_youtube_service

def fix_specific_video_globalization():
    youtube = get_youtube_service()
    video_id = "maWpQOK7dEI"
    
    print(f"--- [Target Fix: {video_id}] ---")
    
    try:
        # 1. 현재 메타데이터 가져오기
        v_get = youtube.videos().list(part="snippet", id=video_id).execute()
        if not v_get['items']:
            print("Video not found.")
            return
            
        snippet = v_get['items'][0]['snippet']
        
        # 2. 글로벌 타이틀 및 설명 설계
        new_title = "2026 수익의 연금술 | 2026 AI Revenue Alchemy: The System of Control"
        new_desc = """[EN] 2026 Revenue Alchemy: Detailed disclosure of the 'Dominator's Lineage' built by the AI automation system.
Experience the peak of agentic workflows with OpenClaw.

---

[KR] 2026년 수익의 연금술: AI 자동화 시스템이 구축하는 '지배자의 계보' 상세 공개.
오픈클로(OpenClaw)와 함께 에이전틱 워크플로우의 정점을 경험하십시오.

🔗 Watch more: https://www.youtube.com/@TaeminGames
"""
        
        snippet['title'] = new_title
        snippet['description'] = new_desc
        snippet['tags'] = ["AI", "Automation", "Jarvis", "2026", "Revenue", "PassiveIncome", "OpenClaw", "TaeminGames"]
        
        # 3. 업데이트 수행
        youtube.videos().update(part="snippet", body={"id": video_id, "snippet": snippet}).execute()
        print(f" => SUCCESS: {video_id} is now fully Globalized.")
        
    except Exception as e:
        print(f" => FAIL: {e}")

if __name__ == "__main__":
    fix_specific_video_globalization()
