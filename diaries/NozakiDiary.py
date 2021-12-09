from diaries.AbstractDiary import AbstractDiary

class NozakiDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "グループワーク初日。レッツゴーマグロ漁船"

    def get_author(self):
        return "Nozaki"