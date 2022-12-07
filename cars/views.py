from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import cars


class carsListView(ListView):
    template_name = "cars/cars-list.html"
    model = cars


class carsDetailView(DetailView):
    template_name = "cars/cars-detail.html"
    model = cars


class carsCreateView(CreateView):
    template_name = "cars/cars-create.html"
    model = cars
    fields = ['type' ,'car_model', 'purchaser']


class carsUpdateView(UpdateView):
    template_name = "cars/cars-update.html"
    model = cars
    fields = ['type' ,'car_model', 'purchaser']


class carsDeleteView(DeleteView):
    template_name = "cars/cars-delete.html"
    model = cars
    success_url = reverse_lazy("cars-list")

