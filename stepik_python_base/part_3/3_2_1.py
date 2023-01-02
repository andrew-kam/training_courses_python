import sys
import re

pattern = r'cat'
for line in sys.stdin:
    string = line.rstrip()
    duplicates = re.findall(pattern, string)
    if len(duplicates) > 1:
        print(string)

'''
import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"cat.*cat", line):
        print(line)
        
        
import sys
import re
[print(line.rstrip()) for line in sys.stdin if len(re.findall(r"cat", line)) > 1]
'''