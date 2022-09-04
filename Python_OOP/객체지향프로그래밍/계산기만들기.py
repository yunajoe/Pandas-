'''
 인스턴스 변수나 클래스 변수를 쓰지 않을 거라면 
 정적 메소드(static method)를 사용
'''

class SimpleCalculator:     
    @staticmethod 
    def add(num1, num2):
        return num1 + num2 
    
    @staticmethod
    def subtract(num1, num2):
        return num1-num2
    
    @staticmethod
    def multiply(num1, num2):
        return num1 * num2
    
    @staticmethod
    def divide(num1, num2):
        return num1 / num2

# 계산기 인스턴스 생성
calculator = SimpleCalculator()
print(calculator.add(4, 5))
print(calculator.subtract(4, 5))
print(calculator.multiply(4, 5))
print(calculator.divide(4, 5))
