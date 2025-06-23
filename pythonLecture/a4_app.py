##전체 import
#import a4_mod1

#print(a4_mod1.PI)
#print(a4_mod1.add(10,20))
#print(a4_mod1.sub(10,3))

##원하는 개상면 선별해서 import
#from a4_mod1 import PI, add, sub

##전체 임포트
##모듈 안에 정의된 모근 공개(public)키를 가져온다.
##네임스페이스오염 떄문에 비권장
#from a4_mod1 import *

#print(PI)
#print(add(100,20))
#print(sub(10,5))

##모듈 가칭 정하기
#import a4_mod1 as mo
#print(mo.PI)
#print(mo.add(100,20))
#print(mo.sub(10,5))


##다른 디렉토리 내부에 있는 파일 호출출
import a4_mod.mod1 as mod

## 보통이라면 모듈(파일) 이름이 나오지만, 실행을 실시하는 파일은 __main__으로 표시된다.
print('모듈 이름: ', __name__)


print(mod.PI)
print(mod.add(100,20))
print(mod.sub(10,5))






