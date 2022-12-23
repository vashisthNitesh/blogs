from django.shortcuts import redirect,get_object_or_404
from django.views.generic import FormView, ListView, View, CreateView, UpdateView, DeleteView
from .forms import LogInForm,SignUpForm,BlogCreateForm
from django.urls import reverse_lazy, reverse
from .models import BlogModel
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
# Create your views here.


UserModel = get_user_model()


class LoginFormView(FormView):
    template_name = "user/user_login.html"
    form_class = LogInForm
    success_url = reverse_lazy("blogs:user_blogs_list")

    def form_valid(self, form):
        # print(form.cleaned_data)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return redirect("blogs:user_blogs_list")
        return self.form_invalid(form)

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('blogs:login')
    template_name = 'user/user_signup.html'

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class BlogsListView(ListView):
    template_name = "blog/blogs.html"
    model = BlogModel
    context_object_name = "blogs"

    def post(self,request,pk):
        id = self.request.POST.get("pk")
        blog = get_object_or_404(BlogModel, pk=id)
        liked=False
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
            liked = False
        else:
            blog.likes.add(request.user)
            liked = True

        return HttpResponseRedirect(reverse("blogs:blogs_list"))
        

class UserBlogsListView(ListView):
    template_name = "blog/user_blogs.html"
    model = BlogModel
    context_object_name = "blogs"   
    
    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.filter(user=self.request.user) 
    def post(self,request,pk):
        id = self.request.POST.get("pk")
        blog = get_object_or_404(BlogModel, pk=id)
        liked=False
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
            liked = False
        else:
            blog.likes.add(request.user)
            liked = True
        return HttpResponseRedirect(reverse("blogs:user_blogs_list"))

# blog Views

class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogCreateForm
    template_name = "blog/user_blog_create.html"

    def get_initial(self, *args, **kwargs):
        initial = super(BlogCreateView, self).get_initial(**kwargs)
        initial['user'] = self.request.user
        return initial

    def get_success_url(self):
        return reverse_lazy("blogs:user_blogs_list")

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogModel
    form_class = BlogCreateForm
    template_name = "blog/user_blog_update.html"
    def get_success_url(self):
        return reverse_lazy("blogs:user_blogs_list")
    
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogModel
    template_name = "blog_app/user_blog_delete.html"
    def get_success_url(self):
        return reverse_lazy("blogs:user_blogs_list")        


# user related views

class UserListView(LoginRequiredMixin, ListView):
    template_name = "user/user_list.html"
    model = UserModel
    context_object_name = "users"


class UserCreateView(LoginRequiredMixin,CreateView):
    form_class = SignUpForm
    template_name = "user/user_create.html"

    def get_success_url(self):
        return reverse_lazy("blogs:user_list")

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = SignUpForm
    template_name = "user/user_update.html"
    def get_success_url(self):
        return reverse_lazy("blogs:user_list")

class UserdeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = "user/user_delete.html"
    def get_success_url(self):
        return reverse_lazy("blogs:user_list")      