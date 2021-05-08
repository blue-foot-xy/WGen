from generator.filters import *
from config import *
import generator.modify_wordlist


# Asks user to input info about the target and returns a profile dictionary
def get_profile():
    print("[+] Insert the information about the target to make a dictionary")
    print("[+] If you don't know all the info, just hit enter when asked! ;)")
    print("\n[+] If you are not sure about any word's spelling put them inside tags")
    print("    Eg: If you're not sure if your word is spelled 'money' or 'manee' ")
    print("    Use: <money/manee> and both the spellings will be considered")
    print("\n[+] All spaces will be ignored but if you really want one use <SPACE> instead")

    # The following dictionary will store all info about the target
    profile = {}
    profile["people"] = []

    # Asking for target's names and birthdate
    target_name = input("> First Name: ").replace(' ', '').replace("<SPACE>", " ")
    target_surname = input("> Surname: ").replace(' ', '').replace("<SPACE>", " ")
    print("\nUse comma for separation if there are multiple middle names or nicknames")
    target_middlename = input("> Middle Name(s): ").replace(' ', '').replace("<SPACE>", " ").split(',')
    target_nickname = input("> Nickname(s): ").replace(' ', '').replace("<SPACE>", " ").split(',')
    target_birthdate = input("> Birthdate (DDMMYYYY): ").replace(' ', '')
    while len(target_birthdate) != 0 and len(target_birthdate) != 8:
        print("\n[-] You must enter 8 digits for birthday!")
        target_birthdate = input("> Birthdate (DDMMYYYY): ").replace(' ', '')
    profile["people"] += [clean_profile({
        'targetfirstname'       : target_name,
        'targetsurname'    : target_surname,
        'targetmiddlename' : target_middlename,
        'targetnickname'   : target_nickname,
        'targetbirthdate'  : target_birthdate
    })]
    print("\n")

    # Asking for partner's names and birthdate
    partner_name = input("> Partner's First Name: ").replace(' ', '').replace("<SPACE>", " ")
    partner_surname = input("> Partner's Surname: ").replace(' ', '').replace("<SPACE>", " ")
    print("\nUse comma for separation if there are multiple middle names or nicknames")
    partner_middlename = input("> Partner's Middle Name(s): ").replace(' ', '').replace("<SPACE>", " ").split(',')
    partner_nickname = input("> Partner's Nickname(s): ").replace(' ', '').replace("<SPACE>", " ").split(',')
    partner_birthdate = input("> Partner's Birthdate (DDMMYYYY): ").replace(' ', '')
    while len(partner_birthdate) != 0 and len(partner_birthdate) != 8:
        print("\n[-] You must enter 8 digits for birthday!")
        partner_birthdate = input("> Partner's Birthdate (DDMMYYYY): ").replace(' ', '')
    print("\n")
    profile["people"] += [clean_profile({
        'partnerfirstname'       : partner_name,
        'partnersurname'    : partner_surname,
        'partnermiddlename' : partner_middlename,
        'partnernickname'   : partner_nickname,
        'partnerbirthdate'  : partner_birthdate
    })]

    # Asking for names and birthdates of other people related to the target
    i = 1
    while True:
        continue_ = input("> Any more people related to target?(y/n): ").lower()
        if not continue_.startswith("y"):
            break
        name = input("> Person's First Name: ").replace(' ', '').replace("<SPACE>", " ")
        surname = input("> Person's Surname: ").replace(' ', '').replace("<SPACE>", " ")
        print("\nUse comma for separation if there are multiple middle names or nicknames")
        middlename = input("> Person's Middle Name(s): ").replace(' ', '').replace("<SPACE>", " ").split(',')
        nickname =  input("> Person's Nickname(s): ").replace(' ', '').replace("<SPACE>", " ").split(',')
        birthdate = input("> Person's Birthdate (DDMMYYYY): ").replace(' ', '')
        while len(birthdate) != 0 and len(birthdate) != 8:
            print("\n[-] You must enter 8 digits for birthday!")
            birthdate = input("> Person's Birthdate (DDMMYYYY): ").replace(' ', '')
        profile["people"] += [clean_profile({
            'firstname'  : name,
            'surname'    : surname,
            'middlename' : middlename,
            'nickname'   : nickname,
            'birthdate'  : birthdate
        })]
        print("\n")
        i += 1

    print("\n> If there are multiple pets separate the names by comma")
    profile["pet"] = input("> Pet's name(s): ").replace(' ', '').replace("<SPACE>", " ").split(',')
    profile["company"] = input("> Company's name(s): ").replace(' ', '').replace("<SPACE>", " ").split(',')
    print("\n\n")

    print("[+] INPUT SOME KEYWORDS RELATED TO THE TARGET")

    print("\n[+] Input a word & hit 'Enter', keep doing it until you're done")
    print("[+] Once completed leave a blank line, then the program will proceed")

    print("\n[+] Tips: If the words are related, enter them in same line by separating them with comma")
    print("[+] Words in the same line will be joined togethar in different ways")
    print("[+] Ex: If the target likes chips, bisucits and noodles enter: ")
    print("[+] chips, biscuits, noodles")
    print("[+] in the same line so that combinations such as: chipsbiscuits, noodlesChips123 can also be created")

    # Taking in other keywords related to tagret
    profile["words"] = []
    i = 0
    while True:
        words = input("> ").replace(" ", "").replace("<SPACE>", " ")
        if ',' in words:
            words = words.split(",")
        elif not words.replace(' ', ''):
            break
        else:
            words = [words]
        profile["words"].append(words)
        i += 1

    # Removing some blank entries forom the profile to prevent errors
    profile = clean_profile(profile)

    print("\nprofile = ", profile , '\n')

    return profile


# The functions wil add strings and multiple entries of lists, into a
# single 1 dimensional array
def join_strings_and_list(*args):
    output = []
    for item in args:
        if isinstance(item, list):
            output += item
        else:
            output.append(item)
    return output


# removes values that are blank strings (and lists with only blank
# strings) from a dictionary
def clean_profile(profile):
    output = {}
    for key in profile:
        if isinstance(profile[key], str):
            if profile[key].replace(' ', ''):
                output[key] = profile[key]
        elif isinstance(profile[key], list):
            for item in profile[key]:
                try:
                    if item.replace(' ', ''):
                        output[key] = profile[key]
                        break
                except AttributeError:
                    output[key] = profile[key]
        else:
            output[key] = profile[key]
    return output


# Takes the profile dictionary and uses the content to create a list of
# possible combinations
def get_wordlist_from_profile(profile):
    output = []
    firstnames = []

    for people in profile["people"]:
        # Permutating firstnames, middlesnames, secondname, nicknames
        # with r=2
        temp=[]
        for key in people:
            if "name" in key:
                temp += join_strings_and_list(people[key])
        temp = shuffle_and_join_words(temp, also_join_using = symbols_to_join_related_words_with, max_value_of_r = 2)
        output += temp
        # For targets with middle names permuatations with higher value
        # of r will also be done
        temp = []
        for key in people:
            if "name" in key and not "nick" in key:
                temp += join_strings_and_list(people[key])
        max_value_of_r = len(temp)
        if max_value_of_r >=3:
            temp=[]
            for key in people:
                if "name" in key:
                    temp += join_strings_and_list(people[key])
            temp = shuffle_and_join_words(
                temp,
                also_join_using = symbols_to_join_related_words_with,
                min_value_of_r = 3,
                max_value_of_r = max_value_of_r)
            output += temp
        # For permutaing all firstnames and nicknames with r=2
        for key in people:
            if "firstname" in key:
                firstnames.append(people[key])
            if "nickname" in key:
                firstnames += people[key]

    # Permutating person's name and pet's names togethar
    if "pet" in profile:
        temp=profile["pet"]
        for people in profile["people"]:
            for key in people:
                if "name" in key and not "sur" in key:
                    temp += join_strings_and_list(people[key], profile["pet"])
        temp = shuffle_and_join_words(
            temp,
            also_join_using = symbols_to_join_related_words_with,
            max_value_of_r = 2)
        output += temp

    # Permuatating person's name and company name
    if "company" in profile:
        temp=profile["company"]
        for people in profile["people"]:
            for key in people:
                if "targetfirstname" == key or "targetsurname"==key:
                    temp += join_strings_and_list(
                        people[key],
                        profile["company"])
        temp = shuffle_and_join_words(temp,
            also_join_using = symbols_to_join_related_words_with,
            max_value_of_r = 2)
        output += temp

    # Adding keywords to the output
    if "words" in profile:
        for words in profile["words"]:
            output += shuffle_and_join_words(
                words,
                also_join_using = symbols_to_join_related_words_with,
                max_value_of_r = 2)

    # Permutating all firstnames and nicknames with r=2
    output += shuffle_and_join_words(
        firstnames,
        also_join_using = symbols_to_join_related_words_with,
        max_value_of_r = 2)

    return list(set(output))


# Turns user entered birthdate into a string of possible numbers that
# could be put into the password
def process_birthdate_from_profile(profile):
    output =[]
    for people in profile["people"]:
        if 'birthdate' in people:
            output += process_birth_date(people['birthdate'])
        if 'targetbirthdate' in people:
            output += process_birth_date(people['targetbirthdate'])
        if 'partnerbirthdate' in people:
            output += process_birth_date(people['partnerbirthdate'])
    return output


# checks if there are any birthdates in the profile
def is_birthdate_present_in_profile(profile):
    answer = False
    for people in profile["people"]:
        if ('birthdate' in people
           or 'targetbirthdate' in people
           or 'partnerbirthdate' in people):
            answer = True
            break
    return answer


# Turns ['<hello,hi><world,earth>'] into ['helloworld','hiworld',
#                                         'helloearth','hiearth']
# Useful for processing words of which the user doesn't exactly know the
# right spelling
def process_alternatives(wordlist):
    output = []
    for word in wordlist:
        if '<' in word:
            output += all_choices(word)
        else:
            output.append(word)
    return output


def main():
    # Making the user input information about target, and building a
    # profile from it
    profile = get_profile()

    # Few global varibles of the module 'modify_wordlist' will be
    # changed so that it
    # will behave as it's required to here
    generator.modify_wordlist.imported = True
    if is_birthdate_present_in_profile(profile):
        generator.modify_wordlist.also_join_birthdate = True
        generator.modify_wordlist.birthdates = process_birthdate_from_profile(profile)

    # Asking for input and output wordlist path
    input_wordlist =  process_alternatives(
        get_wordlist_from_profile(profile))
    output_file_name = input("> Set Output File Name: ")
    preference = generator.modify_wordlist.get_preference()

    # If the user does not want words with capital letters they will be
    # stripped away
    if not preference['capitalize'].startswith("y"):
        input_wordlist = remove_words_with_capitals(input_wordlist)

    # If the user does not want words with symbols they will be stripped
    # away
    try:
        if not preference['symbol+words'].startswith("y"):
            input_wordlist = remove_words_with_symbols(
                input_wordlist,
                symbols_to_join_related_words_with)
    except KeyError:
        input_wordlist = remove_words_with_symbols(
            input_wordlist,
            symbols_to_join_related_words_with)

    # Generating the wordlist as per the profile and prefernces
    generator.modify_wordlist.modify_wordlist(
        input_wordlist,
        preference,
        output_file_name)

    # Prompting user if they want to sort the wordlist and
    # remove duplicates
    if input("\n> Sort & remove duplicates from the output wordlist(y/n): ").lower().startswith('y'):
        generator.modify_wordlist.clean_wordlist(
            output_file_name + '.txt',
            output_file_name + '.txt')

    print("\n[+] Done!!!")
    print("[+] Output file name: {}.txt".format(output_file_name))
