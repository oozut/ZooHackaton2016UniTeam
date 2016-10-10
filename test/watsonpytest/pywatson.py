# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 23:05:29 2016

@author: Pablo
"""

import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3



visual_recognition = VisualRecognitionV3('2016-05-20',
                                         api_key='cac00a793868036fc86bd971e032501a2fe21843')


with open(join(dirname(__file__), 'goat.jpg'), 'rb') as image_file:
    print(json.dumps(visual_recognition.classify(images_file=image_file, threshold=0.1,
                                                 classifier_ids=['default']), indent=2))