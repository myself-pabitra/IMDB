from django.urls import include,path
from .views import *
# from .views import movie_list,movie_Details



urlpatterns = [
    path('list/',Show_List.as_view(), name='movie-list'),
    path('<int:pk>/',Show_Details.as_view(), name='movie-details'),
    path('platform/',Streaming_Platform_List.as_view(), name='platform-list'), # Stream/
    path('platform/<int:pk>/',Stream_Platform_Details.as_view(), name='platform-details'),

    path('<int:pk>/review-create/',ReviewCreate.as_view(), name='review-create'), 
    #This URL will show review of a specific movie 
    path('<int:pk>/review/',ReviewList.as_view(), name='review-list'), 
    path('review/<int:pk>/',ReviewDetail.as_view(), name='review-details'),

    # path('review',Review_List.as_view(), name='review-list'),
    # path('review/<int:pk>/',ReviewDetail.as_view(), name='review-details'),


]

# urlpatterns = [
#     path('list/',movie_list, name='movie-list'),
#     path('<str:pk>/',movie_Details, name='movie-details'),
# ]
