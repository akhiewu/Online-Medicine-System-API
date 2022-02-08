from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pharmacy.models import Invoice, InvoiceManage, Pharmacist, Medicine, MedicineDescription, Customer, CustomerDescription, onlinemedicine, onlinemedicine_description
from pharmacy.serializers import InvoiceSerializer, InvoiceManageSerializer, PharmacistSerializer, MedicineSerializer, MedicineDescriptionSerializer, CustomerSerializer, CustomerDescriptionSerializer, onlinemedicineSerializer, onlinemedicine_descriptionSerializer
from django.http import Http404
from rest_framework.views import APIView




class PharmacistList(APIView):
    
    def get(self, request, format=None):
        pharmacist = Pharmacist.objects.all()
        serializer = PharmacistSerializer(pharmacist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PharmacistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PharmacistDetail(APIView):
   
    def get_object(self, pk):
        try:
            return Pharmacist.objects.get(pk=pk)
        except Pharmacist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Pharmacist_var = self.get_object(pk)
        serializer = PharmacistSerializer(Pharmacist_var)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Pharmacist_var = self.get_object(pk)
        serializer = PharmacistSerializer(Pharmacist_var, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Pharmacist_var = self.get_object(pk)
        Pharmacist_var.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#------------------------------------------------------------------------------------


class MedicineList(APIView):
    
    def get(self, request, format=None):
        medicine = Medicine.objects.all()
        serializer = MedicineSerializer(medicine, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MedicineDetail(APIView):
   
    def get_object(self, pk):
        try:
            return Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Medicine_var = self.get_object(pk)
        serializer = MedicineSerializer(Medicine_var)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Medicine_var = self.get_object(pk)
        serializer = MedicineSerializer(Medicine_var, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Medicine_var = self.get_object(pk)
        Medicine_var.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






#-------------------------------------------------------------------------------------


class MedicineDescripyionList(APIView):
    
    def get(self, request, format=None):
        medicine_description = MedicineDescription.objects.all()
        serializer = MedicineDescriptionSerializer(medicine_description, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MedicineDescriptionDetail(APIView):
   
    def get_object(self, pk):
        try:
            return MedicineDescription.objects.get(pk=pk)
        except MedicineDescription.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Medicine_var1 = self.get_object(pk)
        serializer = MedicineDescriptionSerializer(Medicine_var1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Medicine_var1 = self.get_object(pk)
        serializer = MedicineDescriptionSerializer(Medicine_var1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Medicine_var1 = self.get_object(pk)
        Medicine_var1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#------------------------------------------------------------------------------------------------

class CustomerList(APIView):
    
    def get(self, request, format=None):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomerDetail(APIView):
   
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Customer_var = self.get_object(pk)
        serializer = CustomerSerializer(Customer_var)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Customer_var = self.get_object(pk)
        serializer = CustomerSerializer(Customer_var, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Customer_var = self.get_object(pk)
        Customer_var.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#----------------------------------------------------------------------------------------------------
class CustomerDescriptionList(APIView):
    
    def get(self, request, format=None):
        customer_description = CustomerDescription.objects.all()
        serializer = CustomerDescriptionSerializer(customer_description, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerDescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomerDescriptionDetail(APIView):
   
    def get_object(self, pk):
        try:
            return CustomerDescription.objects.get(pk=pk)
        except CustomerDescription.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Customer_var1 = self.get_object(pk)
        serializer = CustomerDescriptionSerializer(Customer_var1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Customer_var1 = self.get_object(pk)
        serializer = CustomerDescriptionSerializer(Customer_var1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Customer_var1 = self.get_object(pk)
        Customer_var1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






#--------------------------------------------------------------------------------------------------------








@api_view(['GET', 'POST'])
def Invoice_list(request):
    if request.method == 'GET':
        invoice = Invoice.objects.all()
        serializer = InvoiceSerializer(invoice, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def Invoice_detail(request, pk):
    
    try:
        invoice1 = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InvoiceSerializer(invoice1)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = InvoiceSerializer(invoice1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        invoice1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #--------------------------------------------
    
    
@api_view(['GET', 'POST'])
def InvoiceManage_list(request):
    if request.method == 'GET':
        invoice_var = InvoiceManage.objects.all()
        serializer = InvoiceManageSerializer(invoice_var, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InvoiceManageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET', 'PATCH', 'DELETE'])
def InvoiceManage_detail(request, pk):
    
    try:
        invoice_var1 = InvoiceManage.objects.get(pk=pk)
    except InvoiceManage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InvoiceManageSerializer(invoice_var1)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = InvoiceManageSerializer(invoice_var1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        invoice_var1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
    
    #-----------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------
    
    
@api_view(['GET'])
def get_onlinemedicine(request):
    medicine_objs = onlinemedicine_description.objects.all()
    serializer = onlinemedicine_descriptionSerializer(medicine_objs, many=True)
    return Response({'status':200, 'onlinemedicine': serializer.data})


@api_view(['GET'])       
def get_onlinemedicine(request,id):
    medicine_objs = onlinemedicine_description.objects.filter(id=id).first()
    serializer = onlinemedicine_descriptionSerializer(medicine_objs)
    return Response({'status':200, 'onlinemedicine': serializer.data})