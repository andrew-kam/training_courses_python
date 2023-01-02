import re
# () содержимое скобок может повторяться
# | или (a|b)
pattern = r"(\w+)-\1"  # 1 - № группы
# string = "test-test"
string = "test-test chow-chow"
math = re.match(pattern, string)
print(math, '\n')

pattern = r"(\w+)-\1"
string = "test-test chow-chow"
duplicates = re.sub(pattern, r'\1', string)
print(duplicates, '\n')

pattern = r"((\w+)-\2)"
# pattern = r"(\w+)-\1"
string = "test-test chow-chow"
duplicates = re.findall(pattern, string)
print(duplicates)

# match = re.match(pattern, string)
# print(match.groups()) - вернет последние вхождения по каждой группе шаблона
# print(match.group(0)) - вернет последние вхождения по конкретной группе шаблона, 0 - по умолч