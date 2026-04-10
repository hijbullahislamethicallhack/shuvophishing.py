import os
import sys

def banner():
    os.system('clear')
    print("\033[1;32m")
    print("  ##################################################")
    print("  #                                                #")
    print("  #  ("WELCOME TO HIJBULLAH ISLAM'S HACKING HUB")  #")
    print("  #       ---------------------------------        #")
    print("  #      DIGITAL MARKETING,SEO SPECIALIST          #")
    print("  #              & ETHICAL HACKER                  #")
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
    print("\n\033[1;32m[+] Setup Complete! Now you can use the tools.\033[0m")
    input("\nPress Enter to return to Menu...")

def main():
    while True:
        banner()
        print("[1] Facebook/Instagram Phishing (Zphisher)")
        print("[2] Camera Hack (CamPhish)")
        print("[3] IP & Exact Location Tracker (Seeker)")
        print("[4] Phone Info & Advanced Tracker")
        print("[5] Setup: Install All Tools (First Time Only)")
        print("[0] Exit")
        
        choice = input("\n\033[1;34m[?] Select an Option: \033[0m")
        
        if choice == '1':
            if os.path.exists("zphisher"):
                os.system("cd zphisher && bash zphisher.sh")
            else:
                print("\n[!] Please run Option 5 first to install tools.")
                input("Press Enter...")
        
        elif choice == '2':
            if os.path.exists("CamPhish"):
                os.system("cd CamPhish && bash camphish.sh")
            else:
                print("\n[!] Please run Option 5 first.")
                input("Press Enter...")

        elif choice == '3':
            if os.path.exists("seeker"):
                os.system("cd seeker && python3 seeker.py")
            else:
                print("\n[!] Please run Option 5 first.")
                input("Press Enter...")

        elif choice == '4':
            print("\n[*] Installing & Running PhoneInfoga for Hijbullah...")
            
            if not os.path.exists("PhoneInfoga"):
                os.system("git clone https://github.com/sundowndev/phoneinfoga.git")
                os.system("cd phoneinfoga && pip install -r requirements.txt")
            
          
            number = input("\n[?] Enter Phone Number with Country Code (e.g. +8801xxx): ")
            os.system(f"cd phoneinfoga && python3 phoneinfoga.py -n {number}")
            input("\nPress Enter to return to Menu...")

        elif choice == '5':
            install_all()
            
        elif choice == '0':
            print("\nGoodbye Hijbullah! See you again.")
            sys.exit()
        
        else:
            print("\n[!] Invalid choice! Try again.")
            input("Press Enter...")

if __name__ == "__main__":
    main()
