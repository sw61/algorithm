# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
# (1 ≤ A, B ≤ 10,000)

A, B = map(int, input().split())

# 주어진 범위 내에 있는지 확인
if 1 <= A <= 10000 and 1 <= B <= 10000:
    
    print(A + B)
    print(A - B)
    print(A * B)

    if B != 0: 
        print(A // B)

    # 나머지
    if B != 0: 
        print(A % B)
    else:
        print("0으로 나눌 수 없습니다.")
else:
    print("입력값이 유효하지 않습니다.")