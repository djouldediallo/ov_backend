from django.urls import path
from .views import CompanyListView, CompanyOneView
from .views import CategoryListView, CategoryOneView
from .views import UserListView, UserOneView
from .views import ArticleListView, ArticleOneView
from .views import LikeListView, LikeOneView
from .views import FavoriteListView, FavoriteOneView
from .views import FavoriteContentListView, FavoriteContentOneView
from .views import ShareListView, ShareOneView 


urlpatterns = [
    path("companies/", CompanyListView.as_view(), name="api-company-list"),
    path("companies/<int:pk>/", CompanyOneView.as_view(), name="api-company-show"),
    path("categories/", CategoryListView.as_view(), name="api-category-list"),
    path("categories/<int:pk>/", CategoryOneView.as_view(), name="api-category-show"),   
    path("users/", UserListView.as_view(), name="api-user-list"),
    path("users/<int:pk>/", UserOneView.as_view(), name="api-user-show"),
    path("articles/", ArticleListView.as_view(), name="api-articles-list"),
    path("user/<int:pk>/", ArticleOneView.as_view(), name="api-articles-show"),
    path("user/likes/", LikeListView.as_view(), name="api-like-list"),
    path("user/likes/<int:pk>/", LikeOneView.as_view(), name="api-like-show"),
    path("user/favorites/", FavoriteListView.as_view(), name="api-like-list"),
    path("user/favorites/<int:pk>/", FavoriteOneView.as_view(), name="api-like-show"),
    path("user/favoriteContent/", FavoriteContentListView.as_view(), name="api-like-list"),
    path("user/favoriteContent/<int:pk>/", FavoriteContentOneView.as_view(), name="api-like-show"),
    path("user/shares/", ShareListView.as_view(), name="api-like-list"),
    path("user/shares/<int:pk>/", ShareOneView.as_view(), name="api-like-show"),
    
    
]
