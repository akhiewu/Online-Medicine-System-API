from django.contrib import admin
from .models import Invoice, InvoiceManage, Pharmacist, MedicineDescription,Medicine, Customer, CustomerDescription, onlinemedicine ,onlinemedicine_description
 
# Register your models here.

admin.site.register(Invoice)
admin.site.register(InvoiceManage)
admin.site.register(Pharmacist)
admin.site.register(Medicine)
admin.site.register(MedicineDescription)
admin.site.register(Customer)
admin.site.register(CustomerDescription)
admin.site.register(onlinemedicine)
admin.site.register(onlinemedicine_description)