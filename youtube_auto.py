from selenium.webdriver import Chrome
import time
import requests
import os 
import json 

# initilize your path to chrome driver

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
        res = print('response was = ' , call.status_code)
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
        _paly_video = (watch_on_yotube + video_id)
        driver =
    else:
        Exception()

play_video()