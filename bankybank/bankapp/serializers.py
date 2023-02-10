from rest_framework import serializers
import random
class OurUserSerializer(serializers.Serializer):
    user_id=serializers.CharField(label="enter user_id")
    f_name=serializers.CharField(label="enter first name")
    l_name=serializers.CharField(label="enter last name")
    res_addr=serializers.CharField(label="enter residential address")
    off_addr=serializers.CharField(label="enter oddicial address")
    phone_no=serializers.CharField(label="enter phone number")
    #acc_no=random.randint(100001,200000)
    


