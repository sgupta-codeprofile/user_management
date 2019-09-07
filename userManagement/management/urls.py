from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .views import Index,SignUp,UserDashboard,AdminDashboard,logout,showAdminData,deleteuser,activeUser,deactiveUser,UserDetailEdit,uploadImage
# from .views import Index,UserDashboard,SignUp,AdminDashboard
app_name='management'


urlpatterns = [
    # path('',homepage,name="index"),
    path('',Index.as_view(), name='index'),
    path('signup',SignUp.as_view(),name="signup"),
    path('userdashboard',UserDashboard.as_view(),name="userDashboard"),
    path('admindashboard',AdminDashboard.as_view(),name="adminDashboard"),
    path('admindashboard/showuserdata/',showAdminData.as_view(),name='showAdminData'),
    path('admindashboard/showuserdata/deleteuser/<userId>',deleteuser,name='deleteuser'),
    path('admindashboard/showuserdata/activeUser/<userId>', activeUser, name='activeUser'),
    path('admindashboard/showuserdata/deactiveUser/<userId>', deactiveUser, name='deactiveUser'),
    path('uploadimage/',uploadImage,name="uploadImage"),
    path('editUserDetail/',UserDetailEdit.as_view(),name='userEditDetail'),
    path('logout',logout,name='logout')
]

