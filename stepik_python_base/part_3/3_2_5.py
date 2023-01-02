import re
import sys
pattern = r'\b(\w+)\1\b'  # находит слова, состоящее из двух одинаковых частей (тандемный повтор)
for line in sys.stdin:
    line = line.strip()
    if re.search(pattern, line):
        print(line)
