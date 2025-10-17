class Dog:
    """포유류: 개 정보를 담는 클래스"""
    def __init__(self, name, sound="멍멍"):
        self.name = name
        self.sound = sound
        self.category = "Mammal"

    def info(self):
        return f"{self.name}는 포유류이며 '{self.sound}' 소리를 냅니다."