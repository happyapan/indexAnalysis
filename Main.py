from Analysis import Analysis
from indexData.PigPrice365Day import PigData
from tools.PrintUtil import *
from indexData.BaseData import BaseData
import tools.TimeUtil as tu

bd = BaseData('sample')

analysis = Analysis()
pigDate = PigData("猪肉")
pr(analysis.change_rate_day(pigDate.get_data(), [1, 2, 5, 10, 30, 100]), pigDate.name)

# 铁矿石
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('I' + tu.qi_huo_next_month() + '.DCE', tu.pre_year_date(), tu.today(), '铁矿石'),
    [1, 2, 5, 10, 30, 100]), '铁矿石')

#
# ['A1905.DCE', 'A1905', '豆一1905', '20171115', '20190515']
# ['B1905.DCE', 'B1905', '豆二1905', '20180516', '20190515']
# ['BB1905.DCE', 'BB1905', '胶合板1905', '20180516', '20190515']
# ['C1905.DCE', 'C1905', '玉米1905', '20180516', '20190515']
# ['CS1905.DCE', 'CS1905', '玉米淀粉1905', '20180516', '20190515']
# ['FB1905.DCE', 'FB1905', '纤维板1905', '20180516', '20190515']
# ['I1905.DCE', 'I1905', '铁矿石1905', '20180516', '20190515']
# ['J1905.DCE', 'J1905', '焦炭1905', '20180516', '20190515']
# ['JD1905.DCE', 'JD1905', '鸡蛋1905', '20180529', '20190528']
# ['JM1905.DCE', 'JM1905', '焦煤1905', '20180516', '20190515']
# ['L1905.DCE', 'L1905', '塑料1905', '20180516', '20190515']
# ['M1905.DCE', 'M1905', '豆粕1905', '20180516', '20190515']
# ['P1905.DCE', 'P1905', '棕榈油1905', '20180516', '20190515']
# ['PP1905.DCE', 'PP1905', '聚丙烯1905', '20180516', '20190515']
# ['V1905.DCE', 'V1905', 'PVC1905', '20180516', '20190515']
# ['Y1905.DCE', 'Y1905', '豆油1905', '20180516', '20190515']
