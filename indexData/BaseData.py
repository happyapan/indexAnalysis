import urllib.request


class BaseData:
    def __init__(self):
        self.return_data = {
            "name": "",
            "week": 0,
            "data": []
        }

    def get_data(self):
        pass

    def get_url_date(self, url):
        return urllib.request.urlopen(url).read().decode('gb2312')
