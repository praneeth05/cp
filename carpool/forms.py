from django import forms
from  carpool.models import User,Hatchback,Sedan,Compactsuv,Suv,Appointment

class HatchbackForm(forms.ModelForm):
    class Meta:
        model = Hatchback
        fields = ("__all__")
class SedanForm(forms.ModelForm):
    class Meta:
        model = Sedan
        fields = ("__all__")
class CompactsuvForm(forms.ModelForm):
    class Meta:
        model = Compactsuv
        fields = ("__all__")
class SuvForm(forms.ModelForm):
    class Meta:
        model = Suv
        fields = ("__all__")
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("__all__")
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ("__all__")