import re

from config import translation_map


# Returns a list of possible words in english font, for a given
# non-english unicode string
def convert_word(input_word, translation_map):
    wordmap = []
    wordlist = []
    for char in input_word:
        try:
            wordmap.append(translation_map[char])
        except KeyError:
            wordmap.append([char])
    while True:
        if len(wordmap) == 1:
            break
        wordmap[0] = [i + j for i in wordmap[0] for j in wordmap[1]]
        wordmap.pop(1)
    for word in wordmap[0]:
        while '<REPEAT>' in word:
            replacement_char = word[word.find('<REPEAT>')-1]
            word = word.replace('<REPEAT>', replacement_char, 1)
        wordlist.append(re.sub('.<DELETE>', '', word))
    if not input_word.endswith('ा'):
        for output_word in wordlist:
            if output_word.endswith('a'):
                wordlist.append(output_word[:-1])
    return wordlist


# Outputs Wordlist with english font for given non-english unicode font
# worldlist
def write_wlist(nepali_wordlist_path, translation_map, output_file_path):
    with open(nepali_wordlist_path, encoding="utf8") as f:
        nepali_wordlist = [line.rstrip() for line in f]
    nepali_wordlist = list(set(nepali_wordlist))
    f = open("{}.txt".format(output_file_path), "w", encoding="utf8")
    for nepali_word in nepali_wordlist:
        translations = []
        for english_word in convert_word(nepali_word, translation_map):
            print(english_word)
            translations.append(english_word)
        translations = list(set(translations))
        translations.sort()
        for translation in translations:
            f.write(translation + '\n')
    f.close()


def check_chars(wordlist_path):
    with open(wordlist_path, encoding="utf8") as f:
        wordlist = [line.rstrip() for line in f]
    charlist = []
    for word in wordlist:
        temp_charlist = list(word)
        for char in temp_charlist:
            if char not in charlist:
                charlist.append(char)
    print(
        "\n[+] Following chars are present in your output wordlist: \n", charlist)
    print("[+] If any characters haven't been converted, revise the 'translation_map' ")


def get_file_path():
    input_file_path  = input("> Enter the Nepali Wordlist Path: ")
    output_file_name = input("> Set Output File Name: ")
    if input_file_path.startswith('"') and input_file_path.endswith('"'):
        input_file_path = input_file_path[1:-1]
    return input_file_path, output_file_name


def main():
    print("[+] Please modify the translation map in config.py file ")
    print("[+] according to your language to define the rules to follow ")
    print("[+] during translation. By default the translation only works ")
    print("[+] for Nepali and possibly other South Asian languages.")
    print("[+] First Convert your Nepali wordlist to unicode if it isn't, from here:")
    print("[+] https://subtitletools.com/convert-text-files-to-utf8-online\n")
    nepali_wordlist_path, output_file_path = get_file_path()
    write_wlist(nepali_wordlist_path, translation_map, output_file_path)
    check_chars("{}.txt".format(output_file_path))
    print("\n[+] Done!!!")
    print("[+] Output file name: {}.txt".format(output_file_path))


if __name__ == '__main__':
    main()
