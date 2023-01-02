import re

x = re.match(r'text', "TEXT", re.IGNORECASE)  # игнор заглавные или строчные
print(x, '\n')

x = re.match(r"(te)*?xt", "TEXT", re.IGNORECASE | re.DEBUG)
print(x)
