print("area 모듈 이름 : {}".format(__name__))

PI = 3.14 # 상수의 경우에는 대문자를 사용하는 것이 좋음

def circle(radius):
    return PI * radius ** 2 

def square(length):
    return length ** 2



# __name__
# __main__

#모듈의 이름을 저장해 둔 변수 

if __name__ == "__main__":
    print(circle(5))