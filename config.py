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
             # This is often done when 'ँ' symbol appears in the word
             'ँ': ['', 'n', 'ng', '<REPEAT>'],

             'ं': ['', 'n', 'm', 'ng', 'mg'],

             'ः': ['', 'h'],

             'अ': ['a'],

             'आ': ['a', 'aa'],

             'इ': ['i', 'e', 'ii', 'ee'],

             'ई': ['i', 'e', 'ii', 'ee'],

             'उ': ['u','uu', 'oo'],

             'ऊ': ['u','uu', 'oo'],

             'ऋ': ['ri'],

             'ए': ['e'],

             'ऐ': ['ai'],

             'ओ': ['o'],

             'औ': ['au', 'ou'],

             'क': ['ka'],

             'ख': ['kha'],

             'ग': ['ga'],

             'घ': ['gha'],

             'ङ': ['nga', 'na'],

             'च': ['cha'],

             'छ': ['cha', 'chha'],

             'ज': ['ja'],

             'झ': ['jha'],

             'ञ': ['ja'],

             'ट': ['ta'],

             'ठ': ['tha'],

             'ड': ['da'],

             'ढ': ['dha'],

             'ण': ['na', 'da'],

             'त': ['ta'],

             'थ': ['tha'],

             'द': ['da'],

             'ध': ['dha'],

             'न': ['na'],

             'प': ['pa'],

             'फ': ['pha'],

             'ब': ['ba'],

             'भ': ['bha', 'va'],

             'म': ['ma'],

             'य': ['ya', 'ea'],

             'र': ['ra'],

             'ल': ['la'],

             'व': ['wa', 'ba', 'va'],

             'श': ['sa', 'sha'],

             'ष': ['sa', 'sha'],

             'स': ['sa', 'sha'],

             'ह': ['ha'],

              # <DELETE> removes a character that comes before it
              # Following example demonstrates it's usecase:
              #     क(ka) + ृ(ri)  = kari   (X, not what we need)
              #     ka + <DELETE>ri = kri    (✓, exactly what we need)

             'ा': ['<DELETE>a', '<DELETE>aa'],

             'ि': ['<DELETE>i', '<DELETE>ii', '<DELETE>e', '<DELETE>ee'],

             'ी': ['<DELETE>i', '<DELETE>ii', '<DELETE>e', '<DELETE>ee'],

             'ु': ['<DELETE>u', '<DELETE>uu', '<DELETE>oo'],

             'ू': ['<DELETE>u', '<DELETE>uu', '<DELETE>oo'],

             'ृ': ['<DELETE>ri'],

             'े': ['<DELETE>e'],

             'ै': ['<DELETE>ai'],

             'ो': ['<DELETE>o'],

             'ौ': ['<DELETE>au'],

             '्': ['<DELETE>'],

             'ॐ': ['om'],

             '०': ['0'],

             '१': ['1'],

             '२': ['2'],

             '३': ['3'],

             '४': ['4'],

             '५': ['5'],

             '६': ['6'],

             '७': ['7'],

             '८': ['8'],

             '९': ['9']
}
