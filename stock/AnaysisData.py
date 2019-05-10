class AnaysisData(object):
    def __init__(self):
        # ---------MACD
        self._ema_short = []
        self._ema_lang = []
        self._diff = []
        self._eda = []

    def get_ema_short(self):
        return self._ema_short

    def set_ema_short(self, value):
        self._ema_short = value

    def get_ema_lang(self):
        return self._ema_lang

    def set_ema_lang(self, value):
        self._ema_lang = value

    def get_diff(self):
        return self._diff

    def set_diff(self, value):
        self._diff = value

    def get_eda(self):
        return self._eda

    def set_eda(self, value):
        self._eda = value


