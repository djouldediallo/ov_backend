import os
import django
from faker import Faker
from random import choice

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'outils_veille_project.settings')
django.setup()

from django.contrib.auth import get_user_model
from outils_veille_app.models import Company, Category, Article, Like, Favorite, Favorite_content, Share

User = get_user_model()
fakegen = Faker()

def create_users(N=10):
    users = []
    for _ in range(N):
        unique_username = False
        while not unique_username:
            first_name = fakegen.first_name()
            last_name = fakegen.last_name()
            username = f"{first_name}.{last_name}{fakegen.random_int(min=1, max=9999)}"
            if not User.objects.filter(username=username).exists():
                unique_username = True

        email = fakegen.email()
        password = fakegen.password()

        user, created = User.objects.get_or_create(
            username=username,
            first_name=first_name, 
            last_name=last_name, 
            email=email
        )
        user.set_password(password)
        user.save()
        users.append(user)
    return users


def add_company(users):
    user = choice(users)

    name = fakegen.company()[:20]
    address = fakegen.address()[:50]
    city = fakegen.city()
    country = fakegen.country()[:20]
    postal_code = fakegen.postcode()

    company, created = Company.objects.get_or_create(
        name=name, 
        address=address, 
        city=city, 
        country=country, 
        postal_code=postal_code, 
        created_by=user, 
        updated_by=user
    )
    return company

def add_category(users):
    user = choice(users)

    name = fakegen.word()
    description = fakegen.text(max_nb_chars=50)

    category, created = Category.objects.get_or_create(
        name=name, 
        description=description[:50], 
        created_by=user, 
        updated_by=user
    )
    return category

def add_article(users):
    user = choice(users)

    title = fakegen.sentence()[:20]
    description = fakegen.text(max_nb_chars=100)

    article, created = Article.objects.get_or_create(
        title=title, 
        description=description[:50], 
        created_by=user, 
        updated_by=user
    )
    return article



def add_like(users):
    user = choice(users)
    article = add_article(users)

    like, created = Like.objects.get_or_create(
        created_by=user, 
        id_article=article
    )
    return like

def add_favorite(users):
    user = choice(users)
    article = add_article(users)

    favorite, created = Favorite.objects.get_or_create(
        created_by=user, 
        id_article=article
    )
    return favorite

def add_favorite_content(users):
    user = choice(users)
    category = add_category(users)

    favorite_content, created = Favorite_content.objects.get_or_create(
        created_by=user, 
        id_category=category
    )
    return favorite_content

def add_share(users):
    user = choice(users)
    article = add_article(users)

    share, created = Share.objects.get_or_create(
        created_by=user, 
        id_article=article
    )
    return share

def populate(N=5):
    users = create_users(N)
    for _ in range(N):
        add_company(users)
        add_category(users)
        add_article(users)

        add_like(users)
        add_favorite(users)
        add_favorite_content(users)
        add_share(users)

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(2000)
    print('Populating Complete')
