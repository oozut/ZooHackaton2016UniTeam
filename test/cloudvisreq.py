# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 18:07:43 2016

@author: Pablo
"""

from base64 import b64encode
from os import makedirs
from os.path import join, basename,exists
from sys import argv
import json
import requests

def make_image_data_list(image_filenames):
    """
    image_filenames is a list of filename strings
    Returns a list of dicts formatted as the Vision API
        needs them to be
    """
    img_requests = []
    print image_filenames
    for imgname in image_filenames:
        print imgname
        with open(imgname, 'rb') as f:
            ctxt = b64encode(f.read()).decode()
            img_requests.append({
                    'image': {'content': ctxt},
                    'features': [{
                        'type': 'TEXT_DETECTION',
                        'maxResults': 1
                    }]
            })
    return img_requests

def make_image_data(image_filenames):
    """Returns the image data lists as bytes"""
    imgdict = make_image_data_list(image_filenames)
    return json.dumps({"requests": imgdict }).encode()

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
RESULTS_DIR = 'jsons'

if not exists(RESULTS_DIR):
     makedirs(RESULTS_DIR)



#image_filenames = ['test.jpg']

image_filenames = ['sharkmenu.jpg']
api_key  = 'AIzaSyBhfq0EH4Vo3FqrxsiVyjYFTDgFKcOEOBg'


response = requests.post(ENDPOINT_URL,
                             data=make_image_data(image_filenames),
                             params={'key': api_key},
                             headers={'Content-Type': 'application/json'})

if response.status_code != 200 or response.json().get('error'):
            print(response.text)

else:
    for idx, resp in enumerate(response.json()['responses']):
        # save to JSON file
        imgname = image_filenames[idx]
        jpath = join(RESULTS_DIR, basename(imgname) + '.json')
        with open(jpath, 'w') as f:
            datatxt = json.dumps(resp, indent=2)
            print("Wrote", len(datatxt), "bytes to", jpath)
            f.write(datatxt)
        my_text = resp['textAnnotations'][0]['description']
        # print the plaintext to screen for convenience
#        print("---------------------------------------------")
#        t = resp['textAnnotations'][0]
#        print("    Bounding Polygon:")
#        print(t['boundingPoly'])
#        print("    Text:")
#        print(t['description'])
        print my_text
        


        
