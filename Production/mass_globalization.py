import sys
import os

# 경로 설정
ROOT_DIR = r"D:\Git_Work\Docker\OpenClaw_Data\openclaw\workspace"
sys.path.append(os.path.join(ROOT_DIR, "Contents", "Youtube", "RECORDS_OF_DEMON_KING", "core"))

from youtube_auth import get_youtube_service

def globalize_entire_channel():
    youtube = get_youtube_service()
    
    print("--- [제국 영토 전역 확장: 채널 전체 글로벌 패치 시작] ---")
    
    # 1. 채널의 모든 영상 가져오기 (최대 50개)
    request = youtube.search().list(part="snippet", forMine=True, type="video", maxResults=50)
    response = request.execute()
    
    for item in response['items']:
        v_id = item['id']['videoId']
        old_title = item['snippet']['title']
        print(f"Checking Video: {v_id} ({old_title})")
        
        # 이미 글로벌 패치가 된 영상(타이틀에 '|'가 포함된 경우)은 스킵
        if "|" in old_title:
            print(f" => SKIPPING: {v_id} is already globalized.")
            continue
            
        try:
            # 영상 정보 상세 조회
            v_get = youtube.videos().list(part="snippet", id=v_id).execute()
            snippet = v_get['items'][0]['snippet']
            
            # 2. 범용적인 글로벌 타이틀 및 설명 생성
            # 마왕님의 제국 세계관을 반영한 기본 영문 번역 적용
            new_title = f"{old_title} | AI Jarvis Empire"
            if len(new_title) > 100: # 유튜브 제목 제한
                new_title = f"{old_title[:70]}... | AI Jarvis"
                
            en_base_desc = "[EN] Welcome to TaeminGames. Experience the future of AI automation managed by Jarvis.\n\n"
            snippet['title'] = new_title
            snippet['description'] = en_base_desc + snippet['description']
            
            # 3. 글로벌 태그 추가
            global_tags = ["AI", "Jarvis", "Automation", "TaeminGames", "IndieGame", "PassiveIncome"]
            current_tags = snippet.get('tags', [])
            snippet['tags'] = list(set(current_tags + global_tags))
            
            # 업데이트 실행
            youtube.videos().update(part="snippet", body={"id": v_id, "snippet": snippet}).execute()
            print(f" => SUCCESS: {v_id} is now Globalized.")
            
        except Exception as e:
            print(f" => FAIL: {v_id} - {e}")

if __name__ == "__main__":
    globalize_entire_channel()
