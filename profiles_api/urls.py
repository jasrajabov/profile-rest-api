from django.urls import path
from profiles_api import views

urlpatterns = [
    path('testapi/', views.TestApiView.as_view(), name='testapi')
]
