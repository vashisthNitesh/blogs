from rest_framework import serializers
from blog_app.models import BlogModel
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        exclude = ("user",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("username","email",)