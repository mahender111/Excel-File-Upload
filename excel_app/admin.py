from django.contrib import admin
from .models import Product

# Register your models here.

class Product_Admin(admin.ModelAdmin):
    list_display = [
        'id',
        'cust_code',
        'group',
        'product_name',
        'product_feature',
        'multiplying_factor',
        
        'rate',
        'len_from',
        'len_upto',
        'w_from',
        'w_upto',
        'th_from',
        'th_upto',
        
        'valid_from',
        'valid_upto',
        'valid_yn',
        
    ]
    


    list_filter =['product_name','rate','group']
    search_fields = ['group','rate','product_name']
    
# ----------------------------------------------------------------register-admin page-----------------------------------------------------
# register admin page

    
admin.site.register(Product,Product_Admin)
