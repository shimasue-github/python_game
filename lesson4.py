#カレンダー
import calendar
print(calendar.month(2019,2))
#うるう年かどうか調べる
print(calendar.isleap(2020))
#日時
import datetime
print(datetime.date.today())
#時刻を出力する
print(datetime.datetime.now())
d = datetime.datetime.now()
print(d.hour)
print(d.minute)
print(d.second)
#生まれた時から経過した日時
today = datetime.date.today()
birth = datetime.date(1995,1,29)
print(today-birth)
#乱数
import random
r = random.random()
print(r)
#整数乱数
m = random.randint(1,7)
print(m)
#複数の項目から選ぶ
jan = random.choice(["guu","tyoki","pa"])
print(jan)
#確率
cnt = 0 
while True :
    w = random.randint(1,100)
    print(w)
    cnt = cnt + 1
    if w == 77 :
        break 
print (str(cnt)+"回目でレアキャラゲット")


