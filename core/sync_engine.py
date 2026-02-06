import os
import subprocess
import re

def get_speech_ranges(file_path, noise_threshold="-35dB", min_silence=0.2):
    """
    FFmpeg의 silencedetect 필터를 사용하여 실제 대화(발화)가 일어나는 구간을 탐지합니다.
    """
    cmd = ["ffmpeg", "-i", file_path, "-af", f"silencedetect=noise={noise_threshold}:d={min_silence}", "-f", "null", "-"]
    output = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8').stderr
    
    starts = [float(x) for x in re.findall(r"silence_start: ([\d\.]+)", output)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d\.]+)", output)]
    
    # 전체 길이 확인
    cmd_dur = ["ffprobe", "-i", file_path, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"]
    total_duration = float(subprocess.run(cmd_dur, capture_output=True, text=True).stdout.strip())
    
    ranges = []
    last_end = 0.0
    for s_start, s_end in zip(starts, ends):
        if s_start > last_end + 0.05: # 매우 짧은 구간도 포함
            ranges.append((last_end, s_start))
        last_end = s_end
    if last_end < total_duration - 0.05:
        ranges.append((last_end, total_duration))
    return ranges

def format_srt_time(seconds):
    """초 단위를 SRT 타임스탬프 형식(HH:MM:SS,mmm)으로 변환합니다."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds * 1000) % 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def create_synced_srt(script_lines, voice_file_path, output_srt_path, start_offset=0.0):
    """
    문장 리스트와 음성 파일을 분석하여 정밀 싱크가 적용된 SRT 파일을 생성합니다.
    """
    speech_ranges = get_speech_ranges(voice_file_path)
    
    # 챕터 내 총 글자 수 기반 비례 배분 (정밀 분석 대안)
    total_chars = sum(len(line) for line in script_lines)
    total_speech_duration = sum(e - s for s, e in speech_ranges)
    
    srt_entries = []
    current_speech_pointer = 0.0
    
    for i, text in enumerate(script_lines):
        char_ratio = len(text) / total_chars
        line_duration = char_ratio * total_speech_duration
        
        def map_speech_to_abs(speech_time):
            acc = 0.0
            for s, e in speech_ranges:
                seg_dur = e - s
                if acc + seg_dur >= speech_time:
                    return s + (speech_time - acc)
                acc += seg_dur
            return speech_ranges[-1][1] if speech_ranges else 0.0

        start_rel = map_speech_to_abs(current_speech_pointer)
        end_rel = map_speech_to_abs(current_speech_pointer + line_duration)
        
        start_ts = format_srt_time(start_offset + start_rel)
        end_ts = format_srt_time(start_offset + end_rel)
        
        srt_entries.append(f"{i+1}\n{start_ts} --> {end_ts}\n{text}\n")
        current_speech_pointer += line_duration
        
    with open(output_srt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_entries))
    
    return start_offset + get_duration(voice_file_path) # 다음 챕터용 오프셋 반환

def get_duration(file_path):
    cmd = ["ffprobe", "-i", file_path, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"]
    return float(subprocess.run(cmd, capture_output=True, text=True).stdout.strip())

if __name__ == "__main__":
    print("Record of Demon King: Precision Sync Engine v1.0")
