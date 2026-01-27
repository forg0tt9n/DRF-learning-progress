from django.shortcuts import render
from rest_framework import generics
from women.serializer import WomenSerializer
from women.models import Women


# Create your views here.
class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
