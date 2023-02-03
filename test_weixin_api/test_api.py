import requests


class TestToken():
    def setup(self):
        """
        获取TOKEN
        :return:
        """
        #定义凭证
        corpid= 'wwf39d4a17555d0bb6'
        corpsecret ='5timW2hZA_80OcpSUkrl4nYyL5FTiP7pwmFzy502UNk'
        url=('https://qyapi.weixin.qq.com/cgi-bin/gettoken')
        param={'corpid':corpid,'corpsecret':corpsecret}
        r=requests.get(url=url,params=param)
        print(r.json())
        self.token=r.json()['access_token']
