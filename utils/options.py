#!/usr/bin/env python
# ! -*- coding: utf-8 -*-

"""
    Command line option handling.
"""

import optparse
import utils.config as config
import utils.constants as constants


class Options(object):

    @staticmethod
    def get_cli_options():
        """
        Returns backend command line options.
        :return: command line options object
        """
        opt_parser = optparse.OptionParser()

        opt_parser.add_option(constants.OPT_PARAM_DEVICE_ADDRESS_SHORT,
                              constants.OPT_PARAM_DEVICE_ADDRESS,
                              help=constants.OPT_PARAM_DEVICE_ADDRESS_HELP,
                              default=config.OPT_PARAM_DEVICE_ADDRESS_DEFAULT,
                              dest=constants.OPT_PARAM_DEVICE_ADDRESS_OUT)

        opt_parser.add_option(constants.OPT_PARAM_MINIMUM_ABSENCE_TIME_SHORT,
                              constants.OPT_PARAM_MINIMUM_ABSENCE_TIME,
                              help=constants.OPT_PARAM_MINIMUM_ABSENCE_TIME_HELP,
                              type="int",
                              default=config.OPT_PARAM_MINIMUM_ABSENCE_TIME_DEFAULT,
                              dest=constants.OPT_PARAM_MINIMUM_ABSENCE_TIME_OUT)

        opt_parser.add_option(constants.OPT_PARAM_SCAN_INTERVAL_SHORT,
                              constants.OPT_PARAM_SCAN_INTERVAL,
                              help=constants.OPT_PARAM_SCAN_INTERVAL_HELP,
                              type="int",
                              default=config.OPT_PARAM_SCAN_INTERVAL_DEFAULT,
                              dest=constants.OPT_PARAM_SCAN_INTERVAL_OUT)

        options, args = opt_parser.parse_args()

        return options
