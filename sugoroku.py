#ランダムモジュールを読み込む
import random

#変数
pl_pos = 1
com_pos = 1

#関数の宣言def banmen()のもとの場所を決める
def banmen():
    print ("・" * (pl_pos-1)+ "P" +"・"  *(30-pl_pos)+"GOAL")
    print ("・" * (com_pos-1)+ "C" +"・"  *(30-com_pos)+"GOAL")

#〜の間・無限の間(true)
while True:
    banmen()
    input("スゴロクスタートです！")

    pl_pos = pl_pos + random.randint(1,6)
    com_pos = com_pos + random.randint(1,6)
    #30についた時その場所に留まらせる
    if pl_pos > 30:
        pl_pos = 30
        banmen()
    if com_pos > 30:
        com_pos = 30
        banmen()
    #結果を伝えbreak そこでゲームを終了する
    if pl_pos == 30:
        print("あなたの勝ちです！")
        break  
    if com_pos ==30:
        print("あなたの負けです!")
        break 
    
    # pl_pos = pl_pos + 2
    # com_pos = com_pos + 2
    # pl_pos = pl_pos + random.randint(1,6)
    # com_pos = com_pos + random.randint(1,6)




