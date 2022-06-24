import threading
import time
import datetime
import json
import asyncio
import time
from datetime import datetime
import json
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from multiprocessing import Pool


def update_cache_queue():
    #time.sleep(3)
    print("\n running thread function update cache queue :-")
    with open("/home/mmorya/cache_queue.json", "r+") as file:
        print(file)
        print(file.read())
        file_json_obj = json.load(file)
        file_json_obj["change_cache"] = True
        file.seek(0)
        json.dump(file_json_obj, file, indent=0)
        print("file update secussfully ")


def clear_cache():
    time.sleep(3)
    print("\n running clear_cache thread function ")
    cache.clear()
    print("cache cleared ")


def send_welcome_mail(fname, lname, email):
    time.sleep(3)
    print("running send welcome mail thread function ")
    try:
        print("User Created succesfully sending an Welcome massage through email ")
        subject = 'Greetings from Codebook...'
        message = f"Hello {fname} {lname} Welcome to Coodbook , we are glad to have you "
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email
        send_mail(subject, message, email_from, recipient_list)
    except:
        print("error occured in sending the email")
        # messages.error(
        #     request, " there was some error in sending the welcome mail  ")
        # return redirect(request.META['HTTP_REFERER'])
        pass

