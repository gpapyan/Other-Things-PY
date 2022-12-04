import json

with open('group_people.json', 'r') as file:
    data = json.load(file)

    maximum = 0
    max_group = None

    for group in data:
        id_group = group['id_group']
        count = 0
        for person in group['people']:
            # print(id_group, person)
            if person['gender'] == 'Female' and person['year'] > 1987:
                count += 1
                # print(id_group, person)
        if count > maximum:
            maximum = count
            max_group = id_group
        print(id_group, count)
    # print(max_group, maximum)

