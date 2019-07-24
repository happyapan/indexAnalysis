class AnaysisData(object):
    def __init__(self):
        # ---------Boll
        #股价在boll【下轨，中轨，上轨】线下天数
        self._down_line_day_count = 0

    def get_down_line_day_count(self):
        return self._down_line_day_count

    def set_down_line_day_count(self, value):
        self._down_line_day_count = value





