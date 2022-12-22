from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import BlogModel


UserModel = get_user_model()


class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LogInForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"





# Sign Up Form
class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ('is_publish','user','title','image','content')
        widgets = {
        'user': forms.HiddenInput(),
        }
        