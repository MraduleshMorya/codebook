import threading
import time
import datetime

def cronjob_handler():
    with open("cron_log.txt","a") as f:
        f.write("\n cron runs successfully ")
    print("entered cron handler ")
    t = datetime.date
    with open("cron_log.txt","a") as f:
        f.write(f" \n cron runs successfully at -- {t} ")
