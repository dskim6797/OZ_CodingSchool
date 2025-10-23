class Transaction:
    # 거래(Transaction) 클래스를 정의하고, transaction_type, amount, balance 속성을 초기화하는 생성자를 구현합니다.
    # 거래 정보를 문자열로 반환하는 str 메서드를 구현합니다.
    # 거래 정보를 튜플로 반환하는 to_tuple 메서드를 구현합니다.
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:
        self.transaction_type = transaction_type # 거래 유형을 나타내는 문자열 (예: "입금", "출금")
        self.amount = amount # 거래 금액을 나타내는 정수
        self.balance = balance # 거래 후 잔고를 나타내는 정수

    # 문자열 반환 메서드
    def __str__(self) -> str:
        return f"{self.transaction_type} {self.amount}원, 잔고: {self.balance}"

    # 튜플 반환 메서드
    def to_tuple(self) -> tuple:
        return (self.transaction_type, self.amount, self.balance)