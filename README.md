# user_management

steps to run projects 


 
1- virtualenv projectName    {create virtual eviroment}
2- cd projectName            {go inside virtual evirometn directory}
3- Scripts\activate          {Active virtual eviroment}
4- git clone https://github.com/shubhamguptaorg/user_management/      {clone the project inside the virtual enviroment directory}
5- cd user_management         {go inside user_management directory which contain all project files}
6- pip install -r requirements.txt  {install all project requirements}
7- cd userManagement  {go inside userManagement directory}
8- python manage.py runserver  {stat the local server}
9- open web browser-->>>> open lcoalhost:8000

Login-detail
 username- shubham
 password - 1234
 
 Admin-login 
  username- admin
 password - loginlogin
 
 For create new admin user 
 python manage.py createsuperuser
 
 
 NOTE->> After registration user create as not active. First login admin pannel and active the user to allow login in userDashboard.
