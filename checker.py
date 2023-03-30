import requests
import threading

def check_proxy(proxy):
    try:
        response = requests.get('https://www.google.com/', proxies={'http': proxy, 'https': proxy}, timeout=10)
        if response.status_code == 200:
            print(f"Proxy {proxy} is working")
            with open('checked.txt', 'a') as f:
                f.write(proxy + '\n')
        else:
            print(f"Proxy {proxy} is not working")
    except:
        print(f"Proxy {proxy} is not working")

# Read proxies from a file
with open('proxy.txt', 'r') as f:
    proxy_list = f.read().splitlines()

# Create threads to check proxies
threads = []
for proxy in proxy_list:
    thread = threading.Thread(target=check_proxy, args=[proxy])
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
