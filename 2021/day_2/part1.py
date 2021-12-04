with open('input', 'r') as file:
    commands = []
    for l in file.readlines():
        commands.append((l.rstrip().split(' ')))
    
    horizontal = 0
    depth = 0

    for c in commands:
        command = c[0]
        number = int(c[1])

        if command == 'forward':
            horizontal = horizontal + number
        elif command == 'down':
            depth = depth + number
        elif command == 'up':
            depth = depth - number
        else:
            print('opps')

    print(f'Depth: {depth}')
    print(f'Horizontal: {horizontal}')

    print(f'Answer: {depth * horizontal}')