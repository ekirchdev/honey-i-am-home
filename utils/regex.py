#!/usr/bin/env python
# ! -*- coding: utf-8 -*-

"""
    Utility methods for regex matching.
"""

import re


class Regex(object):
    @staticmethod
    def valid_mac_address(mac_address):
        """
        :param mac_address: The string that represents a mac address.
        :return: True if the passed parameter is a valid mac address. False otherwise.
        """
        return re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower())

    @staticmethod
    def find_ipv4(str_to_search):
        """
        Extracts an ipv4 address from a string line.
        :param str_to_search: The line that has to be searched.
        :return: The ipv4 if found. None otherwise.
        """
        ipv4_match = re.search('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', str_to_search, re.M | re.I)
        if ipv4_match:
            first, last = ipv4_match.span()
            return ipv4_match.string[first:last]
        return None
