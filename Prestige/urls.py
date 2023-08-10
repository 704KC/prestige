from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("likes/", views.likes, name="likes"),
    path("Lease/",views.Lease,name="Lease"),
    path("aboutus/",views.aboutUs,name="aboutus"),
    path("property/",views.Properties,name='property'),
    path("contactus/",views.Contactus,name='contactus'),
    path("services/",views.service,name='service'),
    
]

