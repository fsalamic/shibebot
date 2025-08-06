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

# To get other animals, just change "lynxes" string to one of the following:
# caracals, cheetahs, coyotes, foxes, huskies, servals, wolves

def get_random_lynx_url():
    # Try up to 5 times to get a valid image, randomizing every attempt
    for _ in range(5):
        url = f"https://hourly.photo/u/lynxes/p/{random_date('1/2024', datetime.today().strftime('%m/%Y'), random.random())}/0{random.randint(1, 30)}"
        try:
            response = requests.get(url, timeout=7)
            if not response.ok:
                continue
            soup = BeautifulSoup(response.text, 'html.parser')
            imgs = soup.find_all('img')
            if imgs:
                random_img = random.choice(imgs)
                img_url = random_img.get('src')
                if img_url and img_url.startswith("/"):
                    img_url = "https://hourly.photo" + img_url
                return img_url
        except Exception:
            continue
    return None

if __name__ == "__main__":
    url = get_random_lynx_url()
    if url:
        print(url)
    else:
        print("No lynx image found.")