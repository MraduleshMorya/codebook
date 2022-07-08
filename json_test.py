import json
with open("/home/mmorya/cache_queue.json", "w") as file:
    data = {
        "cache_changed":False
    }
    print(type(json.dumps(data)))
    file.write(json.dumps(data))


# with open("/home/mmorya/cache_queue.json", "r+") as file:
#     print("file ")
#     print(file)
#     #print(file.read())
#     temp = file.read()
#     print(type(temp))
#     file_json_obj = json.loads(temp)
#     print(type(file_json_obj))
#     file_json_obj["cache_changed"] = True
#     file.seek(0)
#     json.dump(file_json_obj, file, indent=0)
#     print("file update secussfully ")

import subprocess
import time
import threading
#
# log_file = open("/home/mmorya/custom_log_files/notification_consumer_logs.txt", "a")
# for i in range(1,10):
#     log_file.write(f"{i}--th log \n")
#     time.sleep(2)
#     print(i)
# log_file.close()


# with open("/home/mmorya/custom_log_files/stopserver_logs.txt", "w") as log_file:
#     p = subprocess.run("cd && sudo netstat -ntulp | grep 8000 | awk '{print $7}'",shell=True,text=True,capture_output=True)
#     print(p)
#     pid = (p.stdout).split("/")
#     print(pid[0])
#     kill = subprocess.run(f"cd && sudo kill {pid[0]}",shell=True,text=True,capture_output=True)
#     print(kill)
#     log_file.write(f"{kill}")
#     if len(kill.stdout)>0:
#         print("got an stdout ")
#     if len(kill.stderr)>0:
#         print("got an error ")


# p1 = subprocess.run(" cd && pwd",stdout=True,stderr=True,shell=True)
# p1 = subprocess.Popen(" cd && cd django_project/codebook && python3 manage.py runserver localhost:8000",stdout=True,stderr=True,shell=True,stdin=True)
# time.sleep(10)
# print("dsgfsdfgsdfg")
# print(p1.stdout)
# print(p1.stderr)

# with open("/home/mmorya/custom_log_files/stopserver_logs.txt", "a") as log_file:
#     log_file.write("dfghdasgfhjhjgdashshbcjdgasvyvfjctqgewaDSyfugasdhjgfhXZJbcghcdzjsgfcbnXVZcxvcfdgsvXZcgZxhj")