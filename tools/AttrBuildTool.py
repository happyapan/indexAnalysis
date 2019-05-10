def build(name):
    print("def get_"+name+"(self):")
    print("    return self._" + name)
    print("")
    print("")
    print("def set_" + name + "(self, value):")
    print("    self._" + name+" = value")
    print("")
    print("")


attrs='ts_code,trade_date , open , high ,  low , close , pre_close , change   , pct_chg , vol ,       amount'
attrList=attrs.split(",")
for one in attrList:
    build(one.strip())