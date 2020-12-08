from django import forms
from  carpool.models import User,Car,Appointment

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("__all__")
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("__all__")
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ("__all__")