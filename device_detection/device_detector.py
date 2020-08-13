#!/usr/bin/env python
# ! -*- coding: utf-8 -*-

"""
    Device detection class.
"""

import os
import time
from datetime import datetime

from notification.notification_service import NotificationService
from utils.regex import Regex
import utils.config as config


class DeviceDetector(object):

    def __init__(self,
                 device_address=config.OPT_PARAM_DEVICE_ADDRESS_DEFAULT,
                 minimum_absence_for_notification=config.OPT_PARAM_MINIMUM_ABSENCE_TIME_DEFAULT,
                 device_scan_interval=config.OPT_PARAM_SCAN_INTERVAL_DEFAULT,
                 notification_service=None):
        """
        Initialize device detector.
        :param device_address: The mac address of the device.
        :param minimum_absence_for_notification: Send a message when a device is detected that was last seen x minutes
        ago.
        :param device_scan_interval: Interval in minutes that indicates how often a device search is performed.
        """
        if not device_address:
            raise ValueError("Address of device not set!")
        if not Regex.valid_mac_address(device_address):
            raise ValueError("Please pass a proper mac address format for parameter 'device_address'!")
        if not notification_service or not isinstance(notification_service, NotificationService):
            raise ValueError("Invalid value for 'notification_service'!")
        self._device_address = device_address
        self._last_seen = None
        self._minimum_absence_for_notification = minimum_absence_for_notification
        self._device_scan_interval = device_scan_interval
        self._notification_service = notification_service

    def run(self):
        """
        Endless loop which executes the following steps:
            1. find ipv4 address in network for device
            2. check if the device is available
            3. if available, compare current time with last seen timestamp
            4. if the difference is greater than the minimum absence time, send a notification
        """
        while True:
            try:
                print("\n\n---")
                iphone_available = self._check_availability_of_device()
                if iphone_available:
                    current_time = datetime.now()
                    send_notification = self._check_timestamp_diff(current_time)
                    self._update_last_seen(current_time)
                    if send_notification:
                        self._notify(message="Your boyfriend just came home!")
                print("---\n\n")
                time.sleep(self._device_scan_interval * 60)
            except KeyboardInterrupt:
                print("Exit tool by keyboard interrupt.")
                exit(0)

    @property
    def _ipv4_of_device(self):
        cmd_output = os.popen("arp -a").read()
        lines = cmd_output.split('\n')
        device_ipv4 = None
        for line in lines:
            if self._device_address in line:
                device_ipv4 = Regex.find_ipv4(line)
                print("found ip of device: %s" % device_ipv4)
        return device_ipv4

    def _check_availability_of_device(self):
        ipv4 = self._ipv4_of_device
        if not ipv4:
            return False
        return os.system("ping " + ipv4) == 0

    def _update_last_seen(self, timestamp):
        self._last_seen = timestamp
        print("last seen: %s" % self._last_seen.strftime("%m/%d/%Y, %H:%M:%S"))

    def _check_timestamp_diff(self, timestamp):
        if not self._last_seen:
            return False
        timestamp_diff = (timestamp - self._last_seen).seconds / 60
        print('Difference in minutes: ', timestamp_diff)
        return timestamp_diff > self._minimum_absence_for_notification

    def _notify(self, message):
        if not self._notification_service:
            print("No notification service configured.")
            return
        self._notification_service.send_message(message)
