class Analysis:
    # 计算N天的涨幅（与最新值比）
    def change_rate_day(self, date, dayCount):
        if date:
            if len(date) > dayCount + 1:
                rate = 100 * (date[0] - date[dayCount]) / date[dayCount]
                return rate
        return None
