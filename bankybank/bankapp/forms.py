from django import forms


class RegForm(forms.Form):
    user_id=forms.CharField(max_length=20)
    f_name=forms.CharField(max_length=20)
    l_name=forms.CharField(max_length=20)
    res_addr=forms.CharField(max_length=250)
    off_addr=forms.CharField(max_length=250)
    phone_no=forms.IntegerField(help_text='Enter 10 digit mobile number!')

class DepWithForm(forms.Form):
    Enter_amount=forms.FloatField()

class AdminOps(forms.Form):
    user_id=forms.CharField(max_length=20)

class UpdateForm(forms.Form):
    f_name=forms.CharField(max_length=20)
    l_name=forms.CharField(max_length=20)
    res_addr=forms.CharField(max_length=250)
    off_addr=forms.CharField(max_length=250)
    phone_no=forms.IntegerField(help_text='Enter 10 digit mobile number!')
