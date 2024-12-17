import hashlib


def read_and_parse_file(filename):
    return open(filename, 'r').read()


def solve():
    find_digest_starting_with('00000')
    find_digest_starting_with('000000')


def find_digest_starting_with(prefix):
    key = read_and_parse_file('input.txt')

    for i in range(10_000_000):
        attempt = str(key + str(i))
        buffer = attempt.encode('utf-8')
        digest = hashlib.md5(buffer).hexdigest()

        if digest.startswith(prefix):
            print(f"Lowest integer with hash starting with '{prefix}' is {i}")
            break


if __name__ == '__main__':
    solve()
