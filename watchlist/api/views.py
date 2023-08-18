from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics


from watchlist.models import Show,StreamPlatform,Review
from .serializers import ShowSerializer,PlatformSerializer,ReviewSerializer


"""

Class Based Views 

"""

class Streaming_Platform_List(APIView):
    """
    List all movies, or create a new movie.
    """ 
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

    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        movie = Show.objects.get(pk=pk)

        serializer.save(showlist=movie)



class ReviewList(generics.ListAPIView):
    
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(showlist=pk)



class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer





# class Review_List(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ReviewDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)




    








"""

 Function Based Views 

"""


# @api_view(['GET', 'POST'])
# def movie_list(request):

#     """
#     List all movies, or create a new movie.

#     """
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = WatchListSerializer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = WatchListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT','DELETE'])
# def movie_Details(request,pk):
#     """
#     Retrieve, update or delete a movie instance.

#     """
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except:
#             return Response({'Error':'Movie Not Found'},status=status.HTTP_404_NOT_FOUND)
#         serializer = WatchListSerializer(movie)
#         return Response(serializer.data)

#     """
#     Edit a movie by its title and description and return a Response the error message associated with the error message.

#     """
#     if request.method == 'PUT':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except:
#             return Response({'Error':'Movie Not Found to Edit'},status=status.HTTP_404_NOT_FOUND)
#         movie = Movie.objects.get(pk=pk)
#         serializer = WatchListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         """
#         Delete a movie by its title and return a Response the error message associated with the error message.

#         """

#     if request.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except:
#             return Response({'Error':'Movie Not Found to Delete'},status=status.HTTP_404_NOT_FOUND)
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
