from django.contrib import admin
from .models import Doctor,Customer,Appointment,Contact,Treatment
# Register your models here.
class doctorAdmin(admin.ModelAdmin):
    list_display = ['name','email','fields']
    search_fields = ['name']
admin.site.register(Doctor,doctorAdmin)


class customerAdmin(admin.ModelAdmin):
    list_display = ['customer', 'occupation', 'reviews']
    search_fields = ['customer']
admin.site.register(Customer,customerAdmin)

class Appointmentadmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date','time','doctors']
    search_fields= ['first_name', 'last_name', 'date','time','doctors']
admin.site.register(Appointment,Appointmentadmin)

admin.site.register(Contact)
admin.site.register(Treatment)
