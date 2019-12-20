from django.db import models
# Create your models here.
import datetime 

class Individual(models.Model):
    Fid = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=100)
    Fcontact = models.CharField(max_length=15)
    Faadhar = models.CharField(max_length=20, blank=True, null=True)
    Faddress1 = models.CharField(max_length=100)
    Faddress2 = models.CharField(max_length=100, blank=True, null=True)
    Faddress3 = models.CharField(max_length=100, blank=True, null=True)
    Fration = models.CharField(max_length=100, blank=True, null=True)
    Farogya = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(default=750, blank=True, null=True)
    from_date = models.DateField(default=datetime.date(2020, 1, 1))
    to_date = models.DateField(default=datetime.date(2020, 12, 31)) 
    pc = models.IntegerField(default=0, blank=True, null=True)
    paid =models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        db_table = "individual"

class Family(models.Model):
    Fid = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=100)
    Fcontact = models.CharField(max_length=15)
    Faadhar = models.CharField(max_length=20, blank=True, null=True)
    Faddress1 = models.CharField(max_length=100)
    Faddress2 = models.CharField(max_length=100, blank=True, null=True)
    Faddress3 = models.CharField(max_length=100, blank=True, null=True)
    Fration = models.CharField(max_length=100, blank=True, null=True)
    Farogya = models.CharField(max_length=100, blank=True, null=True)
    Member_1_name = models.CharField(max_length=100)
    Member_1_aadhar = models.CharField(max_length=20, blank=True, null=True)
    Member_2_name = models.CharField(max_length=100, blank=True, null=True)
    Member_2_aadhar = models.CharField(max_length=20, blank=True, null=True)
    Member_3_name = models.CharField(max_length=100, blank=True, null=True)
    Member_3_aadhar = models.CharField(max_length=20, blank=True, null=True)
    Member_4_name = models.CharField(max_length=100, blank=True, null=True)
    Member_4_aadhar = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateField(default=datetime.date(2020, 1, 1))
    to_date = models.DateField(default=datetime.date(2020, 12, 31)) 
    pc = models.IntegerField(default=0, blank=True, null=True)
    price = models.IntegerField(default=1350, blank=True, null=True)
    paid =models.BooleanField(default=True, blank=True, null=True)
    class Meta:
        db_table = "family"
