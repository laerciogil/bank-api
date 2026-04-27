class AccountNotFoundError(Exception):
    pass


class BusinessError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class InsufficientFundsError(BusinessError):
    def __init__(self, funds: float) -> None:
        self.funds = funds
        super().__init__(f"Not enough funds. Available: {funds}")
