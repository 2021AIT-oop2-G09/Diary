from diaries.AbstractDiary import AbstractDiary

class YudaiDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-24"

    def get_summary(self):
        return "クリスマスだった。バイトだった"

    def get_author(self):
        return "Yudai"