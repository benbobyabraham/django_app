from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView
# authentication
from rest_framework.permissions import IsAuthenticated
# api views
from rest_framework import generics
from rest_framework import mixins

from .serializers import PostSerializer
from .models import Post


class PostView(
    mixins.ListModelMixin ,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(self, request, *args, **kwargs)

    def get(self,request, *args,**kwargs):
        return self.list(self, request, *args, **kwargs)

    

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()





    

# def test_view(request):
#     data = {
#         'data1': 'laptop',
#         'data2': 26
#     }
#     return JsonResponse(data)

# class TestView(APIView):

#     permission_classes = (IsAuthenticated,)

#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         post = qs.first()
#         serializer = PostSerializer(qs,many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             print(request.user)
#             serializer.owner = request.user
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)