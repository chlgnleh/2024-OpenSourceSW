def fun(a, b, i):
    result = a * a * i + b
    return result

a = int(input('a = '))
b = int(input('b = '))
X = int(input('Max = '))
for i in range(X+1): #for문에서 리스트, 문자열 등 아니면 range 꼭 사용
    z = fun(a, b, i)
    print(f'{a}X{a}X{i} + {b} = {z}')
