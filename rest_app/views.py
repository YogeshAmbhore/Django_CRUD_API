from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthorSerializer
from .models import Author


@api_view(['GET', 'POST'])
def get_home(request):
    if request.method == 'GET':
        data = Author.objects.all()
        serializer = AuthorSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def get_details(request, pk):
    if request.method == 'GET':
        data = Author.objects.get(id=pk)
        serializer = AuthorSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        try:
            author = Author.objects.get(id=pk)
        except Author.DoesNotExist:
            return Response({"detail": "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            author = Author.objects.get(id=pk)
        except Author.DoesNotExist:
            return Response({"detail": "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        
        author.delete()
        return Response({"details": "Author deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    return Response({"detail": "Method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)    