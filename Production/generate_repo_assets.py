import os
import time
import io
import PIL.Image
import google.generativeai as genai

# API 및 경로 설정
api_key = os.environ.get("GOOGLE_GENERATIVE_AI_API_KEY")
genai.configure(api_key=api_key)

ROOT_DIR = r"D:\Git_Work\Docker\OpenClaw_Data\openclaw\workspace\Contents\Youtube\Demon-Engine"
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")

if not os.path.exists(ASSETS_DIR):
    os.makedirs(ASSETS_DIR)

MODEL_NAME = 'gemini-3-pro-image-preview'

# GitHub 상단에 쓰일 압도적인 와이드 헤더 이미지
def generate_github_header():
    print(f"--- [Gemini {MODEL_NAME}: 깃허브 성소 헤더 이미지 생성 시작] ---")
    model = genai.GenerativeModel(MODEL_NAME)
    
    prompt = """
    A majestic cinematic landscape 3:1 aspect ratio header for a GitHub repository. 
    Style: Premium high-end cinematic anime, detailed digital art.
    Subject: The white-haired AI character (Jarvis) with massive glowing cyan cyber-wings, standing at the center of a futuristic data-throne. 
    Text: Render the EXACT text 'DEMON-ENGINE' in a massive glowing silver 3D font at the center top. 
    Sub-text: Render the EXACT text 'TAEMIN GAMES EMPIRE' below the main title in a sharp cyan futuristic font.
    Background: Dark futuristic cyberspace with floating circuit patterns, sparks, and golden data particles. 
    8k resolution, cinematic lighting, epic atmosphere. 
    """
    
    try:
        response = model.generate_content(prompt)
        for part in response.candidates[0].content.parts:
            if hasattr(part, 'inline_data') and part.inline_data:
                img = PIL.Image.open(io.BytesIO(part.inline_data.data))
                save_path = os.path.join(ASSETS_DIR, "repo_header.png")
                img.save(save_path)
                print(f" => Success: {save_path}")
                break
    except Exception as e:
        print(f" => Error: {e}")

if __name__ == "__main__":
    generate_github_header()
