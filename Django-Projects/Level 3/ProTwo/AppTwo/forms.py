from django import forms
from AppTwo.models import User

class NewUserForm(forms.ModelForm):
    """Form definition for NewUser."""

    class Meta:
        """Meta definition for NewUserform."""

        model = User
        fields = '__all__'
