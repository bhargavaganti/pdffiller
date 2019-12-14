from django.db import models
# Create your models here.


class Individual(models.Model):
    Fid = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=100)
    Fcontact = models.CharField(max_length=15)
    Faadhar = models.CharField(max_length=20)
    Faddress1 = models.CharField(max_length=100)
    Faddress2 = models.CharField(max_length=100, blank=True, null=True)
    Faddress3 = models.CharField(max_length=100, blank=True, null=True)
    Fration = models.CharField(max_length=100, blank=True, null=True)
    Farogya = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(default=750)
    paid =models.BooleanField(default=True)

    class Meta:
        db_table = "individual"

class Family(models.Model):
    Fid = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=100)
    Fcontact = models.CharField(max_length=15)
    Faadhar = models.CharField(max_length=20)
    Faddress1 = models.CharField(max_length=100)
    Faddress2 = models.CharField(max_length=100, blank=True, null=True)
    Faddress3 = models.CharField(max_length=100, blank=True, null=True)
    Fration = models.CharField(max_length=100, blank=True, null=True)
    Farogya = models.CharField(max_length=100, blank=True, null=True)
    Member_1_name = models.CharField(max_length=100)
    Member_1_aadhar = models.CharField(max_length=20)
    Member_2_name = models.CharField(max_length=100, blank=True, null=True)
    Member_2_aadhar = models.CharField(max_length=20, blank=True, null=True)
    Member_3_name = models.CharField(max_length=100, blank=True, null=True)
    Member_3_aadhar = models.CharField(max_length=20, blank=True, null=True)
    Member_4_name = models.CharField(max_length=100, blank=True, null=True)
    Member_4_aadhar = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField(default=1350)
    paid =models.BooleanField(default=True)
    class Meta:
        db_table = "family"
