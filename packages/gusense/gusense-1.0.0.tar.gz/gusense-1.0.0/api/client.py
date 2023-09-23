# -*- coding:utf-8 -*-

"""
Date: 2023.05.09
author: wugp
contact: 284250692@qq.com
"""

import json
import requests
import pandas as pd
from functools import partial
from gusense.common import contant

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
pd.set_option('max_colwidth', 1000)
pd.set_option('display.width', 5000)


class HttpClient:

    def __init__(self, token=''):
        self.url = contant.BASIC_URL
        self.token = token

    def query(self, api_name, fields='', **kwargs):
        token = self.token
        if token == '':
            raise Exception(contant.TOKEN_NULL_MSG)
        json_params = {
            'apiName': api_name,
            'fields': fields,
            'params': kwargs
        }
        headers = {
            'Connection': 'close',
            'token': token
        }
        res = requests.post(self.url, json=json_params, timeout=contant.TIME_OUT, headers=headers)
        if res:
            result = json.loads(res.text)
            code = result['code']
            if code == 200:
                data = result['data']
                return pd.DataFrame(data)
            else:
                raise Exception(code, result['msg'])
        else:
            return pd.DataFrame()

    def __getattr__(self, name):
        return partial(self.query, name)
