
from django.contrib import admin
from django.urls import path,include
from .import views
from blog_app.api.views import BlogListView, BLogCreateView, BLogRetreiveUpdateDelete,UserApiListView,UserApiCreateView,UserRetreiveUpdateDelete
from rest_framework import routers
app_name = "blogs"
router = routers.DefaultRouter()
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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/blogs/list', BlogListView.as_view(), name="api_blog_list"),
    path('api/blogs/create', BLogCreateView.as_view(), name="api_blog_create"),
    path('api/blogs/actions/<int:pk>', BLogRetreiveUpdateDelete.as_view(), name="api_blog_actions"),

    # api admin urls
    path('api/users/list', UserApiListView.as_view(), name="api_user_list"),
    path('api/user/create', UserApiCreateView.as_view(), name="api_user_create"),
    path('api/user/actions/<int:pk>', UserRetreiveUpdateDelete.as_view(), name="api_user_actions"),
    
]
