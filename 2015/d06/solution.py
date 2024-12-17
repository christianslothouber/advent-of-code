import re


def read_and_parse_file(filename):
    instructions = []

    pattern = r'(toggle|turn off|turn on) (\d+),(\d+) through (\d+),(\d+)'

    with open(filename, 'r') as file:
        for line in file:
            match = re.match(pattern, line.strip())

            if match:
                command = match.group(1)
                start_coords = (int(match.group(2)), int(match.group(3)))
                end_coords = (int(match.group(4)), int(match.group(5)))

                instructions.append((command, start_coords, end_coords))

    return instructions


def execute_instruction_digital(instruction, lights):
    command, (x1, y1), (x2, y2) = instruction

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            match command:
                case 'toggle':
                    lights[x][y] = not lights[x][y]
                case 'turn off':
                    lights[x][y] = False
                case 'turn on':
                    lights[x][y] = True


def execute_instruction_analog(instruction, lights):
    command, (x1, y1), (x2, y2) = instruction

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            match command:
                case 'toggle':
                    lights[x][y] += 2
                case 'turn off':
                    lights[x][y] = max(lights[x][y] - 1, 0)
                case 'turn on':
                    lights[x][y] += 1


def count_lights(lights):
    return sum(sum(row) for row in lights)


def solve():
    instructions = read_and_parse_file('input.txt')

    part1(instructions)
    part2(instructions)


def part2(instructions):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]

    for instruction in instructions:
        execute_instruction_analog(instruction, lights)

    print(f'After following instructions, total brightness is {count_lights(lights)}')


def part1(instructions):
    lights = [[False for _ in range(1000)] for _ in range(1000)]

    for instruction in instructions:
        execute_instruction_digital(instruction, lights)

    print(f'After following instructions, {count_lights(lights)} lights are lit')


if __name__ == '__main__':
    solve()
