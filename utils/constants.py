#!/usr/bin/env python
# ! -*- coding: utf-8 -*-

"""
    Central file for defining constants.
"""

# command line options
OPT_PARAM_DEVICE_ADDRESS = "--device"
OPT_PARAM_DEVICE_ADDRESS_SHORT = "-d"
OPT_PARAM_DEVICE_ADDRESS_OUT = "device"
OPT_PARAM_DEVICE_ADDRESS_HELP = "The mac address of the device."

OPT_PARAM_MINIMUM_ABSENCE_TIME = "--absence"
OPT_PARAM_MINIMUM_ABSENCE_TIME_SHORT = "-a"
OPT_PARAM_MINIMUM_ABSENCE_TIME_OUT = "absence"
OPT_PARAM_MINIMUM_ABSENCE_TIME_HELP = "Send a message when a device is detected that was last seen x minutes ago."

OPT_PARAM_SCAN_INTERVAL = "--scan-interval"
OPT_PARAM_SCAN_INTERVAL_SHORT = "-s"
OPT_PARAM_SCAN_INTERVAL_OUT = "scan_interval"
OPT_PARAM_SCAN_INTERVAL_DEFAULT = 1
OPT_PARAM_SCAN_INTERVAL_HELP = "Interval in minutes that indicates how often a device search is performed."

# telegram config
KEY_TELEGRAM_BOT_TOKEN = "bot_token"
KEY_TELEGRAM_BOT_CHAT_ID = "bot_chat_id"

# telegram messaging
URL_SEND_TELEGRAM_MESSAGE = "https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s"
