def read_and_parse_file(filename):
    dimensions = open(filename, 'r').readlines()
    dimensions = [line.split('x') for line in dimensions]
    dimensions = [list(map(int, line)) for line in dimensions]

    return dimensions


def calculate_required_paper(dimensions):
    footage = 0

    for dimension in dimensions:
        l, w, h = dimension

        surfaces = [l * w, l * w, w * h, w * h, h * l, h * l]

        smallest_surface = min(surfaces)
        required_paper = sum(surfaces)

        footage += required_paper + smallest_surface

    return footage


def calculate_required_ribbon(dimensions):
    footage = 0

    for dimension in dimensions:
        l, w, h = dimension

        perimeters = [2 * l + 2 * w, 2 * w + 2 * h, 2 * h + 2 * l]

        smallest_perimeter = min(perimeters)
        cubic_volume = l * w * h

        footage += smallest_perimeter + cubic_volume

    return footage


def solve():
    dimensions = read_and_parse_file('input.txt')

    required_paper = calculate_required_paper(dimensions)
    print(f'Packaging requires {required_paper} square feet of wrapping paper')

    required_ribbon = calculate_required_ribbon(dimensions)
    print(f'Packaging requires {required_ribbon} feet of ribbon')


if __name__ == '__main__':
    solve()
