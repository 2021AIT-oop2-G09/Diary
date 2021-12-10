from diaries.AbstractDiary import AbstractDiary

class KurataDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "ちゃんとコミュニケーションを取れるように頑張る。"

    def get_author(self):
        return "Kurata"