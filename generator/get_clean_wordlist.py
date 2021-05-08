from generator import modify_wordlist

def main():
    input_file_path, output_file_name = modify_wordlist.get_file_path()
    input_wordlist = modify_wordlist.load_input(input_file_path)
    modify_wordlist.clean_wordlist(input_file_path,
                                   output_file_name + '.txt')
    print("\n[+] Done!!!")
    print("[+] Output file name: {}.txt".format(
                                             output_file_name + '.txt'))
