from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from .models import *
# Create your views here.
# def index(request):
#     return HttpResponse("HI there")


def users():
    return HttpResponse("Hi user")


def Properties(request):
    property = Property.objects.order_by('property_name')
    context = {'properties': property}
    return render(request, 'property.html',context )

def likes(request):
    response ="You like this property "
    return HttpResponse(response )

def index(request):
    latest_question_list = Property.objects.order_by("property_name")[:5]
    # output = ", ".join([q.property_name for q in latest_question_list])
    return render(request,'index.html')
def Lease(request):
    try:
        lease=Lease.object.get(Pk=lease_id)
    except  Lease.DoesNotExist:
        raise Http404("Lease does not exist")
    return render(request, "lease.html", {"question": lease})

    
def aboutUs(request):
    return render(request,"aboutus.html")

def service(request):
    return(request,'service.html')