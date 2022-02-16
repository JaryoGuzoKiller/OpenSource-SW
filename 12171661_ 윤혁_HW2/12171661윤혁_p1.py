def mul(a, b):
    length = 0
    flag=True

    print("곱셈 결과 출력")
    print(" " * (len(str(int(a) * int(b))) - len(str(a)))+ a)
    print("x", end='')
    print(" " * (len(str(int(a) * int(b))) - len(str(b)) - 1)+ b)
    if (int(a)<0)or(int(b)<0):
        print("-",end='')
    print("-" * len(str(int(a) * int(b))))

    if int(a)<0:
        a=str(abs(int(a)))
        flag=False
    if int(b) < 0:
        b=str(abs(int(b)))
        flag = False

    if len(str(a)) <= len(str(b)):
        length=len(str(a))
    else:
        length=len(str(b))

    result_len=len(str(int(a) * int(b)))
    tail_len = 0
    if flag==False:
        tail_len-=1
    for i in range(0, length):
        print(" "*(result_len-len(str(int(a)*int(b[len(str(b))-i-1])))-tail_len),end='')
        print((int(a)*int(b[len(str(b))-i-1])))
        tail_len+=1

    if flag == False:
        print("-",end='')
    print("-" * (len(str(int(a) * int(b)))+1))
    if flag==False:
        print("-",end='')
    print(int(a)*int(b))

print("1번째 n자리 정수 출력")
a = (input("n자리 정수를 입력하세요: "))
print("2번째 n자리 정수 출력")
b = (input("n자리 정수를 입력하세요: "))

mul(a,b)
