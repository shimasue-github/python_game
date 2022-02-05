#時間を競うこと　=タイムアタック

import random
import datetime
#指定する配列がある場合 変数 ->1つづつ入れていく　そうでない場合 range(1)
ALP = ["A","B","C","D","E","F","G"]
r = random.choice(ALP)
alp = ""
for i in ALP :
    if i != r:
        alp = alp + i
print(alp)
st = datetime.datetime.now()
ans = input("抜けてるアルファベットは？")
if ans == r :
    print('正解')
    en = datetime.datetime.now()
    print(str((en - st).seconds) + "秒かかりました")
else :
    print('不正解')