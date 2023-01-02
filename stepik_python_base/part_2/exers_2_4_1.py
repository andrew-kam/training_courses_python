lines = []
with open('input_2_4_1.txt') as file_in, open('output_2_4_1.txt', "w") as file_out:
    for line in file_in:
        lines.append(line.rstrip())
    file_out.write('\n'.join(lines[-1::-1]))
