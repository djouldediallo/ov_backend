from typing import Any
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Company, Category, Article, Favorite, Share, Favorite_content




User = get_user_model()


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'created_by', 'updated_by', 'created_at']
    fields = ['name', 'address', 'city', 'country', 'postal_code', 'active']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'active', 'created_by', 'updated_by']
    fields = ['name', 'description', 'active']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)
        
        
#id, titre, description,created_by, created_by, created_at, updated_at, active
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'description', 'created_by', 'active']
    fields = ['title', 'description', 'active']
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)
        
        
        


#id, id_user, id_article, created_at updta
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'id_article', 'created_at']
    fields = ['id_article']
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)    
        
        
        
        
#id, id_user, id_article, shared_at
@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'id_article', 'shared_at']
    fields = ['id_article']
    
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)      
        
        
        
        
#id, id_user, id_category, created_at, updated_at
@admin.register(Favorite_content)
class FavoriteContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'id_category', 'created_at', 'updated_at']
    fields = ['id_category']
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)
        





# Supprimez ou commentez la classe UsersAdmin, car le modèle User est déjà géré par Django
# @admin.register(User)
# class UsersAdmin(admin.ModelAdmin):
#    ...





# @admin.register(Share)
# class ShareAdmin(admin.ModelAdmin):
#     list_display = ['id', 'id_user', 'id_article', 'shared_at']
#     fields = []

#     def save_model(self, request, obj, form, change):
#         if not obj.pk:
#             obj.created_by = request.user
#         else:
#             obj.updated_by = request.user
#         super().save_model(request, obj, form, change)
