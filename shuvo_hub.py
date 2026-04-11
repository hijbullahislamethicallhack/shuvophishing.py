import os
import sys

def banner():
    os.system('clear')
    print("\033[1;32m")
    print("  ##################################################")
    print("  #                                                #")
    print("  #        HIJBULLAH ISLAM'S CYBER TOOLKIT         #")
    print("  #       ---------------------------------        #")
    print("  #      DIGITAL MARKETING,SEO SPECIALIST          #")
    print("  #             & ETHICAL HACKER                   #")
    print("  ##################################################")
    print("\033[0m")

def install_all():
    banner()
    print("[*] Installing Required Packages & Tools...")
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install php python git wget curl -y")
    
    os.system("git clone https://github.com/htr-tech/zphisher.git")
    os.system("git clone https://github.com/thewhiteh4t/seeker.git")
    os.system("git clone https://github.com/techchipnet/CamPhish.git")
    
    os.system("git clone https://github.com/hijbullahislamethicallhack/hijbullah-ethical-hacking1.git")
    print("\n\033[1;32m[+] All tools (including SMS Bomber) installed!\033[0m")
    input("\nPress Enter to return to Menu...")

def main():
    while True:
        banner()
        print("[1] Facebook/Instagram Phishing (Zphisher)")
        print("[2] Camera Hack (CamPhish)")
        print("[3] IP & Exact Location Tracker (Seeker)")
        print("[4] SMS Bomber (Hijbullah Edition)")
        print("[5] Setup: Install/Update All Tools")
        print("[0] Exit")
        
        choice = input("\n\033[1;34m[?] Select an Option: \033[0m")
        
        if choice == '1':
            os.system("cd zphisher && bash zphisher.sh")
        elif choice == '2':
            os.system("cd CamPhish && bash camphish.sh")
        elif choice == '3':
            os.system("cd seeker && python3 seeker.py")
        elif choice == '4':
            
            if os.path.exists("hijbullah-ethical-hacking1"):
                
                os.system("cd hijbullah-ethical-hacking1 && python shuvo.py")
            else:
                print("\n[!] SMS Bomber not found. Run Option 5 first.")
                input("Press Enter...")
        elif choice == '5':
            install_all()
        elif choice == '0':
            sys.exit()
        else:
            print("\n[!] Invalid choice!")
            input("Press Enter...")

if __name__ == "__main__":
    main()
