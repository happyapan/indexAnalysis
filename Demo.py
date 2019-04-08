import tushare as ts

# token:
# 3fe0a7c39610e6d7a4b56ca611270c8d7411c36ccb3a53c227c68b31
# print(ts.get_hist_data('600770'))

pro = ts.pro_api('3fe0a7c39610e6d7a4b56ca611270c8d7411c36ccb3a53c227c68b31')
df = pro.fut_basic(exchange='DCE', fut_type='1', fields='ts_code,symbol,name,list_date,delist_date')
# df.to_csv("d:\\08Python\\indexAnalysis\\ZFile\\sqihuo.csv", 'wb+')
values = df.values.tolist()
for one in values:
    print(one)
