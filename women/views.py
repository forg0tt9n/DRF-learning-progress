from rest_framework.decorators import  action
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render
from rest_framework import generics, status, viewsets
from women.serializers import WomenSerializer
from women.models import Women, Category


class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk)
    @action(methods=['get'], detail=True)
    def categories(self, request, pk=None):

        cats = Category.objects.get(pk=pk)
        return Response({'categories': cats.name})


#class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
