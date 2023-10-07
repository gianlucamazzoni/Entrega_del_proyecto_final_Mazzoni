from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Nintendo, Playstation, Xbox, Avatar

class NintendoFormulario(forms.Form):
    Desarrolladora=forms.CharField(max_length=60)
    Fecha_de_inauguración=forms.DateField()
    Juego=forms.CharField(max_length=50)
    Fecha_de_salida=forms.DateField()

class NintendoFormulario(forms.ModelForm):
    class Meta:
        model=Nintendo
        fields=("Desarrolladora", "Fecha_de_inauguración", "Juego", "Fecha_de_salida")

class PlaystationFormulario(forms.Form):
    Desarrolladora=forms.CharField(max_length=60)
    Fecha_de_inauguración=forms.DateField()
    Juego=forms.CharField(max_length=50)
    Fecha_de_salida=forms.DateField()

class PlaystationFormulario(forms.ModelForm):
    class Meta:
        model=Playstation
        fields=("Desarrolladora", "Fecha_de_inauguración", "Juego", "Fecha_de_salida")

class XboxFormulario(forms.Form):
    Desarrolladora=forms.CharField(max_length=60)
    Fecha_de_inauguración=forms.DateField()
    Juego=forms.CharField(max_length=50)
    Fecha_de_salida=forms.DateField()

class XboxFormulario(forms.ModelForm):
    class Meta:
        model=Xbox
        fields=("Desarrolladora", "Fecha_de_inauguración", "Juego", "Fecha_de_salida")


class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    password1 =forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 =forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields= ["email", "first_name", "last_name", "password1", "password2"]

    
    def clean_password2(self):
        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden, intentelo de nuevo")
        return password2
    
class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ("imagen",)