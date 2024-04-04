from django.db import models
import excel_file

# Create your models here.


product_feature_choices =(
    ('NA','NA'),
    ('NONE','NONE'),
    ('FULL','FULL'),
    ('HALF','HALF'),
    ('OPEN','OPEN'),
    ('CLOSE','CLOSE'),
)

# item_status = Choices('Draft', 'Confirmed', 'Revised', 'Cancelled', 'UnderRevision')

class Product(models.Model):
    group = models.CharField(max_length = 12, blank = True, null = True )  
    cust_code = models.CharField(max_length = 25, blank = True, null = True )      
    product_name = models.CharField(max_length=50,blank=True, null=True)
    product_feature = models.CharField(max_length=50,blank=True, null=True,choices = product_feature_choices)
    
    rate_basis = models.CharField(max_length=12, blank=True, null = True)
    multiplying_factor = models.CharField(max_length=6, blank=True, null = True)
    rate = models.CharField(max_length=50, blank=True, null = True)
    len_from = models.FloatField(blank=True, null = True )
    len_upto = models.FloatField(blank=True, null = True )
    w_from = models.FloatField(blank=True, null = True )
    w_upto = models.FloatField(blank=True, null = True )
    th_from = models.FloatField(blank=True, null = True )
    th_upto = models.FloatField(blank=True, null = True )
   
    valid_from =  models.DateField(blank = True, null = True )      
    valid_upto =  models.DateField(blank = True, null = True )  
    valid_yn = models.BooleanField(default = True)		


