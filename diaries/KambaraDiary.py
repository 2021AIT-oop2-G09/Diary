from diaries.AbstractDiary import AbstractDiary

class KambaraDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return """今日はオブジェクト指向プログラミング２のグループワーク演習だった。わからないことが多かったのでグループのみんなと協力していきたい。"""

    def get_author(self):
        return "Kambara"