import tools.TimeUtil as timeUtil

from stock.BaseStock import BaseStock

# 日K线在布林通道中轨和下轨之间运行，跌出下轨后，股价返再次回通道之内当日即为短线买入时机。
from stock_analysis.Boll import Boll


def analysis_stock(stock_code, stock_name, trade_data):
    base = BaseStock("base")
    datas = base.get_stock_data(stock_code, stock_name, timeUtil.day_after_day(trade_data, -30), trade_data)
    if datas is not None and len(datas) > 1:
        if datas[0].get_trade_date() != trade_data:
            return None

        # 比较时间交易记录
        trade_time_data = datas[0]
        # 比较时间，前一天交易记录
        trade_time_pre = datas[1]

        ball = Boll()
        boll_result = ball.get_boll(stock_code, stock_name)
        boll_compare_index = -1
        for pp in range(len(boll_result["trade_date"])):
            if boll_result["trade_date"][pp] == trade_data:
                boll_compare_index = pp
                break

        if boll_compare_index == -1:
            return None

        # 判断是否上穿Boll线下轨
        if trade_time_data.get_close() >= boll_result["down_track"][pp] and trade_time_pre.get_close() <= \
                boll_result["down_track"][pp - 1]:
            # 获取在Boll线下轨的天数
            continue_down_count = 0
            for tt in range(1, len(datas)):
                if datas[tt].get_close() <= boll_result["down_track"][pp - tt]:
                    continue_down_count += 1
            trade_time_data.set_down_line_day_count(continue_down_count)
            return trade_time_data

    else:
        return None

# for i in range(0, 300):
#     catch_stock = analysis_stock('000004.SZ', '国农科技', timeUtil.day_after_day("20190510", i * -1))
#     if catch_stock is not None:
#         print(catch_stock)
