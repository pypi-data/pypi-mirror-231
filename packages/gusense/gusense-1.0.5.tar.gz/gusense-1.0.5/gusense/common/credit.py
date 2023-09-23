# -*- coding:utf-8 -*-

"""
Date: 2023.05.09
author: wugp
contact: 284250692@qq.com
"""


import json
import pandas as pd
import os
import requests
from ..common import contant


def auth(app_id, app_secret):
    token = get_token(app_id, app_secret)
    if token is None or token == '':
        params = {
            "appId": app_id,
            "appSecret": app_secret
        }
        res = requests.post(contant.LOGIN_URL, params=params, timeout=contant.TIME_OUT)
        json_res = json.loads(res.text)
        code = json_res['code']
        if code == contant.REQ_SUCCESS_CODE:
            token = json_res['data']
            df = pd.DataFrame([[app_id, app_secret, token]], columns=['app_id', 'app_secret', 'token'])
            user_path = os.path.expanduser('~')
            op = os.path.join(user_path, contant.USER_TOKEN_CN)
            df.to_csv(op, index=False)
        else:
            msg = json_res['msg']
            raise Exception(msg)


def get_token(app_id=None, app_secret=None):
    user_path = os.path.expanduser('~')
    op = os.path.join(user_path, contant.USER_TOKEN_CN)
    if os.path.exists(op):
        df = pd.read_csv(op)
        credit_list = df.loc[0]
        if app_id is not None and app_secret is not None:
            oai = credit_list['app_id']
            oas = credit_list['app_secret']
            if app_id != oai:
                return None
            if app_secret != oas:
                return None
        return credit_list['token']
    else:
        return None
