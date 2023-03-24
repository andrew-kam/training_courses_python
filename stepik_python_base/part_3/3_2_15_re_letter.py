import re
import sys

for line in sys.stdin:
    line = line.strip()
    fixed_typos = re.sub(r'(\w)\1+', r'\1', line)
    print(fixed_typos)

# https://stepik.org/lesson/24470/step/15?auth=login&unit=6776
