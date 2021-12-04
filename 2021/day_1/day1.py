with open('input', 'r') as file:
    input_lines = file.readlines()
    input_lines = [int(line.rstrip()) for line in input_lines]

    running_count = 1
    increased = 0

    for n1, n2 in zip(input_lines, input_lines[1:]):
        if n1 < n2:
            increased += 1
    # while running_count != len(input_lines):
    #     if input_lines[running_count] > input_lines[running_count - 1]:
    #         increased = increased + 1
    #     else:
    #         decreased = decreased + 1
        
    #     running_count = running_count + 1

    print(f'Higher: {increased}')
