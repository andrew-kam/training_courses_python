lines = []
with open('2_4_4_input.txt') as file_in, open('2_4_4_output.txt', "w") as file_out:
    for line in file_in:
        lines.append(line.rstrip())
    file_out.write('\n'.join(lines[-1::-1]))

# https://stepik.org/lesson/24465/step/4?unit=6772
