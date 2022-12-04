import json
from random import randint


with open('works.json', 'r') as file:
    person = json.load(file)
    print(person['response']['items'])
    for item in person['response']['items']:
        print(item['first_name'], item['last_name'])
        del item['id']
        item['like'] = randint(100, 300)
    with open('new_work.json', 'w') as like:
        json.dump(person, like, indent=4, sort_keys=True)

