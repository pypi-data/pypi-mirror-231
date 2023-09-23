
import requests
URL = 'https://raw.githubusercontent.com/imvickykumar999/Flask-XAMPP-Onion-Host/main/Tutorial%20Files/VicksTor.py'

r = requests.get(URL, allow_redirects=True)
open('HostTor.py', 'wb').write(r.content)
