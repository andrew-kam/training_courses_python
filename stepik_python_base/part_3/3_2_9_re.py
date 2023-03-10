import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r'z.{3}z', line):  # r'z...z'
        print(line)

# https://stepik.org/lesson/24470/step/9?unit=6776
