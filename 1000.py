# 두 수 입력 받아 더해서 출력 
# 입력 1 2 ==> 출력 3

a,b = map(int,input().split())
print(a+b)

#  input().split()의 결과가 문자열 리스트라서 map함수를 쓸 수 있다.

x = input().split()    # input().split()의 결과는 문자열 리스트
m = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
a, b = m               # 맵 객체는 변수 여러 개에 저장할 수 있음