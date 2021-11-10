people = [
    {"name": "Subas", "relation": "self"},
    {"name": "Ashok", "relation": "eldest brother"},
    {"name": "Krishna", "relation": "elder brother"}
]

people.sort(key=lambda person: person["relation"])

print(people)