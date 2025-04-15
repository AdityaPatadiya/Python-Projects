from faker import Faker
import random

fake = Faker()

available_keys = {
    "name": fake.name,
    "email": fake.email,
    "age": lambda: fake.random_int(18, 60),
    "address": lambda: fake.address().replace("\n", ", "),
    "phone": fake.phone_number,
    "company": fake.company,
    "job": fake.job,
    "date_of_birth": fake.date_of_birth,
    "salary": lambda: round(random.uniform(30000, 150000), 2),
    "username": fake.user_name,
}


def generate_advanced_dummy_data():
    print("\nAvailable Fields:")
    for i, key in enumerate(available_keys.keys(), start=1):
        print(f"{i}. {key}")

    selections = input("\nEnter the field number or name you want (comma separated): ").replace(" ", "").split(',')

    selected_keys = []

    for item in selections:
        if item.isdigit():
            idx = int(item) - 1
            if 0 <= idx < len(available_keys):
                selected_keys.append(list(available_keys.keys())[idx])
        elif item in available_keys:
            selected_keys.append(item)
    
    selected_keys = list(dict.fromkeys(selected_keys))

    dummy_data = {key: available_keys[key]() for key in selected_keys}

    print("\nDummy data Genereated:")
    for k, v in dummy_data.items():
        print(f"{k}: {v}")

generate_advanced_dummy_data()
