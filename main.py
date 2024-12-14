import requests


def solve(year, day, part, session):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session}
    response = requests.get(url, cookies=cookies)

    if response.status_code != 200:
        print(f"Fetching input failed with status code {response.status_code}")

    url = f"https://advent.fly.dev/solve/{year}/{day}/{part}"
    data = response.text
    response = requests.post(url, data=data)

    if response.status_code != 200:
        print(f"Solving failed with status code {response.status_code}")
        return

    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    answer = response.text
    form = {
        'level': part,
        'answer': answer
    }
    response = requests.post(url, cookies=cookies, data=form)

    if response.status_code != 200:
        print(f"Submitting failed with status code {response.status_code}")
        return

    if "that's the right answer" in response.text or 'Funny seeing you here' in response.text:
        print(f'The answer to year {year}, day {day}, part {part} is correct')
    else:
        print(f'The answer to year {year}, day {day}, part {part} is wrong')


def main():
    session = 'fill-with-your-session-cookie'

    for year in range(2015, 2023):
        for day in range(1, 25):
            for part in range(2):
                solve(year + 1, day + 1, part + 1, session)


if __name__ == '__main__':
    main()
