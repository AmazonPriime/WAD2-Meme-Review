from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from meme_app.models import UserProfile, Meme, Category, Comment

class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Username'}))
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'First Name'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Last Name'}))
    email = forms.CharField(widget = forms.EmailInput(attrs = {'class' : 'form-control', 'placeholder' : 'Email'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control', 'placeholder' : 'Password'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control', 'placeholder' : 'Repeat Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')

class UserProfileForm(forms.ModelForm):
    dob = forms.DateField(widget = DateInput(attrs = {'class' : 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('dob',)

class AccountForm(forms.ModelForm):
    picture = forms.ImageField(widget = forms.FileInput(attrs = {'class' : 'form-control-file submitButton', 'id' : 'changeAccountImage'}), required = False)
    bio = forms.CharField(widget = forms.Textarea(attrs = {'class' : 'form-control fullLength', 'id' : 'userBio', 'rows' : '3'}), required = False)

    class Meta:
        model = UserProfile
        fields = ('picture', 'bio')

class MemeForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Title'}), required = True)
    category = forms.ModelChoiceField(widget = forms.Select(attrs = {'class' : 'form-control'}), queryset = Category.objects.all(), required = True)
    nsfw = forms.BooleanField(widget = forms.CheckboxInput(attrs = {'class' : 'form-check-input', 'id' : 'isOver18'}), required = False)

    class Meta:
        model = Meme
        fields = ('title', 'category', 'nsfw')

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control', 'type' : 'text', 'placeholder' : 'Please enter a comment'}), required = True)

    class Meta:
        model = Comment
        fields = ('text',)
