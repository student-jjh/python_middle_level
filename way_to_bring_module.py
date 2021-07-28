from area import circle,PI #필요한 몇개만 가지고 옴
from area import square as sq #필요한 함수를 간단한 이름으로 변경하여 가지고 옴
# *표시를 하면 모든 함수를 가지고 오게 됨 그런데 필요 없는 것을가지고 오기도 하고 어디서 가지고 왔는지를 모르게 되기 때문에 권장하지 않은 방법
print(circle(5))
print(PI)

#dir 은 그 모듈에서 정의해둔 모든 것을 보여줌