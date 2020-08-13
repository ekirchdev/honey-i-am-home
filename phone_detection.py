#!/usr/bin/env python
# ! -*- coding: utf-8 -*-

"""
    Main entry point.
    Starts the device detection with notification service.
"""

from notification.telegram_service import TelegramService
from utils.options import Options
from device_detection.device_detector import DeviceDetector

if __name__ == "__main__":
    options = Options.get_cli_options()

    telegram_service = TelegramService()

    detection = DeviceDetector(device_address=options.device,
                               minimum_absence_for_notification=options.absence,
                               device_scan_interval=options.scan_interval,
                               notification_service=telegram_service)
    detection.run()
