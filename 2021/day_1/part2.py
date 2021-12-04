with open('input', 'r') as file:
    input_lines = file.readlines()
    input_lines = [int(line.rstrip()) for line in input_lines]

    windows_size = 3

    values = []

    increased = 0

    for i in range(len(input_lines)- windows_size +1 ):
        values.append(sum(input_lines[i: i + windows_size]))

    for n1, n2 in zip(values, values[1:]):
        if n1 < n2:
            increased += 1

    print(f'Higher: {increased}')
