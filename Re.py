import re

pattern = r'spam'

match = re.search(pattern, 'eggsspamsausages')
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())