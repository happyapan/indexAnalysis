import os

from stock.AnaysisData import AnaysisData


class StockDayDataHFQ(AnaysisData):
    # ts_code trade_date  open  high   low  close  pre_close
    def __init__(self, oneRowData):
        self._ts_code = oneRowData[0]
        self._trade_date = oneRowData[1]
        self._open = float(oneRowData[2])
        self._high = float(oneRowData[3])
        self._low = float(oneRowData[4])
        self._close = float(oneRowData[5])

    def __str__(self):
        return ("%s,%s,%.2f,%.2f,%.2f,%.2f"
              % (
                self._ts_code,
                 self._trade_date,
                 self._open,
                 self._high,
                 self._low,
                 self._close
              )
              )

    def info(self):
        return ("股票代码 : %s\n"
              "交易日期 : %s\n"
              "开盘价 : %.2f\n"
              "最高价 : %.2f\n"
              "最低价 : %.2f\n"
              "收盘价 : %.2f\n"
              "昨收价 : %.2f\n"
              % (
                self._ts_code,
                 self._trade_date,
                 self._open,
                 self._high,
                 self._low,
                 self._close
              )
              )


    def get_ts_code(self):
        return self._ts_code

    def set_ts_code(self, value):
        self._ts_code = value

    # trade_date     str    交易日期
    def get_trade_date(self):
        return self._trade_date

    def set_trade_date(self, value):
        self._trade_date = value

        # open           float  开盘价

    def get_open(self):
        return self._open

    def set_open(self, value):
        self._open = value

        # high           float  最高价

    def get_high(self):
        return self._high

    def set_high(self, value):
        self._high = value

        # low            float  最低价

    def get_low(self):
        return self._low

    def set_low(self, value):
        self._low = value

        # close          float  收盘价

    def get_close(self):
        return self._close

    def set_close(self, value):
        self._close = value
