from django.urls import path
from .views import carsListView,carsDetailView,carsCreateView,carsUpdateView,carsDeleteView

urlpatterns = [
    path('cars/', carsListView.as_view(), name='cars-list'),
    path('cars/<int:pk>/', carsDetailView.as_view(), name='cars-detail'),
    path('cars/create/', carsCreateView.as_view(), name='cars-create'),
    path('cars/<int:pk>/update/', carsUpdateView.as_view(), name='cars-update'),
    path('cars/<int:pk>/delete/', carsDeleteView.as_view(), name='cars-delete'),
]