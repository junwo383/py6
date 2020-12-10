coffer = 4
Efnelmintchoco = 5000              
Irisamericano = 7000
Lilicapuccino = 9000
StellaYeonYusmudie = 11000
print("================================소울워커인들의카페===================================")
menu={"1.에프넬민트초코":5000,"2.이리스아메리카노":7000,"3.릴리카푸치노":9000,"4.스텔라연유스무디":11000}
print(menu)
Money = int(input("소울워커인들아 커피먹어라! 먹을거면 돈내놔!>"))
while True :
    if coffer >=1 :
        choice = input("1.에프넬민트초코 2.이리스아메리카노3.릴리카푸치노 4.스텔라연유스무디 숫자를 입력하세요")
        a = print("소울워커인이여~ 에프넬민트초코드리겠습니다.")
        print("제니"+str(Money-5000)+"원이나왔습니다.")
        coffer-= 1
        Money-=Efnelmintchoco
    elif choice == 2 and Money>"이리스아메리카노" :
        b = print("소울워커인이여~ 이리스아메리카노드리겠습니다.")
        print("제니"+str(Money-7000)+"원이나왔습니다.")
        coffer-= 1
        Money-=Irisamericano
    elif choice == 3 and Money>"릴리카푸치노" :
        c = print("소울워커인이여~ 릴리카푸치노드리겠습니다.")
        print("제니"+str(Money-9000)+"원이나왔습니다.")
        coffer-=1
        Money-= Lilicapuccino
    elif choice == 4 and Money>"스텔라연유스무디" or choice :
        d = print("소울워커인이여~ 스텔라연유스무디드리겠습니다.")
        coffer-=1
        Money-=StellaYeonYusmudie
        print("제니"+str(Money-11000)+"원이나왔습니다.")
    else :
        print("당신은 끼에엥님처럼 소울워커인 인가요? 왜돈"+str(Money-4000)+"을 이상하게 꼭 로렌님처럼 멋지게 넣었습니까?")
        continue
    end = input("소울워커인이여~ 결제가완료가됬다면 (네/아니요) 해주세요")
    if end <"네" :
        print("소울워커인이여~ 결제가끝났어요. 당신자유입니다. 야! 떠나세요!")
    elif end <"아니요" :
         print("소울워커인이여~ 결제가끝났어요. 당신자유입니다. 야! 떠나세요!")
         break
