from random import randint
class Die:
    """seizi"""
   
    def __init__(self,sides=6,face=6):
        """初始化数据,骰子的次数，骰子的面数"""
        self.sides = sides
        self.face = face
    
    def roll_die(self):
        for _ in range(self.sides):
            print(randint(1,self.face))
number1 = int(input("请输入投骰子的次数"))
number2 = int(input("请输入投骰子的面数"))
dice = Die(number1,number2)
dice.roll_die()


        
        