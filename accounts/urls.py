from .views import RegisterAPI
from django.urls import path, include
from knox import views as knox_views
from .views import LoginAPI



# router = routers.DefaultRouter()
# router.register('register',views.RegisterAPI, basename='Register')
# router.register('login',views.LoginAPI, basename='Login')


urlpatterns = [
    path('', RegisterAPI.as_view(), name='register'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'), 
]