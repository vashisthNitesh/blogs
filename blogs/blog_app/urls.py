
from django.contrib import admin
from django.urls import path,include
from .import views

app_name = "blogs"

urlpatterns = [
    path('user_login', views.LoginFormView.as_view(), name='login'),
    path('user_logout', views.LogoutView.as_view(), name='logout'),
    path('user_signup', views.SignUpView.as_view(), name='signup'),

    #blogs
    path('',views.BlogsListView.as_view(),name="blogs_list"),
    path('<int:pk>',views.BlogsListView.as_view(),name="blogs_list_heart"),

    #user blogs 
    path('user/blogs',views.UserBlogsListView.as_view(),name="user_blogs_list"),
    path('user/blogs/<int:pk>',views.UserBlogsListView.as_view(),name="user_blogs_list_heart"),

    # blog crud
    path('user/blog/create',views.BlogCreateView.as_view(),name="blog_create"),
    path('user/blog/<int:pk>/update',views.BlogUpdateView.as_view(),name="blog_update"),
    path('user/blog/<int:pk>/delete',views.BlogDeleteView.as_view(),name="blog_delete"),

    # admin
    path('user/list',views.UserListView.as_view(),name="user_list"),
    path('user/create',views.UserCreateView.as_view(),name="user_create"),
    path('user/<int:pk>/update',views.UserUpdateView.as_view(),name="user_update"),
    path('user/<int:pk>/delete',views.UserdeleteView.as_view(),name="user_delete"),

    # api urls
    path("api/", include("blog_app.api.urls")),
    
]
