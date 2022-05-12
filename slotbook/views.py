from django.shortcuts import render, redirect
from slotbook.models import slot


from django.contrib import messages


def slotbook(request):
    if request.method == "POST":
        Name = request.POST['Name']
        email = request.POST['email']
        number = request.POST['number']
        appointment = request.POST['appointment']
        vaccinecenter = request.POST['vaccinecenter']
        pin = request.POST['pin']
        idnumber = request.POST['idnumber']
        dose = request.POST['dose']
        date = request.POST['date']
        time = request.POST['time']

        slot(Name=Name, email=email, number=number, vaccinecenter=vaccinecenter, pin=pin, idnumber=idnumber,
             appointment=appointment, dose=dose, date=date, time=time).save()
        return redirect('confirm')

    else:
        return render(request, 'slotbooking.html')


def confirm(request):
    details = slot.objects.all()
    return render(request, 'confirm.html',
                  {'details': details})
# Create your views here
