import factory
from django.contrib.auth import get_user_model
from .models import Company, Article, Category, Log, User, Like, Favorite, Favorite_content

# Assuming your AUTH_USER_MODEL is the default Django User model
# If you have a custom user model, you should import and use that instead
UserModel = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModel

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    city = factory.Faker('city')
    country = factory.Faker('country')
    postal_code = factory.Faker('postalcode')
    password = factory.PostGenerationMethodCall('set_password', 'password123')

class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker('company')
    address = factory.Faker('address')
    city = factory.Faker('city')
    country = factory.Faker('country')
    postal_code = factory.Faker('postalcode')
    created_by = factory.SubFactory(UserFactory)
    updated_by = factory.SubFactory(UserFactory)

class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker('sentence')
    description = factory.Faker('text')
    created_by = factory.SubFactory(UserFactory)
    updated_by = factory.SubFactory(UserFactory)

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    description = factory.Faker('text')
    created_by = factory.SubFactory(UserFactory)
    updated_by = factory.SubFactory(UserFactory)

class LogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Log

    id_user = factory.SubFactory(UserFactory)
    action = factory.Faker('word')
    comment = factory.Faker('sentence')

class LikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Like

    id_user = factory.SubFactory(UserFactory)
    id_Article = factory.SubFactory(ArticleFactory)

class FavoriteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Favorite

    id_user = factory.SubFactory(UserFactory)
    id_Article = factory.SubFactory(ArticleFactory)

class FavoriteContentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Favorite_content

    id_user = factory.SubFactory(UserFactory)
    id_category = factory.SubFactory(CategoryFactory)
