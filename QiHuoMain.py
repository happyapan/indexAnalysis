from Analysis import Analysis
from indexData.MofComData import MofComData
from indexData.PigPrice365Day import PigData
from tools.PrintUtil import *
from indexData.BaseData import BaseData
import tools.TimeUtil as tu
import IndexConstants
bd = BaseData('sample')
mofComData = MofComData('MofComData')
analysis = Analysis()

next_month = tu.qi_huo_next_month()
pre_year_date = tu.pre_year_date()
today_date = tu.today()

cycle_index = [1, 2, 5, 10, 30, 100, 200]

# 猪肉
pigDate = PigData("猪肉")
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(pigDate.get_data(), cycle_index),
       pigDate.name)

# 鸡蛋
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('JD' + next_month + '.DCE', pre_year_date, today_date, '鸡蛋'),
    cycle_index), '鸡蛋' + tu.qi_huo_next_month())

# 铁矿石
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('I' + next_month + '.DCE', pre_year_date, today_date, '铁矿石'),
    cycle_index), '铁矿石' + tu.qi_huo_next_month())

# 乙二醇
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('EG1906.DCE', pre_year_date, today_date, '乙二醇'),
    cycle_index), '乙二醇1906')

# 豆一
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('A' + next_month + '.DCE', pre_year_date, today_date, '豆一'),
    cycle_index), '豆一' + tu.qi_huo_next_month())

# 豆二
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('B' + next_month + '.DCE', pre_year_date, today_date, '豆二'),
    cycle_index), '豆二' + tu.qi_huo_next_month())

# 豆粕
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('M' + next_month + '.DCE', pre_year_date, today_date, '豆粕'),
    cycle_index), '豆粕' + tu.qi_huo_next_month())

# 豆油
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('Y' + next_month + '.DCE', pre_year_date, today_date, '豆油'),
    cycle_index), '豆油' + tu.qi_huo_next_month())

# 棕榈油
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('P' + next_month + '.DCE', pre_year_date, today_date, '棕榈油'),
    cycle_index), '棕榈油' + tu.qi_huo_next_month())

# 玉米
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('C' + next_month + '.DCE', pre_year_date, today_date, '玉米'),
    cycle_index), '玉米' + tu.qi_huo_next_month())

# 玉米淀粉
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('C' + next_month + '.DCE', pre_year_date, today_date, '玉米淀粉'),
    cycle_index), '玉米淀粉' + tu.qi_huo_next_month())

# 纤维板
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('FB' + next_month + '.DCE', pre_year_date, today_date, '纤维板'),
    cycle_index), '纤维板' + tu.qi_huo_next_month())

# 焦炭
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('J' + next_month + '.DCE', pre_year_date, today_date, '焦炭'),
    cycle_index), '焦炭' + tu.qi_huo_next_month())

# 焦煤
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('JM' + next_month + '.DCE', pre_year_date, today_date, '焦煤'),
    cycle_index), '焦煤' + tu.qi_huo_next_month())

# 塑料
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('L' + next_month + '.DCE', pre_year_date, today_date, '塑料'),
    cycle_index), '塑料' + tu.qi_huo_next_month())

# PVC聚氯乙烯
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('V' + next_month + '.DCE', pre_year_date, today_date, 'PVC聚氯乙烯'),
    cycle_index), 'PVC聚氯乙烯' + tu.qi_huo_next_month())

# 聚丙烯
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('PP' + next_month + '.DCE', pre_year_date, today_date, '聚丙烯'),
    cycle_index), '聚丙烯' + tu.qi_huo_next_month())

# 胶合板
p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(
    bd.get_qihuo_simaple('BB' + next_month + '.DCE', pre_year_date, today_date, '胶合板'),
    cycle_index), '胶合板' + tu.qi_huo_next_month())

all_qi_huo = mofComData.get_all_product()
for key in all_qi_huo:
    p_file(IndexConstants.date_file_path + 'qihuo' + today_date + '.txt', analysis.change_rate_day(mofComData.get_data(key), cycle_index),
           all_qi_huo[key])
