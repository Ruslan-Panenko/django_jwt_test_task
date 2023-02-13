from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd

from countries.models import Country
from countries.serializers.serializer import CountrySerializer


class CountriesView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


# class CountryView(APIView):
#     def get(self, request):
#         countries = Country.objects.all()
#         data = []
#         for country in countries:
#             country_dict = {
#                 'id': country.id,
#                 'name': country.name,
#                 'iso2': country.iso2,
#                 'iso3': country.iso3,
#                 'cities': [{'id': city.id, 'name': city.name} for city in country.city_set.all()],
#             }
#             data.append(country_dict)
#         return Response(data)

