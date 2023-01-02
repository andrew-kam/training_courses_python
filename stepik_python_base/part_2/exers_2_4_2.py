import os
lst = []
for current_dir, dirs, files in os.walk('main'):
    #print(current_dir, files)
    for file in files:
        if file.split('.')[1] == 'py':
            lst.append(current_dir)
            break
lst.sort()
contents = '\n'.join(lst)

print(*lst)
print(contents)
with open('sample_ans2.txt', 'w') as w:
    w.write(contents)
