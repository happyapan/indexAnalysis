from Analysis import Analysis
from indexData.PigPrice365Day import PigData
from tools.PrintUtil import *
from indexData.BaseData import BaseData
import tools.TimeUtil as tu

bd = BaseData('sample')

analysis = Analysis()

next_month = tu.qi_huo_next_month()
pre_year_date = tu.pre_year_date()
today_date = tu.today()


# 猪肉
pigDate = PigData("猪肉")
pr(analysis.change_rate_day(pigDate.get_data(), [1, 2, 5, 10, 30, 100]), pigDate.name)

# 鸡蛋
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('JD' + next_month + '.DCE', pre_year_date, today_date, '鸡蛋'),
    [1, 2, 5, 10, 30, 100]), '鸡蛋' + tu.qi_huo_next_month())

# 铁矿石
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('I' + next_month + '.DCE', pre_year_date, today_date, '铁矿石'),
    [1, 2, 5, 10, 30, 100]), '铁矿石'+tu.qi_huo_next_month())

# 豆一
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('A' + next_month + '.DCE', pre_year_date, today_date,  '豆一'),
    [1, 2, 5, 10, 30, 100]), '豆一'+tu.qi_huo_next_month())

# 豆二
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('B' + next_month + '.DCE', pre_year_date, today_date,  '豆二'),
    [1, 2, 5, 10, 30, 100]), '豆二'+tu.qi_huo_next_month())

# 豆粕
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('M' + next_month + '.DCE', pre_year_date, today_date, '豆粕'),
    [1, 2, 5, 10, 30, 100]), '豆粕' + tu.qi_huo_next_month())

# 豆油
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('Y' + next_month + '.DCE', pre_year_date, today_date, '豆油'),
    [1, 2, 5, 10, 30, 100]), '豆油' + tu.qi_huo_next_month())

# 棕榈油
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('P' + next_month + '.DCE', pre_year_date, today_date, '棕榈油'),
    [1, 2, 5, 10, 30, 100]), '棕榈油' + tu.qi_huo_next_month())

# 玉米
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('C' + next_month + '.DCE', pre_year_date, today_date,  '玉米'),
    [1, 2, 5, 10, 30, 100]), '玉米'+tu.qi_huo_next_month())

# 玉米淀粉
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('C' + next_month + '.DCE', pre_year_date, today_date,  '玉米淀粉'),
    [1, 2, 5, 10, 30, 100]), '玉米淀粉'+tu.qi_huo_next_month())

# 纤维板
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('FB' + next_month + '.DCE', pre_year_date, today_date,  '纤维板'),
    [1, 2, 5, 10, 30, 100]), '纤维板'+tu.qi_huo_next_month())

# 焦炭
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('J' + next_month + '.DCE', pre_year_date, today_date,  '焦炭'),
    [1, 2, 5, 10, 30, 100]), '焦炭'+tu.qi_huo_next_month())

# 焦煤
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('JM' + next_month + '.DCE', pre_year_date, today_date, '焦煤'),
    [1, 2, 5, 10, 30, 100]), '焦煤' + tu.qi_huo_next_month())

# 塑料
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('L' + next_month + '.DCE', pre_year_date, today_date, '塑料'),
    [1, 2, 5, 10, 30, 100]), '塑料' + tu.qi_huo_next_month())

# PVC聚氯乙烯
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('V' + next_month + '.DCE', pre_year_date, today_date, 'PVC聚氯乙烯'),
    [1, 2, 5, 10, 30, 100]), 'PVC聚氯乙烯' + tu.qi_huo_next_month())

# 聚丙烯
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('PP' + next_month + '.DCE', pre_year_date, today_date, '聚丙烯'),
    [1, 2, 5, 10, 30, 100]), '聚丙烯' + tu.qi_huo_next_month())

# 胶合板
pr(analysis.change_rate_day(
    bd.get_qihuo_simaple('BB' + next_month + '.DCE', pre_year_date, today_date,  '胶合板'),
    [1, 2, 5, 10, 30, 100]), '胶合板'+tu.qi_huo_next_month())


