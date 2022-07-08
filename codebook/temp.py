import threading
import time
import json

def func1():
    print("running func1 ")
    threading.Thread(target=func2).start()
    print("something ")

def func2():
    time.sleep(3)
    print("after 3 secs ")

with open("/home/mmorya/cache_queue.json", "r+") as file:
    print(file)
    print(file.read())
    file_json_obj = json.load(file)
    file_json_obj["change_cache"] = True
    file.seek(0)
    json.dump(file_json_obj, file, indent=0)
    print("file update secussfully ")
