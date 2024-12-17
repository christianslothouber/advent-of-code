def read_and_parse_file(filename):
    return open(filename, 'r').readlines()


def is_nice_string(string):
    vowels = 'aeiou'
    illegal = ['ab', 'cd', 'pq', 'xy']

    vowel_counter = len(list(filter(lambda c: c in vowels, string)))
    contains_double = any(filter(lambda c: c + c in string, string))
    contains_illegal = all(sub not in string for sub in illegal)

    return vowel_counter >= 3 and contains_double and contains_illegal


def is_real_nice_string(string):
    return has_two_pairs(string) and has_sandwich(string)


def has_two_pairs(string):
    for i in range(len(string) - 2):
        if string[i: i + 2] in string[i + 2:]:
            return True

    return False


def has_sandwich(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True

    return False


def solve():
    strings = read_and_parse_file('input.txt')

    nice_strings = list(filter(is_nice_string, strings))
    print(f'The number of nice strings is {len(nice_strings)}')

    real_nice_strings = list(filter(is_real_nice_string, strings))
    print(f'The number of really nice strings is {len(real_nice_strings)}')


if __name__ == '__main__':
    solve()
