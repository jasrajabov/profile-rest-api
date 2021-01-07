from django.urls import path, include
from profiles_api import views
from  rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pokemon_viewset', views.TestViewSet, base_name='pokemon_viewset')


urlpatterns = [
    path('pokemon_apiview/', views.TestApiView.as_view(), name='pokemon_apiview'),
    path('', include(router.urls))
]
