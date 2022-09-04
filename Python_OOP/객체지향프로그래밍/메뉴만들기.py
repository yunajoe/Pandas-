'''
MenuItem 클래스를 정의  

인스턴스 변수(타입):
name(문자열): 메뉴 이름
price(숫자): 메뉴 가격

인스턴스 메소드:
__init__: MenuItem 클래스의 모든 인스턴스 변수를 초기화한다.
__str__: MenuItem 인스턴스의 정보를 문자열로 리턴

'''

class MenuItem:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
        
    def __str__(self):
        return f"{self.name}가격: {self.price}"     
    
food1 = MenuItem("햄버거", 4000)
food2 = MenuItem("콜라", 1500)
food3 = MenuItem("후렌치 후라이", 1500)

print(food1)
print(food2)
print(food3)

        