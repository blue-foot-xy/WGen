from generator import (generate_wordlist, modify_wordlist,
                      nep_to_eng, get_clean_wordlist)

def main():
    while True:
        print("\n[+] Choose an option:")
        print("\n\n 1. Generate Wordlist from User Profile")
        print(" 2. Improve an existing Wordlist")
        print(" 3. Translate a Non-English (Deevanagari by default) Wordlist's script to English")
        print(" 4. Sort and Remove Duplicates from a Wordlist")
        print(" 5. Exit")

        option = input("\n> ")
        print('\n')

        if option=='1':
            generate_wordlist.main()
        elif option=='2':
            modify_wordlist.main()
        elif option=='3':
            nep_to_eng.main()
        elif option=='4':
            get_clean_wordlist.main()
        elif option=='5':
            break
        else:
            print("[-] Invalid Input")

if __name__ == '__main__':
    main()
