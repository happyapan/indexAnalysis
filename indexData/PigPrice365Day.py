import json

from indexData.BaseData import BaseData


class PigData(BaseData):
    def __init__(self, name):
        BaseData.__init__(self, name)

    def get_data(self):
        res_data = self.get_url_date('http://zhujia.zhuwang.cc/index.php?m=zhujia&c=ajax&a=chartData&areaId=&')
        json_date = json.loads(res_data)
        price_data = json_date["pigprice"]
        price_data.reverse()
        self.return_data = {
            "name": "猪肉",
            "week": 7,
            "data": price_data
        }
        return self.return_data
