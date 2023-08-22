from django.urls import path
from .views import user_registration, user_logout

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', user_registration, name='register'),
    path('logout/', user_logout, name='logout'),

    # This urls are for JWT authentication 
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
