from Analysis import Analysis
from indexData.PigPrice365Day import PigData
from tools.PrintUtil import *

analysis = Analysis()
pigDate = PigData("猪肉")
print()

pr(analysis.change_rate_day(pigDate.get_data(), [1, 2, 4, 5, 88, 200]), pigDate.name)


