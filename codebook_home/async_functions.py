import asyncio
import time
from datetime import datetime
import json
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from multiprocessing import Pool


async def update_cache_queue():
    time.sleep(3)
    print("\n running async function update cache queue :-")
    with open("cache_queue.json", "a+") as file:
        file_json_obj = json.load(file)
        file_json_obj[0]["change_cache"] = True
        json.dump(file_json_obj, file)
        print("file update secussfully ")


async def clear_cache():
    time.sleep(3)
    print("\n running clear_cache async function ")
    cache.clear(prefix="data")
    print("cache cleared ")


async def send_welcome_mail(fname, lname, email):
    time.sleep(3)
    print("running send welcome mail async function ")
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
