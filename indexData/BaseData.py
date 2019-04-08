import urllib.request


class BaseData:
    def __init__(self, name):
        self.name = name;
        self.return_data = {
            "name": "",
            "week": 0,
            "data": []
        }

    def get_data(self):
        pass

    def name(self):
        return self.name

    def get_url_date(self, url):
        return urllib.request.urlopen(url).read().decode('gb2312')
