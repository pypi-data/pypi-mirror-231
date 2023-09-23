# -*- coding:utf-8 -*-

"""
Date: 2023.05.09
author: wugp
contact: 284250692@qq.com
"""

from gusense.common.credit import get_token
from gusense.api import client
from gusense.common import contant


def goco_api():

    token = get_token()
    if token is None or token == '':
        raise Exception(contant.TOKEN_NULL_MSG)
    else:
        api = client.HttpClient(token=token)
        return api
