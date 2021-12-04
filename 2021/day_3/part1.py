with open('input', 'r') as file:
    input_lines = file.readlines()
    input_lines = [line.rstrip('\n') for line in input_lines]

    count = 0
    gamma_rate = ''
    epsilon_rate = ''
    while count != len(input_lines[0]):
        nums = []
        for l in input_lines:
            nums.append(l[count])
        count_of_1 = nums.count('1')
        count_of_0 = nums.count('0')

        print(f'Count 1: {count_of_1}, Count 0: {count_of_0}')

        if count_of_1 > count_of_0:
            gamma_rate = gamma_rate + '1'
            epsilon_rate = epsilon_rate + '0'
        else:
            gamma_rate = gamma_rate + '0'
            epsilon_rate = epsilon_rate + '1'

        count = count + 1
    
    print(f'Gamma: {int(gamma_rate, 2)}')
    print(f'Epsilon: {int(epsilon_rate, 2)}')
    print(f'Answer: {int(gamma_rate, 2) * int(epsilon_rate, 2)}')