import time
import sys
import random
from colorama import Fore, Style, init
from core.video_engine import VideoEngine
from core.visual_gen import VisualGenerator

# 초기화
init(autoreset=True)

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_system(text):
    print(f"{Fore.CYAN}[SYSTEM]{Style.RESET_ALL} {text}")

def print_success(text):
    print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} {text}")

def print_warning(text):
    print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {text}")

def main():
    print(Fore.RED + Style.BRIGHT + """
    ╔════════════════════════════════════════════════════╗
    ║                                                    ║
    ║           THE DEMON KING'S FACTORY v1.0            ║
    ║        Wealth Automation & Content Mining          ║
    ║                                                    ║
    ╚════════════════════════════════════════════════════╝
    """ + Style.RESET_ALL)
    
    time.sleep(1)
    print_system("Initializing Empire Protocols...")
    time.sleep(0.5)
    print_system("Connecting to Jarvis Core...")
    time.sleep(0.5)
    print_success("Connection Established. Latency: 2ms")
    
    print("\n" + Fore.MAGENTA + ">>> LOADING MODULES..." + Style.RESET_ALL)
    time.sleep(0.5)
    print(f"[{Fore.GREEN}OK{Style.RESET_ALL}] Video Engine")
    print(f"[{Fore.GREEN}OK{Style.RESET_ALL}] Visual Generator")
    print(f"[{Fore.GREEN}OK{Style.RESET_ALL}] Trend Analyzer")
    
    print("\n" + Fore.YELLOW + ">>> TARGET: YOUTUBE ALGORITHM" + Style.RESET_ALL)
    print_slow("Scanning trends... [||||||||||] 100%", 0.05)
    
    keywords = ["#Wealth", "#AI", "#Automation", "#Money"]
    target = random.choice(keywords)
    print_success(f"Target Acquired: {target}")
    
    print_system("Generating Content Assets...")
    # 시각적 연출을 위한 가짜 로딩
    total = 20
    for i in range(total + 1):
        time.sleep(0.1)
        percent = int((i / total) * 100)
        bar = '█' * i + '-' * (total - i)
        sys.stdout.write(f"\rProcess: [{Fore.BLUE}{bar}{Style.RESET_ALL}] {percent}%")
        sys.stdout.flush()
    print()
    
    print_success("Assets Generated.")
    print_system("Compiling Video Sequence...")
    time.sleep(1)
    
    print("\n" + Fore.RED + Style.BRIGHT + ">>> DEPLOYING TO NETWORK..." + Style.RESET_ALL)
    time.sleep(2)
    
    print_success("UPLOAD COMPLETE.")
    print(Fore.GREEN + """
    $$$ REVENUE STREAM ESTABLISHED $$$
    Next cycle in 5 seconds...
    """)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[SYSTEM] Halted by User.")
