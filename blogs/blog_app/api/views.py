
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from blog_app.models import BlogModel
from .import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class BlogListView(generics.ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = serializers.BlogSerializer

class BLogCreateView(LoginRequiredMixin,generics.CreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)   

class BLogRetreiveUpdateDelete(LoginRequiredMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = []


    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 


#  user api views
class UserApiListView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = serializers.UserSerializer

class UserApiCreateView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]

class UserRetreiveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]

        