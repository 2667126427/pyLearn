import requests
import config

token_url = 'https://api.weixin.qq.com/cgi-bin/token?' \
            'grant_type=client_credential&appid={0}&secret={1}'
msg_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?' \
          'access_token={}'

if __name__ == '__main__':
    url = token_url.format(config.app_id, config.app_secret)
    token = requests.get(url).json()['access_token']

    post_data = {
        'touser': config.my_id, 'template_id': config.template_id,
        'topcolor': '#FF0000',
        'data': {
            'city': {'value': 'Wuhan',
                     'color': '#173177'
                     },
            'msg': {
                'value': 'Nothing',
                'color': '#173177'
            }
        }
    }

    req = requests.post(url=msg_url.format(token), json=post_data)
    print(req.text)
