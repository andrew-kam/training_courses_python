import re

# * - любое количество символа перед знаком включая ноль (r'ab*a')
# + - любое количество символа перед знаком больше ноля (r'ab+a')
# ? - ноль или одно вхождение символа перед знаком (r'ab?a')
# {} - конкретное число или диапазон вхождений символа перед знаком (r'ab{3}a')

pattern = r"ab{2,4}a"
string = "aa, aba, abba, abbba, abbbba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
print()

# r'a[ab]+?a] будет искать вхождение наименьшей длинны
pattern = r"a[ab]+?a"
string = "abaaba"
print(re.match(pattern, string))
print(re.findall(pattern, string))

