from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pharmacy import views

urlpatterns = [
    path('invoice_list/', views.Invoice_list),
    path('invoice_detail/<int:pk>', views.Invoice_detail),
    
    path('invoicemanage_list/', views.InvoiceManage_list),
    path('invoicemanage_detail/<int:pk>', views.InvoiceManage_detail),
    
    path('pharmacist_list/', views.PharmacistList.as_view()),
    path('pharmacist_detail/<int:pk>/', views.PharmacistDetail.as_view()),
    
    path('medicine_list/', views.MedicineList.as_view()),
    path('medicine_detail/<int:pk>/', views.MedicineDetail.as_view()),
    
    path('medicine_description_list/', views.MedicineDescripyionList.as_view()),
    path('medicine_description_detail/<int:pk>/', views.MedicineDescriptionDetail.as_view()),
    
    path('customer_list/', views.CustomerList.as_view()),
    path('customer_detail/<int:pk>/', views.CustomerDetail.as_view()),
    
    path('customer_description_list/', views.CustomerDescriptionList.as_view()),
    path('customer_description_detail/<int:pk>/', views.CustomerDescriptionDetail.as_view()),
    
    path('get-onlinemedicine/', views.get_onlinemedicine),
    path('get-onlinemedicine/<id>/', views.get_onlinemedicine)
]

urlpatterns = format_suffix_patterns(urlpatterns)