from rest_framework import serializers
from outils_veille_app.models import Company, Category, User, Article, Like, Favorite, Favorite_content, Share

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'city', 'country', 'postal_code', 'active']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def update(self, instance, validated_data):
        # Update instance with validated data
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.save()
            
        return super().update(instance, validated_data)
    
        
    
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_by', 'updated_by', 'created_at', 'updated_at', 'active']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        # Update instance with validated data
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        
        
        instance.save()
    
        return super().update(instance, validated_data)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'city', 'country', 'postal_code', 'password', 'created_by', 'updated_by', 'created_at', 'updated_at', 'active']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def update(self, instance, validated_data):
        # Update instance with validated data
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.save()
        
        return super().update(instance, validated_data)
    
    
class ArticleSerializer(serializers.ModelSerializer):
    #id, title, category_id, created_by, updated_by, created_at, updated_at, active

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'created_by', 'updated_by', 'created_at', 'updated_at', 'active']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def update(self, instance, validated_data):
        # Update instance with validated data
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        
        return super().update(instance, validated_data)
    
    
class LikeSerializer(serializers.ModelSerializer):
    # id, id_user, id_article, created_at
    class Meta:
        model = Like
        fields = ['id', 'id_user', 'id_Article', 'created_at']
        read_only_fields = ['id', 'created_at']
        
    def update(self, instance, validated_data):
        instance.id_user = validated_data.get('id_user', instance.id_user)
        instance.id_article = validated_data.get('id_Article', instance.id_article)
        instance.save()
        
        return super().update(instance, validated_data)
        
    
    


class FavoriteSerializer(serializers.ModelSerializer):
    #id, id_user, id_Article, created_at

    class Meta: 
        Model = Favorite
        fields = ['id', 'id_user', 'id_article', 'created_at']
        read_only_fields = ['id', 'created_at']
        
        
    def updated(self, instance, validated_data):
        instance.id_user = validated_data.get('id_user', instance.id_user)
        instance.id_article = validated_data.get('id_article', instance.id_artiicle)
        instance.save()
        
        return super().update(instance, validated_data)
        
        
        
        
class Favorite_contentSerializer(serializers.ModelSerializer):
    # id, id_user, id_category

    class Meta:
        Model = Favorite_content
        fields = ['id', 'id_user', 'id_category']
        read_only_fields = ['id', 'id_user', 'id_category']
        
    def update(self, instance, validated_data):
        instance.id_user = validated_data.get('id_user', instance.id_user)
        instance.id_category = validated_data.get('id_category', instance.id_category)
        instance.save()
        
        return super().update(instance, validated_data)
    
    
    
class ShareSerializer(serializers.ModelSerializer):
    # id, id_user, id_article, shared_at
    
    class Meta: 
        model = Share
        fields = ['id', 'id_user', 'id_article', 'shared_at']
        read_only_fields = ['id', 'id_user', 'id_article', 'shared_at']
        
    def update(self, instance, validate_data):
        instance.id_article = validate_data('id_article', instance.id_article)
        instance.save()
        
        return super().update(instance, validate_data)
    
    