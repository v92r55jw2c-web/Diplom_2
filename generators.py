from faker import Faker

fake = Faker('en_US')

def generate_user_data():

    username = fake.user_name()
    email = f"{username}@{fake.free_email_domain()}"
    password = fake.password(length=12, special_chars=True)
    
    return {
        "email": email,
        "password": password,
        "name": username
    }
