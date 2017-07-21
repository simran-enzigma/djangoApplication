from django.db import models

# Create your models here.
class Contact(models.Model):
    SerialNo = models.AutoField(primary_key=True)
    FirstName = models.CharField( max_length=50, null=True)
    LastName = models.CharField( max_length=50)
    Email =  models.EmailField(max_length=50)
    MobileNo = models.DecimalField(max_digits=12, decimal_places=0)

    
    def __str__(self):
         return self.LastName + self.FirstName +self.Email