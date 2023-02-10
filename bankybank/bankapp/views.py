from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegForm,DepWithForm,AdminOps,UpdateForm
from .models import OurUser,AccountDetails,AccountTransactions
import random
from django.db import IntegrityError
from django.contrib import messages
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
# from .models import *
from bankapp.serializers import *
from rest_framework.generics import GenericAPIView
# from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO')

class initial_ops:

    def admin_home(request):
        return render(request,'adminhome.html')

    def reg_form(request):
        context={}
        context['form']=RegForm
        return render(request,'register.html',context)

    def create_user(request):
        form=RegForm(request.POST)
        if form.is_valid():
            user_id=form.cleaned_data['user_id']
            f_name=form.cleaned_data['f_name']
            l_name=form.cleaned_data['l_name']
            res_addr=form.cleaned_data['res_addr']
            off_addr=form.cleaned_data['off_addr']
            phone_no=form.cleaned_data['phone_no']
            if OurUser.objects.filter(user_id=user_id).exists():
                context={}
                context['form']=form
                context['msg_exist']='The User Id already exists!'
                return render(request,'register.html',context)

            try:
                our_user=OurUser.objects.create(user_id=user_id,f_name=f_name,l_name=l_name,res_addr=res_addr,off_addr=off_addr,phone_no=phone_no)
            except IntegrityError:
                logger.error('user name already exists')
                our_user=OurUser.objects.get(user_id=user_id)
            logger.info('new user create')
            acc_no=random.randint(100001,200000)
            account=AccountDetails.objects.create(acc_no=acc_no,acc_id=our_user)
            # context={}
            # context['our_user']=our_user
            # context['account']=account

            # acc_obj=AccountDetails.objects.get(pk=acc_no)
            # context['acc_no']=acc_obj.acc_no
            # context['acc_bal']=acc_obj.acc_bal
            logger.info('new account created for user')
            context=initial_ops.get_details(user_id)
            return render(request,'userdetails.html',context)
        

    def user_details_form(request):
        context={}
        context['form']=AdminOps
        return render(request,'userdetailsform.html',context)
    
    def get_details(user_id):
        # if OurUser.objects.filter(user_id=user_id).exists():
        user_obj=OurUser.objects.get(pk=user_id)
        acc_obj=AccountDetails.objects.get(acc_id=user_id)
        # trsn_obj=AccountTransactions.objects.get(trsn_acc_no=acc_obj.acc_no)
        context={}
        context['f_name']=user_obj.f_name
        context['l_name']=user_obj.l_name
        context['res_addr']=user_obj.res_addr
        context['off_addr']=user_obj.off_addr
        context['phone_no']=user_obj.phone_no
        context['user_id']=user_obj.user_id
        context['acc_no']=acc_obj.acc_no
        context['acc_name']='Savings'
        context['acc_bal']=acc_obj.acc_bal
        return context
        
    
    def display_user_details(request):
        form=AdminOps(request.POST)
        if form.is_valid():
            user_id=form.cleaned_data['user_id']
            if OurUser.objects.filter(user_id=user_id).exists():
                context=initial_ops.get_details(user_id)
                logger.info('user details displayed')
                return render(request,'userdetails.html',context)
            else:
                context={}
                context['form']=AdminOps
                context['msg_exist']='The user does not exist!'
                return render(request,'userdetailsform.html',context)
        
class Transactions:
    def dep_form(request,acc_no):
        context={}
        context['form']=DepWithForm
        context['acc_no']=acc_no
        return render(request,'deposit.html',context)


    def trsn_deposit(request,acc_no):
        form=DepWithForm(request.POST)
        if form.is_valid():
            # acct_no=form.cleaned_data['acc_no']
            trsnc_amount=form.cleaned_data['Enter_amount']
            trsn_type='Deposit'
            acc_obj=AccountDetails.objects.get(pk=acc_no)
            balance=acc_obj.acc_bal
            trnsc_balance=balance+trsnc_amount
            dep_update=AccountTransactions.objects.create(trsn_acc_no=acc_obj,trsn_type=trsn_type,trsn_amount=trsnc_amount,trsn_balance=trnsc_balance)
            # change bal in acc details table
            acc_obj.acc_bal=trnsc_balance
            acc_obj.save()
            
            # show updated bal on details page
            acc_obj=AccountDetails.objects.get(pk=acc_no)
            user_id=acc_obj.acc_id_id
            context=initial_ops.get_details(user_id)
            context['msg_dep']='Deposited Successfully!'
            logger.info('deposit successful')
            return render(request,'userdetails.html',context)
        
    def withd_form(request,acc_no):
        context={}
        context['form']=DepWithForm
        context['acc_no']=acc_no
        return render(request,'withdraw.html',context)
        
    def trsn_withdraw(request,acc_no):
        form=DepWithForm(request.POST)
        if form.is_valid():
            context={}
            # acct_no=form.cleaned_data['acc_no']
            trsnc_amount=form.cleaned_data['Enter_amount']
            acc_obj=AccountDetails.objects.get(pk=acc_no)
            context['bal']=acc_obj.acc_bal
            context['acc_no']=acc_no
            if acc_obj.acc_bal<trsnc_amount:
                context['form']=DepWithForm
                context['msg_insuf']='Insufficient Funds'
                return render(request,'withdraw.html',context)
            if trsnc_amount>40000:
                context['form']=DepWithForm
                context['msg_limit']='Please withdraw in limit'
                return render(request,'withdraw.html',context)

            trnsc_balance=acc_obj.acc_bal-trsnc_amount
            withd_update=AccountTransactions.objects.create(trsn_acc_no=acc_obj,trsn_type='Withdraw',trsn_amount=trsnc_amount,trsn_balance=trnsc_balance)
            acc_obj.acc_bal=trnsc_balance
            acc_obj.save()
            
            acc_obj=AccountDetails.objects.get(pk=acc_no)
            context=initial_ops.get_details(acc_obj.acc_id_id)
            context['msg_with']='Withdrawn successfully!'
            logger.info('withdraw successful')
            return render(request,'userdetails.html',context)
        
    # def trsn_hist(request,acc_no):
    #     obj=AccountTransactions.objects.filter(trsn_acc_no_id=acc_no)
    #     context={}
    #     for i in range(len(obj)):
    #         context[i]=[]
    #     i=0
    #         context[i].append(elem.trsn_type)
    #         context[i].append(elem.trsn_amount)
    #         context[i].append(elem.trsn_balance)
    #         i=i+1
    #     context[i]=i
    #     bal_obj=AccountDetails.objects.get(pk=acc_no)
    #     context['final_bal']=bal_obj.acc_bal
    #     return render(request,'trsndetails.html',context)
            

class DelUpdate:

    def del_user(request,user_id):
        acc_obj=OurUser.objects.get(user_id=user_id)
        acc_obj.delete()
        
        context={}
        context['form']=AdminOps
        context['msg_del']="User deleted successfully!"
        logger.info('user deleted successfully')
        return render(request,'userdetailsform.html',context)
    
    def update_user_form(request,user_id):
        context={}
        context['form']=UpdateForm
        context['user_id']=user_id
        return render(request,'updateuserform.html',context)
    
    def update_user(request,user_id):
        form=UpdateForm(request.POST)
        if form.is_valid():
            user_obj=OurUser.objects.get(user_id=user_id)
            user_obj.user_id=user_id
            user_obj.f_name=form.cleaned_data['f_name']
            user_obj.l_name=form.cleaned_data['l_name']
            user_obj.res_addr=form.cleaned_data['res_addr']
            user_obj.off_addr=form.cleaned_data['off_addr']
            user_obj.phone_no=form.cleaned_data['phone_no']
            user_obj.save()
            
            context=initial_ops.get_details(user_obj.user_id)
            context['msg_update']= "User updated successfully!"
            logger.info('user updated successfully')
            return render(request,'userdetails.html',context)
    

class UserOps:

    def self_home(request):
        return render(request,'index.html')
    
    def self_register(request):
        context={}
        context['form']=RegForm
        return render(request,'selfregister.html',context)
    
    def self_create_user(request):
        form=RegForm(request.POST)
        if form.is_valid():
            user_id=form.cleaned_data['user_id']
            f_name=form.cleaned_data['f_name']
            l_name=form.cleaned_data['l_name']
            res_addr=form.cleaned_data['res_addr']
            off_addr=form.cleaned_data['off_addr']
            phone_no=form.cleaned_data['phone_no']
            if OurUser.objects.filter(user_id=user_id).exists():
                context={}
                context['form']=form
                context['msg_exist']='The User Id already exists!'
                return render(request,'selfregister.html',context)

            try:
                our_user=OurUser.objects.create(user_id=user_id,f_name=f_name,l_name=l_name,res_addr=res_addr,off_addr=off_addr,phone_no=phone_no)
            except IntegrityError:
                logger.error('user name already exists')
                our_user=OurUser.objects.get(user_id=user_id)

            acc_no=random.randint(100001,200000)
            account=AccountDetails.objects.create(acc_no=acc_no,acc_id=our_user)
            # context={}
            # context['our_user']=our_user
            # context['account']=account

            # acc_obj=AccountDetails.objects.get(pk=acc_no)
            # context['acc_no']=acc_obj.acc_no
            # context['acc_bal']=acc_obj.acc_bal
            context=initial_ops.get_details(user_id)
            logger.info('new user created')
            return render(request,'selfuserdetails.html',context)


class OurUserApiView(GenericAPIView):

    serializer_class=OurUserSerializer

    def get(self,request):
        allUser=OurUser.objects.all().values()
        return Response({"Message":"List of User", "User List":allUser})
 
    def post(self,request):
        try:
            print('Request data is : ',request.data)
            serializer_obj=OurUserSerializer(data=request.data)
            if(serializer_obj.is_valid()):

                if serializer_obj.data.get("user_id"):
                                our_user=OurUser.objects.create(user_id=serializer_obj.data.get("user_id"),
                                f_name=serializer_obj.data.get("f_name"),
                                l_name=serializer_obj.data.get("l_name"),
                                res_addr=serializer_obj.data.get("res_addr"),
                                off_addr=serializer_obj.data.get("off_addr"),
                                phone_no=serializer_obj.data.get("phone_no"),
                                )
                acc_no=random.randint(100001,200000)
                our_user=OurUser.objects.get(user_id=serializer_obj.data.get("user_id"))
                AccountDetails.objects.create(acc_no=acc_no,acc_id=our_user)

            user=OurUser.objects.all().filter(user_id=request.data["user_id"]).values()
            return Response({"Message":"New User Added!", "User":user})

        except IntegrityError:
            return HttpResponse("Username already exists")