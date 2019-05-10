import os


class StockDayData:
    # ts_code trade_date  open  high   low  close  pre_close  change    pct_chg  vol  amount
    def __init__(self, oneRowData):
        self._ts_code = oneRowData[0]
        self._trade_date = oneRowData[1]
        self._open = oneRowData[2]
        self._high = oneRowData[3]
        self._low = oneRowData[4]
        self._close = oneRowData[5]
        self._pre_close = oneRowData[6]
        self._change = oneRowData[7]
        self._pct_chg = oneRowData[8]
        self._vol = oneRowData[9]
        self._amount = oneRowData[10]

    def __str__(self):
        return ("股票代码 : %s\n"
              "交易日期 : %s\n"
              "开盘价 : %.2f\n"
              "最高价 : %.2f\n"
              "最低价 : %.2f\n"
              "收盘价 : %.2f\n"
              "昨收价 : %.2f\n"
              "涨跌额 : %.2f\n"
              "涨跌幅 : %.2f\n"
              "成交量 （手） : %.2f\n"
              "成交额 （千元）: %.2f\n"
              % (
                self._ts_code,
                 self._trade_date,
                 self._open,
                 self._high,
                 self._low,
                 self._close,
                 self._pre_close,
                 self._change,
                 self._pct_chg,
                 self._vol,
                 self._amount
              )
              )

    # ts_code        str    股票代码
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

        # pre_close      float  昨收价

    def get_pre_close(self):
        return self._pre_close

    def set_pre_close(self, value):
        self._pre_close = value

        # change         float  涨跌额

    def get_change(self):
        return self._change

    def set_change(self, value):
        self._change = value


        # pct_chg        float  涨跌幅 （未复权，如果是复权请用 通用行情接口 ）

    def get_pct_chg(self):
        return self._pct_chg

    def set_pct_chg(self, value):
        self._pct_chg = value

        # vol            float  成交量 （手）

    def get_vol(self):
        return self._vol

    def set_vol(self, value):
        self._vol = value

        # amount         float  成交额 （千元）

    def get_amount(self):
        return self._amount

    def set_amount(self, value):
        self._amount = value
