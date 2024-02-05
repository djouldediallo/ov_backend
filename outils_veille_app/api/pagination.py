from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class CompanyPagination(PageOffsetPagination):
    page_size = 2  # Définissez la limite par défaut pour Company

class CategoryPagination(PageNumberPagination):
    page_size = 3  # Définissez la taille de la page par défaut pour Category


class UserPagination(PageNumberPagination):
    page_size = 3  # Définissez la taille de la page par défaut pour User
    
    
class ArticlePagination(PageNumberPagination):
    page_size = 3  # Définissez la taille de la page par défaut pour Article
    
class LikePagination(PageNumberPagination):
    page_size = 3 # Définissez la taille de la page Article Liked 
    
    
class FavoritePagination(PageNumberPagination):
    page_size = 3 # Définissez la taille de la page Article Liked
    
    
class Favorite_contentPagination(PageNumberPagination):
    page_size = 3 
    
    


    


    
    

    

