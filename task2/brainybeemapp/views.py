# cars/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Purchase

def home(request):
    purchases = Purchase.objects.all()  
    return render(request, 'cars/home.html', {'purchases': purchases})

def car_form(request):
    if request.method == 'POST':

        company = request.POST.get('company')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')

        if company and model and year and price:
            try:
               
                car = Car.objects.create(company=company, model=model, year=year, price=price)

                purchase = Purchase(car=car)
                purchase.save()  

                return redirect('car_success')  

            except Exception as e:
                return render(request, 'cars/car_form.html', {'error': f'Error: {str(e)}'})

        else:
            return render(request, 'cars/car_form.html', {'error': 'All fields are required.'})

    return render(request, 'cars/car_form.html')

def car_success(request):
    return render(request, 'cars/car_success.html')
