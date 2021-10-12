from pyfiglet import figlet_format
from requests import get
from random import choice

url = "https://icanhazdadjoke.com/search"
defualt_text = figlet_format("Dad Joke Project", font="smslant")
print(defualt_text)


def print_joke():
    # specific search term
    term = input("Please enter the topic to search joke: \t")
    # fetching the api to list jokes for a specific search term
    response = get(
        url,
        headers={"Accept": "application/json"},
        params={"term": term}
    )

    data = response.json()
    if data['total_jokes'] == 0:
        print("Please enter valid search term",
              'red', 'on_cyan', attrs=['concealed'])
        print_joke()
    elif data['total_jokes'] > 0:
        print(
            f"You have fetched {data['total_jokes']} jokes and among those below joke is random one\n")
        print(choice(data['results'])['joke'])
        print()


print_joke()
