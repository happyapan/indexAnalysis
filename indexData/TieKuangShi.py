from indexData.BaseData import BaseData
import tools.TimeUtil as tu


class TieKuangShi(BaseData):
    def __init__(self, name):
        BaseData.__init__(self, name)

    def get_data(self):
        res_data = self.get_ts_qihuo("I" + tu.qi_huo_next_month() + '.DCE', tu.pre_year_date(), tu.today())
        # res_data = self.get_ts_qihuo("I1906" + '.DCE', tu.pre_year_date(), tu.today())
        self.return_data = {
            "name": "铁矿石",
            "week": 7,
            "data": res_data
        }
        return self.return_data
