from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from codebook_posts.models import posts, notifications
from codebook_user.models import friends2, liked_posts, post_commnets
from django.db.models import Q
from .serializer import invoke_detailSerializer
from .models import invoke_detail
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import time
from codebook_user.models import User_model
from django.core.paginator import Paginator
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
import threading
from codebook_home.threads import clear_cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.


def is_user_loggedin(request):
    print("request.method in logged in ", request.method)
    print("\n \n running is user logge din function ")
    if "username" not in request.session:
        print("inside if block ")
        try:
            return redirect("index")
        except:
            print("\n \n try didnt worked")
            return HttpResponse("not working ")
    else:
        print("\n \n request  == ", request.session["username"])
        return True


def home(request):
    print("running home function -- ")
    page_no = 1
    try:
        page_no = int(request.GET.get("page_no"))
    except:
        pass

    if type(page_no) != int:
        page_no = 1

    # print("request.method == ",request.method)
    # print("request.POST == ", request.POST)
    # print("request.headers == ", request.headers)
    # print("request.body  == ", request.body)
    # print("request.path == ",request.path_info)
    # print("request.META.REMOTE_ADDR == ", request.META["REMOTE_ADDR"])
    # print("request.HTTP_USER_AGENT == ",request.META["HTTP_USER_AGENT"])
    # print("request.META.get('REMOTE_ADDR')",
    #       request.META.get('HTTP_X_FORWARDED_FOR'))
    #
    # print(" printing request ==", request)
    print("page no == ", page_no)
    if "username" not in request.session:
        return redirect("index")
    your_friends = friends2.objects.filter(
        username=request.session["username"], status="friend").values()

    friends_list = []
    for x in your_friends:
        friends_list.append(x["friend_with"])

    print("\n \n friends_list", friends_list)
    friends_list.append(request.session['username'])
    if "data" not in cache:
        print("\n \n cahce miss ")
        data = posts.objects.all()
        #data = posts.objects.filter(username__in=friends_list)
        print("\n \n \n data", data.filter(username__in=friends_list))
        cache.set("data", data.filter(username__in=friends_list), timeout=CACHE_TTL)
    else:
        print("\n \n cache hit ")
        data = cache.get("data")
        data = data.filter(username__in=friends_list)
        print("data inside chache hit ",data)
        #threading.Thread(target=clear_cache).start()
    # adding pagination
    paged_data = Paginator(data, 5)
    total_no_of_data = paged_data.count
    total_no_of_pages = paged_data.num_pages
    print("total no of page == ", total_no_of_pages)
    data_page = paged_data.get_page(page_no)

    context = {"posts": data_page, "username": request.session['username'],
               "total_no_of_pages_range": list(range(1, paged_data.num_pages + 1)),
               "total_no_of_pages": total_no_of_pages, "total_no_of_data": total_no_of_data,
               "current_page_no": int(page_no)}

    return render(request, "home.html", context)


def get_api_invokedata(request, username):
    try:
        print("running get api invokedata ")

        start = time.time()
        if username == "all":
            data = invoke_detail.objects.all().using('mongo')
            serialized_data = invoke_detailSerializer(data, many=True)
            # return HttpResponse(serialized_data.data)
            return JsonResponse(serialized_data.data, safe=False)
        elif len(username) > 0:
            try:
                data = invoke_detail.objects.filter(username=username).using('mongo')
                # print("\n data == ",data)
                serialized_data = invoke_detailSerializer(data, many=True)
                print("serialization passed ")
                # print("data",serialized_data)
                # print("\n data .data",serialized_data.data)
                print("execution completed of invoked api ")
                end = time.time()
                print("took this much time --", end - start)
                print("api finished ")
                return JsonResponse(serialized_data.data, safe=False)

            except:
                print("exception in get api ")
                return HttpResponse("NO DATA FOUND FOR THIS USER ")
    except:
        return HttpResponse("AN ERROR OCCURRED ")


def user_report(request):
    print("running user report function ")

    # get data using raw sql queries
    result = User_model.objects.raw(
        f""" SELECT * FROM codebook_user_user_model CROSS JOIN codebook_posts_posts WHERE codebook_user_user_model.username = codebook_posts_posts.username """)
    print("result = ", result)
    for results in result:
        print(results)
    return render(request, "temp.html", context={"result": result})


def user_report1(request, username):
    print("\n \n running report1 function ")
    # result = User_model.objects.raw(
    #     f""" SELECT * FROM codebook_user_user_model CROSS JOIN codebook_posts_posts
    #     on codebook_user_user_model.username = {username} AND codebook_posts_posts.username = {username}
    #     CROSS JOIN codebook_user_post_commnets ON codebook_user_post_commnets = {username}
    #
    #     """)
    # select um.*,pp.* from codebook_user_user_model um join codebook_posts_posts pp on um.username='test2@' and pp.username='test2@' join codebook_user_liked_posts;
    # result = User_model.objects.raw(f'''select um.*,pp.* from codebook_user_user_model um join codebook_posts_posts pp on um.username='{username}' and pp.username='{username}' join codebook_user_liked_posts;''')
    # print(result)
    # obj1 = User_model.objects.raw(f'''select um.*,p.* from codebook_user_user_model um join codebook_posts_posts p on um.username='{username}' and pp.username='{username}' join codebook_user_post_commnets c where(select p. from codebook_posts_posts where username = '{username}');''')
    # select um.*,p.*,c.* from codebook_user_user_model um left join codebook_posts_posts p on um.username=p.username left join codebook_user_post_commnets c on p.postid = c.postid_id where um.username = 'test2@';

    requested = friends2.objects.filter(username=request.session["username"], status="pending")

    your_friends = friends2.objects.filter(Q(
        username=username, status="friend") | Q(friend_with=username, status="friend")).values()

    requests_ = friends2.objects.filter(
        friend_with=request.session["username"], status="pending")
    print("\n \n your friend ", your_friends)
    tempuser = []
    for x in your_friends:
        tempuser.append(x["friend_with"])

    print("\n \n tempuser", tempuser)

    obj4 = User_model.objects.filter(username__in=tempuser)
    personal_info = User_model.objects.filter(username=username)

    user_liked_post_ids = liked_posts.objects.filter(username=username).values_list('postid')

    liked_post_obj = posts.objects.filter(
        Q(postid__in=liked_posts.objects.filter(username=username).values_list('postid')) | Q(
            postid__in=post_commnets.objects.filter(username=username))).values()

    created_posts = posts.objects.filter(username=username)

    user_post_comments = post_commnets.objects.filter(username=username).values()

    user_notification = notifications.objects.filter(author_username=username)
    print(user_notification)

    return render(request, "activity_report.html",
                  context={"personal_info": personal_info, "created_posts": created_posts,
                           "user_notification": user_notification, "friend_list": obj4, "request": requests_,
                           "requested": requested, "liked_post_ids": user_liked_post_ids,
                           "comments": user_post_comments, "notifications": user_notification,
                           "l_c_posts": liked_post_obj})
