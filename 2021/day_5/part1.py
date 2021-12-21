import re
import numpy as np
        
def arrange_coords(x1: int, y1: int, x2: int, y2: int):
    """ Make sure coordinates go from L -> R and U -> D """
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    elif x1 == x2 and y1 > y2:
        y1, y2 = y2, y1
    return x1, y1, x2, y2

def is_diagonal(x1: int, y1: int, x2: int, y2: int) -> bool:
    """ Return true if line is diagonal """
    return any([x1 + y2 == y1 + x2, x1 + x2 == y1 + y2, x1 + y1 == x2 + y2])

def parse(puzzle_input):
    pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    data = []
    for line in puzzle_input:
        match = re.search(pattern, line)
        nums = [int(c) for c in match.groups()]
        x1, y1, x2, y2 = arrange_coords(*nums)
        data.append(([x1, y1], [x2, y2]))
    return data

def find_straight_lines(lines):
    straight_lines = []
    for l in lines:
        start, end = l
        x1, y1 = start
        x2, y2 = end
        if any([x1 == x2, y1 == y2]):
            straight_lines.append(l)
    return straight_lines

def make_grid(lines):
    x_values, y_values = [], []
    for line in lines:
        x_coord = line[0]
        y_coord = line[1]
        x_values.extend(x_coord)
        y_values.extend(y_coord)
    return np.zeros((max(y_values) + 1, max(x_values) + 1), dtype=int)

def mark_grid(grid: 'np.ndarray[int]', start: int, end: int, r: int,
              c: int) -> None:
    """ Update an array along rows or columns by one """
    for i in range(start, end):
        if r is not None and c is not None:
            # A hack to cancel out the negative value
            grid[abs(r)][c] += 1
            r += 1
            c += 1
        elif r is not None and c is None:
            grid[r][i] += 1
        elif c is not None and r is None:
            grid[i][c] += 1

def make_paths(grid, v):
    start_x, start_y = v[0]
    end_x, end_y = v[1]
    if is_diagonal(start_x, start_y, end_x, end_y):
        initial_point = start_x
        end_point = end_x + 1
        row = start_y if start_y < end_y else - start_y
        col = start_x
    # For horizontals
    elif start_y == end_y:
        initial_point = start_x
        end_point = end_x + 1
        row, col = start_y, None
    # For verticals
    elif start_x == end_x:
        initial_point = start_y
        end_point = end_y + 1
        row, col = None, start_x
    mark_grid(grid, initial_point, end_point, row, col)

def get_diagonals(lines):
    """ get 45 degree diagonal vents """
    diagonals = []
    for line in lines:
        if is_diagonal(line.start.x, line.start.y, line.end.x, line.end.y):
            diagonals.append(line)
    return diagonals

with open('input', 'r') as file:
    input_lines = file.readlines()
    input_lines = [line.rstrip('\n') for line in input_lines]
    file.close()
    
data = parse(input_lines)

def part1(data):
    straight_lines = find_straight_lines(data)
    grid = make_grid(straight_lines)
    for l in straight_lines:
        make_paths(grid, l)
    return np.count_nonzero(grid > 1)

def part2(data):
    lines = get_diagonals(data)
    print(lines)
    

# print(f'Part 1: {part1(data)}')

part2(data)