import json
from faker import Faker
import random

fake = Faker()

# List of common job types at a large software engineering firm
job_types = ["Software Engineer", "Data Scientist", "Product Manager", "System Analyst", "Network Administrator", "Database Administrator", "Web Developer", "UX Designer", "Quality Assurance Engineer"]

data = []

for _ in range(200):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"

    employee = {
        "model": "djangoapp.employee",
        "fields": {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": str(random.randint(1000000000, 9999999999)),
            "email": email,
            "role": random.choice(job_types)
        }
    }
    data.append(employee)

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"

    customer = {
        "model": "djangoapp.customer",
        "fields": {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": str(random.randint(1000000000, 9999999999)),
            "email": email,
            "company": fake.company()
        }
    }
    data.append(customer)

with open('seed_data.json', 'w') as f:
    json.dump(data, f)
