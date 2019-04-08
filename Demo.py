import tushare as ts
from tools.PrintUtil import *
from indexData.BaseData import BaseData
from Analysis import Analysis
bd=BaseData('sample')
analysis = Analysis()

pr(analysis.change_rate_day(bd.get_qihuo_simaple('I1905.DCE', '20180408', '20190408', 'tie'),
                            [1, 2, 5, 10, 30, 100]), 'tie')



# 所有期货
# pro = ts.pro_api('3fe0a7c39610e6d7a4b56ca611270c8d7411c36ccb3a53c227c68b31')
# df = pro.fut_basic(exchange='DCE', fut_type='1', fields='ts_code,symbol,name,list_date,delist_date')
# values = df.values.tolist()
# for one in values:
#     print(one)