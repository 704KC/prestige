from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=["username","password","email","role"]
    pass

# admin.site.register(Property)
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display=["property_name","property_type","location","description","bedrooms","bathrooms","maps","cost","photos"]
    pass
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=["user","property","comment"]
    pass

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display=["property","tenant","lease_status", "lease_date"]
    pass 

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display=["tenant","property","rating"]
    pass 
admin.site.register(Payment)
# @admin.register(Payment)
# class PaymentAdmin(admin.ModelAdmin):
#     list_display=["lease","amount","payment_date"]
#     pass

@admin.register(Like) 
class LikeAdmin(admin.ModelAdmin):
    list_display=["user","property"]
    pass

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    pass