#!/usr/bin/env python
# ! -*- coding: utf-8 -*-

from utils.options import Options
from device_detection.device_detector import DeviceDetector

if __name__ == "__main__":
    options = Options.get_cli_options()

    detection = DeviceDetector(device_address=options.device,
                               minimum_absence_for_notification=options.absence,
                               device_scan_interval=options.scan_interval)
    detection.run()
