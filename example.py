#!/usr/bin/env python
# coding: utf-8

from API.dribbble_api import DribbbleAPI


def dribbble_api_example():
    dribble_api = DribbbleAPI('your access token', 'dribbble api base url')

    result = dribble_api.get('dribble source uri', pameters='needed pameters')

    print result