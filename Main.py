from Analysis import Analysis
from indexData.PigPrice365Day import PigData
from indexData.TieKuangShi import TieKuangShi
from tools.PrintUtil import *

analysis = Analysis()
pigDate = PigData("猪肉")
tie = TieKuangShi("铁矿石")

pr(analysis.change_rate_day(pigDate.get_data(), [1, 2, 5, 10, 30, 100]), pigDate.name)
pr(analysis.change_rate_day(tie.get_data(), [1, 2, 5, 10, 30, 100]), tie.name)