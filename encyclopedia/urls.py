from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>/', views.my_entry, name='my_entry'),
    path('create/', views.create_entry, name='create_entry'),
    path('wiki/', SearchResultsView.as_view(), name='search_results'),
    path('random_entry/', views.random_entry, name='random_entry'),
    path('entry/<str:title>/update/', views.update_entry, name='update_entry'),
    path('detailentry/<str:title>/', views.detail_entry, name='detail_entry'),
]
