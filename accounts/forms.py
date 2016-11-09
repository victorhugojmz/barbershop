from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth import (authenticate, login , get_user_model,logout)
User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    def clean(self, *args, **kwargs): 
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:    
            user = authenticate(username = username , password  = password)
            if not User:
               raise forms.ValidationError("El usuario no existe")
            if not user.check_password(password):
               raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
               raise forms.ValidationError("El usuario ya no esta activo")
        return super(UserLoginForm, self).clean(*args, **kwargs)
class UserRegistrationForm(forms.ModelForm):
      password = forms.CharField(widget = forms.PasswordInput)
      class Meta:
              model  = User 
              fields = ['username','email', 'password']
          
