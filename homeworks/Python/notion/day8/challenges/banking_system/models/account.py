from models.transaction import Transaction 
from utils.decorators import validate_transaction

class Account:
    # __balance와 transactions 리스트를 초기화하는 생성자를 구현합니다.
    # 입금을 위한 deposit 메서드를 구현합니다.
    # 출금을 위한 withdraw 메서드를 구현합니다.
    # 잔고를 반환하는 get_balance 메서드를 구현합니다.
    # 거래 내역을 반환하는 get_transactions 메서드를 구현합니다.
    # 클래스 변수 bank_name와 클래스 메소드 get_bank_name, set_bank_name을 구현합니다.
    def __init__(self) -> None:
        self.__balance = 0 # 계좌 잔고를 나타내는 프라이빗 정수 변수
        self.transactions = [] # 거래 내역을 저장하는 리스트

    @validate_transaction
    def deposit(self, amount: int) -> None: 
        self.__balance += amount
        self.transactions.append(Transaction("입금", amount, self.__balance))
        
    @validate_transaction
    def withdraw(self, amount: int) -> None: 
        self.__balance -= amount
        self.transactions.append(Transaction("출금", amount, self.__balance))

    # 잔고 반환 메서드
    def get_balance(self) -> int: 
        return self.__balance

    # 거래내역 반환 메서드
    def get_transactions(self) -> list: 
        return self.transactions

    @classmethod 
    def get_bank_name(cls) -> str:
        return cls.bank_name # 은행 이름을 나타내는 클래스 변수 문자열
    
    @classmethod
    def set_bank_name(cls, name: str) -> None:
        cls.bank_name = name
        return cls.bank_name