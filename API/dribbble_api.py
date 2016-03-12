#!/usr/bin/env python
# coding: utf-8

import requests
import logging


class DribbbleAPI(object):
    def __init__(self, access_token, base_url):
        self.access_token = access_token
        self.base_url = base_url

    def get(self, uri, **kwargs):
        url = "{}/{}".format(self.base_url, uri)

        kwargs["access_token"] = self.access_token

        try:
            resp = requests.Session().get(url, params=kwargs, timeout=50)
            return resp.json()
        except Exception as e:
            logging.warning(e, exc_info=True)
            raise

