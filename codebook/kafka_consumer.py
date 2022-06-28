from kafka import KafkaProducer
from kafka import KafkaConsumer
import base64

from codebook_posts.models import notifications


def de_serialize(data):
    ascii_encoded_obj = data.encode("ascii")
    b64_encoded_data = base64.b64decode(ascii_encoded_obj)
    encoded_data = b64_encoded_data.decode("ascii")
    return encoded_data


consumer_obj = KafkaConsumer('notification', group_id='notification', bootstrap_servers='localhost:9092',key_deserializer=de_serialize)

for data in consumer_obj:
    print("\n consuming the data ......")
    print(data.key)
    print(data.value)

    notification_obj = notifications(postid=data["post_obj"], author_username=data['auther_username'],
                                     friend_username=data["friend_username"], postid_toshow=data["postid_toshow"], operation=data["username"])

    notification_obj.save()