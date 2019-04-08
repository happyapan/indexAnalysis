class Analysis:
    # 计算N天的涨幅（与最新值比）
    # date ：数据
    # cycle_list ：周期列表
    def change_rate_day(self, date, cycle_list):
        if date:
            if date["data"]:
                return_value = []
                if not cycle_list:
                    cycle_list = [1, 2, 7, 10, 50, 100]
                for cycle in cycle_list:
                    if len(date["data"]) > cycle + 1:
                        rate = 100 * (date["data"][0] - date["data"][cycle]) / date["data"][cycle]
                        return_value.append((date["name"], cycle, rate))

                return return_value

        return None
