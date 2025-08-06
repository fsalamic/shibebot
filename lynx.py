# Copyright Xunillen2
# https://github.com/xunillen2

import time
import random
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime("%y%m", time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%Y', prop)


# This parses hourly.photo site as it does not have a public api... buhu
# Not the best way and I didn't get premission of owner to this...
# To get other animals, just change "lynxes" string to one of the following:
#       caracals
#       cheetahs
#       coyotes
#       foxes
#       huskies
#       servals
#       wolves


def get_random_lynx_url():
    # Random monthly page and image index
    url = f"https://hourly.photo/u/lynxes/p/{random_date('1/2024', datetime.today().strftime('%m/%Y'), random.random())}/0{random.randint(1, 5)}"
    imgs = []
    # Try up to 5 times to get a valid image
    for _ in range(5):
        Httpresponse = requests.get(url)
        supica = BeautifulSoup(Httpresponse.text, 'html.parser')
        imgs = supica.find_all('img')
        if imgs:
            break
    if not imgs:
        return None
    random_img = random.choice(imgs)
    img_url = random_img.get('src')
    # Ensure the URL is absolute
    if img_url and img_url.startswith("/"):
        img_url = "https://hourly.photo" + img_url
    return img_url
