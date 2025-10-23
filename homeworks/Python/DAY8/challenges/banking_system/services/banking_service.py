from models.user import User 
from utils.exceptions import UserNotFoundError
from utils.exceptions import InsufficientFundsError, NegativeAmountError 

class BankingService:
    # 사용자 목록을 초기화하는 생성자를 구현합니다.
    # 사용자를 추가하는 add_user 메서드를 구현합니다.
    # 사용자를 찾는 find_user 메서드를 구현합니다.
    # 사용자 메뉴를 제공하는 user_menu 메서드를 구현합니다.
    def __init__(self) -> None:
        self.users = [] # 사용자 목록을 저장하는 리스트

    def add_user(self, username: str) -> None:
        user = User(username) # User 객체를 나타내는 변수
        self.users.append(user)
        
    def find_user(self, username: str) -> User:
        for user in self.users:
            if user.username == username:
                print(f"{username}님은 등록된 사용자 입니다.")
                return user
        raise UserNotFoundError(username)

    def user_menu(self, username: str) -> None:
        user = self.find_user(username)
        
        while True:
            print("  \n작업 목록:")
            print("  1. 입금")
            print("  2. 출금")
            print("  3. 잔고확인")
            print("  4. 거래내역")
            print("  5. 종료")

            choice = input("  작업 선택: ") # 사용자의 선택을 나타내는 문자열
            try: 
                if choice == "1":
                    amount = int(input("  입금할 금액 입력: ")) # 입금 또는 출금 금액을 나타내는 정수
                    user.account.deposit(amount)

                elif choice == "2":
                    amount = int(input("  출금할 금액 입력: ")) # 입금 또는 출금 금액을 나타내는 정수
                    user.account.withdraw(amount)

                elif choice == "3":
                    print(f"  현재 잔고: {user.account.get_balance()}")

                elif choice == "4":
                    transactions = user.account.get_transactions()
                    for i, transaction in enumerate(transactions):
                        print(f"  {i}. {transaction}")

                elif choice == "5":
                    print("  메뉴 화면을 종료합니다.")
                    break
                
                else:
                    print("  잘못된 입력입니다. 다시 시도하세요.")
            
            except InsufficientFundsError as e:
                print(f"오류: {e}")
            except NegativeAmountError as e:
                print(f"오류: {e}")
            
            print("-"*40)