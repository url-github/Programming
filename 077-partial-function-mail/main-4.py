import requests
import os
from functools import partial

def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)

    file_path = os.path.join(dir, file)
    with open(file_path, "wb") as f:
        f.write(r.content)

DEFAULT_DIR = '/Users/p/Documents/Scripts/Programming/temp'
DEFAULT_MSG = "Please wait: {}"

# Tworzenie funkcji partial
save_url_to_dir = partial(save_url_file, dir=DEFAULT_DIR, msg=DEFAULT_MSG)

url = 'http://mobilo24.eu/spis'
file = 'spis.html'
save_url_to_dir(url=url, file=file)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
file = 'logo.png'
save_url_to_dir(url=url, file=file)