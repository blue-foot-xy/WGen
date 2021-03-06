""" Modify the values below to modify the rules followed by the program
while building your worldlist.
"""


# RULES FOR APPENDING AND PREPENDING NUMBERS
append_numbers_of_range = (0, 999)
prepend_numbers_of_range = (0, 999)
symbols_in_between_numbers_and_character = ['@'] # Given symbols will be put in
                                                 # the middle of digits & words
                                                 # Eg: ['@','_','-','#','.']


# RULES FOR APPENDING AND PREPENDING SYMBOLS
# The symbols mentioned will be jumbled around in all possible ways and
# be added
symbols_to_append = '!@#$%&*-_'
symbols_to_prepend = '!@#$%&*-_'
length_range_for_symbol_string = (1, 3)


# RULES FOR SUBITUTION
# Sometimes your target may apply substitution and use words like
# 'p@$$w0rd' instead of 'password' as their password.
# For such cases subsitution will be used as described below.
subsitution_rules = {
    'a' : ['@'],
    's' : ['$', '5'],
    'o' : ['0'],
    'i' : ['1'],
    'l' : ['1']
}


# RULES FOR APPENDING AND PREPENDING STRINGS
words_to_append = [
                   '1234',
                   'abc',
                   'abcd',
                   'ABC',
                   'ABCD',
                   'xyz',
                   'XYZ' ]
words_to_prepend = words_to_append # Choose different words to be
                                   # prepended if you wish to.
# Given symbols will be put in the middle of appended strings.
symbols_separating_joined_words = symbols_in_between_numbers_and_character


# RULES FOR JOINING RELATED WORDS
# You'll be asked to mention some closely related words about target
# that might come together in the same password. So while shuffling and
# joining them togethar following symbols will also be put in the middle
# of the related words.
symbols_to_join_related_words_with = symbols_in_between_numbers_and_character


# RULES FOR TRANSLATING NON-ENGLISH WORDLIST TO ENGLISH SCRIPT
# Mention all the possible subsitutions for your non-english characters
# here. If your target speaks language other than english, modify this
# dictionary accordingly, to get a output-worldlist containing their
# local words in english script.
# The following one is done for Nepali language.
translation_map = {

             # <REPEAT> gets subsituted with character before it
             # This is often done when '???' symbol appears in the word
             '???': ['', 'n', 'ng', '<REPEAT>'],

             '???': ['', 'n', 'm', 'ng', 'mg'],

             '???': ['', 'h'],

             '???': ['a'],

             '???': ['a', 'aa'],

             '???': ['i', 'e', 'ii', 'ee'],

             '???': ['i', 'e', 'ii', 'ee'],

             '???': ['u','uu', 'oo'],

             '???': ['u','uu', 'oo'],

             '???': ['ri'],

             '???': ['e'],

             '???': ['ai'],

             '???': ['o'],

             '???': ['au', 'ou'],

             '???': ['ka'],

             '???': ['kha'],

             '???': ['ga'],

             '???': ['gha'],

             '???': ['nga', 'na'],

             '???': ['cha'],

             '???': ['cha', 'chha'],

             '???': ['ja'],

             '???': ['jha'],

             '???': ['ja'],

             '???': ['ta'],

             '???': ['tha'],

             '???': ['da'],

             '???': ['dha'],

             '???': ['na', 'da'],

             '???': ['ta'],

             '???': ['tha'],

             '???': ['da'],

             '???': ['dha'],

             '???': ['na'],

             '???': ['pa'],

             '???': ['pha'],

             '???': ['ba'],

             '???': ['bha', 'va'],

             '???': ['ma'],

             '???': ['ya', 'ea'],

             '???': ['ra'],

             '???': ['la'],

             '???': ['wa', 'ba', 'va'],

             '???': ['sa', 'sha'],

             '???': ['sa', 'sha'],

             '???': ['sa', 'sha'],

             '???': ['ha'],

              # <DELETE> removes a character that comes before it
              # Following example demonstrates it's usecase:
              #     ???(ka) + ???(ri)  = kari   (X, not what we need)
              #     ka + <DELETE>ri = kri    (???, exactly what we need)

             '???': ['<DELETE>a', '<DELETE>aa'],

             '???': ['<DELETE>i', '<DELETE>ii', '<DELETE>e', '<DELETE>ee'],

             '???': ['<DELETE>i', '<DELETE>ii', '<DELETE>e', '<DELETE>ee'],

             '???': ['<DELETE>u', '<DELETE>uu', '<DELETE>oo'],

             '???': ['<DELETE>u', '<DELETE>uu', '<DELETE>oo'],

             '???': ['<DELETE>ri'],

             '???': ['<DELETE>e'],

             '???': ['<DELETE>ai'],

             '???': ['<DELETE>o'],

             '???': ['<DELETE>au'],

             '???': ['<DELETE>'],

             '???': ['om'],

             '???': ['0'],

             '???': ['1'],

             '???': ['2'],

             '???': ['3'],

             '???': ['4'],

             '???': ['5'],

             '???': ['6'],

             '???': ['7'],

             '???': ['8'],

             '???': ['9']
}
