# 매개변수로 올해 연도와 태어난 해를 전달
# 성인(20세)의 경우 무료로 2년마다 건강 검진
# 짝수해에 태어난 사람은 짝수년에 검사
# 40세 이상이면 암 검사 무료

thisYear=input('this year: ')
birthYear=input('year of birth: ')

thisYear=int(thisYear)
birthYear=int(birthYear)
age=thisYear-birthYear


if age>=20 and birthYear%2==thisYear%2:
    if age>=40:
        print('cancer GG')
    else :
        print('GG')
else: 
    print('Bye')