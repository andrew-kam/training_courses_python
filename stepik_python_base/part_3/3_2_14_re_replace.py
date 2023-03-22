import re
import sys

for line in sys.stdin:
    line = line.strip()
    fixed_typos = re.sub(r'\b(\w)(\w)', r'\2\1', line)
    print(fixed_typos)

# https://stepik.org/lesson/24470/step/14?auth=login&unit=6776
