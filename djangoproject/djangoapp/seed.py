import json
from faker import Faker
import random

fake = Faker()

# List of common job types at a large software engineering firm
job_types = ["Software Engineer", "Data Scientist", "Product Manager", "System Analyst", "Network Administrator", "Database Administrator", "Web Developer", "UX Designer", "Quality Assurance Engineer"]

data = []

for _ in range(20):
    employee = {
        "model": "djangoapp.employee",
        "fields": {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "phone_number": str(random.randint(100000000, 999999999)),
            "email": fake.email(),
            "role": random.choice(job_types)
        }
    }
    data.append(employee)

    customer = {
        "model": "djangoapp.customer",
        "fields": {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "phone_number": str(random.randint(100000000, 999999999)),
            "email": fake.email(),
            "company": fake.company()
        }
    }
    data.append(customer)

with open('seed_data.json', 'w') as f:
    json.dump(data, f)
