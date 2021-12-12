from diaries.DiarySample import DiarySample
from diaries.KanadaDiary import KanadaDiary
from diaries.NozakiDiary import NozakiDiary
from diaries.YudaiDiary import YudaiDiary
from diaries.K20006Diary import K20006Diary
from diaries.KurataDiary import KurataDiary
from diaries.TakumaDiary import TakumaDiary
from diaries.KambaraDiary import KambaraDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  KanadaDiary(),
  NozakiDiary(),
  YudaiDiary(),
  K20006Diary(),
  KurataDiary(),
  TakumaDiary(),
  KambaraDiary()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()