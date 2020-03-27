from django import forms
from django.contrib.auth.models import User
from meme_app.models import UserProfile, Meme, Category

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
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")

class UserProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=DateInput(attrs = {'class' : 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('picture', 'dob', 'bio')

class MemeForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Title'}), required = True)
    category = forms.ModelChoiceField(widget = forms.Select(attrs = {'class' : 'form-control'}), queryset = Category.objects.all(),required = True)
    nsfw = forms.BooleanField(widget = forms.CheckboxInput(attrs = {'class' : 'form-check-input', 'id' : 'isOver18'}), required=False)

    class Meta:
        model = Meme
        fields = ('title', 'picture', 'category', 'nsfw')
