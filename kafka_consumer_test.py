from kafka import KafkaConsumer
import json
import base64

def de_serialize(data):
      # ascii_encoded_obj = data.encode("ascii")
     # b64_encoded_data = base64.b64decode(ascii_encoded_obj)
     # encoded_data = b64_encoded_data.decode("ascii")
     # return dict(encoded_data)
     return json.loads(data.decode('utf-8'))



consumer_obj = KafkaConsumer('notification', group_id='notification', bootstrap_servers='localhost:9092')
print(consumer_obj)

for data in consumer_obj:
    print("\n consuming the data ......")
    print(data.key)
    print(data.value)