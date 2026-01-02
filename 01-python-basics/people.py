people = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 22,
    "David": 35,
    "Emma": 28,
    "Frank": 45,
    "Grace": 32,
    "Henry": 27,
    "Iris": 29,
    "Jack": 26
}

age_min=int(input("Age minimum ?"))

filtered={nom:age for nom,age in people.items() if age>=age_min}

print(f"Personnes avec âge >= {age_min} :")
for nom, age in filtered.items():
    print(f"  {nom}: {age} ans")

print(f"Total : {len(filtered)} personnes")
