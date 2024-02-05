import os
import django
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

fakegen = Faker()

def create_fake_users(N=10):
    for _ in range(N):
        username = fakegen.user_name()
        email = fakegen.email()
        password = User.objects.make_random_password()
        User.objects.create_user(username=username, email=email, password=password)

def create_fake_groups(N=5):
    for _ in range(N):
        name = fakegen.word()
        Group.objects.get_or_create(name=name)

def create_fake_permissions(N=10):
    content_type = ContentType.objects.get_for_model(User)
    for _ in range(N):
        codename = fakegen.word()
        name = fakegen.sentence(nb_words=3)
        Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)

if __name__ == '__main__':
    print("Populating Django's default tables with fake data...Please Wait")
    create_fake_users(10)
    create_fake_groups(5)
    create_fake_permissions(10)
    print('Populating Complete')
