from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Utilisation du modèle utilisateur par défaut de Django
User = get_user_model()

class Company(models.Model):
    #id, name, address, city, country, postal_code, created_by, updated_by, created_at, updated_at, active
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    created_by = models.ForeignKey(User, related_name='creator_of_companies', on_delete=models.CASCADE, blank=True, null=True)
    updated_by = models.ForeignKey(User, related_name='updater_of_companies', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'companies'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class Article(models.Model):
    #id, titre, description,created_by, created_by, created_at, updated_at, active
    id = models.AutoField(db_column='ID', primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, related_name='creator_of_article', on_delete=models.CASCADE, blank=True, null=True)
    updated_by = models.ForeignKey(User, related_name='updater_of_article', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'articles'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

class Category(models.Model):
    # id, name, description, created_by, updated_by, created_at, updated_at, active 
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, related_name='creator_of_categories', on_delete=models.CASCADE, blank=True, null=True)
    updated_by = models.ForeignKey(User, related_name='updater_of_categories', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Like(models.Model):
    # id, id_user, id_article, created_at, updated_at
    id = models.AutoField(db_column='ID', primary_key=True)
    created_by = models.ForeignKey(User, related_name='creator_of_like', on_delete=models.CASCADE, blank=True, null=True)
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='article_id', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'likes'
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return str(self.id)

class Favorite(models.Model):
    #id, id_user => changer par created_by , id_article, created_at updta
    id = models.AutoField(db_column='ID', primary_key=True)
    created_by = models.ForeignKey(User, related_name='creator_of_favorite', on_delete=models.CASCADE, blank=True, null=True)
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='article_id', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'favorites'
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return str(self.id)

class Favorite_content(models.Model):
    #id, id_user, id_category, created_at, updated_at
    id = models.AutoField(db_column='ID', primary_key=True)
    created_by = models.ForeignKey(User, related_name='creator_of_favorite_content', on_delete=models.CASCADE, blank=True, null=True)
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category_id', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'favorite_content'
        verbose_name = 'Favorite Content'
        verbose_name_plural = 'Favorite Contents'

    def __str__(self):
        return str(self.id)

class Share(models.Model):
    #id, id_user, id_article, shared_at
    id = models.AutoField(db_column='ID', primary_key=True)
    created_by = models.ForeignKey(User, related_name='creator_of_share', on_delete=models.CASCADE, blank=True, null=True)
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    shared_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shares'
        verbose_name = 'Share'
        verbose_name_plural = 'Shares'

    def __str__(self):
        return str(self.id)
