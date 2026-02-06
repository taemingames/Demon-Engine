import os
import requests
from openai import OpenAI

# API 키는 환경 변수나 설정 파일에서 관리하는 것을 권장합니다.
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class VisualGenerator:
    """마왕의 미학을 현실로 구현하는 비주얼 생성기"""
    
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.base_style = (
            "Masterpiece, ultra-high-end cinematic anime style, professional digital art, "
            "sophisticated lighting, clean and sharp linework, "
            "elegant color palette (deep midnight blue, refined gold), 8k resolution."
        )

    def generate_image(self, prompt, save_path, aspect_ratio="1024x1024"):
        """
        DALL-E 3를 통해 고품격 비주얼 자산을 생성합니다.
        (참고: DALL-E 3 API는 '1024x1024', '1024x1792', '1792x1024' 등을 지원)
        """
        full_prompt = f"{self.base_style} {prompt}"
        print(f"[AI Painter] Generating: {save_path}...")
        
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=full_prompt,
                size=aspect_ratio,
                quality="hd",
                n=1,
            )

            image_url = response.data[0].url
            img_data = requests.get(image_url).content
            
            with open(save_path, 'wb') as handler:
                handler.write(img_data)
                
            print(f" => Success: {save_path}")
        except Exception as e:
            print(f" => Error generating image: {e}")

if __name__ == "__main__":
    print("Record of Demon King: Visual Generation Module v1.0")
