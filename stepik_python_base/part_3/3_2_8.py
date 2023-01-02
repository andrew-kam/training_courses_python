import re
import sys

for line in sys.stdin:
    line = line.strip()
    fixed_typos = re.sub(r'\b(\w)(\w)', r'\2\1', line)
    print(fixed_typos)
