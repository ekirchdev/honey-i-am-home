#!/usr/bin/env python
# ! -*- coding: utf-8 -*-

"""
    Service that publishes a message to a telegram channel.
"""

import json

import requests
import utils.constants as constants
from notification.notification_service import NotificationService


class TelegramService(NotificationService):
    def __init__(self):
        """
        Initializes a telegram message interface.
        """
        super(TelegramService, self).__init__()
        self._read_config()
        if not self._bot_token or not self._bot_chat_id:
            raise ValueError("Can not instantiate TelegramService because configuration values are invalid!")

    def send_message(self, message_text):
        """
        Send message via telegram api.
        :param message_text: The text of the message.
        """
        url = self._get_url_for_message(message_text)
        response = requests.post(url)
        if response.status_code != 200:
            print(response.content)

    def _get_url_for_message(self, message_text):
        return constants.URL_SEND_TELEGRAM_MESSAGE % (self._bot_token, self._bot_chat_id, message_text)

    def _read_config(self):
        telegram_config = None
        with open('./notification/config.json') as json_file:
            telegram_config = json.load(json_file)
        if not telegram_config:
            raise FileNotFoundError("Can not find file for telegram configuration!")
        if constants.KEY_TELEGRAM_BOT_CHAT_ID not in telegram_config:
            raise KeyError("Required configuration property '%' missing in config file!" %
                           constants.KEY_TELEGRAM_BOT_CHAT_ID)
        if constants.KEY_TELEGRAM_BOT_TOKEN not in telegram_config:
            raise KeyError("Required configuration property '%' missing in config file!" %
                           constants.KEY_TELEGRAM_BOT_TOKEN)
        self._bot_token = telegram_config[constants.KEY_TELEGRAM_BOT_TOKEN]
        self._bot_chat_id = telegram_config[constants.KEY_TELEGRAM_BOT_CHAT_ID]
