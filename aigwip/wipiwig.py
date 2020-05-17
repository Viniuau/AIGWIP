import speedtest
from os import system
from datetime import datetime
from time import sleep
import json

def main():
    def getServers():
        s.get_servers(servers)
        s.get_best_server()

    def getConnectionSpeeds():
        s.download(threads=threads)
        s.upload(threads=threads)

    def getShareResults():
        share = s.results.share()
        share = share[:-4]
        return share

    print("Looking for the best connection server...")

    try:
        getServers()
    except:
        print('The search for servers went into an error.')
        input()
        exit()

    print('Best connection server found successfully.\n')
    sleep(1)

    system('cls')
    print("Obtaining connection speed...")
    print("Estimate time: 20 seconds")

    try:
        getConnectionSpeeds()
    except:
        print('The program went into an error while trying to get connection speed.')
        input()
        exit()

    print('Connection speed was successfully obtained.\n')
    sleep(1)
    system('cls')

    print('Getting results from API...')
    share = getShareResults()

    system('cls')

    results = s.results.dict()

    download = results["download"] / 1000000
    upload = results["upload"] / 1000000
    ping = results["ping"]

    server = results["server"]
    server_url = json.dumps(server["sponsor"])
    server_name = json.dumps(server["name"])
    server_country = json.dumps(server["country"])

    client = results["client"]
    client_ip = json.dumps(client["ip"])
    client_isp = json.dumps(client["isp"])
    client_country = json.dumps(client["country"])

    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_filename = now.strftime("%d%m%y_%H%M%S")

    log = ("Log Timestamp: {}\n".format(dt_string))
    log += ("""Download: {:.2f} Megabits/second
Upload: {:.2f} Megabits/second
Latency: {:.1f}ms
    
Server: {} at {}, {}
    
User IP: {}
User ISP: {} 
User Country: {}

The validity of this test can be confirmed at: {}
    """.format(download, upload, ping, server_url, server_name, server_country, client_ip, client_isp, client_country, share))
    print(log)
    file = open('LOG_'+ dt_filename + '.txt', 'w+')
    file.write(log)
    file.close()
    if (repeat_forever == 'y' or repeat_forever == 'Y'):
        sleep(3)
        main()
    check_again = str(input('Do you want to check your speed one more time? (Y/N) '))
    check_again.lower()
    if (check_again == 'y'):
        main()
    else:
        exit()

if __name__ == "__main__":
    servers = []
    threads = None
    s = speedtest.Speedtest()

    print("""------
WIPWIG? (What I'm Paying Is What I'm Getting?)
Made by: 4pocalipse
Available at: https://github.com/theapocalipse/WIPIWIG
Written in: Python 3.7
------
1 - Start Scan
2 - About
3 - Quit
------""")

    while True:
        menu = str(input('What do you want to do? '))
        if (menu == '1'):
            repeat_forever = str(input('Do you want to repeat the connection speed scan endlessly? (Y/N) '))
            repeat_forever.lower()
            main()
        elif (menu == '2'):
            print("""WIPIWIG?
WIPIWIG is a simple software that test your connection speed
and create logs to report to your ISP if the quality of your
connection match the plan that you are paying for.

PS: Typically, upload speed is half of what is offered in the plan (Example: Plan: 60 Megabits/s -> Upload: 30 Megabits/s)
(Some internet plans are focused in download or upload, pay attention to it).
            """)
        elif (menu == '3'):
            exit()
        else:
            print('Option not found.\n')
