class Eagle:
    """조류: 독수리 정보를 담는 클래스"""
    def __init__(self, name, sound="짹짹"):
        self.name = name
        self.sound = sound
        self.category = "Bird"

    def info(self):
        return f"{self.name}는 조류이며 '{self.sound}' 소리를 냅니다."
