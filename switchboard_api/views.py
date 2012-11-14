# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context, loader
from doctor.forms import ContactForm
from doctor.models import contact
# ...

def index(request):
    form = ContactForm()
    context = Context({'title': 'Add Contact', 'form': form})
    return render(request, 'doctor/index.html', context)
def add1(request):
    return HttpResponse("You're looking at contact ")
def add(request):
    if request.method == 'POST':
        
            # create a new item
            cont = contact.objects.create(
                first_name = request.POST['first_name'],
                middle_name = request.POST['middle_name'],
                last_name = request.POST['last_name'],
                gender = request.POST['gender'],
                date_of_birth = request.POST['date_of_birth'],
                postal_address = request.POST['postal_address'],
                vodacom_phone = request.POST['vodacom_phone'],
                other_phone = request.POST['other_phone'],
                email_address = request.POST['email_address'],
            )
            # Always redirect after a POST
            return render(request, 'doctor/index.html')
def add2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # create a new item
            cont = contact.objects.create(
                first_name = request.POST['first_name'],
                middle_name = request.POST['middle_name'],
                last_name = request.POST['last_name'],
                gender = request.POST['gender'],
                date_of_birth = request.POST['date_of_birth'],
                postal_address = request.POST['postal_address'],
                vodacom_phone = request.POST['vodacom_phone'],
                other_phone = request.POST['other_phone'],
                email_address = request.POST['email_address'],
            )
            # Always redirect after a POST
            return HttpResponseRedirect('/doctor/')

    else:
        # This the the first page load, display a blank form
        form = ContactForm()
    context = Context({'title': 'Add Item', 'form': form})
    return render(request, 'doctor/index.html', context)
