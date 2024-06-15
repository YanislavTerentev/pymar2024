PERCENT_PER_YEAR = .10
MONTHS_PER_YEAR = 12


class Bank:
    @staticmethod
    def deposit(amount, period):
        months_count = period * MONTHS_PER_YEAR
        res_amount = amount
        for i in range(months_count):
            res_amount += res_amount * PERCENT_PER_YEAR / MONTHS_PER_YEAR
        return round(res_amount, 2)


class Deposit:
    def __init__(self, deposit_amount, deposit_period):
        self.deposit_amount = deposit_amount
        self.deposit_period = deposit_period


bank = Bank()
dep1 = Deposit(1000, 1)
assert bank.deposit(dep1.deposit_amount, dep1.deposit_period) == 1104.71

