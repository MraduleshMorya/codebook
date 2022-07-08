from kafka import KafkaProducer
import base64
import json
import time


def encode_dict(data):
    # ascii_encoded_obj = data.encode("ascii")
    # b64_encoded_data = base64.b64decode(ascii_encoded_obj)
    # encoded_data = b64_encoded_data.decode("ascii")
    # return dict(encoded_data)
    print(type(json.dumps(data).encode('utf-8')))
    print(len(json.dumps(data).encode('utf-8')))
    
    return json.dumps(data).encode('utf-8')

j=0
producer_obj = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=encode_dict)

while True:
    j+=1
    data = {"value":j}
    print(data)
    # producer_obj.send("myTopic", data)
    producer_obj.send("myTopic", value=data, key=bytes(j))
    time.sleep(4)

