from kafka import KafkaProducer
from kafka import KafkaConsumer
import base64
from codebook_posts.models import notifications,posts
import json
import datetime


def decode_dict(data):
    return data.decode("utf-8")


def kafkaconsumer_notification_sender():
    print("\nconsumer invoked ..... consuming the data ......")
    consumer_obj = KafkaConsumer('notification', group_id='notification', bootstrap_servers='localhost:9092',key_deserializer=decode_dict, enable_auto_commit=True)

    for data in consumer_obj:
        with open("/home/mmorya/custom_log_files/notification_consumer_logs.txt","a") as log_file:
            try:
                print(data.key)
                print(data.value)
                notification_obj = notifications(postid=posts.objects.get(postid=data["post_obj"]), author_username=data['auther_username'],
                                                 friend_username=data["friend_username"], postid_toshow=data["postid_toshow"], operation=data["username"])

                notification_obj.save()
                log_obj = f"""\n notification sent to user {data['auther_username']} at -- {datetime.datetime.now()}"""
            except Exception as e :
                log_obj = f""" \n error occured {e}    -- at --{datetime.datetime.now()}"""

            log_file.write(log_obj)
            print("\n loop comlpleted once ")


