from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render
from rest_framework import generics
from women.serializer import WomenSerializer
from women.models import Women

class WomenAPIView(APIView):
    def get(self, request):
        women_list = Women.objects.all().values()
        return Response({'post': list(women_list)})

    def post(self, request):
        post_new = Women.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})
# Create your views here.
# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
