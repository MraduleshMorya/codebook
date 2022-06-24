import threading
import time
from datetime import datetime
import json
from django.core.cache import cache


def cronjob_handler_clear_cache():
    print("\n running cronjob_handler_clear_cache ")
    with open("/home/mmorya/cache_queue.json","a+") as file:
        try:
            file_json_obj = json.load(file)
            if file_json_obj["change_cache"] == True:
                cache.clear(prefix="data")
                print("cache cleared ")
                file_json_obj["change_cache"] = False
                json.dump(file_json_obj,file)
                print("file update secussfully to false after clearing cache ")
                with open("cron_log.txt","a") as f:
                    f.write(f" \n cache cleared at -- {datetime.now()} ")
            else:
                with open("/home/mmorya/cron_log.txt","a") as f:
                    f.write(f" \n cron ran but cache didn't need to update -- {datetime.now()} ")
        except:
            with open("/home/mmorya/cron_log.txt", "a") as f:
                f.write(f" \n cron ran but cache didn't need to update -- {datetime.now()} ")
