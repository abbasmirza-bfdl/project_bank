from django.db import models

class OurUser(models.Model):
    user_id=models.CharField(primary_key=True,max_length=200)
    f_name=models.CharField(max_length=200)
    l_name=models.CharField(max_length=200)
    res_addr=models.CharField(max_length=250)
    off_addr=models.CharField(max_length=250)
    phone_no=models.CharField(max_length=160)

class AccountDetails(models.Model):
    acc_no=models.IntegerField(primary_key=True)
    acc_id=models.ForeignKey(OurUser,on_delete=models.CASCADE)
    acc_bal=models.FloatField(default=0.0)
    
class AccountTransactions(models.Model):
    trsn_acc_no=models.ForeignKey(AccountDetails,on_delete=models.CASCADE)
    trsn_date=models.DateTimeField(auto_now_add=True)
    trsn_type=models.CharField(max_length=12)
    trsn_amount=models.FloatField()
    trsn_balance=models.FloatField()