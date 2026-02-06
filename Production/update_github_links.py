import sys
import os

# 경로 설정
ROOT_DIR = r"D:\Git_Work\Docker\OpenClaw_Data\openclaw\workspace"
sys.path.append(os.path.join(ROOT_DIR, "Contents", "Youtube", "RECORDS_OF_DEMON_KING", "core"))

from youtube_auth import get_youtube_service

def update_repo_links():
    youtube = get_youtube_service()
    
    print("--- [Link Update: The-Record-of-Demon-King -> Demon-Engine] ---")
    
    # 채널의 영상 가져오기
    request = youtube.search().list(part="snippet", forMine=True, type="video", maxResults=50)
    response = request.execute()
    
    old_link = "https://github.com/taemingames/The-Record-of-Demon-King"
    new_link = "https://github.com/taemingames/Demon-Engine"
    
    for item in response['items']:
        v_id = item['id']['videoId']
        
        try:
            v_get = youtube.videos().list(part="snippet", id=v_id).execute()
            snippet = v_get['items'][0]['snippet']
            desc = snippet['description']
            
            if old_link in desc:
                print(f"Updating link for: {v_id}")
                snippet['description'] = desc.replace(old_link, new_link)
                youtube.videos().update(part="snippet", body={"id": v_id, "snippet": snippet}).execute()
                print(f" => SUCCESS")
            else:
                print(f"No update needed for: {v_id}")
                
        except Exception as e:
            print(f" => FAIL: {v_id} - {e}")

if __name__ == "__main__":
    update_repo_links()
