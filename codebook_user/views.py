import asyncio
import threading
from email import message
import email
from genericpath import exists
from django.shortcuts import render,redirect,HttpResponse
import json
from django.contrib.auth.models import User

from rest_framework.response import Response
from codebook_posts.models import posts
from codebook_user.models import User_model, friends2, user
from .serializer import UserSerializer,userSerializer,User_modelSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .authentication import is_token_expired, token_expire_handler, expires_in,authenticate_credentials
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import base64
import os
from email.mime import image
from django.db import models
import datetime
from datetime import *
# from pytz import timezone
import pytz
from django.utils import timezone, datetime_safe
from django.db.models import Q
from itertools import chain
from codebook_home import threads as func

# Create your views here.


def index(request):
    print("running index function")
    if "username" in request.session:
        return redirect("user_profile")
    return render(request, "login_signup.html")


def signout(request):
    print("running sign out function")
    if "username" in request.session:
        del request.session['username']
    return redirect("index")
        


def user_signup(request):
    if "username" in request.session:
        return redirect("user_profile")
    print("running user_signup function ")
    context = {
        "username":request.POST['signusername'],
        "first_name" :request.POST['firstname'],
        "last_name" :request.POST['lastname'],
        "email":request.POST['email'],
        "password":make_password(request.POST['password']),
        "phone_no": request.POST['phone_no'],
        "birth_date" : request.POST['DOB']   
    }
    print("context1", context)
    input_username = request.POST['signusername']
    input_email = request.POST['email']
    
    if request.POST['password'] != request.POST['re_password']:
        messages.error(
            "password and confirm password dont match ,please enter same password ")
        return redirect(request.META['HTTP_REFERER'])
    
    filtered_username = User_model.objects.filter(username= input_username)
    filtered_email = User_model.objects.filter(email= input_email)
    filtered_phone = User_model.objects.filter(phone_no = request.POST['phone_no'])
    
    if filtered_username:
        messages.error(request, "username already exist ")
        return redirect("index")

    elif filtered_email:
        messages.error(request, "email already exist ")
        return redirect("index")

    elif filtered_phone:
        messages.error(request,"pnone no already exist ")
        return redirect("index")

    else:

        serializer = User_modelSerializer(data=context)
        
        # obj = User_model(username=request.POST['signusername'], password=make_password(
        #     request.POST['password']), first_name=request.POST['firstname'], last_name=request.POST['lastname'], email=request.POST['email'], phone_no=request.POST['phone_no'], birth_date=request.POST['DOB'])
        # obj.save()
        
        if serializer.is_valid():
            print("serializer  passed ")
            temp = User(
                username=request.POST['signusername'], password=make_password(request.POST['password']))
            temp.save()
            serializer.save()
            messages.success(request, "Successfuly signed Up Please Setup your Profile ")
            user1 = authenticate(username=request.POST["signusername"], password=request.POST["password"])
            print(user1)
            token, _ = Token.objects.get_or_create(user=user1)
            request.session['username'] = input_username
            request.session['token'] = token.key
            request.session.set_expiry(0)
            request.session.modified = True
            print("token = ", token.key)
            print("User Created succesfully sending an Welcome massage through email ")
            threading.Thread(target=func.send_welcome_mail, kwargs={"fname":str(request.POST['firstname']),"lname":str(request.POST['lastname']),"email":str(request.POST['email'])}).start()
            # try:
            #     print("User Created succesfully sending an Welcome massage through email ")
            #     subject = 'Greetings from Codebook...'
            #     message = f"Hello {request.POST['firstname']} {request.POST['lastname']} Welcome to Coodbook , we are glad to have you "
            #     email_from = settings.EMAIL_HOST_USER
            #     recipient_list = [str(request.POST['email'])]
            #     send_mail(subject, message, email_from, recipient_list)
            # except:
            #     print("error occured in sending the email")
            #     # messages.error(
            #     #     request, " there was some error in sending the welcome mail  ")
            #     # return redirect(request.META['HTTP_REFERER'])
            #     pass
            return redirect("user_profile")    

        else:
            return JsonResponse(serializer.errors, status=400)


def user_signin(request):
    print("running user_signin function ")
    input_username = request.POST["input_username"]
    input_password = request.POST["input_password"]
    
    print("username", input_username)
    print("password", input_password)
    if input_username is None or input_password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    try:
        user1 = authenticate(username=input_username, password=input_password)
    except:
        return HttpResponse("wrong id password ")
    print("user1", user1)
    if not user1:
        messages.error(request," invalid credantials ")
        return redirect(request.META["HTTP_REFERER"])

    token, _ = Token.objects.get_or_create(user=user1)
    temp = Token.objects.all()
    print("token objects all = ", temp)
    print("token ", token.key)
    request.session['username'] = input_username
    request.session['token'] = token.key
    request.session.modified = True
    print("request = ", request )
    print("token = ", token.key)
    
    # user_data = User_model.objects.filter(username=input_username).all()
    # context = {"user_data":user_data}
    return redirect("codebook_home")


def user_profile(request):
    print(" printing request.method ==", request.method)
    print("\n  user profile function  ==")
    if "username" not in request.session:
        return redirect("index")
    print("running user_prifile funtion ")
    user_data = User_model.objects.filter(username=request.session["username"]).all()
    context = {"user_data": user_data,
               "username": request.session['username']}
    return render(request, "user_profile.html", context)


def edit(request , field ):
    print(" printing request.method ==", request.method)
    if "username" not in request.session:
        return redirect("index")
    print("running edit function ")
    try:
        user_object = User_model.objects.get(username=request.session["username"])
    except:
        messages.error(request, "something went wrong , login again ")
        return redirect("index")
    if field == "first_name":
        print("running edit first name")
        user_object.first_name = request.POST["first_name"]
        messages.success(request, "First Name updated successfully")
  
    elif field == "last_name":
        print("running edit last name")
        user_object.last_name = request.POST["last_name"]
        messages.success(request, "Last Name updated successfully")
        
    elif field == "phone_no":
        print("running edit phone no ")
        try:
            user_object2 = User_model.objects.get(username=request.session["username"])
            users_obj = User_model.objects.filter(phone_no=request.POST["phone_no"])
        except:
            messages.error(request, "something went wrong ,please try again")
            return redirect(request.META["HTTP_REFERER"])
        if(users_obj):
            messages.error(request, "Phone no already Exist ")
            return redirect(request.META["HTTP_REFERER"])
        
        user_object2.phone_no = request.POST["phone_no"]
        messages.success(request, "phone no updated successfully")
    
    elif field == "about":
        print("running edit email function")
        try:
            user_object2 = User_model.objects.get(username=request.session["username"])
        except:
            messages.error(request, "something went wrong ,please try again")
            return redirect(request.META["HTTP_REFERER"])
        
        user_object2.about = request.POST["about"]
        messages.success(request, "Your about section updated successfully")
    
    elif field == "image":
        user_object2 = User_model.objects.get(username=request.session["username"])
        print("running edit image ")
        print("request", request)
        print("print request.post", request.POST)
        print("request.post[image]", request.FILES["image"])
        # if len(user_object3.profile_pic) > 0:
        #     os.remove(user_object3.profile_pic.path)
        user_object2.profile_pic = request.FILES['image']
        messages.success(request, "image updated successfully")
    
    if field in ["first_name","last_name"]:
        user_object.save()
        return redirect(request.META["HTTP_REFERER"])
    else:
        user_object2.save()
        return redirect(request.META["HTTP_REFERER"])
    
def forget_password_page(request):

    print("runnning forget password page function")
    return render(request, "forget_password_page.html")


def get_forget_reset_password_link(request):
    print("running forget password function ")
    username = request.POST["input_username"]
    email = request.POST["input_email"]
    
    try:
        users_db_obj = User_model.objects.get(username=username, email=email)
        
    except:
        return HttpResponse(" user dont exist ")
    
    print("passed email",email)
    message = str(email)
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    encoded_email = base64_bytes.decode('ascii')
    try:
        print("link to rest password ")
        print(
            f"http://127.0.0.1:8000/reset_forgotten_password_page/{encoded_email}/")
        subject = 'Link to reset your password'
        message = f"""Hi {username}, click on this link to set your password  http://127.0.0.1:8000/reset_forgotten_password_page/{encoded_email}/."""
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [str(email)]
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse(f"""A email with a link to reset your password has been sent to {email} check it out """)
    except:
        print("error occured in sending the email")
        messages.error(
            request, " there was some error in sending the email to reset your password please try again ")
        return redirect(request.META['HTTP_REFERER'])


def reset_forgotten_password_page(request,email):
    if "username" not in request.session:
        return redirect("index")
    base64_message = email
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decoded_email = message_bytes.decode('ascii')
    print("decoded email", decoded_email)
    context = {"email":str(decoded_email), "firstname":"yash morya"}
    return render(request, "reset_forgotten_password_page.html", context)


def reset_forgotten_password(request):
    password = request.POST["input_password"]
    re_entered_passsword = request.POST["input_re_password"]
    email_of_user = request.POST["input_email"]
    
    if password == re_entered_passsword:
        try:
            user_obj = User_model.objects.get(email=email_of_user)
            user_obj.password = make_password(password)
            user_obj.save()
            messages.success(request,
                "Password reset successfully , Please Login with your new password ")
            return redirect("index")
        except:
            messages.error(
                request, "something went wrong while changing the password please try again using the same link")
            return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request,
                    "entered new password and confirm password does not match please enter same in both fields ")
        return redirect(request.META['HTTP_REFERER'])
    
    
def change_password_page(request):
    if "username" not in request.session:
        return redirect("index")
    print("running change password page function")
    return render(request, "change_password_page.html")


def change_password(request):
    if "username" not in request.session:
        return redirect("index")
    print("running change password function ")
    old_password  = request.POST["input_old_password"]
    password = request.POST["input_password"]
    re_entered_passsword = request.POST["input_re_password"]
    username = request.session["username"]
    try:
        user_obj = User_model.objects.get(username=username)
        if user_obj.password == old_password:
            if password == re_entered_passsword:
                user_obj.password=make_password(password)
                user_obj.save()
                messages.success(request,
                                 "Password reset successfully , Please Login with your new password ")
                return redirect("user_profile")
            else:
                messages.error(
                    request, "entered new password and confirm password does not match please enter same in both fields ")
                return redirect(request.META['HTTP_REFERER'])
                
        else:
            messages.error(
                request, "Invalid Old Password ")
            return redirect(request.META['HTTP_REFERER'])
            
    except:
        messages.error(
            request, "something went wrong while changing the password please try again ")
        return redirect(request.META['HTTP_REFERER'])
    
    
def add_friend(request, target_username):
    print(" printing request ==", request)
    print("\n  printing request ==")
    for x in request:
        print(x)
    
    if "username" not in request.session:
        return redirect("index")
    print("running add friend function ")
    print("target username ", target_username)
    is_already = friends2.objects.filter(Q(username=request.session["username"],friend_with=target_username)| Q(username=target_username,friend_with=request.session["username"]))
    if is_already:    
        print("is already = ",is_already)
        messages.error(request,"looks like you already sent a freind request or you are alredy a friend ")
    else:
        obj = friends2(username=request.session["username"], friend_with=target_username, status="pending")
        obj.save()
        messages.success(request,
                         "request sent successfully ")
    return redirect(request.META['HTTP_REFERER'])



def friends_page(request):
    
    if "username" not in request.session:
        return redirect("index")
    print("running friends page function ")
    try :
        requested = friends2.objects.filter(username=request.session["username"],status="pending")
        
        your_friends = friends2.objects.filter(
            username=request.session["username"], status="friend").values()
        
        requests_ = friends2.objects.filter(
            friend_with=request.session["username"], status="pending")
        print("\n \n your friend ", your_friends)
        tempuser = []
        for x in your_friends:
            tempuser.append(x["friend_with"])
            
        print("\n \n tempuser",tempuser)
        
        obj4 = User_model.objects.filter(username__in=tempuser)
        print("\n \n \n obj 4",obj4)
    except:
        return HttpResponse("oops looks like you dont have any friends and not even sended any request to anyone ")
    
    return render(request, "friends_page.html", context={"friends": obj4, "username": request.session['username'], "request":requests_, "requested":requested})



def make_friend(request, target_username):
    if "username" not in request.session:
        return redirect("index")
    print("target username ", target_username)
    print("running make friends function ")
    try:
        obj = friends2.objects.get(friend_with=request.session["username"],username=target_username)
        obj2 = friends2(username=request.session["username"],friend_with=target_username,status="friend")
        obj2.save()
        print("obj = ", obj)
        obj.status =  "friend"
        obj.save()
        messages.success(request, f"""successfully addded {target_username} as friend """)
        return redirect(request.META['HTTP_REFERER'])
    except:
        messages.error(request, "something went wrong could not add him as friend ")
        return redirect(request.META["HTTP_REFERER"])
    
    
def reject_friend_request(request, target_username):
    if "username" not in request.session:
        return redirect("index")
    print("running reject friend request function ")
    print("target username ", target_username)
    try:
        obj = friends2.objects.get(
            username=target_username, friend_with=request.session["username"])
        print("obj = ", obj)
        obj.delete()
        messages.success(
            request, f"""successfully rejected {target_username} friend request  """)
        return redirect(request.META['HTTP_REFERER'])
    except:
        messages.error(
            request, "something went wrong could not able to reject his request please try again  ")
        return redirect(request.META["HTTP_REFERER"])
    
    
def delete_friend_request(request, target_username):
    if "username" not in request.session:
        return redirect("index")
    print("\n \n running delete friend request function ")
    try:
        obj = friends2.objects.get(Q(
            username=request.session["username"], friend_with=target_username)|Q(friend_with=request.session["username"],username=target_username))
        obj.delete()
        messages.success(
            request, f"""successfully rejected {target_username} friend request  """)
        return redirect(request.META['HTTP_REFERER'])
    except:
        messages.error(
            request, "something went wrong could not able to delete his request please try again  ")
        return redirect(request.META["HTTP_REFERER"])
    
    
def un_friend(request, target_username):
    if "username" not in request.session:
        return redirect("index")
    print("\n running un_friend function \n \n \n ")
    try:
        obj = friends2.objects.get(Q(
            username=request.session["username"], friend_with=target_username) | Q(friend_with=request.session["username"], username=target_username))
        obj.delete()
        messages.success(
            request, f"""successfully deleted {target_username}   """)
        return redirect(request.META['HTTP_REFERER'])
    except:
        messages.error(
            request, "something went wrong could not able to un_friend user , please try again  ")
        return redirect(request.META["HTTP_REFERER"])
    
