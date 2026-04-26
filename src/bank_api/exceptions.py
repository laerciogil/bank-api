class AccountNotFoundError(Exception):
    pass


class BusinessError(Exception):
    pass


class InsufficientFundsError(Exception):
    def __init__(self, funds: float) -> None:
        self.funds = funds
        super().__init__(f"Not enough funds. Available: {funds}")
