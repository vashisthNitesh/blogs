from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from . import views

urlpatterns = [
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("blog/", views.BlogAPIView.as_view()),
    path("blog/<int:pk>", views.BlogAPIView.as_view()),

]
