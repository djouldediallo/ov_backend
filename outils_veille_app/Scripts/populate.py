import os
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'outils_veille_project.settings')
django.setup()

from outils_veille_app.models import Company, Article, Category, Log, User, Like, Favorite, Favorite_content

fake = Faker()

def create_company(N):
    for _ in range(N):
        Company.objects.create(
            name=fake.company(),
            address=fake.address(),
            city=fake.city(),
            country=fake.country(),
            postal_code=fake.postcode(),
            created_by=User.objects.order_by('?').first(),
            updated_by=User.objects.order_by('?').first(),
        )

def create_article(N):
    for _ in range(N):
        Article.objects.create(
            title=fake.sentence(),
            description=fake.text(),
            created_by=User.objects.order_by('?').first(),
            updated_by=User.objects.order_by('?').first(),
        )

def create_category(N):
    for _ in range(N):
        Category.objects.create(
            name=fake.word(),
            description=fake.text(),
            created_by=User.objects.order_by('?').first(),
            updated_by=User.objects.order_by('?').first(),
        )

def create_log(N):
    for _ in range(N):
        Log.objects.create(
            id_user=User.objects.order_by('?').first(),
            action=fake.word(),
            comment=fake.sentence(),
        )

def create_user(N):
    for _ in range(N):
        User.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            city=fake.city(),
            country=fake.country(),
            postal_code=fake.postcode(),
            password=fake.password(),
            created_by=User.objects.order_by('?').first(),
            updated_by=User.objects.order_by('?').first(),
        )

def create_like(N):
    for _ in range(N):
        Like.objects.create(
            id_user=User.objects.order_by('?').first(),
            id_Article=Article.objects.order_by('?').first(),
        )

def create_favorite(N):
    for _ in range(N):
        Favorite.objects.create(
            id_user=User.objects.order_by('?').first(),
            id_Article=Article.objects.order_by('?').first(),
        )

def create_favorite_content(N):
    for _ in range(N):
        Favorite_content.objects.create(
            id_user=User.objects.order_by('?').first(),
            id_category=Category.objects.order_by('?').first(),
        )

if __name__ == '__main__':
    print("Populating the database... Please Wait")
    create_user(10)  # Create 10 users first, as they are needed for other models
    create_company(10)
    create_article(10)
    create_category(10)
    create_log(10)
    create_like(10)
    create_favorite(10)
    create_favorite_content(10)
    print("Populating Complete")
