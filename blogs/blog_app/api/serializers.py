from rest_framework import serializers
from blog_app.models import BlogModel


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        exclude = ("user",)
