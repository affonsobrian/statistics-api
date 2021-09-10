from factory import django, Faker
from statistics_api.users.models import User 

class UserFactory(django.DjangoModelFactory):

    class Meta:
        model = User

    username = Faker("user_name")
    password = Faker("password")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")
