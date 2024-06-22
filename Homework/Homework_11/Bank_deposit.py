PERCENT_PER_YEAR = .10
MONTHS_PER_YEAR = 12


class Currency:
    rates = {
        'USD': 3.2690,
        'EUR': 3.5200,
        'CAD': 2.3000,
        'BYN': 1.0000,
    }

    def convert_rate(self, currency_from, amount, currency_to):
        final_amount = amount * (self.rates[currency_from] / self.rates[currency_to])
        return round(final_amount, 2)


class Bank:

    def __init__(self):
        self.currency = Currency()

    @staticmethod
    def deposit(amount, period):
        months_count = period * MONTHS_PER_YEAR
        res_amount = amount
        for i in range(months_count):
            res_amount += res_amount * PERCENT_PER_YEAR / MONTHS_PER_YEAR
        return round(res_amount, 2)

    def exchange_currency(self, currency_from, amount, currency_to='BYN'):
        var = self.currency.convert_rate(currency_from, amount, currency_to)
        return var, currency_to


class Deposit:
    def __init__(self, deposit_amount, deposit_period):
        self.deposit_amount = deposit_amount
        self.deposit_period = deposit_period


class Person:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


bank = Bank()
dep1 = Deposit(1000, 1)
assert bank.deposit(dep1.deposit_amount, dep1.deposit_period) == 1104.71

vasya = Person('USD', 10)
petya = Person('EUR', 10)
assert bank.exchange_currency(vasya.currency, vasya.amount) == (32.69, "BYN"), 'error'
assert bank.exchange_currency(petya.currency, petya.amount, 'USD') == (10.77, "USD"), 'error'
