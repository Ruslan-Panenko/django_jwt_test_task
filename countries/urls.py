from django.urls import path
from countries.views import CountriesView

urlpatterns = [
    path('', CountriesView.as_view()),
]
