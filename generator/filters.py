import itertools


# ADD STRING
def add_string(word, string_list=['@'], mode = 'append'):
    output=[]
    for entry in string_list:
        if mode == 'append':
            output.append(word + entry)
        elif mode == 'prepend':
            output.append(entry + word)
    return output


# ADD DIGITS
def add_digits(word, min_number = 0, max_number = 999, mode = 'append'):
    output=[]

    for num in range(min_number, max_number + 1):
        num = str(num)
        if mode == 'append':
            output.append(word + num)
        elif mode == 'prepend':
            output.append(num + word)

        max_digits = len(str(max_number))
        while len(num) < max_digits:
            num = '0' + num
            if mode == 'append':
                output.append(word + num)
            elif mode == 'prepend':
                output.append(num + word)
    return output


# ADD SYMBOLS
def add_symbols(word, min_length=2, max_length=4,
                symbols='!@#$%&*', mode = 'append'):
    output=[]
    for r in range(min_length, max_length + 1):
        for symbol in list(
            map(''.join, itertools.product(symbols, repeat=r))):
                if mode == 'append':
                    output.append(word + symbol)
                elif mode == 'prepend':
                    output.append(symbol + word)
    return output


# CHANGE CASING
def lowercase_all(word):
    return word.lower()

def uppercase_all(word):
    return word.upper()

def capitalize_first_letter_lowercase_rest(word):
    try:
        return word.upper()[0] + word.lower()[1:]
    except:
        return word

def lowercase_the_first_letter(word):
    try:
        return word.lower()[0] + word[1:]
    except:
        return word


def apply_subsitution(
        word,
        subsitution_rules={
            'a':['@'],
            's':['$','5'],
            'o':['0'],
            'i':['1'],
            'l':['1']}):
    output = []

    key_combo = []
    for r in range(1, len(subsitution_rules) + 1):
        key_combo += list(
            itertools.combinations(subsitution_rules, r = r))

    rules_combo = []
    for keys in key_combo:
        temp = {}
        for key in keys:
            temp[key] = subsitution_rules[key]
        rules_combo.append(temp)

    rules_combo_broken = []
    for rules in rules_combo:
        rules_combo_broken += [dict(zip(rules.keys(), (sub_item for sub_item in item)))
                                  for item in itertools.product(*rules.values())]

    for rules in rules_combo_broken:
        leet_word = ''
        for char in word:
            try:
                leet_word+=rules[char]
            except KeyError:
                leet_word+=char
        output.append(leet_word)

    return list(set(output))


def shuffle_and_join_words(words,
                           also_join_using = ['@'],
                           min_value_of_r=1,
                           max_value_of_r = None):
    output1 = []
    output2 = []
    output  = []

    # if value of r is not mentioned the maximum possible will be taken
    if not max_value_of_r:
        max_value_of_r = len(words)

    # finding all necessary permutations
    for r in range(min_value_of_r, max_value_of_r + 1):
        output1 += list(permutation_without_repeat(words, r=r))

    # joining
    for item in output1:
        output2.append(
            tuple(map(capitalize_first_letter_lowercase_rest, item)))
    for item in output1 + output2:
        output.append(''.join(item))
        for string in also_join_using:
            output.append(string.join(item))

    return list(set(output))


# Input Format DDMMYYYY
def process_birth_date(date):
    birthdates = [
        date[-2:], # YY
        date[-3:], # YYY
        date[-4:], # YYYY
        date[1:2], # XD
        date[3:4], # XM
        date[:2],  # DD
        date[2:4], # MM
    ]
    output = []
    for birthdates1 in birthdates:
        output.append(birthdates1)
        for birthdates2 in birthdates:
            if birthdates.index(birthdates1) != birthdates.index(
              birthdates2):
                output.append(birthdates1 + birthdates2)
                for birthdates3 in birthdates:
                    if (
                        birthdates.index(birthdates1) != birthdates.index(
                            birthdates2)
                        and birthdates.index(birthdates2) != birthdates.index(
                            birthdates3)
                        and birthdates.index(birthdates1) != birthdates.index(
                            birthdates3)
                    ):
                        output.append(birthdates1 + birthdates2 + birthdates3)
    return output


def permutation_without_repeat(iterable, r=None):
    previous = tuple()
    for p in itertools.permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p


def remove_words_with_symbols(words, symbols):
    output = words

    for word in words:
        for symbol in symbols:
            if symbol in word:
                output = [x for x in output if x != word]
    return output


def remove_words_with_capitals(words):
    output = words

    for word in words:
        if any(x.isupper() for x in word):
            output = [x for x in output if x != word]

    return output


# Turns string '<hello,hi><world,earth>' into a list
# ['helloworld', 'hiworld', 'helloearth', 'hiearth']
def all_choices(text):
    output = []
    tokens = (block2 for block1 in text.split('<')
                     for block2 in block1.split('>'))
    decisions = []
    literals = []
    try:
        while True:
            literal = next(tokens)
            literals.append(literal)
            options = next(tokens).split('/')
            decisions.append(options)
    except StopIteration:
        pass
    decisions.append(('',))
    for choices in itertools.product(*decisions):
        output.append(''.join(x for pair in zip(literals, choices)
                        for x in pair))
    return output
