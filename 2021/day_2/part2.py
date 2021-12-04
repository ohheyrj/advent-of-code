with open('input', 'r') as file:
    commands = []
    for l in file.readlines():
        commands.append((l.rstrip().split(' ')))
    aim = 0
    horizontal = 0
    depth = 0

    for c in commands:
        command = c[0]
        number = int(c[1])

        if command == 'forward':
            horizontal = horizontal + number
            depth = depth + (aim * number)
        elif command == 'down':
            aim = aim + number
        elif command == 'up':
            aim = aim - number
        else:
            print('opps')

    print(f'Depth: {depth}')
    print(f'Horizontal: {horizontal}')
    print(f'Aim: {aim}')

    print(f'Answer: {depth * horizontal}')