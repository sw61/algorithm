# 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오. (0 < A, B < 10)

a , b= map(int,input().split())
if a > 0 and b < 10:
    print(a / b)
else:
    print('')