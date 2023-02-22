
import os
lst = []
for current_dir, dirs, files in os.walk('main'):
    for file in files:
        if file.split('.')[1] == 'py':
            lst.append(current_dir)
            break
lst.sort()
contents = '\n'.join(lst)

print(*lst)
print(contents)
with open('2_4_6_sample_ans.txt', 'w') as w:
    w.write(contents)

# https://stepik.org/lesson/24465/step/6?unit=6772
