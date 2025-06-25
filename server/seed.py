# server/seed.py

#!/usr/bin/env python3

from faker import Faker
from app import app
from models import db, Pet

fake = Faker()

with app.app_context():
    print("Clearing pets table...")
    Pet.query.delete()

    print("Seeding pets table...")
    pets = []
    species_list = ['Dog', 'Cat', 'Hamster', 'Turtle', 'Chicken']

    for i in range(10):
        pet = Pet(
            name=fake.first_name(),
            species=fake.random_element(elements=species_list)
        )
        pets.append(pet)

    db.session.add_all(pets)
    db.session.commit()
    print("Done seeding.")
