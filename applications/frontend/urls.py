from django.urls import path

from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.AppHome.as_view(), name='home'),
    path('search/', views.AppSearch.as_view(), name='search'),
    path('details/<app_id>/', views.AppDetails.as_view(), name='details')
]