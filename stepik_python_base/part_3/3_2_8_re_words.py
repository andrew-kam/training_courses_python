import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"\bcat\b", line):
        print(line)

# https://stepik.org/lesson/24470/step/8?unit=6776
