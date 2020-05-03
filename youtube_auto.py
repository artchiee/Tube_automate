from selenium import webdriver
from selenium.webdriver.opera.options import Options
import time
import requests
import os 
import json 

# required to do if opera is not installed in default loacation 
options = Options()
options.binary_location = "A:\\Opera\\launcher.exe"
options.add_argument("--remote-debugging-port=9222") 

# driver initiliazation 
driver_path =webdriver.Opera(
    executable_path= "C:\\Users\\nouamane\\Downloads\\Programms\\operadriver.exe",
    options = options
)

def play_video():

    # global youtube watch url 
    watch_on_yotube = 'http://www.youtube.com/watch?v='

    api_key = os.environ.get('TUBE_KEY')  # get it from google developer api key
    channel_id = 'UCwO_xoYm2vjhu4kZSxFO5mA'  # your favorite youtuber id channel 

    base_url = 'https://www.googleapis.com/youtube/v3/search?'

    # optional parameters to be passed to the url 
    optional = 'date'

    # make request to the api   
    make_call = str(base_url  + 'key={}&channelId={}&part=snippet,id&order={}').format(api_key, channel_id, optional)
    if make_call:
        call = requests.get(make_call)
        print('response was = ' , call.status_code)
        to_json = call.json()   
    
        # save to local file    
        with open('Youtube_dt.json', 'w') as write:
            json.dump(to_json, write, indent=4, sort_keys=True)
    else:
        Exception()

    # fetch data recieved 
    get_video = to_json['items'][0]
    video_id = get_video['id']['videoId']

    if video_id:
        print('found new video : ', video_id)
        _play_video = (watch_on_yotube + video_id)
        print('url is ', _play_video)

        driver_path.get(_play_video)

    else:
        Exception()

play_video()