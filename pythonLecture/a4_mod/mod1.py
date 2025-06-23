
# import mod.mod2
# from mod.mod2 import mul

print('mod1.py 시작')
print('모듈 이름: ', __name__)


PI = 2.19

def add(n1, n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2


print('mod1.py 끝')

if __name__=='__main__':
    # 실행 포인트
    # mod1 프로그램의 처음 실행 위치X, 모듈로써의 역할
    # 테스트: PI 변수 선언/할당, add함수, sub함수
    print(PI)
    print(add(10,3))
    print(sub(10,9))