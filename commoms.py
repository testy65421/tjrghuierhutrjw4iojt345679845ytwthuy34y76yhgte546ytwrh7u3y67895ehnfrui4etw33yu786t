import os, sys, platform, ctypes, requests, time
from time import sleep



def clear():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Linux':
        os.system('clear')
    else:
        print('\n')*120
    return


def setTitle(str):
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{str}")
    else:
        os.system(f"\033]0;{str}\a")


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.05)


def proxy_scrape():
    startTime = time.time()
    temp = os.getenv("temp")+"\\proxies.txt"
    r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=8500&country=all&ssl=all&anonymity=elite&simplified=true", headers=getheaders())
    with open(temp, "wb") as f:
        f.write(r.content)
    

def proxy():
    temp = os.getenv("temp")+"\\proxies.txt"
    if not os.path.exists(temp):
        with open(temp, "w") as f:
            f.close()
    if os.stat(temp).st_size == 0:
        proxy_scrape()
    proxies = open(temp).read().split('\n')
    proxy = proxies[1]

    with open(temp, 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[1:])
    return proxy


def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers