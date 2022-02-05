#1つの条件が成り立つ場合にはor 
#両方の条件が成り立つ場合にはand

print("サザエさんの名前は??")
ans = input()
if ans == "マスオ" or ans ==  "ますお":
    print("正解です")
else:
    print("不正解です")

#リストとタプル
#タプルは宣言時に代入した値を変更できない
QUESTION =[
    "問題1",
    "問題2",
    "問題3"]
R_ANS = ["問題1","問題2","問題3"]
for i in range(3):
    print(QUESTION[i])
    ans = input()
    if ans == R_ANS[i]:
        print("正解です")
    else:
        print("不正解です")



