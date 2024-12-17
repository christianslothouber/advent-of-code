def read_and_parse_file(filename):
    return open(filename, 'r').read()


def solve():
    instructions = read_and_parse_file('input.txt')
    part1(instructions)
    part2(instructions)


def part2(instructions):
    floor = 0

    for index, instruction in enumerate(instructions):
        if instruction == '(':
            floor += 1
        if instruction == ')':
            floor -= 1

        if floor < 0:
            print(f'Instruction {index + 1} take you to the basement')
            break


def part1(instructions):
    floor = 0

    for instruction in instructions:
        if instruction == '(':
            floor += 1
        if instruction == ')':
            floor -= 1

    print(f'Instructions take you to floor {floor}')


if __name__ == '__main__':
    solve()
