from config import *
from generator.filters import *


imported = False
also_join_birthdate = False
birthdates = ['']


def get_file_path():
    input_file_path  = input("> Enter the Input Wordlist Path: ")
    output_file_name = input("> Set Output File Name: ")
    if (input_file_path.startswith('"')
       and input_file_path.endswith('"')):
        input_file_path = input_file_path[1:-1]
    return input_file_path, output_file_name


def load_input(input_file_path):
    with open(input_file_path, encoding="utf8") as f:
        input_wordlist = [line.rstrip() for line in f]
    input_wordlist = list(set(input_wordlist))
    return input_wordlist


def get_preference():
    preference = {}

    print("\n[+] Do you want to add combinations with capitalized first letter in list?(y/n): ")
    print("> i.e. combinations of type: Monkey, Apple")
    preference['capitalize'] = input("> ").lower()

    print("\n[+] Do you want to add combinations with all letters uppercased in the list?(y/n): ")
    print("> i.e. combinations of type: MONKEY, APPLE")
    preference['uppercase'] = input("> ").lower()

    print("\n[+] Do you want to add combinations with appended numbers in the list?(y/n): ")
    print("> i.e. combinations of type: monkey002, apple243")
    preference['append_num'] = input("> ").lower()

    print("\n[+] Do you want to add combinations with prepended numbers in the list?(y/n): ")
    print("> i.e. combinations of type: 32monkey, 010apple")
    preference['prepend_num'] = input("> ").lower()

    if preference['append_num'].startswith("y") or preference['prepend_num'].startswith("y"):
        print("\n[+] Do you want to add combinations with symbols in between numbers and words?(y/n): ")
        print("> i.e. combinations of type: 54@monkey, apple@921")
        preference['symbol+num'] = input("> ").lower()

    print("\n[+] Do you want to add combinations with appended symbols in the list?(y/n): ")
    print("> i.e. combinations of type: monkey#$, apple&%!")
    preference['append_symbols'] = input("> ").lower()

    print("\n[+] Do you want to add combinations with prepended symbols in the list?(y/n): ")
    print("> i.e. combinations of type: #$monkey, &%!apple")
    preference['prepend_symbols'] = input("> ").lower()

    print("\n[+] Do you want to add combinations with appended words in the list?(y/n): ")
    print("> i.e. combinations of type: monkeyXYZ, appleabc")
    preference['append_words'] = input("> ").lower()

    print("\n[+] Do you want to add combinations with prepended words in the list?(y/n): ")
    print("> i.e. combinations of type: ABCmonkey, xyzapple")
    preference['prepend_words'] = input("> ").lower()

    if (preference['append_words'].startswith("y")
       or preference['prepend_words'].startswith("y")
       or imported):
        print("\n[+] Do you want combinations with symbols in between joined words?(y/n): ")
        print("> i.e. combinations of type: monkey@XYZ, abcd@apple")
        preference['symbol+words'] = input("> ").lower()

    print("\n[+] Do you want combinations with subitutions(like a-->@, s-->$) performed on the characters in the list?(y/n): ")
    print("> i.e. combinations of type: m0nkey, @pple")
    preference['subsitute'] = input("> ").lower()

    return preference


def add_numbers_and_symbols(word, preference):

    output = [word]

    if preference['append_num'].startswith("y"):
        # append numbers
        output += add_digits(
            word,
            min_number = append_numbers_of_range[0],
            max_number = append_numbers_of_range[1],
            mode = 'append')

        # append symbols + numbers
        try:
            if preference['symbol+num'].startswith("y"):
                temp = []
                temp = add_string(
                    word,
                    string_list=symbols_in_between_numbers_and_character,
                    mode = 'append')
                for item in temp:
                    output += add_digits(
                        item,
                        min_number = append_numbers_of_range[0],
                        max_number = append_numbers_of_range[1],
                        mode = 'append')
        except KeyError:
            pass

    if preference['prepend_num'].startswith("y"):
        # prepend numbers
        output += add_digits(
            word,
            min_number = prepend_numbers_of_range[0],
            max_number = prepend_numbers_of_range[1],
            mode = 'prepend')

        # prepend numbers + symbols
        try:
            if preference['symbol+num'].startswith("y"):
                temp = []
                temp = add_string(
                   word,
                   string_list=symbols_in_between_numbers_and_character,
                   mode = 'prepend')
                for item in temp:
                    output += add_digits(
                        item,
                        min_number = prepend_numbers_of_range[0],
                        max_number = prepend_numbers_of_range[1],
                        mode = 'prepend')
        except KeyError:
            pass

    # append symbols
    if preference['append_symbols'].startswith("y"):
        output += add_symbols(
            word,
            min_length=length_range_for_symbol_string[0],
            max_length=length_range_for_symbol_string[1],
            symbols = symbols_to_append,
            mode = 'append')

    # prepend symbols
    if preference['prepend_symbols'].startswith("y"):
        output += add_symbols(
            word,
            min_length=length_range_for_symbol_string[0],
            max_length=length_range_for_symbol_string[1],
            symbols = symbols_to_prepend,
            mode = 'prepend')

    if preference['append_words'].startswith("y"):
        # append words
        output += add_string(
            word,
            string_list=words_to_append,
            mode = 'append')

        # append symbols + words
        try:
            if preference['symbol+words'].startswith("y"):
                temp = []
                temp = add_string(
                    word,
                    string_list=symbols_separating_joined_words,
                    mode = 'append')
                for item in temp:
                    output += add_string(
                        item,
                        string_list=words_to_append,
                        mode = 'append')
        except KeyError:
            pass

    if preference['prepend_words'].startswith("y"):
        # prepend words
        output += add_string(
             word,
             string_list=words_to_prepend,
             mode = 'prepend')

        # prepend words + symbols
        try:
            if preference['symbol+words'].startswith("y"):
                temp = []
                temp = add_string(
                    word,
                    string_list=symbols_separating_joined_words,
                    mode = 'prepend')
                for item in temp:
                    output += add_string(
                    item,
                    string_list=words_to_prepend,
                    mode = 'prepend')
        except KeyError:
            pass

    if preference['subsitute'].startswith("y"):
        # subsitute characters
        temp = []
        for password in output:
            temp += apply_subsitution(
                password,
                subsitution_rules=subsitution_rules)
        output += temp

    # when called by generate_wordlist module it may be necessary
    # to add target's birthdate to the list
    if also_join_birthdate:
        # append birthdate
        if preference['append_num'].startswith("y"):
            output += add_string(
                word,
                string_list=birthdates,
                mode = 'append')

            # append symbols + birthdate
            try:
                if preference['symbol+num'].startswith("y"):
                    temp = []
                    temp = add_string(
                        word,
                        string_list=symbols_separating_joined_words,
                        mode = 'append')
                    for item in temp:
                        output += add_string(
                        item,
                        string_list=birthdates,
                        mode = 'append')
            except KeyError:
                pass

        if preference['prepend_num'].startswith("y"):
            # prepend birthdate
            output += add_string(
                word,
                string_list=birthdates,
                mode = 'prepend')

            # prepend birthdate + symbols
            try:
                if preference['symbol+num'].startswith("y"):
                    temp = []
                    temp = add_string(
                        word,
                        string_list=symbols_separating_joined_words,
                        mode = 'prepend')
                    for item in temp:
                        output += add_string(
                            item,
                            string_list=birthdates,
                            mode = 'prepend')
            except KeyError:
                pass

    return output


def modify_wordlist(input_wordlist, preference, output_file_name):
    f = open("{}.txt".format(output_file_name), "w", encoding="utf8")
    for input_word in input_wordlist:
        output_words = []
        for output_word in add_numbers_and_symbols(input_word, preference):
            print(output_word)
            output_words.append(output_word)
        if any(x.isupper() for x in input_word):
            for output_word in add_numbers_and_symbols(input_word.lower(),
                                                       preference):
                print(output_word)
                output_words.append(output_word)
        if preference['uppercase'].startswith("y"):
            for output_word in add_numbers_and_symbols(input_word.upper(),
                                                       preference):
                print(output_word)
                output_words.append(output_word)
        try:
            if (preference['capitalize'].startswith("y") and
               not input_word[0].isupper()):
                for output_word in add_numbers_and_symbols(
                    capitalize_first_letter_lowercase_rest(input_word),
                                                           preference):
                    print(output_word)
                    output_words.append(output_word)
            output_words = list(set(output_words))
            output_words.sort()
        except:
            pass
        for output_word in output_words:
            f.write(output_word + '\n')
    f.close()


# Sorts and removes duplicates in the same path
def clean_wordlist(input_path, output_path):
    print("[+] Cleaning... ")
    with open(input_path, encoding="utf8") as f:
        wordlist = [line.rstrip() for line in f]
    wordlist = list(set(wordlist))
    wordlist.sort()
    with open(output_path, "w", encoding="utf8") as f:
        for word in wordlist:
            f.write(word + '\n')


def main():
    input_file_path, output_file_name = get_file_path()
    preference = get_preference()
    input_wordlist = load_input(input_file_path)

    modify_wordlist(input_wordlist, preference ,output_file_name)
    if input("\n[+] Sort & remove duplicates from the output wordlist(y/n): ").lower().startswith('y'):
        clean_wordlist(output_file_name+'.txt', output_file_name+'.txt')

    print("\n[+] Done!!!")
    print("[+] Output file name: {}.txt".format(output_file_name))
