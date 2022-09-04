class GameCharacter:
    def __init__(self, name, hp, power):
        """사용할 모든 인스턴스 변수를 설정"""
        self.name = name 
        self.hp = hp 
        self.power = power 
        
    def is_alive(self):
        """ 게임 캐릭터의 체력이 0보다 큰지(살았는지 죽었는지) 확인"""
        return self.hp > 0
    
    def get_attacked(self,damage):
        """게임 캐릭터의 체력이 0보다 큰 상태라면 파라미터로 받은 공격력만큼 체력을 깎는다. """
        if self.is_alive():
            if self.hp > damage:
                self.hp = self.hp - damage
            else:
                self.hp = 0
        else:
            print("{} 이미 죽음".format(self.name))
            
    def attack(self, other_character):
        """ 게임캐릭터가 살아 있으면 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다"""
        if self.is_alive():
            other_character.get_attacked(self.power)
            
            
    def __str__(self):
        return self.name + "님의 hp는" + str(self.hp) + "만큼 남았습니다."
            
            
# 게임 캐릭터 인스턴스 생성                        
character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

# 게임 캐릭터 인스턴스들 서로 공격
character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)


# 게임 캐릭터 인스턴스 출력
print(character_1)
print(character_2)
                
        
            
            
            
            
            
            
        
    
        