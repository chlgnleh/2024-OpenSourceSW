#짝수 프로그램 소스코드
def main():
    N = int(input('어디까지~?: '))
    for number in range(0, N+1, 1):
        if number % 2 == 0:
            print(f'{number}')
main()