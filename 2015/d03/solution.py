def read_and_parse_file(filename):
    return open(filename, 'r').read()


def visit_house(instruction, point):
    x, y = point

    if instruction == '>': x += 1
    if instruction == '<': x -= 1
    if instruction == '^': y += 1
    if instruction == 'v': y -= 1

    house = (x, y)

    return house


def find_visited_houses(instructions):
    santa = (0, 0)
    houses = {santa}

    for instruction in instructions:
        house = visit_house(instruction, santa)
        houses.add(house)
        santa = house

    return houses


def find_visited_houses_with_robot_santa(instructions):
    santa = (0, 0)
    robot = (0, 0)
    houses = {santa, robot}

    for index, instruction in enumerate(instructions):
        if index % 2 == 0:
            house = visit_house(instruction, santa)
            houses.add(house)
            santa = house
        else:
            house = visit_house(instruction, robot)
            houses.add(house)
            robot = house

    return houses


def solve():
    instructions = read_and_parse_file('input.txt')

    houses = find_visited_houses(instructions)
    print(f'Number of visited houses is {len(houses)}')

    houses = find_visited_houses_with_robot_santa(instructions)
    print(f'Number of visited houses together with Robot Santa is {len(houses)}')


if __name__ == '__main__':
    solve()
