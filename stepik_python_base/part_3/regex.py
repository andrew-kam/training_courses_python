import re

# print(re.match) # подходит ли строка или её начало под шаблон
# print(re.search) # находит первую подстроку под шаблон
# print(re.findall) # находит все подстроки под шаблон
# print(re.sub) # заменяет все подстроки под шаблон

# [] -- можно указать множество подходящих символов
# a[abc]c на 2й позиции может быть любой символ из указанных в скобках
# если есть несколько подходящий вхождений вернет самый длинный
# . ^ $ * + ? { } [ ] \ | ( ) -- метасимволы
# \d ~ [0-9] -- цифры
# \D ~ [^0-9] -- не цифры
# \s ~ [ \t\n\r\f\v] -- пробельные символы
# \S ~ [^ \t\n\r\f\v] -- не пробельные символы
# \w ~ [a-zA-Z0-9_] -- буквы + цифры + _
# \W ~ [^a-zA-Z0-9_] -- не

pattern = r"abc"
string = "babc"
match_object = re.match(pattern, string)
print(match_object)
print()

pattern = r"abc"
string = "babc"
match_object = re.search(pattern, string)
print(match_object)
print()

pattern = r"a.c"
string = "acc"
match_object = re.match(pattern, string)
print(match_object)
print()

string = "abc, a.c, aac, a-c, aBc, azc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)
