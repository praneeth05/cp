from django import forms
from  carpool.models import User,Carprice,Appointment,Package,Message

class CarpriceForm(forms.ModelForm):
    class Meta:
        model = Carprice
        fields = ("__all__")
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("__all__")
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ("__all__")
class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ("__all__")
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("__all__")