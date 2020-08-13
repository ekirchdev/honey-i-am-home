#!/usr/bin/env python
# ! -*- coding: utf-8 -*-

"""
    Interface for a notification service.
"""


class NotificationService(object):
    def send_message(self, message_text):
        """
        Send the message via selected technology/api.
        :param message_text: The text of the message.
        """
        raise NotImplementedError
