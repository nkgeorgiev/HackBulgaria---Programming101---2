class CashDesk:

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, cash):
        for bill in cash:
            self.money[bill] += cash[bill]

    def total(self):
        total = 0
        for bill in self.money:
            total += bill * self.money[bill]
        return total

    def can_withdraw_money(self, amount_of_money):
        total = self.total()
        if total < amount_of_money:
            return False
        if total == amount_of_money:
            return True

        for a in range(self.money[100] + 1):
            for b in range(self.money[50] + 1):
                for c in range(self.money[20] + 1):
                    for d in range(self.money[10] + 1):
                        for e in range(self.money[5] + 1):
                            for f in range(self.money[2] + 1):
                                for g in range(self.money[1] + 1):
                                    if a * 100 + b * 50 + c * 20 + d *10 + e *5 + f * 2 + g * 1 == amount_of_money:
                                        return True

        return False

