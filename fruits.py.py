def main():
    fruits = {
        '사과' : 1000,
        '바나나' : 2000,
        '자두' : 500,
        '복숭아' : 4000
    }
    s = input('어서옵쇼~ 어떤 과일을 찾으세요? ')
    if s in fruits:
        print(f'{s}는 {fruits[s]}원입죠~')
    else:
        print(f'아이고~ {s}는 매장에 없네요.')
main()