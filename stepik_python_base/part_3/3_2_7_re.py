import sys
import re

pattern = r'cat'
for line in sys.stdin:
    string = line.rstrip()
    duplicates = re.findall(pattern, string)
    if len(duplicates) > 1:
        print(string)

'''
for line in sys.stdin:
    line = line.strip()
    if re.search(r"cat.*cat", line):
        print(line)
'''
# https://stepik.org/lesson/24470/step/7?unit=6776
