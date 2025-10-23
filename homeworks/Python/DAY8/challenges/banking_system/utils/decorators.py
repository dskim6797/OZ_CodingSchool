from typing import Callable
from utils.exceptions import InsufficientFundsError, NegativeAmountError

def validate_transaction(func: Callable) -> Callable:
    def wrapper(self, amount: int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        
        if func.__name__ == 'withdraw':
            current_balance = self.get_balance() 
            if amount > current_balance:
                raise InsufficientFundsError(current_balance)
        
        return func(self, amount)
    return wrapper