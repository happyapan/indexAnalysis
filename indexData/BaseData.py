import urllib.request

import tushare as ts


class BaseData:
    def __init__(self, name):
        self.pro = ts.pro_api('3fe0a7c39610e6d7a4b56ca611270c8d7411c36ccb3a53c227c68b31')
        self.name = name
        self.next_month = '1905'
        self.return_data = {
            "name": "",
            "week": 0,
            "data": []
        }

    def get_data(self):
        pass

    def next_month(self):
        return self.next_month

    def name(self):
        return self.name

    def get_url_data(self, url):
        return urllib.request.urlopen(url).read().decode('gb2312')

    def get_ts_qihuo(self, code, st, ed):
        # fields = 'ts_code,trade_date,pre_close,pre_settle,open,high,low,close,settle,vol'

        print("Get %s From [%s] To [%s]" % (code, st, ed))
        pro = ts.pro_api('3fe0a7c39610e6d7a4b56ca611270c8d7411c36ccb3a53c227c68b31')
        result = pro.fut_daily(ts_code=code, start_date=st, end_date=ed, fields='close')
        return_list = []
        for one in result.values.tolist():
            return_list.append(one[0])
        return return_list

    def get_qihuo_simaple(self, code, st, ed, name):
        # fields = 'ts_code,trade_date,pre_close,pre_settle,open,high,low,close,settle,vol'

        print("Get %s From [%s] To [%s]" % (code, st, ed))
        pro = ts.pro_api('3fe0a7c39610e6d7a4b56ca611270c8d7411c36ccb3a53c227c68b31')
        result = pro.fut_daily(ts_code=code, start_date=st, end_date=ed, fields='close')
        return_list = []
        for one in result.values.tolist():
            return_list.append(one[0])

        simple_return_data = {
            "name": name,
            "week": 7,
            "data": return_list
        }
        return simple_return_data
