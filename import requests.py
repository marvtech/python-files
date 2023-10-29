import requests

url = 'https://cdn.wallpapersafari.com/18/78/LjlgD4.jpg'
r = requests.get(url, allow_redirects=True)
open('LjlgD4.jpg', 'wb').write(r.content)