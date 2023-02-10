from django.urls import path
from . import views
from django.contrib import admin

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Users description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [path('',views.UserOps.self_home,name='selfhome'),
               path('adminhome/',views.initial_ops.admin_home,name='adminhome'),
               # path to admin home was ''
               path('user_reg_form/',views.initial_ops.reg_form,name='reg_form'),
               path('create_user/',views.initial_ops.create_user,name='create_user'),
               path('userdetailsform/',views.initial_ops.user_details_form,name='user_details_form'),
               path('userdetails/',views.initial_ops.display_user_details,name='user_details'),
               path('depositform/<int:acc_no>',views.Transactions.dep_form,name='dep_form'),
               path('deposit/succ/<int:acc_no>',views.Transactions.trsn_deposit,name='deposit'),
               path('withdform/<int:acc_no>',views.Transactions.withd_form,name='with_form'),
               path('withdraw/succ/<int:acc_no>',views.Transactions.trsn_withdraw,name='with_form'),
               # path('trsndetails/<int:acc_no>',views.Transactions.trsn_hist,name='trsnhistory'),
               path('deleteuser/<str:user_id>',views.DelUpdate.del_user,name='deleteuser'),
               path('updateuserform/<str:user_id>',views.DelUpdate.update_user_form,name='updateuserform'),
               path('updateuser/<str:user_id>',views.DelUpdate.update_user,name='updateuser'),
               path('selfhome/',views.UserOps.self_home,name='selfhome'),
               path('selfregister/',views.UserOps.self_register,name='selfregister'),path('selfcreate_user/',views.UserOps.self_create_user,name='selfcreateuser'),
               path('swagger/',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')]
