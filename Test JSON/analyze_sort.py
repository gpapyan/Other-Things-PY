import json


with open('group_people.json', 'r') as file:
    data = json.load(file)

    for group in data:
        id_group = group['id_group']
        count = 0
        for person in group['people']:
            print(id_group, person['year'])
            # print(sorted(person, key=lambda i: i['year']))



