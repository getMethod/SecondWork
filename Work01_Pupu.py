import json
import time
import requests

# 在headers中的User-Agent表示为网站的代理

# 创建类的名称
class ppshopping:

    # 初始化方法：获取url，headers
    def __init__(self):
        self.url="http://j1.pupuapi.com/client/search/search_box/products?store_id=deef1dd8-65ee-46bc-9e18-8cf1478a67e9&search_term=%E6%B3%A1%E9%9D%A2&sort=0&search_term_from=20&place_id=41823320-5111-429a-b22b-a3d32e60100e&place_zip=350102&page=1&size=20"
        self.headers = {
            "Host": "j1.pupuapi.com",
            "Connection": "keep-alive",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0(Windows NT 6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/53.0.2785.143Safari/537.36MicroMessenger/7.0.9.501NetType/WIFIMiniProgramEnv/WindowsWindowsWechat",
            "content-type": "application/json",
            "open-id": "oMwzt0Jjg_xWi4tAl4CaKnBYn3vo",
            "pp-os": "0",
            "pp-placeid": "41823320-5111-429a-b22b-a3d32e60100e",
            "pp-version": "2021061900",
            "pp_storeid": "deef1dd8-65ee-46bc-9e18-8cf1478a67e9",
            "sign": "e651251676ea51d48207f4811d5e99ce",
            "timestamp": "1647273803645",
            "Referer": "https//servicewechat.com/wx122ef876a7132eb4/155/page-frame.html"
        }

    # 信息详细处理的方法
    def pp_con(self):
        # 对url地址发送请求,并返回一个JSON格式的数据（方式一）
        # verify：用于关闭无视证书验证
        # response = requests.get(url=self.url,headers=self.headers,verify=False).json()

        # 返回json格式数据的方式二
        response = requests.get(url=self.url,headers=self.headers,verify=False)
        getPupu = json.loads(response.text)

        # 获取当前取到的页面最大的内容量
        # value = getPupu['data']['feed_keywords'][0]['position_value']

        return getPupu


        # 循环遍历商品的名称，并试输出所有的商品名称
        # for i in range(1,value,1):
        #    names.append(getPupu['data']['products'][i]['name'])
        #    print(names[i-1])

        # names.append(getPupu['data']['products'][0]['name'])
        # price.append(getPupu['data']['products'][0]['price'])
        # price_guide.append(getPupu['data']['products'][0]['price_guide'])
        # spec.append(getPupu['data']['products'][0]['spec'])
        # sub_title.append(getPupu['data']['products'][0]['sub_title'])
        # self.getGoods(names[0],price[0],price_guide[0],spec[0],sub_title[0])

    # 获取商品的相关信息的方法（规格，价格，原价/折扣，详细内容）
    def getGoods(self,name,price,price_guide,spec,sub_title):
        theName = '----------------商品：{}----------------'.format(name)
        theSpec = '规格：{}'.format(spec)
        thePrice = '价格：{}'.format(price/100)
        thePrice_Guide = '原价/折扣价：{}/{}'.format(price_guide/100,price/100)
        theTitle = '详细内容：{}'.format(sub_title)
        print(theName,'\n',theSpec,'\n',thePrice,'\n',thePrice_Guide,'\n',theTitle)

    # 获取商品的实时价格变动
    def getPrice(self,price):
        curtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        thePrice = '价格为：{}'.format(price)
        print('当前时间为',curtime,'，',thePrice)
        # 间隔10秒
        time.sleep(10)

    # 内容展示
    def show(self):
        names = []  # 商品名称
        price = []  # 商品实际价格
        price_guide = []  # 商品原价
        spec = []  # 商品规格
        sub_title = []  # 商品详细信息

        res = self.pp_con()
        value = res['data']['feed_keywords'][0]['position_value']

        for i in range(value):
            names.append(res['data']['products'][i]['name'])
            price.append(res['data']['products'][i]['price'])
            price_guide.append(res['data']['products'][i]['price_guide'])
            spec.append(res['data']['products'][i]['spec'])
            sub_title.append(res['data']['products'][i]['sub_title'])
            self.getGoods(names[i],price[i],price_guide[i],spec[i],sub_title[i])
            print('----------------"{}"的价格波动----------------'.format(names[i]))
            num = 0
            while num < 5:
                self.getPrice(price[i]/100)
                num += 1
            print('\n')

    # 运行方法
    def run(self):
        self.show()

# main方法
if __name__ == '__main__':
    ppshopping().run()