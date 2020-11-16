import re

patterns = ['term1', 'term2']

text= 'This is a string with term1, not not other'

# for patt in patterns"":
#     print("I m searching for:" +patt)
#
#     if re.search(patterns, text):
#         print("Match")
#     else:
#         print('No Match')

match = re.search('term1', text)
print(match.start())

split_term ='@'

email = 'user@gmail.com'
print(re.split(split_term, email))


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print('Searching for pattern {}'.format(pat))
        print(re.findall(pat, phrase))
        print('\n')


test_phrase = 'sdsd..sssddd..sddddddsdddd'
test_patterns=['sd*']
multi_re_find(test_patterns, test_phrase)

