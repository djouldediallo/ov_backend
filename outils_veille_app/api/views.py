from rest_framework.response import Response
from rest_framework.views import APIView
from outils_veille_app.api.serializers import CompanySerializer, CategorySerializer, UserSerializer, ArticleSerializer, LikeSerializer, FavoriteSerializer, Favorite_contentSerializer, ShareSerializer
from outils_veille_app.models import Company, Category, User, Article, Like, Favorite, Favorite_content, Share
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated





class CompanyListView(APIView):
    permission_classes = [IsAuthenticated]

    # Handle GET requests for the list of companies
    def get(self, request):
        # Retrieve all Company objects from the database
        queryset = Company.objects.all()
        # Serialize the data
        serializer = CompanySerializer(queryset, many=True)
        # Return the response
        return Response(serializer.data)    

    # Handle POST requests to add a new company
    def post(self, request):
        # Serialize the data received in the request
        serializer = CompanySerializer(data=request.data)
        # Check the validity of the data
        if serializer.is_valid():
            # Save the Company object to the database
            serializer.save()
            # Return the serialized data with status 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Define the view for handling a specific company
class CompanyOneView(APIView):
    permission_classes = [IsAuthenticated]

    # Handle GET requests for a specific company
    def get(self, request, pk):
        # Retrieve the specified company by primary key (pk), or return 404 error if not found
        company = get_object_or_404(Company, pk=pk)
        # Serialize the company
        serializer = CompanySerializer(company)
        # Return the serialized data
        return Response(serializer.data)
       
    # Handle PUT requests to update a specific company
    def put(self, request, pk):
        # Retrieve the specified company, or return 404 error if not found
        company = get_object_or_404(Company, pk=pk)
        # Serialize the data with the data from the request
        serializer = CompanySerializer(company, data=request.data)
        # Check the validity of the data
        if serializer.is_valid():
            # Save the changes
            serializer.save()
            # Return the updated serialized data
            return Response(serializer.data)
        # If the data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Handle DELETE requests to delete a specific company
    def delete(self, request, pk):
        # Retrieve the specified company, or return 404 error if not found
        company = get_object_or_404(Company, pk=pk)
        # Delete the company
        company.delete()
        # Return a response with no content and status 204
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    # Handle PATCH requests for a partial update of a specific company
    def patch(self, request, pk):
        # Retrieve the specified company, or return 404 error if not found
        company = get_object_or_404(Company, pk=pk)
        # Serialize the data with the data from the request, allowing partial update
        serializer = CompanySerializer(company, data=request.data, partial=True)
        # Check the validity of the partial data
        if serializer.is_valid():
            # Save the partial changes
            serializer.save()
            # Return the updated serialized data
            return Response(serializer.data)
        # If the partial data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
    
    
    
    
    


# Define the view for handling lists of categories

class CategoryListView(APIView):
    
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)    
        

    def post(self, request):
        serializer = CategorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Define the view for handling a specific category
class CategoryOneView(APIView):
    
    permission_classes = [IsAuthenticated]
    # Handle GET requests for a specific category
    def get(self, request, pk):
        # Retrieve the specified category by primary key (pk), or return 404 error if not found
        category = get_object_or_404(Category, pk=pk)
        # Serialize the category
        serializer = CategorySerializer(category)
        # Return the serialized data
        return Response(serializer.data)
    
    # Handle PUT requests to update a specific category
    def put(self, request, pk):
        # Retrieve the specified category, or return 404 error if not found
        category = get_object_or_404(Category, pk=pk)
        # Serialize the data with the data from the request
        serializer = CategorySerializer(category, data=request.data)
        # Check the validity of the data
        if serializer.is_valid():
            # Save the changes
            serializer.save()
            # Return the updated serialized data
            return Response(serializer.data)
        # If the data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Handle DELETE requests to delete a specific category
    def delete(self, request, pk):
        # Retrieve the specified category, or return 404 error if not found
        category = get_object_or_404(Category, pk=pk)
        # Delete the category
        category.delete()
        # Return a response with no content and status 204
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Handle PATCH requests for a partial update of a specific category
    def patch(self, request, pk):
        # Retrieve the specified category, or return 404 error if not found
        category = get_object_or_404(Category, pk=pk)
        # Serialize the data with the data from the request, allowing partial update
        serializer = CategorySerializer(category, data=request.data, partial=True)
        # Check the validity of the partial data
        if serializer.is_valid():
            # Save the partial changes
            serializer.save()
            # Return the updated serialized data
            return Response(serializer.data)
        # If the partial data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











# Define the view for handling lists of users
class UserListView(APIView):
    
    permission_classes = [IsAuthenticated]
    # Handle GET requests for the list of users
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)    
    
    # Handle POST requests to add a new user
    def post(self, request):
        # Serialize the data received in the request
        serializer = UserSerializer(data=request.data)
        # Check the validity of the data
        if serializer.is_valid():
            # Save the User object to the database
            serializer.save()
            # Return the serialized data with status 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Define the view for handling a specific user
class UserOneView(APIView):
    
    permission_classes = [IsAuthenticated]
    # Handle GET requests for a specific user
    def get(self, request, pk):
        # Retrieve the specified user by primary key (pk), or return 404 error if not found
        user = get_object_or_404(User, pk=pk)
        # Serialize the user
        serializer = UserSerializer(user)
        # Return the serialized data
        return Response(serializer.data)
    
    # Handle PUT requests to update a specific user
    def put(self, request, pk):
        # Retrieve the specified user, or return 404 error if not found
        user = get_object_or_404(User, pk=pk)
        # Serialize the data with the data from the request
        serializer = UserSerializer(user, data=request.data)
        # Check the validity of the data
        if serializer.is_valid():
            # Save the changes
            serializer.save()
            # Return the updated serialized data
            return Response(serializer.data)
        # If the data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Handle DELETE requests to delete a specific user
    def delete(self, request, pk):
        # Retrieve the specified user, or return 404 error if not found
        user = get_object_or_404(User, pk=pk)
        # Delete the user
        user.delete()
        # Return a response with no content and status 204
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # Handle PATCH requests for a partial update of a specific user
    def patch(self, request, pk):
        # Retrieve the specified user, or return 404 error if not found
        user = get_object_or_404(User, pk=pk)
        # Serialize the data with the data from the request, allowing partial update
        serializer = UserSerializer(user, data=request.data, partial=True)
        # Check the validity of the partial data
        if serializer.is_valid():
            # Save the partial changes
            serializer.save()
            # Return the updated serialized data
            return Response(serializer.data)
        # If the partial data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
   
   
   
   
   
   
   
   
   
# Define the view for handling lists of articles
class ArticleListView(APIView):
    
    permission_classes = [IsAuthenticated]
    # Handle GET requests for the list of articles
    def get(self, request):
        # Retrieve all Article objects from the database
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)    
    
    # Handle POST requests to add a new article
    def post(self, request):
        # Serialize the data received in the request
        serializer = ArticleSerializer(data=request.data)
        # Check the validity of the data
        if serializer.is_valid():
            # Save the Article object to the database
            serializer.save()
            # Return the serialized data with status 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Define the view for handling a specific article
class ArticleOneView(APIView):
    
    permission_classes = [IsAuthenticated]
    # Handle GET requests for a specific article
    def get(self, request, pk):
        # Retrieve the specified article by primary key (pk), or return 404 error if not found
        article = get_object_or_404(Article, pk=pk)
        # Serialize the article
        serializer = ArticleSerializer(article)
        # Return the serialized data
        return Response(serializer.data)
    
    # Handle PUT requests to update a specific article
    def put(self, request, pk):
        # Retrieve the specified article, or return 404 error if not found
        article = get_object_or_404(Article, pk=pk)
        # Serialize the data with the data from the request
        serializer = ArticleSerializer(article, data=request.data)
        # Check the validity of the data
        if serializer.is_valid():
            # Save the changes
            serializer.save()
            # Return the updated serialized data
            return Response(serializer.data)
        # If the data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Handle DELETE requests to delete a specific article
    def delete(self, request, pk):
        # Retrieve the specified article, or return 404 error if not found
        article = get_object_or_404(Article, pk=pk)
        # Delete the article
        article.delete()
        # Return a response with no content and status 204
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    # Handle PATCH requests for a partial update of a specific article
    def patch(self, request, pk):
        # Retrieve the specified article, or return 404 error if not found
        article = get_object_or_404(Article, pk=pk)
        # Serialize the data with the data from the request, allowing partial update
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # Check the validity of the partial data
        if serializer.is_valid():
            # Save the partial changes
            serializer.save()
            # Return the updated serialized data
            return Response(serializer.data)
        # If the partial data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
    
    
# Likes View
class LikeListView(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Like.objects.all()
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data)    
    
    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LikeOneView(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        article = get_object_or_404(Like, pk=pk)
        serializer = LikeSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = get_object_or_404(Like, pk=pk)
        serializer = LikeSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = get_object_or_404(Like, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        article = get_object_or_404(Like, pk=pk)
        serializer = LikeSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









# Favorites View
class FavoriteListView(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Favorite.objects.all()
        serializer = FavoriteSerializer(queryset, many=True)
        return Response(serializer.data)    
    
    def post(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FavoriteOneView(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        article = get_object_or_404(Favorite, pk=pk)
        serializer = FavoriteSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = get_object_or_404(Favorite, pk=pk)
        serializer = FavoriteSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = get_object_or_404(Favorite, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def patch(self, request, pk):
        article = get_object_or_404(Favorite, pk=pk)
        serializer = FavoriteSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
    
    

       
#Favorite_content View
class FavoriteContentListView(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = FavoriteContent.objects.all()
        serializer = FavoriteContentSerializer(queryset, many=True)
        return Response(serializer.data)    
    
    def post(self, request):
        serializer = FavoriteContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FavoriteContentOneView(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        article = get_object_or_404(FavoriteContent, pk=pk)
        serializer = FavoriteContentSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = get_object_or_404(FavoriteContent, pk=pk)
        serializer = FavoriteContentSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = get_object_or_404(FavoriteContent, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def patch(self, request, pk):
        article = get_object_or_404(FavoriteContent, pk=pk)
        serializer = FavoriteContentSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# class CompanyListView(APIView):
        
        
class ShareListView(APIView):
    permission_classes = [IsAuthenticated]

    # Handle GET requests for the list of Shares
    def get(self, request):
        # Retrieve all Share objects from the database
        queryset = Share.objects.all()
        # Serialize the data
        serializer = ShareSerializer(queryset, many=True)
        # Return the response
        return Response(serializer.data)    

    # Handle POST requests to add a new Share
    def post(self, request):
        # Serialize the data received in the request
        serializer = ShareSerializer(data=request.data)
        # Check the validity of the data
        if serializer.is_valid():
            # Save the Company object to the database
            serializer.save()
            # Return the serialized data with status 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Define the view for handling a specific company
class ShareOneView(APIView):
    permission_classes = [IsAuthenticated]

    # Handle GET requests for a specific company
    def get(self, request, pk):
        # Retrieve the specified Share by primary key (pk), or return 404 error if not found
        Share = get_object_or_404(Share, pk=pk)
        # Serialize the company
        serializer = ShareSerializer(Share)
        # Return the serialized data
        return Response(serializer.data)
       
    # Handle PUT requests to update a specific company
    def put(self, request, pk):
        # Retrieve the specified company, or return 404 error if not found
        Share = get_object_or_404(Share, pk=pk)
        # Serialize the data with the data from the request
        serializer = ShareSerializer(Share, data=request.data)
        # Check the validity of the data
        if serializer.is_valid():
            # Save the changes
            serializer.save()
            # Return the updated serialized data
            return Response(serializer.data)
        # If the data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Handle DELETE requests to delete a specific company
    def delete(self, request, pk):
        # Retrieve the specified company, or return 404 error if not found
        Share = get_object_or_404(Share, pk=pk)
        # Delete the company
        Share.delete()
        # Return a response with no content and status 204
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    # Handle PATCH requests for a partial update of a specific company
    def patch(self, request, pk):
        # Retrieve the specified company, or return 404 error if not found
        Share = get_object_or_404(Share, pk=pk)
        # Serialize the data with the data from the request, allowing partial update
        serializer = ShareSerializer(Share, data=request.data, partial=True)
        # Check the validity of the partial data
        if serializer.is_valid():
            # Save the partial changes
            serializer.save()
            # Return the updated serialized data
            return Response(serializer.data)
        # If the partial data is invalid, return the errors with status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
