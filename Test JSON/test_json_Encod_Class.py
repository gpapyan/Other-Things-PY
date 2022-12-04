import json


# person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
#
#
# personJSON = json.dumps(person, indent=4, sort_keys=True)
#
# print(personJSON)
#
# # with open('person.json', 'w') as file:
# #     json.dump(person, file, indent=4) # sarquma JSON
#
#
# with open('person.json', 'r') as file:
#     person = json.load(file)
#     print(person)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Jack', 40)


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        return TypeError('Object not serializable')


userJSON = json.dumps(user, default=encode_user)
print(userJSON)
