# -*- coding:utf-8 -*-

"""
Date: 2023.05.09
author: wugp
contact: 284250692@qq.com
"""

from ..api import client
from ..common import contant
from ..common.credit import get_token


def goco_api():

    token = get_token()
    if token is None or token == '':
        raise Exception(contant.TOKEN_NULL_MSG)
    else:
        api = client.HttpClient(token=token)
        return api
