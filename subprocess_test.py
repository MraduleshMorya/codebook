import subprocess
import time
import sys

command_list_to_start_servers = [
                                 "cd && sudo kafka/apache-zookeeper-3.7.1-bin/bin/zkServer.sh start",
                                 "cd && cd kafka/kafka_2.13-3.0.0 && sudo bin/kafka-server-start.sh config/server.properties",
                                 "cd && sudo systemctl start redis-server.service",
                                 "cd && sudo systemctl start mongod"
                                 ]
command_list_to_stop_servers = [
                                "cd && cd  kafka/kafka_2.13-3.0.0 && sudo bin/kafka-server-stop.sh config/server.properties",
                                "cd && sudo kafka/apache-zookeeper-3.7.1-bin/bin/zkServer.sh stop",
                                "cd && sudo systemctl stop redis-server.service",
                                "cd && sudo systemctl stop mongod",
                                ]


def stop_server(server_list):
    # function to stop running servers
    with open("/home/mmorya/custom_log_files/stopserver_logs.txt", "w") as log_file:
        for cmd in server_list:
            # subprocess.run waits for the standard output or the stand error massage and then executes the second line
            temp = subprocess.run(f"{cmd}", capture_output=True, shell=True)
            print(cmd)
            print("out - ", temp.stdout)
            print("err --", temp.stderr)
            log_file.write(str(temp.stdout))
            log_file.write(str(temp.stderr))


def stop_localhost():
    # function to stop localhost
    with open("/home/mmorya/custom_log_files/stopserver_logs.txt", "a") as log_file:
        find_pid = subprocess.run("cd && sudo netstat -ntulp | grep 8000 | awk '{print $7}'", shell=True, text=True,
                       capture_output=True)
        print(find_pid)
        if len(find_pid.stdout) <= 0:
            print("!!!!!! Localhost:8000 is not running ")
            return False

        pid = (find_pid.stdout).split("/")
        kill = subprocess.run(f"cd && sudo kill {pid[0]}", shell=True, text=True, capture_output=True)
        print(kill)
        log_file.write(f"{kill}")
        return True


def start_localhost():
    # function to start localhost at 8000 port
    with open("/home/mmorya/custom_log_files/runserver_logs.txt", "a") as log_file:
        if stop_localhost() == True:
            print(f"!\n !!!! localhost was already running ")
            time.sleep(1)
            print("Stopped Localhost:8000 ,\n restarting it .....")
        temp = subprocess.Popen(" cd && cd django_project/codebook && python3 manage.py runserver localhost:8000",stdout=log_file,stderr=log_file,shell=True,stdin=True)
        time.sleep(7)
        log_file.write(f"local host log -- {temp}")
        #threading.Thread(target=kafkaconsumer_notification_sender,name="notification",daemon=True).start()
        print("local host started successfully :----")
        return True


def start_localhost_at_IP():
    # function to start localhost at 192.168.50.67:8000
    with open("/home/mmorya/custom_log_files/runserver_logs.txt", "a") as log_file:
        if stop_localhost() == True:
            print(f"!\n !!!! localhost was already running ")
            time.sleep(1)
            print("Stopped Localhost:8000 ,\n restarting it .....")
        temp = subprocess.Popen(" cd && cd django_project/codebook && python3 manage.py runserver 192.168.50.67:8000",stdout=log_file,stderr=log_file,shell=True,stdin=True)
        time.sleep(7)
        log_file.write(f"local host log -- {temp}")
        return True


def start_server():
    # function to start all the servers at local machine
    command_list_to_start_servers = ["cd && sudo kafka/apache-zookeeper-3.7.1-bin/bin/zkServer.sh start",
                                     "cd && cd  kafka/kafka_2.13-3.0.0 && sudo bin/kafka-server-start.sh config/server.properties",
                                     "cd && sudo systemctl start redis-server.service",
                                     "cd && sudo systemctl start mongod"]
    server_list = ["Zookeeper", "Kafka", "Redis", "Mongodb"]
    i = 0
    for cmd in command_list_to_start_servers:
        try:
            # subprocess.Popen runs commands in background and don't wait for the response and the control gets passed to the next line
            print(f"\n \n Starting .............{server_list[i]}\n")
            temp = subprocess.Popen(f"{cmd}", stdout=log_file,stderr=log_file, shell=True)
            time.sleep(5)
            i += 1

            if temp.stderr != None:
                print(f"\n !!!!! Looks like an error occurred while starting .......{server_list[i - 1]}")
                print(temp.stderr)
                log_file.write(f"got an error --- {temp.stderr}")
                stop_server(command_list_to_stop_servers[0:i])
                return False
            else:
                print(f"\n {server_list[i - 1]}........started successfully")
        except Exception as e:
            print(e)
            print(f"!!!!! Error Occurred ...................{e}\n")
            break
    return True


if __name__=="__main__":
    with open("/home/mmorya/custom_log_files/runserver_logs.txt","w") as log_file:
        while True:
            print(f""" 
            0 To exit and stop all 
            1 To start Zookeeper,Kafka,Redis,Mongodb
            2 To start localhost
            3 To start localhost at IP
            4 To stop localhost
            5 To stop Zookeeper,Kafka,Redis,Mongodb
            """)
            choice = int(input("enter your choice:---  "))
            if choice not in [0,1,2,3,4,5]:
                continue
            if choice == 0:
                stop_server(command_list_to_stop_servers)
                stop_localhost()
                print(" Bye Bye .........")
                sys.exit()
            elif choice == 1:
                start_server()
                continue
            elif choice == 2:
                start_localhost()
                continue
            elif choice == 3:
                start_localhost_at_IP()
                continue
            elif choice == 4:
                stop_localhost()
                continue
            elif choice == 5:
                stop_server(command_list_to_stop_servers)
                continue