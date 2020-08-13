#!/usr/bin/env python
# ! -*- coding: utf-8 -*-

"""
    Short script to find out your chat id!
"""

import optparse
import requests
import json

opt_parser = optparse.OptionParser()

opt_parser.add_option('-t',
                      '--token',
                      help='Your telegram bot token',
                      default=None,
                      dest='token')

opt_parser.add_option('-g',
                      '--group',
                      help='Your telegram group name',
                      default=None,
                      dest='group')

options, args = opt_parser.parse_args()

if not options.token:
    raise Exception("Please run this script with option -t / --token and pass your token!")
if not options.group:
    raise Exception("Please run this script with option -g / --group and pass your group name!")

url = "https://api.telegram.org/bot%s/getUpdates" % options.token

response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.content)
    for entry in data['result']:
        if 'message' in entry and 'chat' in entry['message']:
            group_name = entry['message']['chat']['title']
            if group_name == options.group:
                print("Your chat id: ", entry['message']['chat']['id'])
                exit(0)

print("Did not find a chat id. Did you perform the steps from README.md properly?")
