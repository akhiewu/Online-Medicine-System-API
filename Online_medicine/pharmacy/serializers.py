from rest_framework import serializers
from .models import Invoice, InvoiceManage, Pharmacist, Medicine, MedicineDescription, Customer, CustomerDescription, onlinemedicine, onlinemedicine_description
       


class onlinemedicineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = onlinemedicine
        fields = '__all__'
        
        
class onlinemedicine_descriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = onlinemedicine_description
        fields = '__all__' 
        depth = 1
    
    def get_whoweare(self, obj):
        serializer = onlinemedicine_descriptionSerializer(obj.onlinemedicine, many=True) 
        return serializer.data 






class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        depth = 1
        

class InvoiceManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceManage
        fields = '__all__' 
        depth = 1
        
    # def get_invoice(self, obj):
    #     serializer = InvoiceSerializer(obj.invoice_manages, many=True) 
    #     return serializer.data           
    
    
class PharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist
        fields = '__all__' 
        depth = 1
        
    def get_pharmacist(self, obj):
        serializer = InvoiceSerializer(obj.pharmacists, many=True) 
        return serializer.data    
    
class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__' 
        depth = 1  
        
        
class MedicineDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineDescription
        fields = '__all__' 
        depth = 1
         
        
    # def get_medicine(self, obj):
    #     serializer = MedicineSerializer(obj.medicine_descriptions, many=True) 
    #     return serializer.data             
        
        
        
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__' 
        depth = 1  
        
        
class CustomerDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDescription
        fields = '__all__' 
        depth = 1
         
        
    # def get_customer(self, obj):
    #     serializer = CustomerSerializer(obj.Customer_descriptions, many=True) 
    #     return serializer.data        