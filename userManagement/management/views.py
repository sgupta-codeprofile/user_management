from django.shortcuts import render
from django.views import generic
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import extendeduser
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,SignupForm
from .forms import uploadImageUser


class Index(generic.View):
    template_name='management/index.html'
    redirect_template='management/userDashboard.html'
    admin_template='management/adminDashboard.html'
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_superuser and request.user.is_active:
                return redirect('/admindashboard')
            else:
                if request.user.is_active:
                    return redirect('/userdashboard')
                else:
                    return render(request,self.template_name,{'LoginForm':LoginForm,'notActiveStatus':True})
        else:
            return render(request,self.template_name,{'LoginForm':LoginForm})
    def post(self,request):
        formData=LoginForm(request.POST)
        if formData.is_valid():
            userCredential=request.POST
            userName=userCredential['userName']
            password=userCredential['password']
            if userName == 'admin':
                #admin dashboard
                user = auth.authenticate(username=userName, password=password)
                if user is not None:
                    auth.login(request,user)
                    return redirect('/admindashboard')
            else:
                #user dasboard
                try:
                    try:
                        user = auth.authenticate(username=userName, password=password)

                    except:
                        return render(request,self.template_name,{'userNotActive':True})
                    if user is not None:
                        auth.login(request, user)
                        return redirect('/userdashboard')
                    else:
                        return render(request, self.template_name, {'LoginForm':LoginForm})
                except:
                    print("exception")
        else:
            print("form invalid")
        return render(request, 'management/index.html',{'LoginForm':LoginForm})

class AdminDashboard(generic.View):
    template_name='management/adminDashboard.html'
    main_template='management/index.html'
    def get(self,request):
        if request.user.is_authenticated and request.user.is_superuser and request.user.is_active:
            # authDetails= User.objects.all().select_related('getallall') NOt working properly
            sendData=[[{ 'id':user.id,
                         'username': user.username,
                         'firstname': user.first_name,
                         'lastname': user.last_name,
                         'email': user.email,
                         'role': user.is_superuser,
                         'isactive': user.is_active,
                         'gender': extendDetail.gender,
                         'phoneNumber': extendDetail.phoneNumber,
                         } for extendDetail in extendeduser.objects.filter(user_id=user.id)]  for user in User.objects.all()]
            return render(request,self.template_name,{'userData':sendData})
        else:
            print("hello")
            return render(request,self.main_template,{'LoginForm':LoginForm})


class SignUp(generic.View):
    template_name='management/signup.html'
    main_template='management/index.html'
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_superuser and request.user.is_active:
                return redirect('/admindashboard')
            else:
                if request.user.is_active:
                    return redirect('/userdashboard')
                else:
                    return render(request, self.template_name, {'SignupForm': SignupForm})
        else:
            return render(request,self.template_name,{'SignupForm':SignupForm})

    def post(self,request):
        formValid=SignupForm(data=request.POST)
        if formValid.is_valid():
            saveData=request.POST
            if(saveData['password']!=saveData['confirmPassword']):
                print("passWord not match")
                return render(request,self.template_name,{'passwordNotMatch':True,'SignupForm':SignupForm})
            try:
                user=User.objects.get(username=saveData['username'])
                return render(request,self.template_name,{'UsernameExist':True,'SignupForm':SignupForm})
            except:
                user=User.objects.create_user(username=saveData['username'],password=saveData['password'],email=saveData['userEmail'])
                user.first_name=saveData['firstName']
                user.last_name=saveData['lastName']
                user.is_active=0
            registerDate=extendeduser(
                dateOfBirth=saveData['dateOfBirth'],
                phoneNumber=saveData['phoneNumber'],
                gender=saveData['chooseGender'],
                user=user
            )
            registerDate.save()
            user.save()
            render(request,self.main_template,{'LoginForm': LoginForm,'dataSaveSucess':True})
            return redirect('/')
        else:
            print("form is not valid")

        return render(request,self.template_name,{'SignupForm':SignupForm})

class UserDashboard(generic.View):
    template_name='management/userDashboard.html'
    main_template='management/index.html'
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_active and not request.user.is_superuser:
                authDetails= User.objects.get(username=request.user.username)
                userDetail = extendeduser.objects.get(user_id=authDetails.id)
                return render(request, self.template_name, {'userDetail':userDetail,'authDetails':authDetails})
            else:
                return render(request, self.main_template, {'LoginForm': LoginForm, 'notActiveStatus': True})
        else:
            return render(request,self.main_template,{'SignupForm':SignupForm})


    def post(self,request):
        if request.user.is_authenticated and request.user.is_active:
            pass
        else:
            return render(request,self.main_template,{'LoginForm':LoginForm})



class showAdminData(generic.View):
    template_name='management/admin_showUserData.html'
    main_template='management/index.html'
    def get(self,request):
        if request.user.is_authenticated and request.user.is_superuser and request.user.is_active:
            # authDetails= User.objects.all().select_related('getallall') NOt working properly
            sendData=[[{ 'id':user.id,
                         'username': user.username,
                         'firstname': user.first_name,
                         'lastname': user.last_name,
                         'email': user.email,
                         'role': user.is_superuser,
                         'isactive': user.is_active,
                         'gender': extendDetail.gender,
                         'phoneNumber': extendDetail.phoneNumber,
                         'imagePath':extendDetail.profileImage
                         } for extendDetail in extendeduser.objects.filter(user_id=user.id)]  for user in User.objects.all()]
            print(sendData)
            return render(request,self.template_name,{'userData':sendData,'uploadImage':uploadImage})
        else:
            return render(request,self.main_template,{'LoginForm':LoginForm})

class UserDetailEdit(generic.View):
    template_name='management/userEdit.html'
    main_template='management/index.html'
    def get(self,request):
        if request.user.is_authenticated and request.user.is_active:
            authDetails = User.objects.get(username=request.user.username)
            userDetail = extendeduser.objects.get(user_id=authDetails.id)
            return render(request, self.template_name, {'userDetail':userDetail,'authDetails':authDetails,'SignupForm':SignupForm})
        else:
            return render(request, self.main_template, {'LoginForm': LoginForm, 'notActiveStatus': True})
    def post(self,request):
        if request.user.is_authenticated:
            authDetails = User.objects.get(username=request.POST['username'])
            authDetails.first_name=request.POST['firstName']
            authDetails.last_name=request.POST['lastName']
            authDetails.username=request.POST['username']
            authDetails.email=request.POST['userEmail']
            authDetails.save()
            return render(request,self.template_name,{'updateDataSuccess':True})
        else:
            return render(request,self.main_template,{'LoginForm':LoginForm})


def deleteuser(request,userId):
    if request.method=='GET' and len(userId)!=0:
        if request.user.is_authenticated and request.user.is_superuser:
            User.objects.filter(pk=userId).delete()
        else:
            print("not authenticated")
    else:
        print("nt numeric")
    return redirect('/admindashboard/showuserdata/')

def activeUser(request,userId):
    if request.method=='GET' and len(userId)!=0:
        if request.user.is_authenticated and request.user.is_superuser:
            try:
                    User.objects.filter(pk=userId).update(is_active=1)
            except User.DoesNotExist:
                print("Id Not exist")
        else:
            print("not authenticated")
    else:
        print("n0t numeric")
    return redirect('/admindashboard/showuserdata/')


def deactiveUser(request,userId):
    if request.method=='GET' and len(userId)!=0:
        if request.user.is_authenticated and request.user.is_superuser:
            print(userId)

            try:
                User.objects.filter(pk=userId).update(is_active=0)
            except User.DoesNotExist:
                print("Id Not exist")
        else:
            print("not authenticated")
    else:
        print("n0t numeric")
    return redirect('/admindashboard/showuserdata/')

def uploadImage(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username=request.user.username
            authUser=User.objects.get(username=username)
            saveUser=extendeduser.objects.get(user_id=authUser.id)
            check_form=uploadImageUser(request.POST,request.FILES)
            try:
                if check_form.is_valid():
                    catch_image=check_form.cleaned_data['image']
                    saveUser.profileImage=catch_image
                    saveUser.save()
                    return redirect('/userdashboard')
                else:
                    return redirect('/')
            except:
                return redirect('/')
        else:
            return render(request, 'management/uploadImage.html', {'uploadImage': uploadImageUser})
    else:
        print("invalid rquest")
        return render(request,'management/uploadImage.html',{'uploadImage':uploadImageUser})



def logout(request):
    auth.logout(request)
    return redirect('/')





