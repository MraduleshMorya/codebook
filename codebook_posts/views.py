from ctypes import Union
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render
from .models import notifications, posts
from email import message
import email
from django.shortcuts import render, redirect, HttpResponse
import json
from django.contrib.auth.models import User

from rest_framework.response import Response
from codebook_user.models import User_model, liked_posts, post_commnets, user
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
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
from itertools import chain
from django.db import connection
# Create your views here.


def post_image_page(request):
    if "username" not in request.session:
        return redirect("index")
    
    return render(request, "post_image.html" ,context={"username": request.session['username']})


def post_video_page(request):
    if "username" not in request.session:
        return redirect("index")
    return render(request, "post_video.html", context={"username": request.session['username']})


def create_post(request, field):
    if "username" not in request.session:
        return redirect("index")
    if field == "image":
        print("running image ")
        print(request.FILES['image'])
        print(request.POST["text"])
        post_obj = posts(
            username=request.session["username"], photo=request.FILES['image'], description=request.POST["text"])
        try:
            post_obj.save()
            messages.success(
                request, "Your image uploaded successfully  successfully")
            return redirect(request.META['HTTP_REFERER'])
        except:
            return HttpResponse("error occorrud during post the image ")

    elif field == "video":
        print("running video")
        print(request.FILES['video'])
        print(request.POST["text"])
        post_obj = posts(
            username=request.session["username"], video=request.FILES['video'], description=request.POST["text"], catagory="video")
        try:
            post_obj.save()
            messages.success(
                request, "Your video uploaded successfully  successfully")
            return redirect(request.META['HTTP_REFERER'])
        except:
            return HttpResponse("error occorrud during post the image ")
        
        
def open_post_page(request, postid):
    if "username" not in request.session:
        return redirect("index")
    print("open post page running ")
    post_obj = posts.objects.get(postid=postid)
    comment_obj = post_commnets.objects.filter(postid=postid)
    context = {"posted_photos": post_obj,"comments":comment_obj,
               "username": request.session['username']}
    
    return render(request, "particular_post_page.html", context)


def my_post_page(request):
    if "username" not in request.session:
        return redirect("index")
    print("my_post_page running ")
    my_posts = posts.objects.filter(username=request.session["username"])
    # my_posts |= posts.objects.filter(username='test2@')
    # print("printing query set :", my_posts)
    # print("post id ", my_posts["postid"])
    # no_of_posts = my_posts.count()
    # print("total no of posts ",no_of_posts)

    context = {"posts": my_posts , "username": request.session['username']}
    
    return render(request,"my_posts.html", context)


def delete_my_post(request, my_postid):
    if "username" not in request.session:
        return redirect("index")
    print("delete my post finction running ")
    post_obj = posts.objects.get(username=request.session["username"],postid=my_postid)
    print("posts details that is goint to be deleted ")
    post_obj.photo.delete(save=True)
    post_obj.video.delete(save=True)
    post_obj.delete()
    
    return redirect(request.META['HTTP_REFERER'])


def search_user(request):
    if "username" not in request.session:
        return redirect("index")
    print("runnning search user function ")
    print(request.POST)
    target_username = request.POST.get("find")
    
    filtered_users = User_model.objects.filter(username=target_username)
    print("filtered user ",filtered_users)
    
    # filter_by_name = User.objects.get(first_name=username)
    # print("query set appended := ", str(filtered_users))
    # # final = list(chain(filtered_users,filtered_users2))
    # # print("final",final)
    
    # temp = User.objects.raw('SELECT * FROM codebook_user_user WHERE username = %s',[user_to_be_searched])
    # print(temp)
    # for x in temp:
    #     print(x)
    
    # dict1 = {"name":"yash", "lname":"morya"}
    # doct2 = {"name":"yash1", "lname":"morya2"}
    # list1 = [dict1,doct2]
    
    # for x in list1:
    #     print(x["name"])
    #     print(x["lname"])
    
    # with connection.cursor() as cursor:
    #     # cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    #     cursor.execute("CREATE TABLE Persons( PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255))")
    #     cursor.execute("SELECT * FROM codebook_user_user INNER JOIN auth_user WHERE codebook_user_user.username = auth_user.username")
    #     row = cursor.fetchone()
    #     print("row",row)
    
    return render(request, "search_user.html", context={"user":filtered_users, "username":request.session["username"]})


def like_post(request, target_postid):
    if "username" not in request.session:
        return redirect("index")
    print("\n \n running like_post function ")
    
    try:
        print("\n \n  running try block of lik_post")
        liked_post_obj = liked_posts.objects.get(username=request.session["username"], postid=target_postid)
        messages.error(request," you have already liked this post ")
        
    except:
        print("\n \n running except block of like_post ")
        post_obj = posts.objects.get(postid=target_postid)
        post_obj.like_count = post_obj.like_count + 1
        
        print("\n \n check notification ")
        print("auther username  === ", post_obj.username)
        
        liked_post_obj2 = liked_posts(postid=post_obj,username=request.session["username"])
        notification_obj = notifications(postid=post_obj, author_username=post_obj.username, friend_username=request.session["username"], postid_toshow=post_obj.postid, operation ="like")
        
        
        
        notification_obj.save()
        liked_post_obj2.save()
        post_obj.save()
        messages.success(request," liked post successfully ")
        
    finally:
        print("\n \n running final block of like_post function ")
        return redirect(request.META['HTTP_REFERER'])
    
    
def comment(request,target_postid):
    if "username" not in request.session:
        return redirect("index")
    print("\n \n running comment function  ")
    given_comment = request.POST["given_comment"]
    post_obj = posts.objects.get(postid=target_postid)
    liked_post_obj2 = post_commnets(
    postid=post_obj, username=request.session["username"],comment=given_comment)
    notification_obj = notifications(postid=post_obj, author_username=post_obj.username,
                                     friend_username=request.session["username"], postid_toshow=post_obj.postid, operation="Comment")

    notification_obj.save()
    post_obj.comment_count = post_obj.comment_count + 1
    post_obj.save()
    liked_post_obj2.save()
    messages.success(request, " commented successfully successfully ")
    return redirect(request.META['HTTP_REFERER'])
    
    
def edit_post_page(request,target_postid):
    if "username" not in request.session:
        return redirect("index")
    
    post_obj = posts.objects.get(username=request.session["username"],postid=target_postid)
    
    return render(request, "edit_post_page.html", context={"post":post_obj})


def edit_post(request, field, target_postid):
    if "username" not in request.session:
        return redirect("index")

    post_obj = posts.objects.get(username=request.session["username"], postid=target_postid)

    if field == "image":
        post_obj.photo = request.FILES["image"]
        messages.success(request,"..image edited successfully ")
    
    elif field == "video":
        post_obj.video = request.FILES['video']
        messages.success(request, "..video edited successfully ")
        
    elif field == "text":
        messages.success(request, "..text edited successfully ")
        post_obj.description = request.POST["text"]
        
    post_obj.save()
    return redirect(request.META["HTTP_REFERER"])


def notification_page(request):
    if "username" not in request.session:
        return redirect("index")
    notification_obj = notifications.objects.filter(author_username=request.session["username"])
    context = {"nots":notification_obj}
    
    return render(request,"notification_page.html", context)
        