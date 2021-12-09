from diaries.DiarySample import DiarySample
from diaries.K20006Diary import K20006Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  K20006Diary()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()