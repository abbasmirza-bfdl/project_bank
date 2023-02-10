from django.db import models

# Create your models here.
# 1.	CUSTOMERID
# 2.	ACCOUNTNO
# 3.	FIRSTNAME 
# 4.	LASTNAME 
# 5.	RESIDENCE ADDRESS 
# 6.	OFFICE ADDRESS 
# 7.	PHONE 
# 8.    BALANCE

# class User(models.Model):
#     cust_id=models.CharField(max_length=20)
#     acct_no=models.IntegerField(max_length=20)
#     f_name=models.CharField(max_length=50)
#     l_name=models.CharField(max_length=50)
#     usr_res_addr=models.CharField(max_length=200)
#     usr_off_addr=models.CharField(max_length=200)
#     phone_no=models.IntegerField(max_length=15)
#     acc_bal=models.IntegerField(max_length=12)

class OurUser(models.Model):
    user_id=models.CharField(primary_key=True,max_length=20)
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    res_addr=models.CharField(max_length=250)
    off_addr=models.CharField(max_length=250)
    phone_no=models.CharField(max_length=16)

class AccountDetails(models.Model):
    acc_no=models.IntegerField(primary_key=True)
    acc_id=models.ForeignKey(OurUser,on_delete=models.CASCADE)
    acc_bal=models.FloatField(default=0.0)
    
