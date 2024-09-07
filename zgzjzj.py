import base64
import json

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

USERNAME = '14043119700206362X'
PASSWORD = 'zjtx06362X'


def aes_ecb_encode(text):
    key = b'%&^#hdyel1234f86'
    aes = AES.new(key, AES.MODE_ECB)
    padded_obj_bytes = pad(text.encode(), AES.block_size)
    encrypted_obj = aes.encrypt(padded_obj_bytes)
    return base64.b64encode(encrypted_obj).decode('utf-8')


def login(username, password):
    login_data = '{\"username\":\"' + username + '\",\"password\":\"' + password + '\"}'
    login_mes = aes_ecb_encode(login_data)
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    }
    url = "https://zj-api.zgzjzj.com/api/user/user/login"
    data = {
        "data": login_mes
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)

    if '访问正常' in response.text:
        print('登录成功')
    else:
        print('登录失败')


if __name__ == '__main__':
    login(USERNAME, PASSWORD)
