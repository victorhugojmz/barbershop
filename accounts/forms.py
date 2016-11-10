from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth import (authenticate, login , get_user_model,logout)
User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField(label ='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Password' ,'class':'form-control'}))
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
      first_name = forms.CharField(label ='Nombre(s)',widget=forms.TextInput(attrs={'placeholder': 'Nombre(s)','class':'form-control'}))
      last_name = forms.CharField(label ='Apellido(s)',widget=forms.TextInput(attrs={'placeholder': 'Apellido(s)','class':'form-control'}))
      username = forms.CharField(label ='Username',widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: zamacueca2000','class':'form-control'}))
      email = forms.EmailField(label = 'Email', widget=forms.TextInput(attrs={'placeholder': 'Email','class':'form-control'}))
      email2 = forms.EmailField(label ='Confirma tu email', widget=forms.TextInput(attrs={'placeholder': 'Confirma email','class':'form-control'}))
      password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Password' ,'class':'form-control'}))
      class Meta:
              model  = User 
              fields = [
                  'first_name',
                  'last_name',
                  'username',
                  'email',
                  'email2',
                  'password',
              ]