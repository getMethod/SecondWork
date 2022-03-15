import requests

# 在headers中的User-Agent表示为网站的代理

# 创建类的名称
class ppshopping:

    def __init__(self):
        self.url="http://j1.pupuapi.com/client/search/search_box/products?store_id=deef1dd8-65ee-46bc-9e18-8cf1478a67e9&search_term=%E6%B3%A1%E9%9D%A2&sort=0&search_term_from=20&place_id=41823320-5111-429a-b22b-a3d32e60100e&place_zip=350102&page=1&size=20"
        self.headers = {
            "Host": "j1.pupuapi.com",
            "Connection": "keep-alive",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0(Windows NT 6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/53.0.2785.143Safari/537.36MicroMessenger/7.0.9.501NetType/WIFIMiniProgramEnv/WindowsWindowsWechat",
            "content - type": "application/json",
            "open-id": "oMwzt0Jjg_xWi4tAl4CaKnBYn3vo",
            "pp-os" : "0",
            "pp-placeid": "41823320-5111-429a-b22b-a3d32e60100e",
            "pp-version": "2021061900",
            "pp_storeid": "deef1dd8-65ee-46bc-9e18-8cf1478a67e9",
            "sign": "e651251676ea51d48207f4811d5e99ce",
            "timestamp": "1647273803645",
            "Referer" : "https//servicewechat.com/wx122ef876a7132eb4/155/page-frame.html"
        }
    def pp_con(self):
        # 对url地址发送请求,并返回一个JSON格式的数据
        response =requests.get(url=self.url,headers=self.headers,verify=False).json()
        print(response)

    def run(self):
        self.pp_con()


if __name__ == '__main__':
    ppshopping().run()