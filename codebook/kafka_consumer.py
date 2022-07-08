from kafka import KafkaProducer
from kafka import KafkaConsumer
import base64
from codebook_posts.models import notifications,posts
import json
import datetime
import threading
from django.shortcuts import HttpResponse

def consumer_thread(request):
    print("Consumer thread invoked ")
    threading.Thread(target=kafkaconsumer_notification_sender,name="consumer_thread").start()
    return HttpResponse("Consumer Thread invoked successfully ")


def decode_dict(data):
    print("type of recived data ",type(data))
    return json.loads(data.decode("utf-8"))


def kafkaconsumer_notification_sender():
    print("\nconsumer invoked ..... consuming the data ......")
    consumer_obj = KafkaConsumer('notification', group_id='notification', bootstrap_servers='localhost:9092')
    print(consumer_obj)

    for data in consumer_obj:
        print("got the data again ")
        with open("/home/mmorya/custom_log_files/notification_consumer_logs.txt","a") as log_file:
            try:
                # print(data.key)
                # print(data.value)
                data = decode_dict(data.value)
                print("data ",data)
                notification_obj = notifications(postid=posts.objects.get(postid=data["postid"]), author_username=data['author_username'],
                                                 friend_username=data["friend_username"], postid_toshow=data["postid_toshow"], operation=data["operation"])

                notification_obj.save()
                log_obj = f"""\n notification sent to user {data['author_username']} at -- {datetime.datetime.now()}"""
            except Exception as e :
                log_obj = f""" \n error occured {e}    -- at --{datetime.datetime.now()}"""
                print("exception occured ")

            log_file.write(log_obj)
            print("\n loop comlpleted once ")
            # data = decode_dict(data.value)
            # print("data ", data)
            # print(type(data))
            # print(data["postid"])
            # post_obj = posts.objects.get(postid=data["postid"])
            # print(post_obj)
            # notification_obj = notifications(postid=post_obj, author_username=data['author_username'],
            #                                  friend_username=data["friend_username"],
            #                                  postid_toshow=data["postid_toshow"], operation=data["operation"])
            #
            # notification_obj.save()


