
from tools.PrintUtil import *
from indexData.BaseData import BaseData
from Analysis import Analysis
bd=BaseData('sample')
analysis = Analysis()

pr(analysis.change_rate_day(bd.get_qihuo_simaple('I1905.DCE', '20180408', '20190408', 'tie'),
                            [1, 2, 5, 10, 30, 100]), 'tie')
