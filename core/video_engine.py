import os
import subprocess

class VideoEngine:
    def __init__(self):
        pass

    def get_duration(self, file_path):
        """FFprobe를 사용하여 미디어 파일의 길이를 초 단위로 반환합니다."""
        cmd = ["ffprobe", "-i", file_path, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return float(result.stdout.strip())

    def create_video_segment(self, img_path, voice_path, output_path, resolution="1920x1080", fps=30):
        """
        이미지와 음성을 결합하여 부드러운 줌 효과가 포함된 개별 영상 세그먼트를 생성합니다.
        """
        duration = self.get_duration(voice_path)
        # 매우 부드러운 줌인 효과 적용
        zoom_expr = "min(zoom+0.0005,1.5)"
        
        cmd = [
            "ffmpeg", "-y", "-loop", "1", "-i", img_path,
            "-vf", f"scale={resolution}:force_original_aspect_ratio=increase,crop={resolution},zoompan=z='{zoom_expr}':d={int(duration*fps)}:s={resolution}:fps={fps}",
            "-t", str(duration), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(fps), output_path
        ]
        subprocess.run(cmd)

    def assemble_final_video(self, segment_list, audio_path, bgm_path, srt_path, output_path):
        """
        생성된 세그먼트들을 결합하고, 배경음악과 자막을 입혀 최종 영상을 완성합니다.
        """
        # 세그먼트 리스트 파일 생성
        list_file = "segments.txt"
        with open(list_file, "w") as f:
            for s in segment_list:
                f.write(f"file '{s}'\n")

        # FFmpeg 결합 및 마스터링
        # primary_colour=&H00FFFF (황금색 계열 사이언)
        filter_complex = (
            f"[0:v]subtitles=filename='{srt_path}':force_style='FontSize=16,PrimaryColour=&H00FFFF,BorderStyle=1,Outline=1'[v]; "
            f"[1:a]volume=1.2[a1]; [2:a]volume=0.1[a2]; [a1][a2]amix=inputs=2:duration=first[a]"
        )

        cmd = [
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0", "-i", list_file,
            "-i", audio_path,
            "-i", bgm_path,
            "-filter_complex", filter_complex,
            "-map", "[v]", "-map", "[a]",
            "-c:v", "libx264", "-preset", "medium", "-pix_fmt", "yuv420p",
            output_path
        ]
        subprocess.run(cmd)
        if os.path.exists(list_file):
            os.remove(list_file)

if __name__ == "__main__":
    print("Record of Demon King: Video Assembly Engine v1.0")
    engine = VideoEngine()
