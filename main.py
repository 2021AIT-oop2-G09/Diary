from diaries.DiarySample import DiarySample
from diaries.NozakiDiary import NozakiDiary
from diaries.YudaiDiary import YudaiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  NozakiDiary(),
  YudaiDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()