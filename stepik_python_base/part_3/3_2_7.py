import re
import sys

for line in sys.stdin:
    line = line.strip()
    fixed_typos = re.sub(r'\ba+\b', 'argh', line, count=1, flags=re.IGNORECASE)
    print(fixed_typos)
