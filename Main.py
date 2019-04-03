from Analysis import Analysis
from indexData.PigPrice365Day import PigData

analysis = Analysis()
pigDate = PigData().get_data()
print(analysis.change_rate_day(pigDate["data"], 1))
print(analysis.change_rate_day(pigDate["data"], 3))
print(analysis.change_rate_day(pigDate["data"], 100))
print(analysis.change_rate_day(pigDate["data"], 300))
