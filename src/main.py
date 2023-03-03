import requests


def main():
    # url = 'https://ourcommons.ca/en'
    url = 'https://ourcommons.ca/members/en/search'
    print('Sending request to {}'.format(url))
    response = requests.get(url)
    print(response.text)


if __name__ == "__main__":
    main()
