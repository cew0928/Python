"""
#a, b, c 중 가장 큰 수를 찾는 프로그램
a=33
b=4
c=5
largest =a   #가장 큰 수를 저장, 일단은 a로 시작

if largest<b:
    largest=b
if largest<c:
    largest=c

print("가장 큰 수는", largest)

"""
"""
#1부터 n까지 더하는데 그 합이 100이 넘는
#그때의 최소의 n값을 구하시오
#hint: 1~10 합은 55

n=1
sum0=0

while sum0<100:
    sum0+=n
    if sum0>100:
        break
    n+=1

print(sum0)
print("합이 100이 넘는 최소의 n값은: ", n)

"""
"""
#100이하의 3의 배수만 다 합하기
#3, 6, 9, 12, 15..... 99까지 더하기
#5, 10, 15, 20, 25..100까지 더하기
#15,30,45..90

sum0=0
for i in range(1,101):
    if i%3==0 or i%5==0:
        sum0 +=i
print("100이하의 3혹은 5의 배수의 합은", sum0)

#3의배수 합 1683, 5의배수 합 1050
#1683+1050 = 2733
#15의 배수의 합 15,30,45,60,75,90 = 315
#2733 - 315 = 2418
"""
#소인수분해 prime
#12 = 2*2*3 = 2^2*3
#72 = 2*2*2*3*3 = 2^3* 3^2

def Soinsu(n):
    d=2
    while d<=n:
        if n % d==0:
            print(d, end=" ")
            n = n//d
        else:
            d+=1

print("72=", end=" ")
Soinsu(72)

    










