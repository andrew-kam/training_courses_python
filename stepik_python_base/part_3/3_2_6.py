import re
import sys

for line in sys.stdin:
    line = line.strip()
    fixed_typos = re.sub(r'human', 'computer', line)
    print(fixed_typos)


