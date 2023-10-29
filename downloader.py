import requests

url = 'https://images.pexels.com/photos/1821095/pexels-photo-1821095.jpeg'
r = requests.get(url, allow_redirects=True)
open('pexels-photo-1821095.jpeg', 'wb').write(r.content)