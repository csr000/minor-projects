from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from app.models import App, App_second

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def add_view(request):
    content = request.POST['name']
    a=App.objects.all().count()
    b=App_second.objects.all().count()
    if a<=99:
        create_obj = App.objects.create(text=content)
    elif b<=99:
        create_obj = App_second.objects.create(text=content)
    if a==100 and b==100:
        App.objects.all().delete()
        App_second.objects.all().delete()
        create_obj = App.objects.create(text=content)
    messages.success(request, 'Seat Booked Successfully.')
    return HttpResponseRedirect("/")

def admin_panel_view(request):
    #print('Number of Seat Booked(1):{}'.format(App.objects.all().count()))
    #print('Number of Seat Booked(2):{}'.format(App_second.objects.all().count()))
    text = App.objects.all().order_by("time_published")
    text_second = App_second.objects.all().order_by("time_published")
    percent=(App.objects.all().count()/100)*100
    percent_second=(App_second.objects.all().count()/100)*100
    context={'no_of_seat_booked':App.objects.all().count(), 
             'no_of_seat_booked_second':App_second.objects.all().count(),
             'text':text,
             'text_second':text_second,
             'percent':int(percent),
             'percent_second':int(percent_second)} 
    
    return render(request, 'admin.html', context)

import datetime 

if str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) == '2020-09-06 23:22':
    print(str(datetime.datetime.now()))