from collections import Counter


def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        line = file.read()

    numbers = list(map(int, line.split()))

    return numbers


def blink(stones):
    new_stones = Counter()

    for n, cnt in stones.items():
        if n == 0:
            new_stones[1] += cnt
            continue

        num_string = str(n)

        if len(num_string) % 2 == 0:
            mid = len(num_string) // 2
            left = int(num_string[:mid])
            right = int(num_string[mid:])

            new_stones[left] += cnt
            new_stones[right] += cnt

            continue

        new_stones[2024 * n] += cnt

    return new_stones


def run(stones, blinks):
    new_stones = Counter(stones)

    for b in range(blinks):
        new_stones = blink(new_stones)

    print(f'Total number of stones after {blinks} blinks is {sum(new_stones.values())}')


def solve():
    stones = read_and_parse_file('input.txt')

    run(stones, 25)
    run(stones, 75)


solve()
