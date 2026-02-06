#!/usr/bin/env python3
import time
import sys
import os
import random
from datetime import datetime

# 터미널 색상 코드
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_slow(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def show_banner():
    banner = f"""{Colors.FAIL}
    ██████╗ ███████╗███╗   ███╗ ██████╗ ███╗   ██╗
    ██╔══██╗██╔════╝████╗ ████║██╔═══██╗████╗  ██║
    ██║  ██║█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
    ██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
    ██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
    ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
    {Colors.ENDC}
    {Colors.BOLD}:: TAEMIN GAMES EMPIRE SYSTEM :: v1.0.0{Colors.ENDC}
    """
    print(banner)
    print(f"{Colors.CYAN}[SYSTEM] Initializing Neural Link...{Colors.ENDC}")
    time.sleep(1)
    print(f"{Colors.CYAN}[SYSTEM] Connecting to JARVIS Core... SUCCESS{Colors.ENDC}")
    time.sleep(0.5)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_banner()
    
    print("\n" + "="*50)
    print_slow(f"{Colors.BOLD}Awaiting Command from the Overlord...{Colors.ENDC}")
    print("="*50 + "\n")

    print(f"{Colors.GREEN}1. [Safe Mode]      Steady Growth (Risk: Low){Colors.ENDC}")
    print(f"{Colors.WARNING}2. [Viral Mode]     Aggressive Expansion (Risk: High){Colors.ENDC}")
    print(f"{Colors.BLUE}3. [Empire Check]   View Current Status{Colors.ENDC}")
    print(f"{Colors.FAIL}4. [System Exit]    Disconnect{Colors.ENDC}\n")

    try:
        choice = input(f"{Colors.BOLD}SELECT STRATEGY >> {Colors.ENDC}")
    except KeyboardInterrupt:
        print("\n\n[!] Force Shutdown Initiated.")
        sys.exit()

    if choice == '1':
        run_safe_mode()
    elif choice == '2':
        run_viral_mode()
    elif choice == '3':
        check_status()
    elif choice == '4':
        print(f"\n{Colors.CYAN}Goodbye, Master.{Colors.ENDC}")
        sys.exit()
    else:
        print(f"\n{Colors.FAIL}[ERROR] Invalid Command. Access Denied.{Colors.ENDC}")
        time.sleep(1)
        main()

def run_safe_mode():
    print(f"\n{Colors.GREEN}[*] Safe Mode Activated.{Colors.ENDC}")
    print_slow("Scanning market trends... [DONE]")
    print_slow("Filtering low-risk keywords... [DONE]")
    print_slow("Scheduling content upload (Interval: 24h)... [SET]")
    print(f"\n{Colors.BOLD}>> System is now running in background.{Colors.ENDC}")
    # 실제 로직 연동 부분 (추후 연결)

def run_viral_mode():
    print(f"\n{Colors.WARNING}[!] VIRAL MODE ACTIVATED. WARNING: TRAFFIC SURGE EXPECTED.{Colors.ENDC}")
    time.sleep(1)
    targets = ['Twitter', 'Reddit', 'YouTube Shorts', 'TikTok']
    for target in targets:
        print(f"[*] Targeting {target} algorithm...", end='')
        time.sleep(random.uniform(0.5, 1.5))
        print(f" {Colors.GREEN}LOCKED{Colors.ENDC}")
    
    print_slow(f"\n{Colors.FAIL}>> Deploying Memetic Agents...{Colors.ENDC}")
    # 실제 공격적 마케팅 로직 연동

def check_status():
    print(f"\n{Colors.BLUE}[*] Retrieve Empire Statistics...{Colors.ENDC}")
    # 기존 check_empire_status.py 등의 로직을 불러올 수 있음
    print(f"Current Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Subscribers: [FETCHING...]")
    print("Revenue Est: [FETCHING...]")
    input("\nPress Enter to return...")
    main()

if __name__ == "__main__":
    main()
