from diaries.AbstractDiary import AbstractDiary

class TakumaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "GitHub何もわからん"

    def get_author(self):
        return "Takuma"