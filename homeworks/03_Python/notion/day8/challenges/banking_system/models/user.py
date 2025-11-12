from models.account import Account 

class User:
    # username과 account를 초기화하는 생성자를 구현합니다.
    def __init__(self, username: set) -> None:
        self.username = username
        self.account = Account()