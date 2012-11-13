from django import forms
from doctor.models import country
# Create your forms here.
# created by budoya  
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=40)
    middle_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    gender = forms.CharField(max_length=10)
    date_of_birth = forms.DateField( )
    nationality = forms.ModelChoiceField(country.objects.all())
    postal_address = forms.CharField(max_length=100)
    vodacom_phone = forms.IntegerField()
    other_phone = forms.IntegerField()
    email_address = forms.EmailField()b
