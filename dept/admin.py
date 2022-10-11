from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Faculty)
class FacultyModel(admin.ModelAdmin):
    list_display = ('Username', 'FirstName','LastName')
    # search_fields = ('Username')
    ordering = ['Username']
    

admin.site.register(Emf)
admin.site.register(cn)
admin.site.register(ml)
admin.site.register(ws)
admin.site.register(iot)
admin.site.register(emfdisplay)
admin.site.register(cndisplay)
admin.site.register(mldisplay)
admin.site.register(wsdisplay)
admin.site.register(iotdisplay)
   
