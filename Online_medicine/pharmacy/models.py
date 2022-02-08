from django.db import models

# Create your models here.


class Invoice(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name 
    
class InvoiceManage(models.Model):
    name = models.CharField(max_length=200)
    invoice_no = models.CharField(max_length=500)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name = 'invoice_manages')
    phone = models.IntegerField()
    address = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.IntegerField()
    discount = models.IntegerField() 
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return self.name     
        
        
    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'invoice':
                return(field.name, self.invoice.name, field.get_internal_type())
            else:
                return(field.name, self.value_from_object(self), field.get_internal_type())
            return[get_dynamic_fields(field) for field in self.__class__._meta.fields]      
        
        
        


class Pharmacist(models.Model):
    name = models.CharField(max_length=100)
    descrition = models.CharField(max_length=500)
    email = models.EmailField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name = 'pharmacists')
    
    def __str__(self):
        return self.name         
    
    
    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'invoice':
                return(field.name, self.invoice.name, field.get_internal_type())
            else:
                return(field.name, self.value_from_object(self), field.get_internal_type())
            return[get_dynamic_fields(field) for field in self.__class__._meta.fields] 
        
        
    
class Medicine(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    
    
class MedicineDescription(models.Model):
    title = models.CharField(max_length=100)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name = 'medicine_descriptions')
    description = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add= True)

    
    def __str__(self):
        return self.title
    
    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'medicine':
                return(field.name, self.medicine.title, field.get_internal_type())
            else:
                return(field.name, self.value_from_object(self), field.get_internal_type())
            return[get_dynamic_fields(field) for field in self.__class__._meta.fields]   
    
        
        
 
#---------------------------------------------------------------------------


class Customer(models.Model):
    
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.name
    
        
class CustomerDescription(models.Model):
    
    title = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name = 'Customer_descriptions')
    description = models.TextField(null=True, blank=True)
    medicine = models.ManyToManyField(MedicineDescription)
    
    def __str__(self):
        return self.title    
    
    
    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'customer':
                return(field.name, self.customer.name, field.get_internal_type())
            else:
                return(field.name, self.value_from_object(self), field.get_internal_type())
            return[get_dynamic_fields(field) for field in self.__class__._meta.fields]
        
        
        
        
        
        
        
class onlinemedicine(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

            
            
class onlinemedicine_description(models.Model):
    title = models.CharField(max_length=200)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='onlinemedicine')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='onlinemedicine')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='onlinemedicine')            
    
    def __str__(self):
        return self.title
    
    
    
    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'title':
                return(field.name, self.vision.name, field.get_internal_type())
            else:
                return(field.name, self.value_from_object(self), field.get_internal_type())
            return[get_dynamic_fields(field) for field in self.__class__._meta.fields]
        
        
        
    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'invoice':
                return(field.name, self.invoice.name, field.get_internal_type())
            else:
                return(field.name, self.value_from_object(self), field.get_internal_type())
            return[get_dynamic_fields(field) for field in self.__class__._meta.fields]    

        
        
        
        
        
        
        
        