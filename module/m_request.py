# coding=utf-8
import requests

# r = requests.get('https://api.douban.com/v2/book/2129650')
r = requests.post('http://192.168.13.55:60003/frontend/json', json={'actionid': 'Test', 'DeviceId': '123'})
#cookiess = dict(cookies_are='working', cookies_am='working2')
#r = requests.get("http://www.umrdm.top",allow_redirects=True, cookies=cookiess)
print('Status:', r.status_code, r.reason)
for k, v in r.headers.items():
    print("%s:%s" % (k, v))
print('Data:', r.json())
