from diaries.DiarySample import DiarySample
from diaries.NozakiDiary import NozakiDiary
from diaries.YudaiDiary import YudaiDiary
from diaries.K20006Diary import K20006Diary
from diaries.KurataDiary import KurataDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  NozakiDiary(),
  YudaiDiary(),
  K20006Diary(),
  KurataDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()