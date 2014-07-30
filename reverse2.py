import re
print re.sub(r'[\-a-zA-Z0-9]+', lambda x: x.group(0)[::-1], raw_input())
