from collections import Counter

with open('input', 'r') as file:
    input_lines = file.readlines()
    input_lines = [line.rstrip('\n') for line in input_lines]

    position = 0
    oxygen_rate = input_lines
    co2_rate = input_lines
    while position < len(input_lines[0]):
        oxy_count_num = Counter([l[position] for l in oxygen_rate])
        co2_count_num = Counter([l[position] for l in co2_rate])
        print(co2_rate)
        if len(oxygen_rate) > 1:
            if oxy_count_num.get('1') >= oxy_count_num.get('0'):
                oxygen_rate = [l for l in oxygen_rate if l[position] == '1']
            else:
                oxygen_rate = [l for l in oxygen_rate if l[position] == '0']
        if len(co2_rate) > 1:
            if co2_count_num.get('1') < co2_count_num.get('0'):
                co2_rate = [l for l in co2_rate if l[position] == '1']
            else:
                co2_rate = [l for l in co2_rate if l[position] == '0']
        position += 1

    print(f'Oxygen Rate: {oxygen_rate} {int(oxygen_rate[0], 2)}')
    print(f'co2 Rate: {co2_rate} {int(co2_rate[0], 2)}')
    print(f'Answer: {int(oxygen_rate[0], 2) * int(co2_rate[0], 2)}')
