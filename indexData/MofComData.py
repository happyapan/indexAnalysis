import json

from indexData.BaseData import BaseData


class MofComData(BaseData):
    def __init__(self, name):
        self.product_name_list = {
            '281': '黄金',
            '313': '铜',
            '315': '铅 1',
            '316': '锌 0',
            '319': '锡 2',
            '314': '铝'
        }
        BaseData.__init__(self, name)

    def get_product_name(self, product_id):
        return self.product_name_list[product_id]

    def get_data(self, product_id):
        data_url = 'http://price.mofcom.gov.cn/datamofcom/front/price/pricequotation/priceQueryList?seqno=' + product_id + '&startTime=&endTime=&pageNumber=1&pageSize=500'
        res_data = self.post_url_data(data_url, {})
        json_date = json.loads(res_data)
        # print(json_date)
        price_data = json_date["rows"]
        return_data = []
        print(price_data[0]['prod_name'])
        for one in price_data:
            return_data.append(float(one['price']))

        self.return_data = {
            "name": self.product_name_list[product_id],
            "week": 7,
            "data": return_data
        }
        return self.return_data
