import json
import glob

file_prefix = "user"

user1 = {
    'Name': 'Edward',
    'PasswordHash': 'test1',
    'Position': 'Developer',
    'skills': ['Java', 'Python', 'SQL']
}

user2 = {
    'Name': 'Alice',
    'PasswordHash': 'test2',
    'Position': 'Tester',
    'skills': ['Junit', 'Python Unittest', 'Mockito']
}

users = []
users.append(user1)
users.append(user2)

print("Dumping {} to json files".format(users))

for user, i in zip(users, range(1, len(users)+1)):
    filename = file_prefix + str(i) + ".json"
    with open(filename, mode='w', encoding='UTF-8') as file:
        json.dump(user, file)

print("Dump complete")

file_names = glob.glob("*.json")
users = []
print("Loading from json files {}".format(file_names))

for filename in file_names:
    with open(filename, mode='r', encoding='UTF-8') as file:
        user = json.load(file)
    users.append(user)

print("Loading {} complete".format(users))
