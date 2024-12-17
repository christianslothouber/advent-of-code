import time
import os
import requests


def solve(year, day):
    puzzle = fetch_puzzle(year, day)

    if puzzle is None:
        return

    for part in [1, 2]:
        answer = fetch_answer(year, day, part, puzzle)

        if answer is not None:
            submit_answer(year, day, part, answer)
            wait()


def fetch_answer(year, day, part, puzzle):
    url = f'https://advent.fly.dev/solve/{year}/{day}/{part}'
    response = requests.post(url, data = puzzle)

    if response.status_code != 200:
        print(f'Solving failed with status code {response.status_code}')
        return None

    return response.text


def fetch_puzzle(year, day):
    session = os.getenv('SESSION_ID')

    if session is None:
        print('SESSION_ID is not set as environment variable')
        return None

    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cookies = { 'session': session }
    response = requests.get(url, cookies = cookies)

    if response.status_code != 200:
        print(f'Fetching input failed with status code {response.status_code}')
        return None

    return response.text


def submit_answer(year, day, part, answer):
    session = os.getenv('SESSION_ID')

    if session is None:
        print('SESSION_ID is not set as environment variable')
        return

    url = f'https://adventofcode.com/{year}/day/{day}/answer'
    cookies = { 'session': session }
    form = { 'level': part, 'answer': answer }

    response = requests.post(url, cookies = cookies, data = form)

    if response.status_code != 200:
        print(f'Submitting failed with status code {response.status_code}')
    elif "that's the right answer" in response.text:
        print(f'Submitted year {year}, day {day}, part {part} successfully')
    elif 'Did you already complete it?' in response.text:
        print(f'Year {year}, day {day}, part {part} already submitted')
    else:
        print(f'Submitting year {year}, day {day}, part {part} failed')


def wait():
    wait_time = 60
    print(f'Waiting for {wait_time} seconds...')
    time.sleep(wait_time)


def main():
    for year in range(2015, 2024 + 1):
        for day in range(1, 25 + 1):
            solve(year, day)


if __name__ == '__main__':
    main()
