from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from watchlist.api.permissions import IsAdminOrReadOnly,reviewUserorReadOnly
from watchlist.models import Show,StreamPlatform,Review
from .serializers import ShowSerializer,PlatformSerializer,ReviewSerializer


"""

Class Based Views 

"""

class Streaming_Platform_List(APIView):
    """
    List all movies, or create a new movie.
    """ 
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, format=None):
        platforms = StreamPlatform.objects.all()
        serializer = PlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Stream_Platform_Details(APIView):
    """
    Retrieve, update or delete a movie instance.

    """
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk, format=None):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({'Error': 'Platform Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({'Error': 'Platform Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PlatformSerializer(platform, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({'Error': 'Platform Not Found'}, status=status.HTTP_404_NOT_FOUND)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Show_List(APIView):
    """
    List all movies, or create a new movie.
    """
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, format=None):
        movies = Show.objects.all()
        serializer = ShowSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Show_Details(APIView):
    """
    Retrieve, update or delete a movie instance.
    """
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        try:
            movie = Show.objects.get(pk=pk)
        except:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShowSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            movie = Show.objects.get(pk=pk)
        except:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShowSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            movie = Show.objects.get(pk=pk)
        except:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()


    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        movie = Show.objects.get(pk=pk)

        user = self.request.user
        review_Queryset = Review.objects.filter(reviewer = user,showname=movie)
        if review_Queryset.exists():
            raise ValidationError("You have already posted a review for this movie")

        # Updating the average of ratings
        if movie.number_ratings == 0:
            movie.avg_ratings = serializer.validated_data['rating']
        else:
            movie.avg_ratings = (movie.avg_ratings + serializer.validated_data['rating'])/2

        # Updating the total number of ratings
        movie.number_ratings = movie.number_ratings + 1
        movie.save()

        serializer.save(showname=movie,reviewer = user  )



class ReviewList(generics.ListAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticated]
    
    serializer_class = ReviewSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(showname=pk)



class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [reviewUserorReadOnly]


