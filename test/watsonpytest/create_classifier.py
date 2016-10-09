# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 23:18:24 2016

@author: Pablo
"""
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20',
                                         api_key='cac00a793868036fc86bd971e032501a2fe21843')


with open(join(dirname(__file__), 'coral shell souvenir _ Google Search.zip'), 'rb') as corals, \
    open(join(dirname(__file__), 'ivory figurines _ Google Search.zip'), 'rb') as ivory, \
    open(join(dirname(__file__), 'souvenirs.zip'), 'rb') as souvenir, \
      open(join(dirname(__file__), 'crocodile leather products _ Google Search.zip'), 'rb') as crocodile:
   print(json.dumps(visual_recognition.create_classifier('DodgySouvenir', trucks_positive_examples=[corals,ivory,crocodile], negative_examples=souvenir), indent=2))