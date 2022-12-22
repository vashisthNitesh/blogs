from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogModel(BaseModel):
    is_publish = models.BooleanField(default=True)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="user")
    title = models.CharField(max_length=255,null=True,blank=True,default="")
    likes = models.ManyToManyField(UserModel, related_name="blog")
    image = models.ImageField(blank=True, null=True)
    content = models.TextField(default="", null=True, blank=True)
    
    def likes_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title
